from cryptography.fernet import Fernet

#function that accepts a key value, message, and file path to encrypt the data
def encryptMessage(key, message, path):
    key = Fernet(key.encode())
    encryptedMessage = key.encrypt(message.encode())
    file = open(path, "ab")
    file.write(encryptedMessage)

#function that accepts a key value and the path to decrypt the data
def decryptMessage(key, path):
    key = Fernet(key)
    file = open(path, "rb")
    encryptedMessage = file.read()
    decryptedMessage = key.decrypt(encryptedMessage).decode()
    return print("Decrypted Message ----> " + decryptedMessage)

loop = 0
while loop == 0:
    generateKeyChoice = input("Would you like to generate a key? (yes/no) ")

    if(generateKeyChoice.lower() == "yes"):
        #generates key with 'b' prefix
        generatedKey = Fernet.generate_key()
        #reformates the key without the 'b' prefix so that it can be used
        formattedKey = generatedKey.decode()
        print(formattedKey)
        loop = 1
    elif(generateKeyChoice.lower() == "no"):
        loop = 1
#Loop to ask the user to user if he wants to encrypt or decrypt a file
loop = 0
while loop == 0:
    choice = input("Would you like to encrypt or decrypt a message. Valid choices ---> (encrypt/decrypt) ")
    #if statement ignores case sensitivity
    if(choice.lower() == "encrypt" or choice.lower() == "decrypt"):
        loop = 1
    else:
        print("Please enter in a valid response")

loop = 0
while loop == 0:
    #if statement depending on if the user wants to encrypt or decrypt the message        
    if choice.lower() == "encrypt":
        keyValue = input("Enter the key that you will be using to encrypt the message ")
        message = input("Enter the message you would like to encrypt ")
        fileName = input("Enter the name of the file you would like the encyrpted message to reside on ")
        encryptMessage(keyValue, message, fileName)
        loop = 1
    elif choice.lower() == "decrypt":
        keyValue = input("Enter the key that you will be using to decrypt the file ")
        path = input("Enter the path or file name of the file you want to decyrpt ")
        decryptMessage(keyValue, path)
        loop = 1