import tkinter as tk
window = tk.Tk()
window.title("EDIT")
window.geometry('1000x1000')

l1 = tk.Label(text='EMPLOYEE ID')
l1.place(x=50, y=50)

e1 = tk.Entry(width="20")
e1.place(x=200, y=50)

l2 = tk.Label(text='NAME')
l2.place(x=50, y=100)

e2 = tk.Entry(width="20")
e2.place(x=200, y=100)

l3 = tk.Label(text='ADDRESS')
l3.place(x=50, y=150)

e3 = tk.Entry(width="20")
e3.place(x=200, y=150)

l4 = tk.Label(text='PASSWORD')
l4.place(x=50, y=200)

e4 = tk.Entry(width="20")
e4.place(x=200, y=200)

l5 = tk.Label(text='CONFIRM PASSWORD')
l5.place(x=50, y=250)

e5 = tk.Entry(width="20")
e5.place(x=200, y=250)

b1 = tk.Button(text="SAVE CHANGES", width="20")
b1.place(x=200, y=300)

window.mainloop()