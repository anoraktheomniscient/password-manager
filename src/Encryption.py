try:
    from Crypto.Protocol.KDF import PBKDF2

    from Crypto.Cipher import AES
    from Crypto.Util.Padding import pad, unpad
    
    from json import loads, dumps
except:
    raise ImportError("Import of modules failed")

class Encryption:
    def __init__(self, filePath: str, password: str) -> None:
        self.filePath = filePath
        self.salt = b'L\xa9\xaed\x1e\xa5\xdc,\xa8\xb3\x00\xc3Gf\x8c\xf4\xe5\x9f7@\\\x8b\xf0\xcb\xc9\x13\xb6\x01\xed\xfaB\xf6'
        
        self.key = PBKDF2(password=password, salt=self.salt, dkLen=32)
    
    def encrypt(self, message: str) -> None:
        message = dumps(message)
        cipher = AES.new(key=self.key, mode=AES.MODE_CBC)
        encrypted_data = cipher.encrypt(pad(bytes(message, 'utf-8'), AES.block_size))
        
        with open(self.filePath, 'wb') as file:
            file.write(cipher.iv)
            file.write(encrypted_data)
            file.close()
    
    def decrypt(self) -> dict:
        with open(self.filePath, 'rb') as file:
            iv = file.read(16)
            data = file.read()
            file.close()
        
        cipher = AES.new(key=self.key, mode=AES.MODE_CBC, iv=iv)
        decrypted_data = unpad(cipher.decrypt(data), AES.block_size).decode('utf-8')
        
        return loads(decrypted_data)