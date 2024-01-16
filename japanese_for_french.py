from tkinter import *
import pandas
import random
class JapaneseForFrench:
    def __init__(self):
        
        try:
            self.data = pandas.read_csv("data/japanese_french_to_learn.csv")
        except FileNotFoundError:
            self.data = pandas.read_csv("data/japanese_french_data.csv")
            
        self.data_list = self.data.to_dict(orient='records')
        self.data_list1 = self.data_list.copy()
        self.BACKGROUND_COLOR = "#B1DDC6" 
        self.dictionary = {}
        self.window = Tk()

        self.window.title("Flashy")

        self.window.config(background=self.BACKGROUND_COLOR,padx=50,pady=30)

        self.after_time = self.window.after(5000,func=self.translate)


        self.image_background1 = PhotoImage(file= "image/Background1.png")
        self.image_background2 = PhotoImage(file="image/Background2.png")
        self.canvas = Canvas(width=692,height=467,bg=self.BACKGROUND_COLOR,highlightthickness=0)
        self.canvas_image = self.canvas.create_image(346,235)
        self.canvas.grid(column=1,row=1,columnspan=2)
        self.language = self.canvas.create_text(346,180,text="", font=("Ariel",40,"italic"))
        self.word = self.canvas.create_text(346,280,text="", font=("Ariel",45,"bold"))
        self.langauage_pronounciation = self.canvas.create_text(346,350,text="", font=("Ariel",30,"bold"))

        self.change_word()


        # button
        self.cross_image = PhotoImage(file="image/cross.png")
        self.cross_button = Button(image=self.cross_image,highlightthickness=0,command=self.change_word)
        self.cross_button.grid(column=1,row=2)
        self.ok_image = PhotoImage(file="image/ok.png")
        self.ok_button = Button(image=self.ok_image,highlightthickness=0,command=self.is_known)
        self.ok_button.grid(column=2,row=2)
        
        # self.canvas1 = Canvas(self.window, width=200,height=420, background="white")
        # self.canvas1.create_text(100,110,text="Salut",font=("Ariel",24,"italic"))
        # self.canvas1.grid(row=1,column=3,columnspan=2)
        # self.entry = Entry(width=15,background="white")
        # self.entry.grid(row=1,column=3,padx=10,pady=(10,0))
        
        
        self.window.mainloop()
        
        
        
    def change_word(self):
        self.window.after_cancel(self.after_time)
        # word_dict = { {row.english:row.french} for (index,row) in data.iterrows()}
        # print(word_dict)
        self.dictionary = random.choice(self.data_list1)
        self.canvas.itemconfig(self.canvas_image,image=self.image_background1)
        self.canvas.itemconfig(self.language,text="Japanese",fill="black")
        self.canvas.itemconfig(self.langauage_pronounciation,text=self.dictionary["ROMAJI"])
        self.canvas.itemconfig(self.word,text= self.dictionary["JAPONAIS"],fill="black")
        self.after_time = self.window.after(3000,func=self.translate)
        

        
    def translate(self):
        
        self.canvas.itemconfig(self.canvas_image,image=self.image_background2)
        self.canvas.itemconfig(self.language,text="French",fill="white")
        self.canvas.itemconfig(self.langauage_pronounciation,text="")
        self.canvas.itemconfig(self.word,text=self.dictionary["FRANÇAIS"],fill="white")

    def is_known(self):
        self.data_list1.remove(self.dictionary)
        self.change_word()
        self.data = pandas.DataFrame(self.data_list1)
        self.data.to_csv("data/japanese_french_to_learn.csv",index=False)

        






