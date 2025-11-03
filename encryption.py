import hashlib 

def encrypt(data):
    data= hashlib.sha256(data.encode())
    data= data.hexdigest()
    return data