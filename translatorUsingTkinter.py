import tkinter as tk
from tkinter import ttk
from googletrans import Translator

class TextTranslator:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Translator")
        self.root.geometry("700x700")  # Set window size to 700x700

        # Sky blue background color
        self.root.configure(bg="skyblue")

        self.languages = {
            "English": "en",
            "Hindi": "hi",
            "Spanish": "es",
            "French": "fr",
            "German": "de",
            "Chinese": "zh-CN",
            "Arabic":"ar",
            "Bengali":"bn",
            "Irish":"ga",
            "Greek":"el",
            "Indonesian":"id",
            "Italian":"it",
            "Japanese":"ja",
            "Kannada":"kn",
            "Kashmiri":"ks",
            "Georgian":"ka",
            "Khmer":"km",
            "Korean":"ko",
            "Latin":"la",
            "Marathi":"mr",
            "Mongolian":"mn",
            "Nepali":"ne",
            "Oriya":"or",
            "Punjabi":"pa",
            "Russian":"ru",
            "Sanskrit":"sa",
            "Sindhi":"sd",
            "Somali":"so",
            "Swedish":"sv",
            "Tamil":"ta",
            "Telugu":"te",
            "Tibetan":"bo",
            "Thai":"th",
            "Turkish":"tr",
            "Urdu":"ur",
            "Polish":"pl"

        }
        
        self.from_language_label = ttk.Label(root, text="From Language:")
        self.from_language_label.grid(row=0, column=0, padx=8, pady=7)
        self.from_language_var = tk.StringVar()
        self.from_language_dropdown = ttk.Combobox(root, values=list(self.languages.keys()), textvariable=self.from_language_var)
        self.from_language_dropdown.grid(row=0, column=1, padx=6, pady=7)
        self.from_language_dropdown.current(0)

        self.to_language_label = ttk.Label(root, text="To Language:")
        self.to_language_label.grid(row=1, column=0, padx=7, pady=7)
        self.to_language_var = tk.StringVar()
        self.to_language_dropdown = ttk.Combobox(root, values=list(self.languages.keys()), textvariable=self.to_language_var)
        self.to_language_dropdown.grid(row=1, column=1, padx=7, pady=7)
        self.to_language_dropdown.current(1)

        self.input_label = ttk.Label(root, text="Input Text:")
        self.input_label.grid(row=2, column=0, padx=7, pady=7)
        self.input_text = tk.Text(root, height=9, width=70)
        self.input_text.grid(row=2, column=1, padx=7, pady=7)

        self.output_label = ttk.Label(root, text="Output Text:")
        self.output_label.grid(row=3, column=0, padx=7, pady=7)
        self.output_text = tk.Text(root, height=9, width=70)
        self.output_text.grid(row=3, column=1, padx=7, pady=7)
        self.output_text.config(state="disabled")

        self.translate_button = ttk.Button(root, text="Translate",command=self.translate_text)
        self.translate_button.grid(row=4, columnspan=2, padx=7, pady=7)

    def translate_text(self):
        translator = Translator()
        input_text = self.input_text.get("1.0", "end-1c")
        from_lang = self.languages[self.from_language_var.get()]
        to_lang = self.languages[self.to_language_var.get()]
        translated_text = translator.translate(input_text, src=from_lang, dest=to_lang).text
        with open('storageFile.txt', 'a',encoding='utf-8') as f:
            f.write("Input Text:\n")
            f.write(input_text + "\n")
            f.write("From Language: " + from_lang + "\n")
            f.write("To Language: " + to_lang + "\n")
            f.write("Translated Text: " + translated_text + "\n")
            
        self.output_text.config(state="normal")
        self.output_text.delete("1.0", "end")
        self.output_text.insert("1.0", translated_text)
        self.output_text.config(state="disabled")

def main():
    root = tk.Tk()
    app = TextTranslator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
