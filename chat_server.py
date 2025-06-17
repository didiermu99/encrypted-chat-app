import socket
from cryptography.fernet import Fernet

# Step 1: Load the shared encryption key from file
with open("key.key", "rb") as key_file:
    key = key_file.read()
fernet = Fernet(key)

# Step 2: Set up server socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 5000))  # Listen on all interfaces, port 5000
server.listen(1)
print("Server listening on port 5000...")

# Step 3: Accept connection from a client
conn, addr = server.accept()
print(f"Connected to {addr}")

try:
    while True:
        # Step 4: Receive encrypted message from client
        enc_msg = conn.recv(1024)
        if not enc_msg:
            break

        # Step 5: Decrypt the received message
        msg = fernet.decrypt(enc_msg).decode()
        print(f"Client: {msg}")

        # Step 6: Get reply from server user, encrypt it, send to client
        reply = input("You: ")
        enc_reply = fernet.encrypt(reply.encode())
        conn.sendall(enc_reply)
finally:
    # Step 7: Clean up sockets
    conn.close()
    server.close()
