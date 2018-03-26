import tkinter as tk

window = tk.Tk()
window.title("REQUEST LEAVE")
window.geometry('1000x1000')

l1 = tk.Label(text='SUBJECT')
l1.place(x=50, y=50)

e2 = tk.Entry(width="20")
e2.place(x=200, y=50)

e2 = tk.Text(width="40", height="10")
e2.place(x=50, y=100)

b1 = tk.Button(text="SEND", width="20")
b1.place(x=100, y=300)



window.mainloop()