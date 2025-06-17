import socket
from cryptography.fernet import Fernet

# Step 1: Load the shared encryption key from file
with open("key.key", "rb") as key_file:
    key = key_file.read()
fernet = Fernet(key)

# Step 2: Connect to server (update IP if needed)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 5000))  # Change IP to server's IP if needed

try:
    while True:
        # Step 3: Get user message, encrypt it, send to server
        msg = input("You: ")
        enc_msg = fernet.encrypt(msg.encode())
        client.sendall(enc_msg)

        # Step 4: Receive encrypted reply from server, decrypt and print
        enc_reply = client.recv(1024)
        if not enc_reply:
            break
        reply = fernet.decrypt(enc_reply).decode()
        print(f"Server: {reply}")
finally:
    # Step 5: Clean up socket
    client.close()
