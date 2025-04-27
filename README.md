# AutoSec Essentials: The Cyber Admin’s Swiss Army Knife

A Security Automation Toolkit GUI that automates routine security tasks like log parsing, patch checks, and privilege audits for different operating systems

<img width="500" height="400" alt="Screenshot 2025-04-26 at 8 18 08 PM" src="https://github.com/user-attachments/assets/70a06f1e-a2b8-48fa-b071-401c3e7be021" />


## Features

- Security Toolkit GUI: A user-friendly interface to run various security tasks, making the system more accessible for non-technical users.
- Log Analysis: Logs are generated for each task (malware scan, privilege audit, etc.) for traceability.
- Malware Scan: Executes a script to scan for malware on the system, providing feedback on successful completion.
- Privilege Audit: Runs a script to check and audit user privileges, ensuring proper access control in the system.
- Firewall Check: Verifies the firewall configuration to ensure the system is properly protected.
- Patch Management: Runs a script to check for and apply necessary system patches to keep the system up-to-date.
- Cross-Platform Compatibility: Should work across platforms like MacOS,Windows, and Linux (may need some adjustments for macOS).
- Python Scripts Integration: The project integrates Python scripts for each task (malware scan, audit, firewall check, etc.), allowing for seamless automation of security tasks.
- Report Generation: Automatically sends generated reports to the system administrator via email.


## Installation

```
# Clone Repository
git clone https://github.com/shikha1149myprojects/Security-Automation-Toolkit.git

# Move into directory
cd security_automation_toolkit

# Update and Load your environment
export $(cat .env | xargs)

# Install Dependencies
pip3 install pyqt5  

# Run toolkit
python3 security_toolkit_gui.py
```
