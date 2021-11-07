from tkinter import *

root=Tk()

root.title("Fibonacci")
root.geometry("1000x400")

label_series = Label(root, text="Fibonacci Series:")
label_flower = Label(root)
label_spiral = Label(root)

def Fib():
    num = 100
    
    fn = 0
    sn = 1
    sum = 0
    counter = 1
    while (counter <= num):
        label_series["text"] += " " + str(sum)
        counter = counter + 1
        fn = sn
        sn = sum
        sum = fn + sn
    label_flower["text"] = "Flower is fully bloomed"
    label_spiral["text"] = "Spirals in the right direction are " + str(fn) + ", spirals in the left direction are " + str(sn) + ", total spirals are " + str(sum)
    
btn = Button(root, text = "Show Fibonacci Series", command = Fib)

btn.pack()
label_series.pack()
label_flower.pack()
label_spiral.pack()
root.mainloop()