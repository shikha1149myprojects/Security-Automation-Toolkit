#!/usr/bin/env python3
import re
import argparse
from datetime import datetime
from collections import defaultdict

parser = argparse.ArgumentParser(description="Log Analysis Tool")
parser.add_argument("logfile", help="Path to the log file")
args = parser.parse_args()

failures = defaultdict(int)
with open(args.logfile, 'r') as log:
    for line in log:
        if "Failed password" in line:
            ip = re.findall(r'from (\d+\.\d+\.\d+\.\d+)', line)
            if ip:
                failures[ip[0]] += 1

# Save report
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open("output/analysis_report.txt", "w") as out:
    out.write(f"Log Analysis Report - {timestamp}\n\n")
    for ip, count in failures.items():
        if count > 5:
            out.write(f"[ALERT] {ip} had {count} failed attempts\n")
        else:
            out.write(f"{ip} had {count} failed attempts\n")
print("[+] Log analysis complete. Report saved.")
