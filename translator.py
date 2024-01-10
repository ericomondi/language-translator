from tkinter import Tk, Label, StringVar, Entry, Button, OptionMenu
from googletrans import Translator

class TranslatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Language Translator")

        self.input_text = StringVar()
        self.output_text = StringVar()
        self.language_var = StringVar(self.master)
        self.language_var.set("en")  # Default language

        self.create_widgets()

    def create_widgets(self):
        # Input
        Label(self.master, text="Enter Text:").grid(row=0, column=0, pady=15)
        Entry(self.master, textvariable=self.input_text, width=80).grid(row=0, column=1, pady=10)

        # Language Selection
        Label(self.master, text="Select Language:").grid(row=1, column=0, pady=10)
        languages = ["en", "es", "fr", "de", "ja", "ko", "zh", "hi"]  # Add more language codes as needed
        OptionMenu(self.master, self.language_var, *languages).grid(row=1, column=1, pady=5)

        # Translate Button
        Button(self.master, text="Translate", command=self.translate_text).grid(row=2, column=0, columnspan=2, pady=10)

        # Output
        Label(self.master, text="Translated Text:").grid(row=3, column=0, pady=5)
        Label(self.master, textvariable=self.output_text, wraplength=400, justify="left").grid(row=3, column=1, pady=5)

    def translate_text(self):
        translator = Translator()
        input_text = self.input_text.get()
        dest_language = self.language_var.get()

        try:
            translation = translator.translate(input_text, dest=dest_language)
            self.output_text.set(translation.text)
        except Exception as e:
            self.output_text.set("Error in translation. Please check your input and try again.")

if __name__ == "__main__":
    root = Tk()
    app = TranslatorApp(root)
    root.mainloop()
