def encrypt(password: str, salt: str) -> str:
    """
    Encrypt the password using a simple character shift with the salt.
    """
    encrypted: str = ""
    key_len: int = len(salt)

    for index, char in enumerate(password):
        encrypted += chr(ord(char) + ord(salt[index % key_len]))

    return encrypted


def decrypt(encoded_pass: str, salt: str) -> str:
    """
    Decrypt the encoded password back to the original using the salt.
    """
    decrypted: str = ""
    key_len: int = len(salt)

    for index, char in enumerate(encoded_pass):
        decrypted += chr(ord(char) - ord(salt[index % key_len]))

    return decrypted


def main() -> None:
    """Run a simple demo."""
    password: str = input("Enter password: ")
    key: str = input("Enter key: ")

    encrypted: str = encrypt(password, key)
    decrypted: str = decrypt(encrypted, key)

    print("Encrypted password:", encrypted)
    print("Decrypted password:", decrypted)


if __name__ == "__main__":
    main()
