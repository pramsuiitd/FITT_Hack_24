import hashlib
import os
import rsa
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class Encrypt:
    def __init__(self, srcID:str, publicKey):
        self.srcID = srcID
        self.publicKey = publicKey

    def encryptPayload(self,payload:str,destID:str):
        password = destID.encode()
        kdf = PBKDF2HMAC(
                algorithm=hashes.SHA256(),
                length = 16,
                iterations = 10000,
                )
        key = base64.urlsafe_b64encode(kdf.derive(password))
        f = Fernet(key)
        token = f.encrypt(payload.encode()) 
        return token

    def encryptDestID(self,destID:str):
        return int(hashlib.sha256((destID).encode()).hexdigest(),16)

    def encryptSrcID(self):
        return rsa.encrypt(self.srcID.encode(),self.publicKey)

class Decrypt:
    def __init__(self, srcID:str ,privateKey = None):
        self.srcID = srcID
        self.privateKey = privateKey
        
    def decryptPayload(self,destID:str,token):
        password = destID.encode()
        kdf = PBKDF2HMAC(
                algorithm = hashes.SHA256(),
                length = 16,
                iterations = 10000,
                )
        key = base64.urlsafe_b64encode(kdf.derive(password))
        f = Fernet(key)
        return f.decrypt(token)
    
    def decryptDestIDTrue(self,hashedDestID)->bool:
        ourHash = int(hashlib.sha256((self.srcID).encode()).hexdigest(),16)
        return (ourHash == hashedDestID)
    
    def decryptSrcID(self, encryptSrcID):
        return rsa.decrypt(encryptSrcID,self.privateKey)

