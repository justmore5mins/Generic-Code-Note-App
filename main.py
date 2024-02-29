import tkinter as tk
from tkinter import filedialog

class TextEditor():
    def __init__(self) -> None:
        self.win = tk.Tk()
        self.win.title = "Text Editor"

        self.text = tk.Text(self.win,wrap=tk.WORD)
        self.text.pack(expand=tk.YES,fill=tk.BOTH)

        self.text.tag_add()

        self.CreateMenu()
        self.win.mainloop()

    def CreateMenu(self):
        menu = tk.Menu(self.win)
        self.win.config(menu=menu)

        file_menu = tk.Menu(menu)
        menu.add_cascade(label="File",menu=file_menu)
        file_menu.add_command(label="New",command=self.NewFile)
        file_menu.add_command(label="Open",command=self.OpenFile)
        file_menu.add_command(label="Save",command=self.SaveFile)
        file_menu.add_separator()
        file_menu.add_command(label="Exit",command=self.win.quit)

        comp_menu = tk.Menu(self.win)
        menu.add_cascade(label="Compile",menu=comp_menu)
        comp_menu.add_command(label="Compile",command=self.CompileRun)

    def NewFile(self):
        self.text.delete(1.0,tk.END)
    
    def OpenFile(self):
        file = filedialog.askopenfilename(defaultextension=".txt",filetypes=[("Code Notes","*.cnote"),("All Files","*.*")])
        if file:
            self.text.delete(1.0,tk.END)
            with open(file,"r",encoding="utf-8") as file_handler:
                self.text.insert(tk.INSERT,file_handler.read())
    
    def SaveFile(self):
        file = filedialog.asksaveasfilename(defaultextension=".cnote", filetypes=[("Code Notes", "*.cnote"), ("All Files", "*.*")])
        if file:
            with open(file=file, mode="w",encoding="utf-8") as file_handler:
                file_handler.write(self.text.get(1.0, tk.END))
            self.window.title(f"Python Text Editor - {file}")
    
    def CompileRun(self):
        index = self.text.index(tk.CURRENT)
        self.text.mark_set(tk.CURRENT,f"{index} linestart")
        LineText = self.text.get(tk.CURRENT,f"{index} lineend")
        if "<code>" in LineText and "</code>" in LineText:
            CodeStart = self.text.search("<code>",tk.CURRENT,backwards=True,regexp=True)
            CodeEnd = self.text.search("</code>",tk.CURRENT,regexp=True)
            if CodeStart and CodeEnd:
                CodeText = self.text.get(f"{CodeStart} + 6 chars",f"{CodeEnd} - 1 chars")
                print(f"Compiling and running:\n{CodeText}")
            else:
                print("invalid code block")
        else:
            print("Not in the code block")

if __name__ == "__main__":
    editor = TextEditor()