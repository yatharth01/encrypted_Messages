
from nltk.corpus import words

#We have imported 'natural language toolkit' module to find meaningful decrypted message.

alphabets = 'abcdefghijklmnopqrstuvwxyz'
decrypted_message=''

print('Enter 1 to Encrypt and 2 to decrypt and 3 to exit:')

response= int(input())
while response is 1:
        encrypted_message = ''
        print('Enter your message')

        original_message=input()

        print('Choose an integer key for encryption ')
        key=int(input())

        #this key is used for shifting of alphabets.

        #below is the algorithm for encryption of message.

        for x in original_message:
            if x in alphabets:
                index=alphabets.find(x)
                new_position= (key+index)%26
                encrypted_character = alphabets[new_position]
                encrypted_message += encrypted_character
            else:
                encrypted_message += x

        print(encrypted_message)

        print('Enter 1 to ENCRYPT and 2 to DECRYPT and 3 to Exit :')
        response=int(input())

while response is 2:
    print('Enter message to decrypt:')
    k=0
    coded_message = input()

    for i in range(1,26):
        decrypted_message=''

        for x in coded_message:
            if x in alphabets:
                index=alphabets.find(x)
                new_position= (i+index)%26

                decrypted_character = alphabets[new_position]
                decrypted_message += decrypted_character
            else:
                decrypted_message += x

    #if the decoded message is present in the english dictionary it prints the message.

        if decrypted_message in words.words():
            print(decrypted_message)
            k=1
    if k is 0:
        print('No meaningful message found :( \n')
        print('Do you want me to show all decrypted codes?\n ENTER 1 FOR YES\n ENTER 0 FOR NO.')
        ans =int(input())
        if ans is 1:
            for j in range(1, 26):
                decrypted_message = ''

                for x in coded_message:
                    if x in alphabets:
                        index = alphabets.find(x)
                        new_position = (j + index) % 26

                        decrypted_character = alphabets[new_position]
                        decrypted_message += decrypted_character
                    else:
                        decrypted_message += x

                print(decrypted_message)

    print('Enter 1 to ENCRYPT and 2 to DECRYPT and 3 to Exit :')
    response = int(input())