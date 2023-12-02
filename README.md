# TextEncryptionDecryption

## What does this code do?
This code allows you to generate a key using the Python Cryptography.Fernet module.
With the generated key you can either encrypt or decrypt the value. 

## Generating a key
The code will always ask if you want to generate a key when it runs. If you already
have a key you can choose to decline and the code will continue to run as usual.

## Encrypting Text
When encrypting text make sure your key does not include the bytes prefix that 
Python adds when generating a key as the code will not work with that prefix. 
When encyrpting the code will ask you the keyvalue you want to use when encrypting
the data, the text you want to encrypt, and the file path to save the text. 

## Decrypting text
When decrypting the data the code will ask you the key that will be used to decrypt
the data and the file path of the encrypted data.

## Example Key
If you don't want to generte a key using the code you can use this example key.
t4wlSjCPkjceEpDBJL2IQj56ZDuZVH1vj_EWZzl4Fe8=