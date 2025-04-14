import hashlib

def generate_hash(filepath):
    with open(filepath, 'rb') as f:
        content = f.read()
        return hashlib.sha256(content).hexdigest()

# Example usage
if __name__ == "__main__":
    path = input("Enter file path: ")
    print("SHA256:", generate_hash(path))
