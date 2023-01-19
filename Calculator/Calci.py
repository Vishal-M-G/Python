from tkinter import *

base = Tk()
base.title("Tkinter Calculator")
base.geometry(f"{base.winfo_screenwidth()}x{base.winfo_screenheight()}")
base.minsize(base.winfo_screenwidth(), base.winfo_screenheight())
base.maxsize(base.winfo_screenwidth(), base.winfo_screenheight())

class Display(Canvas):
    def __init__(self):
        super().__init__(width = base.winfo_screenwidth(),
            height = base.winfo_screenheight(),
            bg = 'grey')
        
        self.pack()
        self.exp = StringVar()
        self.exp.set ("")
        self.create_elements()

    def create_elements(self):
        self.exp_field = Entry(textvar = self.exp, font = ('algerian', 40), justify = RIGHT, state = DISABLED)
        self.create_window(base.winfo_screenwidth()//2, 50,
            window = self.exp_field,
            width = base.winfo_screenwidth() - 20,
            height = 80)
        
        bOpen = Button(text = "(", width = ((base.winfo_screenwidth() // 4) - 120)//10, height = 2, font = 28)
        bOpen.bind('<Button>', self.onClick)
        bOpen.bind('<Enter>', self.colorOn)
        bOpen.bind('<Leave>', self.colorOff)
        self.create_window(192, 150, window = bOpen)
        bClose = Button(text = ")", width = ((base.winfo_screenwidth() // 4) - 120)//10, height = 2, font = 28)
        bClose.bind('<Button>', self.onClick)
        bClose.bind('<Enter>', self.colorOn)
        bClose.bind('<Leave>', self.colorOff)
        self.create_window(576, 150, window = bClose)
        bc = Button(text = "Clear", width = ((base.winfo_screenwidth() // 4) - 120)//10, height = 2, font = 28, background = 'orange')
        bc.bind('<Button>', lambda x:self.exp.set(""))
        bc.bind('<Enter>', self.colorOnSpl)
        bc.bind('<Leave>', self.colorOffSpl)
        self.create_window(960, 150, window = bc)
        bbs = Button(text = "Backspace", width = ((base.winfo_screenwidth() // 4) - 120)//10, height = 2, font = 28, background = 'orange')
        bbs.bind('<Button>', lambda x:self.exp.set(self.exp.get()[:-1]))
        bbs.bind('<Enter>', self.colorOnSpl)
        bbs.bind('<Leave>', self.colorOffSpl)
        self.create_window(1344, 150, window = bbs)

        b9 = Button(text = "9", width = ((base.winfo_screenwidth() // 4) - 120)//10, height = 2, font = 28)
        b9.bind('<Button>', self.onClick)
        b9.bind('<Enter>', self.colorOn)
        b9.bind('<Leave>', self.colorOff)
        self.create_window(192, 300, window = b9)
        b8 = Button(text = "8", width = ((base.winfo_screenwidth() // 4) - 120)//10, height = 2, font = 28)
        b8.bind('<Button>', self.onClick)
        b8.bind('<Enter>', self.colorOn)
        b8.bind('<Leave>', self.colorOff)
        self.create_window(576, 300, window = b8)
        b7 = Button(text = "7", width = ((base.winfo_screenwidth() // 4) - 120)//10, height = 2, font = 28)
        b7.bind('<Button>', self.onClick)
        b7.bind('<Enter>', self.colorOn)
        b7.bind('<Leave>', self.colorOff)
        self.create_window(960, 300, window = b7)
        bdiv = Button(text = "/", width = ((base.winfo_screenwidth() // 4) - 120)//10, height = 2, font = 28)
        bdiv.bind('<Button>', self.onClick)
        bdiv.bind('<Enter>', self.colorOn)
        bdiv.bind('<Leave>', self.colorOff)
        self.create_window(1344, 300, window = bdiv)

        b6 = Button(text = "6", width = ((base.winfo_screenwidth() // 4) - 120)//10, height = 2, font = 28)
        b6.bind('<Button>', self.onClick)
        b6.bind('<Enter>', self.colorOn)
        b6.bind('<Leave>', self.colorOff)
        self.create_window(192, 450, window = b6)
        b5 = Button(text = "5", width = ((base.winfo_screenwidth() // 4) - 120)//10, height = 2, font = 28)
        b5.bind('<Button>', self.onClick)
        b5.bind('<Enter>', self.colorOn)
        b5.bind('<Leave>', self.colorOff)
        self.create_window(576, 450, window = b5)
        b4 = Button(text = "4", width = ((base.winfo_screenwidth() // 4) - 120)//10, height = 2, font = 28)
        b4.bind('<Button>', self.onClick)
        b4.bind('<Enter>', self.colorOn)
        b4.bind('<Leave>', self.colorOff)
        self.create_window(960, 450, window = b4)
        bmul = Button(text = "*", width = ((base.winfo_screenwidth() // 4) - 120)//10, height = 2, font = 28)
        bmul.bind('<Button>', self.onClick)
        bmul.bind('<Enter>', self.colorOn)
        bmul.bind('<Leave>', self.colorOff)
        self.create_window(1344, 450, window = bmul)

        b3 = Button(text = "3", width = ((base.winfo_screenwidth() // 4) - 120)//10, height = 2, font = 28)
        b3.bind('<Button>', self.onClick)
        b3.bind('<Enter>', self.colorOn)
        b3.bind('<Leave>', self.colorOff)
        self.create_window(192, 600, window = b3)
        b2 = Button(text = "2", width = ((base.winfo_screenwidth() // 4) - 120)//10, height = 2, font = 28)
        b2.bind('<Button>', self.onClick)
        b2.bind('<Enter>', self.colorOn)
        b2.bind('<Leave>', self.colorOff)
        self.create_window(576, 600, window = b2)
        b1 = Button(text = "1", width = ((base.winfo_screenwidth() // 4) - 120)//10, height = 2, font = 28)
        b1.bind('<Button>', self.onClick)
        b1.bind('<Enter>', self.colorOn)
        b1.bind('<Leave>', self.colorOff)
        self.create_window(960, 600, window = b1)
        bsub = Button(text = "-", width = ((base.winfo_screenwidth() // 4) - 120)//10, height = 2, font = 28)
        bsub.bind('<Button>', self.onClick)
        bsub.bind('<Enter>', self.colorOn)
        bsub.bind('<Leave>', self.colorOff)
        self.create_window(1344, 600, window = bsub)

        bdot = Button(text = ".", width = ((base.winfo_screenwidth() // 4) - 120)//10, height = 2, font = 28)
        bdot.bind('<Button>', self.onClick)
        bdot.bind('<Enter>', self.colorOn)
        bdot.bind('<Leave>', self.colorOff)
        self.create_window(192, 750, window = bdot)
        b0 = Button(text = "0", width = ((base.winfo_screenwidth() // 4) - 120)//10, height = 2, font = 28)
        b0.bind('<Button>', self.onClick)
        b0.bind('<Enter>', self.colorOn)
        b0.bind('<Leave>', self.colorOff)
        self.create_window(576, 750, window = b0)
        beq = Button(text = "=", width = ((base.winfo_screenwidth() // 4) - 120)//10, height = 2, font = 28, background = 'orange')
        beq.bind('<Button>', self.evaluate)
        beq.bind('<Enter>', self.colorOnSpl)
        beq.bind('<Leave>', self.colorOffSpl)
        self.create_window(960, 750, window = beq)
        badd = Button(text = "+", width = ((base.winfo_screenwidth() // 4) - 120)//10, height = 2, font = 28)
        badd.bind('<Button>', self.onClick)
        badd.bind('<Enter>', self.colorOn)
        badd.bind('<Leave>', self.colorOff)
        self.create_window(1344, 750, window = badd)

    def onClick(self, e):
        self.exp.set(self.exp.get() + e.widget.cget("text"))

    def colorOn(self, e):
        e.widget['background'] = 'aqua'

    def colorOff(self, e):
        e.widget['background'] = 'SystemButtonFace'

    def colorOnSpl(self, e):
        e.widget['background'] = 'yellowgreen'

    def colorOffSpl(self, e):
        e.widget['background'] = 'orange'

    def evaluate(self, e):
        try:
            self.exp.set(eval(str(self.exp.get())))
        except:
            self.exp.set("Syntax Error")

calci = Display()

base.mainloop()