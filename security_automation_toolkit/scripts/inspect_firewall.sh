#!/bin/bash

OUTPUT_DIR="output"
OUTPUT_FILE="${OUTPUT_DIR}/firewall_rules.txt"

mkdir -p "$OUTPUT_DIR"
echo "[*] Detecting system firewall rules..." | tee "$OUTPUT_FILE"
echo "-----------------------------------" >> "$OUTPUT_FILE"

OS_TYPE="$(uname)"

if [[ "$OS_TYPE" == "Linux" ]]; then
    if command -v ufw &> /dev/null; then
        echo "[*] UFW detected on Linux..." | tee -a "$OUTPUT_FILE"
        ufw status verbose >> "$OUTPUT_FILE"
    elif command -v iptables &> /dev/null; then
        echo "[*] iptables detected on Linux..." | tee -a "$OUTPUT_FILE"
        iptables -L -v -n >> "$OUTPUT_FILE"
    else
        echo "[!] No supported firewall found (UFW or iptables)." | tee -a "$OUTPUT_FILE"
    fi

elif [[ "$OS_TYPE" == "Darwin" ]]; then
    echo "[*] macOS detected..." | tee -a "$OUTPUT_FILE"
    
    echo "=== Packet Filter (pf) Status ===" >> "$OUTPUT_FILE"
    sudo pfctl -sr >> "$OUTPUT_FILE" 2>/dev/null

    echo -e "\n=== macOS Application Firewall ===" >> "$OUTPUT_FILE"
    /usr/libexec/ApplicationFirewall/socketfilterfw --getglobalstate >> "$OUTPUT_FILE"
    /usr/libexec/ApplicationFirewall/socketfilterfw --listapps >> "$OUTPUT_FILE"

elif [[ "$OS_TYPE" == "MINGW32_NT"* ]] || [[ "$OS_TYPE" == "MINGW64_NT"* ]]; then
    echo "[*] Windows detected..." | tee -a "$OUTPUT_FILE"

    echo "=== Windows Firewall Rules ===" >> "$OUTPUT_FILE"
    powershell -Command "Get-NetFirewallRule | Format-Table Name, Enabled, Direction, Action, Profile" >> "$OUTPUT_FILE" 2>/dev/null

else
    echo "[!] Unsupported OS: $OS_TYPE" | tee -a "$OUTPUT_FILE"
fi

echo "[✓] Firewall rules saved to ${OUTPUT_FILE}"
