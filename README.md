# 🔒 Encrypted Chat App (Basic)

A simple Python chat app using sockets and symmetric encryption (Fernet) for secure messaging on a LAN.

## 🚀 Features
- End-to-end encrypted messages between two users
- Simple command-line interface

## 🛠️ Requirements
- Python 3.x
- `pip install cryptography`

## ⏳ Usage

1. **Generate the key (run once):**
   ```python
   from cryptography.fernet import Fernet
   key = Fernet.generate_key()
   with open("key.key", "wb") as key_file:
       key_file.write(key)
   ```
   Move `key.key` to both server and client machines.

2. **Run the server:**
   ```bash
   python chat_server.py
   ```
3. **Run the client (on another terminal or machine):**
   ```bash
   python chat_client.py
   ```
4. Start chatting securely!

**Note:**  
- Both server and client must have the same `key.key` file.
- For LAN use only. For real-world use, add authentication and stronger key exchange!

---

**For educational purposes only.**
