
from nltk.corpus import words as ntlk_words

alphabets = 'abcdefghijklmnopqrstuvwxyz'
decrypted_message=''

print('Enter 1 to Encrypt and 2 to decrypt :')
response= int(input())
if response is 1:
    encrypted_message = ''
    print('Enter your message')

    original_message=input()

    print('Choose an integer key for encryption ')
    key=int(input())

    for x in original_message:
        if x in alphabets:
            index=alphabets.find(x)
            new_position= (key+index)%26
            encrypted_character = alphabets[new_position]
            encrypted_message += encrypted_character
        else:
            encrypted_message += x

    print(encrypted_message)

elif response is 2:
    print('Enter message to decrypt:')
    coded_message = input()
    for i in range(1,26):
        decrypted_message=''
        for x in coded_message:
            if x in alphabets:
                index=alphabets.find(x)
               # print(index)
                new_position= (i+index)%26
                #print(new_position)
                decrypted_character = alphabets[new_position]
                decrypted_message += decrypted_character
            else:
                decrypted_message += x

        print(decrypted_message)
