import tkinter as tk

root = tk.Tk()
root.geometry('600x600')
root.resizable(False, False)


def func1():
        pass


bt = []
k = 0
for i in range(10):
    for j in range(10):
        bt.append(tk.Button(text='버튼' + str(k)))
        bt[k].place(x=55 * i, y=55 * j)
        k += 1

bt[40].confing(command=func1)
bt[0].config(bg='red')
bt[1].config(bg='blue')
bt[2].config(bg='red')
bt[3].config(bg='blue')
bt[4].config(bg='red')
bt[5].config(bg='blue')
bt[6].config(bg='red')
bt[7].config(bg='blue')
bt[8].config(bg='red')
bt[9].config(bg='blue')
bt[10].config(bg='red')
bt[11].config(bg='blue')
bt[12].config(bg='red')
bt[13].config(bg='blue')
bt[14].config(bg='red')
bt[15].config(bg='blue')
bt[16].config(bg='red')
bt[17].config(bg='blue')
bt[18].config(bg='red')
bt[19].config(bg='blue')
bt[20].config(bg='red')
bt[21].config(bg='blue')
bt[22].config(bg='red')
bt[23].config(bg='blue')
bt[24].config(bg='red')
bt[25].config(bg='blue')
bt[26].config(bg='red')
bt[27].config(bg='blue')
bt[28].config(bg='red')
bt[29].config(bg='blue')
bt[30].config(bg='red')

root.mainloop()

# import tkinter as tk
#
# root = tk.Tk()
# root.title('아이콘 연습')
# root.geometry('640x400+100+100')
# root.resizable(True, True)
# image = tk.PhotoImage(file='jhg.png')
#
# label = tk.Label(root,image = image)
# label.pack()
#
# root.mainloop()

# import tkinter
# import tkinter.font
#
# root = tkinter.Tk()
#
# font=tkinter.font.Font(family = 'Microsoft JhengHei UI Light', size = 20, slant = 'italic')
# print(tkinter.font.families())
# label = tkinter.Label(root, text = 'kideug kideug', font = font)
# label.pack()
#
# root.mainloop()
