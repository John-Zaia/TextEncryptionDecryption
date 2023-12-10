# TextEncryptionDecryption

## How do I use this code
you can download the main.py file and run it with a python interpreter of your choice. 

## What does this code do?
This code allows you to generate a key using the Python Cryptography.Fernet module.
With the generated key you can either encrypt or decrypt the value. 

## Are there any arguments I have to specify before running the code?
No. The code doesn't require any arguments to run, you can just run the code which will
supply you with a command line interface where you can fill in what the code is asking
from you.

## Generating a key
The code will always ask if you want to generate a key when it runs. If you already
have a key you can choose to decline and the code will continue to run as usual.
An example of the code generating a key is shown below. With this key you can copy
it to your clipboard or save it to a file for multiple uses.
![Example Screenshot](/Images/generatingKey.PNG)

## Encrypting Text
When encrypting text make sure your key does not include the bytes prefix that 
Python adds when generating a key as the code will not work with that prefix. 
When encyrpting the code will ask you the key value you want to use when encrypting
the data, the text you want to encrypt, and the file path to save the text. A screenshot
of encrypting a piece of text is shown below. 
![Example Screenshot](/Images/encrypting.PNG)

## Decrypting text
When decrypting the data the code will ask you for the key that will be used to decrypt
the data and the file path of the encrypted data. An example is shown below
![Example Screenshot](/Images/decrypting.PNG)

## Example Key
If you don't want to generte a key using the code you can use this example key.
t4wlSjCPkjceEpDBJL2IQj56ZDuZVH1vj_EWZzl4Fe8=