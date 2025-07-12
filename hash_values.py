import hashlib


def compute_hashes(input_string):
    # MD5 Hash Computation
    md5_hash = hashlib.md5(input_string.encode()).hexdigest()

    # SHA-256 Hash Computation
    sha256_hash = hashlib.sha256(input_string.encode()).hexdigest()

    return md5_hash, sha256_hash


# Strings to hash
strings_to_hash = ["Cryptography", "Hash Functions", "INT306"]

# Loop through and display hashes
for string in strings_to_hash:
    md5, sha256 = compute_hashes(string)
    print(f"String: {string}")
    print(f"MD5: {md5}")
    print(f"SHA-256: {sha256}")
    print("-" * 50)
