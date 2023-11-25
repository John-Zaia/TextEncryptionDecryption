import cryptography

loop=0

#Loop to ask the user to user if he wants to encrypt or decrypt a file
while loop == 0:
    choice = input("Would you like to encrypt or decrypt a message. Valid choices ---> (encrypt/decrypt) ")
    #if statement ignores case sensitivity
    if(choice.lower() == "encrypt" or choice.lower() == "decrypt"):
        loop = 1
    else:
        print("Please enter in a valid response")