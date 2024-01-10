import hashlib
import os
import rsa
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class Encrypt:
    def __init__(self,password:str,srcID:str,publicKey):
        self.password = password
        self.srcID = srcID
        self.publicKey = publicKey

    def encryptPayload(self,payload:str,destID:str):
        password = destID.encode()
        kdf = PBKDF2HMAC(
                algorithm=hashes.SHA256(),
                length = 16
                iterations = 10000,
                )
        key = base64.urlsafe_b64encode(kdf.derive(password))
        f = Fernet(key)
        token = f.encrypt(payload.encode()) 
        return token

    def encryptDestID(self,destID:str):
        return int(hashlib.sha256((destID).encode()).hexdigest(),16)

    def srcID(self):
        return rsa.encrypt(self.srcID.encode(),self.publicKey)

class Decrypt:
    def __init__(self,password:str,srcID:str,privateKey):
        self.password = password
        self.srcID = srcID
        self.privateKey = privateKey
        
    def decryptPayload(self,destID:str):
        password = destID.encode()
        kdf = PBKDF2HMAC(
                algorithm = hashes.SHA256(),
                length = 16,
                iterations = 10000,
                )


