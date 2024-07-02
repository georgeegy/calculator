import tkinter as tk


class CalcGUI:

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("500x500")
        self.root.title('Simple Calculator')

        self.label = tk.Label(self.root, text='Calculator', font=('Arial', 12))
        self.label.pack()

        self.textbox = tk.Text(self.root, font=('Arial', 12), width=55, height=5)
        self.textbox.pack(padx=20, pady=5)

        self.buttonframe = tk.Frame(self.root)
        self.buttonframe.pack(padx=20, pady=5)

        for i in range(4):
            self.buttonframe.columnconfigure(i, weight=1)

        button_labels = ['1', '2', '3', '+',
                         '4', '5', '6', '-',
                         '7', '8', '9', '*',
                         'C', '0', '=', '/']

        def button_press(label):
            current = self.textbox.get("1.0", tk.END)
            if label == 'C':
                self.textbox.delete("1.0", tk.END)
            elif label == '=':
                try:
                    result = eval(current)
                    self.textbox.delete("1.0", tk.END)
                    self.textbox.insert(tk.END, f"{result}")
                except:
                    self.textbox.delete("1.0", tk.END)
                    self.textbox.insert(tk.END, f"Error")
            else:
                self.textbox.insert(tk.END, label)

        for index, label in enumerate(button_labels):
            row = index // 4
            column = index % 4
            button = tk.Button(self.buttonframe, text=label, font=('Arial', 12), width=20, height=1,
                               command=lambda l=label: button_press(l))
            button.grid(row=row, column=column, sticky=tk.W + tk.E + tk.N + tk.S)

        self.root.mainloop()


CalcGUI()
