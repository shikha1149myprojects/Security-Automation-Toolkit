#!/bin/bash

echo "=============================="
echo " Security Automation Toolkit"
echo "=============================="

mkdir -p output

PS3="Select a task to run: "
options=("Log Analysis" "Privilege Audit" "Patch Management" "Malware Scan" "Inspect Firewall" "Notify Admin" "Exit")
select opt in "${options[@]}"; do
    case $opt in
        "Log Analysis")
            read -p "Enter path to log file: " logfile
            python3 scripts/analyze_logs.py "$logfile"
            ;;
        "Privilege Audit")
            python3 scripts/audit_privileges.py
            ;;
        "Patch Management")
            bash scripts/patch_management.sh
            ;;
        "Malware Scan")
            bash scripts/malware_scan.sh
            ;;
        "Inspect Firewall")
            bash scripts/inspect_firewall.sh
            ;;
        "Notify Admin")
            python3 scripts/notify_admin.py
            ;;
        "Exit")
            echo "Exiting..."
            break
            ;;
        *) echo "Invalid option";;
    esac
done
