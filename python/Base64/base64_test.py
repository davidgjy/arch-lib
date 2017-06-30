import base64
import sys
import os

def encode(message):
    encodeStr = message.encode(encoding="utf-8")
    return base64.b64encode(encodeStr)

def decode(encoded):
    decodeStr = base64.b64decode(encoded)
    return decodeStr.decode()

def main():
    srcStr = "fuck123789"
    print('source string: %s' % srcStr)
    encryptStr = encode(srcStr)
    print('encrypt string: %s' % encryptStr)
    decryptStr = decode(encryptStr)
    print('decrypt string: %s' % decryptStr)    
    
                        
if __name__ == '__main__':
    main()    
    
        
          
