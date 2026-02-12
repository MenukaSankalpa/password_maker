import bcrypt
import pyperclip

# 🔹 Type your original password here
password = "Deshapriya@321##"

# Convert to bytes
password_bytes = password.encode('utf-8')

# Generate salt
salt = bcrypt.gensalt()

# Hash password
hashed = bcrypt.hashpw(password_bytes, salt).decode()

# Copy to clipboard
pyperclip.copy(hashed)

print("✅ Bcrypt Hashed Password:")
print(hashed)
print("\n📋 Hash copied to clipboard!")
