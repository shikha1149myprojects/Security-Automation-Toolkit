import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QFrame, QMessageBox

# Define your functions for running tasks here
def run_malware_scan():
    try:
        os.system('bash scripts/malware_scan.sh')
        QMessageBox.information(window, "Success", "Malware scan completed successfully.")
    except Exception as e:
        QMessageBox.critical(window, "Error", f"Error running malware scan: {e}")

def run_privilege_audit():
    try:
        os.system('python3 scripts/audit_privileges.py')
        QMessageBox.information(window, "Success", "Privilege audit completed successfully.")
    except Exception as e:
        QMessageBox.critical(window, "Error", f"Error running privilege audit: {e}")

def run_firewall_check():
    try:
        os.system('bash scripts/inspect_firewall.sh')
        QMessageBox.information(window, "Success", "Firewall check completed successfully.")
    except Exception as e:
        QMessageBox.critical(window, "Error", f"Error running firewall check: {e}")

def run_patch_management():
    try:
        os.system('bash scripts/patch_management.sh')
        QMessageBox.information(window, "Success", "Patch management completed successfully.")
    except Exception as e:
        QMessageBox.critical(window, "Error", f"Error running patch management: {e}")

def send_reports():
    try:
        os.system('python3 scripts/notify_admin.py')
        QMessageBox.information(window, "Success", "Reports sent to admin successfully.")
    except Exception as e:
        QMessageBox.critical(window, "Error", f"Error sending reports: {e}")

# Create the main application window
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Security Toolkit")
window.setGeometry(100, 100, 650, 500)  # Adjusted window size to give more space
window.setStyleSheet("background-color: #2C3E50;")  # Dark background for better contrast

# Create a layout for the main window
layout = QVBoxLayout()

# Add a heading label with a larger font
heading_label = QLabel("Security Toolkit")
heading_label.setStyleSheet("font: bold 24px Arial; color: #ECF0F1; padding: 20px;")
layout.addWidget(heading_label)

# Create a frame to organize the buttons
frame = QFrame(window)
frame.setStyleSheet("background-color: #2C3E50;")
frame_layout = QVBoxLayout()

# Button styling parameters (with hover effect)
button_style = """
    QPushButton {
        font: bold 12px Arial;
        height: 40px;
        width: 200px;
        background-color: #2980B9;
        color: white;
        border-radius: 5px;
        padding: 5px;
    }
    QPushButton:hover {
        background-color: #3498DB;
    }
"""

# Create buttons to run each script with custom styling
button_malware_scan = QPushButton("Run Malware Scan")
button_malware_scan.setStyleSheet(button_style)
button_malware_scan.clicked.connect(run_malware_scan)
frame_layout.addWidget(button_malware_scan)

button_privilege_audit = QPushButton("Run Privilege Audit")
button_privilege_audit.setStyleSheet(button_style)
button_privilege_audit.clicked.connect(run_privilege_audit)
frame_layout.addWidget(button_privilege_audit)

button_firewall_check = QPushButton("Run Firewall Check")
button_firewall_check.setStyleSheet(button_style)
button_firewall_check.clicked.connect(run_firewall_check)
frame_layout.addWidget(button_firewall_check)

button_patch_management = QPushButton("Run Patch Management")
button_patch_management.setStyleSheet(button_style)
button_patch_management.clicked.connect(run_patch_management)
frame_layout.addWidget(button_patch_management)

# Special button with different color
button_send_reports = QPushButton("Send Reports to Admin")
button_send_reports.setStyleSheet("""
    QPushButton {
        font: bold 12px Arial;
        height: 40px;
        width: 200px;
        background-color: #27AE60;
        color: white;
        border-radius: 5px;
        padding: 5px;
    }
    QPushButton:hover {
        background-color: #2ECC71;
    }
""")
button_send_reports.clicked.connect(send_reports)
frame_layout.addWidget(button_send_reports)

# Add the frame to the main layout
frame.setLayout(frame_layout)
layout.addWidget(frame)

# Add a footer label for additional info or instructions
footer_label = QLabel("© 2025 Security Toolkit | All Rights Reserved")
footer_label.setStyleSheet("font: 10px Arial; color: white;")
layout.addWidget(footer_label)

# Set the layout for the main window
window.setLayout(layout)

# Show the window
window.show()

# Run the application
sys.exit(app.exec_())
