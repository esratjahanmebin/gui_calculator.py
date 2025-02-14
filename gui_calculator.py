import tkinter as tk


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Friendly Calculator")
        self.root.geometry("300x400")
        self.root.configure(bg="#f0f0f0")

        self.expression = ""
        self.input_text = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Entry widget for display
        input_frame = tk.Frame(self.root, bg="#ffffff")
        input_frame.pack(pady=10)

        input_field = tk.Entry(input_frame, textvariable=self.input_text, font=("Arial", 20), width=18, borderwidth=2,
                               relief="ridge", justify='right')
        input_field.grid(row=0, column=0)

        # Buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack()

        buttons = [
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('C', '0', '=', '+')
        ]

        for i, row in enumerate(buttons):
            for j, btn_text in enumerate(row):
                btn = tk.Button(button_frame, text=btn_text, font=("Arial", 18), width=5, height=2,
                                command=lambda text=btn_text: self.on_button_click(text))
                btn.grid(row=i, column=j, padx=5, pady=5)

    def on_button_click(self, button):
        if button == "C":
            self.expression = ""
        elif button == "=":
            try:
                self.expression = str(eval(self.expression))
            except Exception:
                self.expression = "Error"
        else:
            self.expression += button

        self.input_text.set(self.expression)


if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()
