from _tkinter import *
from tkinter import Label, Entry, Button, mainloop, Tk, Spinbox
from tkinter.simpledialog import askstring, askinteger
from nltk.corpus import words

alphabets = 'abcdefghijklmnopqrstuvwxyz'
decrypted_message = ''


def decrypt(coded_message,i):

    decrypted_message=''

    for x in coded_message:
        if x in alphabets:
             index=alphabets.find(x)
             new_position= (i+index)%26

             decrypted_character = alphabets[new_position]
             decrypted_message += decrypted_character
        else:
            decrypted_message += x

    return decrypted_message


def encrypt_window(message):
    global key_encrypt
    key_encrypt = askinteger('Enter Integer', 'Please enter an integer')

    def encrypt(message,key_encrypt):
        encrypted_message = ''
        original_message = message
        # this key is used for shifting of alphabets.

        # below is the algorithm for encryption of message.

        for x in original_message:
            if x in alphabets:
                index = alphabets.find(x)
                new_position = (key_encrypt + index) % 26
                encrypted_character = alphabets[new_position]
                encrypted_message += encrypted_character
            else:
                encrypted_message += x
        new_master = Tk()
        Label(new_master, text="Your Encrypted Message is:\n").grid(row=3)
        Label(new_master, text=encrypted_message).grid(row=4)

    encrypt(message, key_encrypt)

def decoded(coded_message):
    window2=Tk()
    k=0
    i = 1
    rower =7
    for i in range(1, 26):
        decoded = decrypt(coded_message,i)

    #if the decoded message is present in the english dictionary it prints the message.
        Label(window2, text="Results::").grid(row=5)


        if decoded in words.words():
            rower = rower + 1
            Label(window2,text=decoded).grid(row=rower)
            k = 1


    if k is 0:
        rower = rower + 1
        Label(window2, text="No meaningful message found..:(").grid(row=rower)



master = Tk()
Label(master, text="MESSAGE").grid(row=3)

e1 = Entry(master)
e1.grid(row=3, column=1)
Button(master, text='Encrypt', command=lambda: encrypt_window(e1.get())).grid(row=4, column=0, pady=4)
Button(master, text='Decrypt', command=lambda: decoded(e1.get())).grid(row=4, column=1, pady=4)

mainloop()

