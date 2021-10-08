from hashlib import sha256

def hash(s):
    return sha256(s.encode()).hexdigest()