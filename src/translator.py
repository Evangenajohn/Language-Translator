from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

root=Tk()
root.geometry('1100x320')
root.resizable(0,0)
img=PhotoImage(file=r'C:\Users\USER\Desktop\HTML\LT Logo.png')
root.iconphoto(False,img)
root['bg']='skyblue'

root.title('Language Translator by Evangelin John')
Label(root,text="Language Translator",font="Arial 20 bold",bg='skyblue',height=2).pack()

Label(root,text="Enter Text",font='arial 13 bold',bg='skyblue').place(x=165,y=90)

Input_text=Entry(root,width=60)
Input_text.place(x=10,y=130)
Input_text.get()

Label(root,text="Output",font='arial 13 bold',bg='skyblue').place(x=780,y=90)
output_text = Text(root,font='arial 10',height=5,wrap= WORD,padx=5,pady=5,width=50)
output_text.place(x=600,y=130)

language=list(LANGUAGES.values())

dest_lang=ttk.Combobox(root,values=language,width=22,state='r')
dest_lang.place(x=130,y=180)
dest_lang.set('Choose Language')
    
def Translate():
    translator = Translator()
    translated = translator.translate(text=Input_text.get(), dest=dest_lang.get())
    output_text.delete(1.0, END)
    output_text.insert(END, translated.text)

trans_btn= Button(root,text='Translate',font='arial 12 bold',pady=5,command = Translate,bg='lavender',activebackground='medium orchid')
trans_btn.place(x=445,y=180)

root.mainloop()
