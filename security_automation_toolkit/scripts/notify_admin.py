import smtplib
import os
from email.message import EmailMessage

def send_email():
    try:
        sender = os.getenv("EMAIL_SENDER")
        password = os.getenv("EMAIL_PASS")
        recipient = os.getenv("EMAIL_RECIPIENT")

        if not all([sender, password, recipient]):
            raise ValueError("Missing environment variables. Check EMAIL_SENDER, EMAIL_PASS, and EMAIL_RECIPIENT.")

        msg = EmailMessage()
        msg['Subject'] = 'Security Toolkit Report'
        msg['From'] = sender
        msg['To'] = recipient
        msg.set_content("Security tasks have completed. See attached reports.")

        # List of report files to attach
        report_files = [
            'output/analysis_report.txt',
            'output/malware_scan_report.txt',
            'output/privilege_audit.txt',
            'output/firewall_rules.txt'
        ]

        # Attach each report file
        for file_path in report_files:
            if os.path.exists(file_path):
                with open(file_path, 'rb') as f:
                    msg.add_attachment(f.read(), maintype='text', subtype='plain', filename=os.path.basename(file_path))
                print(f"[*] Attached {file_path}")
            else:
                print(f"[!] Report file {file_path} not found.")

        print("[*] Connecting to SMTP server...")
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender, password)
            smtp.send_message(msg)
            print("[+] Email sent successfully to", recipient)

    except smtplib.SMTPAuthenticationError as e:
        print("[!] Authentication failed. Please check your App Password and 2FA settings.")
        print(e)
    except Exception as e:
        print("[!] Error sending email:")
        print(e)

if __name__ == "__main__":
    send_email()
