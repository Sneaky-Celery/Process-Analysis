# Process-Analysis
# I created my own tool to generate a log for expected system behavior to familiarize myself with process analysis. I added a feature to display the PATH of common process names like svchost.exe where malicious processes often hide.
# This is intended to function across platforms.
# The script is intended to be automated, so I have a hash generator and comparison helper files that will shutdown the script if the hash does not match what is expected. You will have to store the hash somewhere safe and specify that location to the script yourself.
