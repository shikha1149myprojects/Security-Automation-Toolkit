#!/usr/bin/env python3
import subprocess
import platform
import os

OUTPUT_FILE = "output/privilege_audit.txt"

def get_sudo_users_linux():
    try:
        output = subprocess.check_output("grep '^sudo:.*$' /etc/group", shell=True)
        return output.decode().strip()
    except subprocess.CalledProcessError:
        return "No sudo group found."

def get_admin_users_mac():
    try:
        output = subprocess.check_output("dscl . -read /Groups/admin GroupMembership", shell=True)
        return output.decode().strip()
    except subprocess.CalledProcessError:
        return "No admin group found or dscl error."

def get_suid_binaries():
    try:
        find_command = "find / -perm -4000 -type f 2>/dev/null"
        output = subprocess.check_output(find_command, shell=True)
        return output.decode().splitlines()
    except subprocess.CalledProcessError:
        return ["Error retrieving SUID binaries."]

def get_admin_users_windows():
    try:
        # Get the list of local administrators using PowerShell
        powershell_command = "Get-LocalGroupMember -Group 'Administrators' | Select-Object -ExpandProperty Name"
        output = subprocess.check_output(["powershell", "-Command", powershell_command], shell=True)
        return output.decode().strip()
    except subprocess.CalledProcessError:
        return "No local admin group found or PowerShell error."

def get_windows_suid_binaries():
    try:
        # Searching for executables with system permissions
        find_command = "Get-ChildItem -Path C:\\ -Recurse -File -Security -ErrorAction SilentlyContinue | Where-Object { $_.IsReadOnly -eq $false }"
        output = subprocess.check_output(["powershell", "-Command", find_command], shell=True)
        return output.decode().splitlines()
    except subprocess.CalledProcessError:
        return ["Error retrieving SUID binaries."]

def main():
    os.makedirs("output", exist_ok=True)

    system = platform.system()

    with open(OUTPUT_FILE, "a") as f:
        f.write("\n===== Privilege Audit =====\n")

        if system == "Linux":
            f.write("== Sudo Users (Linux) ==\n")
            f.write(get_sudo_users_linux() + "\n\n")

        elif system == "Darwin":
            f.write("== Admin Users (macOS) ==\n")
            f.write(get_admin_users_mac() + "\n\n")

        elif system == "Windows":
            f.write("== Admin Users (Windows) ==\n")
            f.write(get_admin_users_windows() + "\n\n")
            f.write("== SUID Binaries (Windows) ==\n")
            for line in get_windows_suid_binaries():
                f.write(line + "\n")

        else:
            f.write("Unsupported OS for privilege auditing.\n\n")

        f.write("== SUID Binaries ==\n")
        for line in get_suid_binaries():
            f.write(line + "\n")

    print("[+] Privilege audit complete. Output saved to privilege_audit.txt")

if __name__ == "__main__":
    main()
