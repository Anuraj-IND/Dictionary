def l(a):
    if a in ['1', '2', '3',1,2,3]:
        return a
    else:
        return  a.lower()
import pyttsx3
from PyDictionary import PyDictionary
dictionary = PyDictionary()
def get_meaning(word):
    meaning = dictionary.meaning(word)
    return meaning
def speaker(a):
    spk=pyttsx3.init()
    spk.say(a)
    spk.runAndWait()
x= "yes"
while x == "yes":
    print("what operation you wants to perform???")
    print("1. Speak the word")
    print("2. Find the meaning of the word")
    print("3. Exit the program")
    ans =input("enter your operation name or number : ")
    ans=l(ans)    
    if ans in [1,"1", "speak", "speak the word"]:
       wd=input("Enter the Word : ")  
       speaker(wd)
    elif ans in [2,"2", "find", "find the meaning of the word"]:
        word = input("Enter a word: ")
        search=get_meaning(word)
        print(search)
        if search not in[None,""," "]:
          a=input("Do you want me to speak the meaning of your searched word? y/n  : ")  
          if a == "y":
            speaker(search)
          else:
            pass
    elif ans in [3,"3", "exit"]:
        print("thank you.....")
        x = "N"
    else:
        print("enter the valid option") 
