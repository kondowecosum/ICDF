import hashlib

common_passwords = [
    "password", "123456", "qwerty", "letmein", "welcome",
    "monkey", "dragon", "master", "admin", "login"
]

def create_rainbow_table(passwords):
    rainbow_table = []
    for password in passwords:
        md5_hash = hashlib.md5(password.encode()).hexdigest()
        sha256_hash = hashlib.sha256(password.encode()).hexdigest()
        rainbow_table.append({
            "password": password,
            "md5": md5_hash,
            "sha256": sha256_hash
        })
    return rainbow_table

def save_rainbow_table(table, filename):
    with open(filename, "w") as file:
        file.write("Password,MD5,SHA-256\n")
        for entry in table:
            file.write(f"{entry['password']},{entry['md5']},{entry['sha256']}\n")
    print(f"[INFO] Rainbow table saved to '{filename}'")

def crack_hash(target_hash, rainbow_table, hash_type="md5"):
    for entry in rainbow_table:
        if entry[hash_type] == target_hash.lower():
            return entry["password"]
    return None

def main():
    print("=== Rainbow Table Generator & Hash Cracker ===\n")

    # Step 1: Generate rainbow table
    rainbow_table = create_rainbow_table(common_passwords)
    print("[INFO] Rainbow table created with common passwords.\n")

    # Step 2: Save to file
    save_option = input("Do you want to save the rainbow table to a file? (y/n): ").strip().lower()
    if save_option == "y":
        filename = input("Enter filename (e.g., rainbow_table.csv): ").strip()
        save_rainbow_table(rainbow_table, filename)

    # Step 3: Interactive hash cracking
    while True:
        print("\n--- Hash Cracker ---")
        print("Supported hash types: md5, sha256")
        hash_type = input("Enter hash type: ").strip().lower()
        if hash_type not in ["md5", "sha256"]:
            print("[ERROR] Unsupported hash type! Please enter 'md5' or 'sha256'.")
            continue

        target_hash = input("Enter the hash to crack: ").strip()
        cracked_password = crack_hash(target_hash, rainbow_table, hash_type)

        if cracked_password:
            print(f"[SUCCESS] Password found: '{cracked_password}'")
        else:
            print("[FAIL] Password not found in rainbow table.")

        again = input("Try another hash? (y/n): ").strip().lower()
        if again != "y":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
