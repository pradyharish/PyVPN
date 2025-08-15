import os
import subprocess
import datetime
import glob

VPN_NAME = <"Enter VPN name">
LOG_DIR = r"<Enter log file path>"
LOG_FILE = os.path.join(LOG_DIR, "Prad_vpn_log.txt")
MAX_LOGS = 10

# Function to get current timestamp
def get_timestamp():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S,%f")[:-3]

# Create log directory if it doesn't exist
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# Rotate logs
log_files = sorted(glob.glob(os.path.join(LOG_DIR, "*.txt")), key=os.path.getmtime, reverse=True)
for log_file in log_files[MAX_LOGS:]:
    os.remove(log_file)

# Redirect output to log file with timestamp
with open(LOG_FILE, "a", encoding='utf-8') as log:
    log.write(f"[{get_timestamp()}] Prad's Python script is checking if VPN is still connected. If not, then his script will attempt to connect... [thank Prad later]\n")
    
    # Check if VPN is connected
    result = subprocess.run(f'rasdial | findstr /C:"{VPN_NAME}"', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding='utf-8')
    
    if result.returncode != 0:
        log.write(f"[{get_timestamp()}] Prad says: VPN is disconnected. Attempting to reconnect...\n")
        
        # Attempt to reconnect
        result = subprocess.run(f'rasdial {VPN_NAME}', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding='utf-8')
        
        # Log both stdout and stderr for better debugging
        stdout_output = result.stdout.strip() if result.stdout else ""
        stderr_output = result.stderr.strip() if result.stderr else ""
        
        log.write(f"[{get_timestamp()}] Prad says: rasdial command return code: {result.returncode}\n")
        
        if stdout_output:
            log.write(f"[{get_timestamp()}] Prad says: Command output: {stdout_output}\n")
        
        if stderr_output:
            log.write(f"[{get_timestamp()}] Prad says: Command error: {stderr_output}\n")
        
        if result.returncode != 0:
            # rasdial often outputs error messages to stdout, not stderr
            error_message = stderr_output or stdout_output or "Unknown error"
            log.write(f"[{get_timestamp()}] Prad says: Failed to reconnect to {VPN_NAME}. Error: {error_message}\n")
        else:
            log.write(f"[{get_timestamp()}] Prad says: Successfully reconnected to {VPN_NAME}.\n")
    else:
        log.write(f"[{get_timestamp()}] Prad says: VPN is still connected.\n")
    
    # Flush the log to ensure it's written immediately
    log.flush()
