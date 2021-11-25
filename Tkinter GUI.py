# Author: Cesar Vicente
# Date  : April 26, 2019
# Translates sentences to morse Code

import tkinter

def morseCode():
    morse = {'a':'.-', 'b':'-...','c':'-.-.',
             'd':'-..', 'e':'.','i':'..',
             'f':'..-.', 'g':'--.', 'h':'....',
             'j':'.---', 'k':'-.-','l':'.-..',
             'm':'--', 'n':'-.','o':'---',
             'p':'.--.', 'q':'--.-' ,'r':'.-.',
             's':'...', 't':'-','u':'..-',
             'v':'...-', 'w':'.--','x':'-..-',
             'y':'-.--', 'z':'--..',
             '1':'.----', '2':'..---', '3':'...--',
             '4':'....-', '5':'.....', '6':'-....',
             '7':'--...', '8':'---..', '9':'----.',
             '0':'-----',  ', ':'--..--', '.':'.-.-.-', 
             '?':'..--..', '/':'-..-.', '-':'-....-', 
             '(':'-.--.', ')':'-.--.-', ' ':'/'}

    myString = entInput.get().lower()
    letters = list(myString)
    translated = ""
    for code in letters:
        translated += (morse.get(code) + " ")
    entOutput.delete(0, tkinter.END)
    entOutput.insert(0, translated)

root = tkinter.Tk();
root.title("Translate to morse only.")
root.geometry("335x300")

lblDirections = tkinter.Label(root, text="Enter a text to be translated to morse code.")
entInput = tkinter.Entry(root)
entOutput = tkinter.Entry(root)
btnTranslate = tkinter.Button(root, text="Translate", command=morseCode)

#GUI Layout
lblDirections.grid(padx=5, pady=5)
entInput.grid(padx=5, pady=5)
btnTranslate.grid(padx=5, pady=5)
entOutput.grid(padx=5, pady=5)

#the quick brown fox jumps over the lazy dog
