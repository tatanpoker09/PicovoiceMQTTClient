import wakeonlan
import os


def change_server_status(status):
    if status == "on":
        wakeonlan.send_magic_packet(os.getenv("SERVER_MAC_ADDRESS"))
    elif status == "off":
        ssh_key_path = os.getenv("SSH_KEY_PATH")
        server_username = os.getenv("SSH_USER")
        server_ip_address = os.getenv("SERVER_IP_ADDRESS")
        os.system(f"ssh -i {ssh_key_path} -o StrictHostKeyChecking=no {server_username}@{server_ip_address} "
                  f"'sudo -S poweroff'")
