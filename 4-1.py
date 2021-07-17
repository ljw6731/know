# import tkinter as tk
# root = tk.Tk()
#
# label1 = tk.Label(root, text='안녕하세요')
# label1.pack()
#
# root.mainloop()


# import tkinter as tk
# root = tk.Tk()
#
# a = tk.Label(root, text='안녕')
# a.pack()
#
# b=tk.Entry()
# b.pack()
#
# root.mainloop()

# import tkinter as tk
#
# def okClick():
#     name=b.get()
#     print(name)
#     c.config(text=name)
#
# def ret(event):
#     c.config(text='니가 친 글자')
#
# root = tk.Tk()
#
# a= tk.Label(text='안녕하세요')
# a.pack()
#
# b=tk.Entry()
# b.pack()
#
# c= tk.Label(text='니가친 글자')
# c.pack()
#
# btn = tk.Button(root, text='OK',command=okClick)
# btn.pack()
#
# c.bind('<Button-1>', ret)
# root.mainloop()

# import tkinter as tk
# root = tk.Tk()
#
# def okClick1():
#     e.config(text=int (b.get())+int(d.get()))
#
# def okClick2():
#     e.config(text=int (b.get())-int(d.get()))
#
# def okClick3():
#     e.config(text=int(b.get()) * int(d.get()))
#
# def okClick4():
#     e.config(text=int(b.get()) / int(d.get()))
#
#
# a = tk.Label(root, text='첫 번째 숫자를 입려하세요')
# a.pack()
#
# b=tk.Entry()
# b.pack()
#
# c = tk.Label(root, text='첫 번째 숫자를 입려하세요')
# c.pack()
#
# d=tk.Entry()
# d.pack()
#
# btn = tk.Button(root, text='더하기',command=okClick1)
# btn.pack()
#
# btn = tk.Button(root, text='빼기',command=okClick2)
# btn.pack()
#
# btn = tk.Button(root, text='곱하기',command=okClick3)
# btn.pack()
#
# btn = tk.Button(root, text='나누기',command=okClick4)
# btn.pack()
#
# e=tk.Label (root, text='결과값을 나타냅니다.')
# e.pack()
#
#
# root.mainloop()