# Author: Sneaky Celery

import os
import sys
import hashlib
import datetime
import psutil

'''
    This script does not necessarily run at startup;
    you will have to set up a Task Scheduler to accomplish the intended results.
'''

SCRIPT_PATH = os.path.abspath(__file__)
HASH_FILE = os.path.join(os.path.dirname(SCRIPT_PATH), "Process_Analysis.hash")

# Check this script's integrity against known HASH
def calculate_hash(file_path):
    sha256 = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            while chunk := f.read(4096):
                sha256.update(chunk)
        return sha256.hexdigest()
    except Exception as e:
        print(f"Error reading script file: {e}")

# Check for existing Hash file
if os.path.exists(HASH_FILE):
    with open(HASH_FILE, "r") as f:
        expected_hash = f.read().strip()
else: 
    print("Hash file not found. Exiting.") 
    sys.exit(1)

current_hash = calculate_hash(SCRIPT_PATH)

if current_hash != expected_hash:
    print("WARNING: Script integrity check failed. Exiting.")
    sys.exit(1)

# Get Timesstamp
timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# Paths to logs
PA_log_dir = r"H:\Startup Logs"
PA_log_file = os.path.join(PA_log_dir, f"{timestamp}_proc.log")

if not os.path.exists(PA_log_dir):
    os.makedirs(PA_log_dir)

# The capture
process_list = []
svchost_paths = []

for proc in psutil.process_iter(attrs=['pid', 'name', 'exe']):
    pid = proc.info['pid']
    name = proc.info['name']
    path = proc.info['exe'] if proc.info['exe'] else "N/A"
    process_list.append(f"{pid}\t{name}")

    if name.lower() == "svchost.exe":
        svchost_paths.append(f"{pid}\t{name}\t{path}")

# Write the processes to the log file
with open(PA_log_file, "a") as f:
    f.write(f"\n=== Startup Log at {timestamp} ===\n")
    f.write("\n".join(process_list))
    f.write("\n\n")

    if svchost_paths:
        f.write("=== svchost.exe Instances and Paths ===\n")
        f.write("\n".join(svchost_paths))
        f.write("\n\n")
                          
