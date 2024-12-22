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
with open(LOG_FILE, "a") as log:
    log.write(f"[{get_timestamp()}] Prad's Python script is checking if VPN is still connected. If not, then his script will attempt to connect... [thank Prad later]\n")
    result = subprocess.run(f'rasdial | findstr /C:"{VPN_NAME}"', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode != 0:
        log.write(f"[{get_timestamp()}] Prad says: VPN is disconnected. Attempting to reconnect...\n")
        result = subprocess.run(f'rasdial {VPN_NAME}', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode != 0:
            error_message = result.stderr.decode('utf-8').strip()
            log.write(f"[{get_timestamp()}] Prad says: Failed to reconnect to {VPN_NAME}. Error: {error_message}\n")
        else:
            log.write(f"[{get_timestamp()}] Prad says: Successfully reconnected to {VPN_NAME}.\n")
    else:
        log.write(f"[{get_timestamp()}] Prad says: VPN is still connected.\n")
