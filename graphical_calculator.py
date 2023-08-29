import tkinter as tk
import random


root = tk.Tk()
root.geometry("1200x900")
root.resizable(False, False)


top_frame = tk.Frame(root, bg='black', height=50)
top_frame.pack(side='top', fill='x')
top_frame_label = tk.Label(root, bg='black', fg='white',
                          text='Graphical Calculator', font=("arial", 16, "normal"))
top_frame_label.place(x=530, y=10)
bottom_frame = tk.Frame(root, bg='grey', height=250)
bottom_frame.pack(side="bottom", fill="x")
count = 1


label2 = None
label3 = None
label5 = None
label6 = None


def zoomin():
   global count, label2, label3, label5, label6, label, label4
   count += 4
   if label2:
       label2.destroy()
   if label3:
       label3.destroy()
   for g in range(120):
       label = tk.Label(root, text="-")
       label.place(x=g * 10, y=350)
   for h in range(58):
       label4 = tk.Label(root, text="|", font=("arial", 10, "normal"))
       label4.place(x=600, y=50+h*10)
   for i in range(11):
       label2 = tk.Label(root, text=f"{i}")
       label2.place(x=594 + i * (58 + count), y=350)
   for j in range(11):
       label3 = tk.Label(root, text=f"-{j}")
       label3.place(x=594 - j * (58 + count), y=350)
   count1 = 0
   count2 = 0
   while label5 is None or label5.winfo_y() + count1 * (58 + count) <= 620:
       if label5:
           label5.destroy()
       new_label5 = tk.Label(root, text=f"-{count1}")
       new_label5.place(x=600, y=350 + count1 * (58 + count))
       label5 = new_label5
       count1 += 1
   while label6 is None or label6.winfo_y() - count2 * (58 + count) >= 50:
       if label6:
           label6.destroy()
       new_label6 = tk.Label(root, text=f"{count2}")
       new_label6.place(x=600, y=350 - count2 * (58 + count))
       label6 = new_label6
       count2 += 1




def zoomout():
   global count, label2, label3, label5, label6, label, label4
   count -= 4
   if label2:
       label2.destroy()
   if label3:
       label3.destroy()
   if label5:
       label5.destroy()
   if label6:
       label6.destroy()
   for g in range(120):
       label = tk.Label(root, text="-")
       label.place(x=g * 10, y=350)
   for h in range(58):
       label4 = tk.Label(root, text="|", font=("arial", 10, "normal"))
       label4.place(x=600, y=50 + h * 10)
   for i in range(11):
       label2 = tk.Label(root, text=f"{i}")
       label2.place(x=594 + i * (58 + count), y=350)
   for j in range(11):
       label3 = tk.Label(root, text=f"-{j}")
       label3.place(x=594 - j * (58 + count), y=350)
   for k in range(5):
       label5 = tk.Label(root, text=f"{k}")
       label5.place(x=600, y=350 + k * (58 + count))
   for l in range(5):
       label6 = tk.Label(root, text=f"{l}")
       label6.place(x=600, y=350 - l * (58 + count))
def x_axis():
   global label, label2, label3
   for i in range(120):
       label = tk.Label(root, text="-")
       label.place(x=i*10, y=350)
   for j in range(11):
       num = j
       label2 = tk.Label(root, text=f"{num}")
       label2.place(x=594+j*58, y=350)
   for k in range(11):
       num2 = k
       label3 = tk.Label(root, text=f"-{num2}")
       label3.place(x=594-k*58, y=350)
def y_axis():
   global label4, label5, label6
   for i in range(58):
       label4 = tk.Label(root, text="|", font=("arial", 10, "normal"))
       label4.place(x=600, y=50+i*10)
   for j in range(5):
       num3 = j
       label5 = tk.Label(root, text=f"-{num3}")
       label5.place(x=600, y=350+j*58)
   for k in range(5):
       num4 = k
       label6 = tk.Label(root, text=f"{num4}")
       label6.place(x=600, y=350-k*58)


button = tk.Button(root, text="+", width=2, height=1, command=zoomin)
button.place(x=1160, y=80)
button2 = tk.Button(root, text="-", width=2, height=1, command=zoomout)
button2.place(x=1160, y=110)


x_axis()
y_axis()


root.mainloop()
