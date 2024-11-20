import subprocess

VPN_NAME = "<Enter VPN name>"

def check_vpn_connection():
    try:
        # Check if the VPN is connected
        result = subprocess.run(['rasdial'], capture_output=True, text=True)
        if VPN_NAME in result.stdout:
            print("Prad says: VPN is still connected.")
            return True
        else:
            print("Prad says: VPN is disconnected. Attempting to reconnect...")
            return False
    except Exception as e:
        print(f"Error checking VPN connection: {e}")
        return False

def connect_vpn():
    try:
        result = subprocess.run(['rasdial', VPN_NAME], capture_output=True, text=True)
        if result.returncode == 0:
            print("Prad says: Successfully reconnected to", VPN_NAME)
        else:
            print("Prad says: Failed to reconnect to", VPN_NAME)
            print(result.stderr)
    except Exception as e:
        print(f"Error connecting to VPN: {e}")

if __name__ == "__main__":
    if not check_vpn_connection():
        connect_vpn()
