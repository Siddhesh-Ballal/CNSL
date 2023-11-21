import hashlib
message = input("Enter the message: ")
message_digest = hashlib.sha1(message.encode()) 
print("The hexadecimal equivalent of SHA1 hash is : ", message_digest.hexdigest()) 
