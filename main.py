import cryptography

loop=0

#function that accepts a key value, message, and file path to encrypt the data
def encryptMessage(key, message, path):
    print()

#function that accepts a key value and the path to decrypt the data
def decryptMessage(key, path):
    print()

#Loop to ask the user to user if he wants to encrypt or decrypt a file
while loop == 0:
    choice = input("Would you like to encrypt or decrypt a message. Valid choices ---> (encrypt/decrypt) ")
    #if statement ignores case sensitivity
    if(choice.lower() == "encrypt" or choice.lower() == "decrypt"):
        loop = 1
    else:
        print("Please enter in a valid response")

#if statement depending on if the user wants to encrypt or decrypt the message        
if choice.lower() == "encrypt":
    keyValue = input("Enter the key that you will be using to encrypt the message")
    message = input("Enter the message you would like to encrypt")
    fileName = input("Enter the name of the file you would like the encyrpted message to reside on")
    encryptMessage(keyValue, message, fileName)
else:
    keyValue = input("Enter the key that you will be using to decrypt the file")
    path = input("Enter the path or file name of the file you want to decyrpt")
    decryptMessage(keyValue, path)