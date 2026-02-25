import bcrypt
import pyperclip
import getpass
import sys

def hash_password(password: str, rounds: int = 12) -> str:
    """
    Hash a password using bcrypt.
    
    :param password: Plain text password
    :param rounds: Cost factor (default 12, secure standard)
    :return: Hashed password string
    """
    password_bytes = password.encode("utf-8")
    salt = bcrypt.gensalt(rounds=rounds)
    hashed = bcrypt.hashpw(password_bytes, salt)
    return hashed.decode("utf-8")


def main():
    try:
        print("🔐 Secure Password Hasher (Bcrypt)\n")

        # Hidden password input
        password = getpass.getpass("Enter password: ")

        if not password:
            print("❌ Password cannot be empty!")
            sys.exit(1)

        hashed_password = hash_password(password)

        # Copy to clipboard
        pyperclip.copy(hashed_password)

        print("\n✅ Hashed Password:")
        print(hashed_password)
        print("\n📋 Hash copied to clipboard!")

    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()