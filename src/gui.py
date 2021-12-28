from tkinter import Tk, Button, Label, Text, END, filedialog
 
class Root(Tk):
    BUTTON_TEXTS = ['Training set folder', 'Test set folder', 'Predict image']

    def __init__(self):
        super(Root,self).__init__()
 
        self.title("Character Recognition")
        self.minsize(500,400)

        self.buttons = []
        self.labels = []

        self.init_items()

    def init_items(self):
        for index, text in enumerate(Root.BUTTON_TEXTS):
            btn = Button(self, text = text, bd = '5',
                    command = lambda i = index: self.select_file(i))

            label = Label(self, text='No Selection')

            self.buttons.append(btn)
            self.labels.append(label)

            btn.grid(row=index,column=0, sticky='w')
            label.grid(row=index, column=1)

        output_field = Text(self, width=80, height=15)
        output_field.configure(state="disabled")
        output_field.grid(row=len(Root.BUTTON_TEXTS), columnspan=2)

        self.output_field = output_field

    def output_text(self,text):
        self.output_field.configure(state="normal")
        self.output_field.insert(END, text)
        self.output_field.configure(state="disabled")

    def set_label(self, text, index):
        self.labels[index].config(text= text)

    def select_file(self, index):
        if(index in [0, 1]):
            selection = filedialog.askdirectory()
        else:
            selection = filedialog.askopenfilename()
            
        if(selection == ''):
            self.output_text('Invalid selection\n')
            return
        else:
            self.set_label('Selection: {}\n'.format(selection), index)
        



