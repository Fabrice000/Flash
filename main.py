#PLAN 
# Combiner les quetres flash card sans accro!
from french_for_english import FrenchForEnglish
from english_for_french import EnglishForFrench
from japanese_for_english import JapaneseForEnglish
from japanese_for_french import JapaneseForFrench
from tkinter import *
BACKGROUND_COLOR = "#B1DDC6" 
def selection():
    choice =  option.get()
    if choice == "French for English":
        root.destroy()
        FrenchForEnglish()
    elif choice == "English for French":
        root.destroy()
        EnglishForFrench()
    elif choice == "Japanese for French":
        root.destroy()
        JapaneseForFrench()
    else:
        root.destroy()
        JapaneseForEnglish()
root = Tk()
root.title("Choice your Option!")
root.minsize(width=200,height=200)
root.config(background="#B1DDC6",padx=20,pady=20)
option = StringVar()

choice1 = Radiobutton(root,
                      text="french for english",
                      variable=option,
                      value="French for English",
                      command=selection,
                      font=("Ariel",24,"italic"),
                      background=BACKGROUND_COLOR,
                      highlightthickness=0,
                      padx=10,pady=10)
choice1.pack()
choice2 = Radiobutton(root,
                      text="english for french",
                      variable=option,
                      textvariable="salut",
                      value="English for French",
                      command=selection,
                      font=("Ariel",24,"italic"),
                      background=BACKGROUND_COLOR,
                      highlightthickness=0,
                      padx=10,pady=10)
choice2.pack()
choice3 = Radiobutton(root,
                      text="japanese for english",
                      variable=option,
                      value="Japanese for English",
                      command=selection,
                      font=("Ariel",24,"italic"),
                      background=BACKGROUND_COLOR,
                      highlightthickness=0,
                      padx=10,pady=10)
choice3.pack()
choice4 = Radiobutton(root,
                      text="japanese for French",
                      variable=option,
                      value="Japanese for French",
                      command=selection,
                      font=("Ariel",24,"italic"),
                      background=BACKGROUND_COLOR,
                      highlightthickness=0,
                      padx=10,pady=10)
choice4.pack()

root.mainloop()


