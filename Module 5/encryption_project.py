#Nick Wendel
#IT - 75
#10/3/19
#Encryption Project


#Part 1: Caesar Cipher

#BKFTAZDAOWE
#A == O

#ABCDEFGHIJKLMNOPQRSTUVWXYZ
#OPQRSTUVWXYZABCDEFGHIJKLMN

#PYTHONROCKS


#Part 2: 
#This program will encrypt the entered plaintext message

alphabet = 'abcdefghijklmnopqrstuvwxyz'
def caesar(plaintext, shift):
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted_alphabet)
    return plaintext.translate(table)

print('Enter Message: ')    
plain = str(input())        #thequickbrownfoxjumpsoverthelazydog
print()
print('Enter Shift: ')      
shift = int(input())        #13
print()
coded = caesar(plain,shift)
print('Encrypted Message:')
print(coded)
ciphertext = coded
print()
print()


#Part 3:
#This program will decrypt the entered ciphertext
#This program will print the message for every possible shift

alphabet = "abcdefghijklmnopqrstuvwxyz"
shift = str.maketrans(alphabet, alphabet[1:] + alphabet[0])

print('Enter Encrypted Message: ')
encrypted = input()         #dzeevjfkrlezkvuwffksrcctcls
print()

print('Messages for each shift:')
for i in alphabet:          #This loop will run each possible shift
    print(encrypted)
    encrypted = encrypted.translate(shift)
print()
print()
    
#The message was properly decoded with a shift of 17
#The decrypted message is 'minnesotaunitedfootballclub'


#Part 4:
#This program will encrypt a message with a jumbled key

alphabet = 'abcdefghijklmnopqrstuvwxyz '
key = 'mwgp bdzxrylacsokjfhtnueivq'
plaintext = 'of shoes and ships and sealing wax of cabbages and kings'
ciphertext = ''

print('Message to be encrypted:')
print(plaintext)
print()

for character in plaintext:
    if character in alphabet:
        num = alphabet.find(character)
        ciphertext += key[num]

print('Encrypted message:')
print(ciphertext)
print()
print()


#Part 5:
#This program will decrypt a message encrypted with a jumbled key

alphabet = 'abcdefghijklmnopqrstuvwxyz '
key = 'mwgp bdzxrylacsokjfhtnueivq'
ciphertext = 'hz qftcqumfqfzxcxcdqscqhz qf mqfzxcxcdquxhzqmllqzxfqaxdzh'
plaintext = ''

print('Encrypted message:')
print(ciphertext)
print()

for character in ciphertext:
    if character in key:
        num = key.find(character)
        plaintext += alphabet[num]

print('Decrypted message:')
print(plaintext)
print()
print()


#Part 6:
#This program allows to the user to create their own encryption key

alphabet = 'abcdefghijklmnopqrstuvwxyz '
ciphertext = ''
plaintext = ''

print('***Custom Key Encryption Machine*** \n')
print()
print('Hello! Enter your own cipher key to begin. \n')
print('NOTE: Use letters a-z and "space" once each! \n')
print()
key = input('Custom Key: ')
print()
message = input('Great! Now enter your message: ')
print()
answer = input('Ok, last thing! Whould you like to encrypt or decrypt your message? ')
print()
print('Here we go!')
print()

for i in range (6):
    print('* \n')
    
if answer == 'encrypt':
    for character in message:
        if character in alphabet:
           num = alphabet.find(character)
           ciphertext += key[num]
    print('Here is your encrypted message! \n')
    print(ciphertext)

elif answer == 'decrypt':
    for character in message:
        if character in key:
            num = key.find(character)
            plaintext += alphabet[num]
    print('Here is your decrypted message! \n')
    print(plaintext)

print()
print()
print()
print('Thank you for using the "Custom Encryption Machine"!!')
