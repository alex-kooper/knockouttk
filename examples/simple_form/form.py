try:
    from tkinter import Tk, Text, TOP, BOTH, X, N, LEFT, RIGHT, DISABLED, ACTIVE
    from tkinter.ttk import Frame, Label, Entry, Button
except ImportError:
    from Tkinter import Tk, Text, TOP, BOTH, X, N, LEFT, RIGHT, DISABLED, ACTIVE
    from ttk import Frame, Label, Entry, Button


class Form(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent

        self.parent.title("Example Form")
        self.pack(fill=BOTH, expand=True)

        f = Frame(self)
        f.pack(fill=X)

        l = Label(f, text='First Name', width=10)
        l.pack(side=LEFT, padx=5, pady=5)
       
        self.firstName = Entry(f)
        self.firstName.pack(fill=X, padx=5, expand=True)
        
        f = Frame(self)
        f.pack(fill=X)
        
        l = Label(f, text='Last Name', width=10)
        l.pack(side=LEFT, padx=5, pady=5)

        self.lastName = Entry(f)
        self.lastName.pack(fill=X, padx=5, expand=True)
        
        f = Frame(self)
        f.pack(fill=X)

        l = Label(f, text='Full Name', width=10)
        l.pack(side=LEFT, padx=5, pady=5)

        self.fullName = Label(f, text='ALEX POOPKIN', width=10)
        self.fullName.pack(fill=X, padx=5, expand=True)

        f = Frame(self)
        f.pack(fill=X)

        l = Label(f, text='', width=10)
        l.pack(side=LEFT, padx=5, pady=0)

        self.errorMessage = Label(f, text='Invalid character int the name!', foreground='red', width=30)
        self.errorMessage.pack(fill=X, padx=5, expand=True)

        f = Frame(self)
        f.pack(fill=X)

        b = Button(f, text='Close', command=lambda : self.parent.quit())
        b.pack(side=RIGHT, padx=5, pady=10)
        b['default'] = ACTIVE
        b.focus_set()

        self.clearButton = Button(f, text='Clear')
        self.clearButton.pack(side=RIGHT, padx=5, pady=10)
        self.clearButton['state'] = DISABLED

        self.sendButton = Button(f, text='Send')
        self.sendButton.pack(side=RIGHT, padx=5, pady=10)


def main():
    root = Tk()
    root.geometry("+400+300")
    app = Form(root)
    root.mainloop()  


if __name__ == '__main__':
    main()
