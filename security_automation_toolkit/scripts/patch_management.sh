#!/bin/bash

LOG_FILE="output/analysis_report.txt"
echo "[*] Running Patch Management Tool..." | tee -a "$LOG_FILE"
echo "------------------------------------" | tee -a "$LOG_FILE"
echo "[*] Date: $(date)" | tee -a "$LOG_FILE"
echo "" | tee -a "$LOG_FILE"

# Detect OS type
OS_TYPE="$(uname)"

if [[ "$OS_TYPE" == "Linux" ]]; then
    # Detect package manager and run updates
    if command -v apt > /dev/null; then
        echo "[+] Debian-based system detected" | tee -a "$LOG_FILE"
        sudo apt update | tee -a "$LOG_FILE"
        sudo apt list --upgradable | tee -a "$LOG_FILE"
        read -p "Install updates? (y/n): " resp
        if [[ $resp == "y" ]]; then
            sudo apt upgrade -y | tee -a "$LOG_FILE"
        fi

    elif command -v yum > /dev/null; then
        echo "[+] RHEL-based system detected" | tee -a "$LOG_FILE"
        sudo yum check-update | tee -a "$LOG_FILE"
        read -p "Install updates? (y/n): " resp
        if [[ $resp == "y" ]]; then
            sudo yum update -y | tee -a "$LOG_FILE"
        fi

    elif command -v brew > /dev/null; then
        echo "[+] macOS system detected" | tee -a "$LOG_FILE"
        brew update | tee -a "$LOG_FILE"
        brew outdated | tee -a "$LOG_FILE"
        read -p "Upgrade outdated packages? (y/n): " resp
        if [[ $resp == "y" ]]; then
            brew upgrade | tee -a "$LOG_FILE"
        fi
    else
        echo "[!] No supported package manager found" | tee -a "$LOG_FILE"
    fi

elif [[ "$OS_TYPE" == "Darwin" ]]; then
    echo "[+] macOS system detected" | tee -a "$LOG_FILE"
    brew update | tee -a "$LOG_FILE"
    brew outdated | tee -a "$LOG_FILE"
    read -p "Upgrade outdated packages? (y/n): " resp
    if [[ $resp == "y" ]]; then
        brew upgrade | tee -a "$LOG_FILE"
    fi

elif [[ "$OS_TYPE" == "MINGW32_NT"* ]] || [[ "$OS_TYPE" == "MINGW64_NT"* ]]; then
    # Check for Windows and apply updates via PowerShell
    echo "[+] Windows detected" | tee -a "$LOG_FILE"
    
    echo "[*] Checking for available updates on Windows..." | tee -a "$LOG_FILE"
    powershell -Command "Get-WindowsUpdate" | tee -a "$LOG_FILE"
    
    read -p "Install updates on Windows? (y/n): " resp
    if [[ $resp == "y" ]]; then
        echo "[*] Installing Windows updates..." | tee -a "$LOG_FILE"
        powershell -Command "Install-WindowsUpdate -AcceptAll -AutoReboot" | tee -a "$LOG_FILE"
    fi

else
    echo "[!] Unsupported OS: $OS_TYPE" | tee -a "$LOG_FILE"
fi

echo "" | tee -a "$LOG_FILE"
echo "[✓] Patch management task completed." | tee -a "$LOG_FILE"
