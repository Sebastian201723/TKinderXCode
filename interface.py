try: #Python 3
    from Tkinter import*
except ImportError: #Python2
    from tkinter import*

raiz = Tk()

raiz.title("KNN Method")

#Re-dimension with width, height
raiz.resizable(1,1)

#Para cambiar imagen de icono:
raiz.iconbitmap("selfi.ico")

raiz.geometry("1000x500")

raiz.config(bg="blue")

miFrame = Frame(raiz, width=1000, height=500)
# O podemos usar miFrame.config(width="650",height="150")
#Father's heritage to inherit background color, icon pic etc
miFrame.pack()

miFrame.config(bg="red")
#Borders settings
#miFrame.config(bd=23)
#miFrame.config(relief="groove")
#miFrame.config(cursor="hand2")

TitleLabel = Label(miFrame, text = "Ingrese Edad: ",fg="green",font=("Arial"))
miFrame.place(x = 10, y = 20)
miImagen = PhotoImage(file="contabilidad1.gif")
Label(miFrame, image=miImagen).place(x=100,y=100)


raiz.mainloop()