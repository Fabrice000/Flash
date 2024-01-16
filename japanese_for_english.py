from tkinter import *
import pandas
import random
from tkinter import messagebox
class JapaneseForEnglish:
    def __init__(self):
        try:
            self.data = pandas.read_csv("data/japanese_english_to_learn.csv")
        except FileNotFoundError:
            self.data = pandas.read_csv("data/japanese_english.csv")
            
        self.data_list = self.data.to_dict(orient='records')
        self.data_list1 = self.data_list.copy()
        self.BACKGROUND_COLOR = "#B1DDC6" 
        self.dictionary = {}
        self.window = Tk()

        self.window.title("Flashy")

        self.window.config(background=self.BACKGROUND_COLOR,padx=50,pady=50)

        self.after_time = self.window.after(3000,func=self.translate)


        self.image_background1 = PhotoImage(file= "image/Background1.png")
        self.image_background2 = PhotoImage(file="image/background2.png")
        self.canvas = Canvas(width=692,height=467,bg=self.BACKGROUND_COLOR,highlightthickness=0)
        self.canvas_image = self.canvas.create_image(346,234)
        self.canvas.grid(column=1,row=1,columnspan=2)
        self.language = self.canvas.create_text(346,150,text="", font=("Ariel",30,"italic"))
        self.word = self.canvas.create_text(346,234,text="", font=("Ariel",40,"bold"))
        self.change_word()


        
        # # entry
        # self.back_image = PhotoImage(file="image/back.png")
        # self.canvas2 = Canvas(width=350,height=448,bg=self.BACKGROUND_COLOR,highlightthickness=0)
        # self.canvas2.create_image(175,224,image=self.back_image)
        # self.canvas2.create_text(180,60,text="Japanese word:",font=("Ariel",20,"italic"))
        # self.canvas2.grid(column=3,row=1,rowspan=2)
        # self.new_word = Entry(width=15,font=("Ariel",14,"italic"))
        # self.new_word.grid(column=3,row=1)
        # self.canvas2.create_text(180,300,text="English definition:",font=("Ariel",20,"italic"))
        # self.new_word_definition = Entry(width=15,font=("Ariel",14,"italic"))
        # self.new_word_definition.grid(column=3,row=2)
        # self.add_button = Button(text="Add",font=("Ariel",24,"bold"),command=self.add_new_word)
        # self.add_button.grid(column=3,row=3)

        # button
        self.cross_image = PhotoImage(file="image/cross.png")
        self.cross_button = Button(image=self.cross_image,highlightthickness=0,command=self.change_word)
        self.cross_button.grid(column=1,row=2)
        self.ok_image = PhotoImage(file="image/ok.png")
        self.ok_button = Button(image=self.ok_image,highlightthickness=0,command=self.is_known)
        self.ok_button.grid(column=2,row=2)


        self.window.mainloop()
    # def add_new_word(self):
    #     if self.new_word.get() == "" or self.new_word_definition.get() == "":
    #         messagebox.showinfo(title="Oops",message="cna't not be a blank field")
    #     elif messagebox.askyesno(title="Save a new word",message=f"Save this word?\nWord:{self.new_word.get()}\nDefinition: {self.new_word_definition.get()}"):
    #         self.data_list1.append({"english":self.new_word.get(),"french":self.new_word_definition.get()})
    #         self.new_word.delete(0,END)
    #         self.new_word_definition.delete(0,END)
    #         self.data = pandas.DataFrame(self.data_list1)
    #         self.data.to_csv("data/japanese_english_to_learn.csv",index=False)
    #     else:
    #         pass
    def change_word(self):
        self.window.after_cancel(self.after_time)
        # word_dict = { {row.english:row.french} for (index,row) in data.iterrows()}
        # print(word_dict)
        self.dictionary = random.choice(self.data_list1)
        self.canvas.itemconfig(self.canvas_image,image=self.image_background1)
        self.canvas.itemconfig(self.language,text="Japanese",fill="black")
        self.canvas.itemconfig(self.word,text= self.dictionary["Japanese"],fill="black")
        self.after_time = self.window.after(3000,func=self.translate)
        

            
    def translate(self):
        
        self.canvas.itemconfig(self.canvas_image,image=self.image_background2)
        self.canvas.itemconfig(self.language,text="English",fill="white")
        self.canvas.itemconfig(self.word,text=self.dictionary["English"],fill="white")

    def is_known(self):
        self.data_list1.remove(self.dictionary)
        self.change_word()
        self.data = pandas.DataFrame(self.data_list1)
        self.data.to_csv("japanese_english_to_learn.csv",index=False)

            