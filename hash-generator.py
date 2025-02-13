# Author: Sneaky Celery

import hashlib
import os
import stat

'''
For testing, I set HASH_FILE path to the same directory as my target script.
Once verified, you may want to move the .hash to a secure directory.
For readability, I use the name of a script as the name of the hash file that will be created.
Always verify your paths. You may want to use a different naming system, this is only an example.
NOTE: the Read-Only functionality for the hash file permission needs expansion and doesn't work for windows and linux is untested.
'''

# I used the generated hash to verify script integrity
SCRIPT_PATH = "E:\\Path\\To\\Your\\Script.py"
HASH_FILE = "E:\\Path\\For\\Generated\\Hash\\File.hash"

def calculate_hash(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        while chunk := f.read(4096):
            sha256.update(chunk)
    return sha256.hexdigest()

# Generate the hash and store it in a file
script_hash = calculate_hash(SCRIPT_PATH)

with open(HASH_FILE, "w") as f:
    f.write(script_hash)

# Make the Hash read only
def set_hash_permissions(file_path):
    if os.name == 'nt': #for Windows
        os.chmod(file_path, stat.S_IREAD)
    else: #for Linux/Mac
        os.chmod(file_path, 0o444)

print(f"Hash saved to {HASH_FILE}: {script_hash}")
