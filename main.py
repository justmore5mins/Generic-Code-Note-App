import tkinter as tk
from tkinter import filedialog

class TextEditor():
    def __init__(self) -> None:
        self.win = tk.Tk()
        self.win.title = "Text Editor"

        self.text = tk.Text(self.win,wrap=tk.WORD)
        self.text.pack(expand=tk.YES,fill=tk.BOTH)

        self.CreateMenu()
        self.win.mainloop()

    def CreateMenu(self):
        menu = tk.Menu(self.win)
        self.win.config(menu=menu)

        file_menu = tk.Menu(menu)
        menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.NewFile)
        file_menu.add_command(label="Open", command=self.OpenFile)
        file_menu.add_command(label="Save", command=self.SaveFile)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.win.quit)

        compile_run_menu = tk.Menu(menu)
        menu.add_cascade(label="Compile & Run", menu=compile_run_menu)
        compile_run_menu.add_command(label="Run", command=self.RunCode)

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
    
    def RunCode(self):
        # 获取当前光标所在位置的行号
        current_line = self.text.index(tk.CURRENT).split(".")[0]

        # 获取当前行的文本内容
        line_text = self.text.get(f"{current_line}.0", f"{current_line}.end").strip()

        # 如果当前行包含 "<code>"，执行代码
        if "code" in line_text:
            code_start = self.text.search("<code>", tk.CURRENT, backwards=True)
            code_end = self.text.search("</code>", tk.CURRENT)

            if code_start and code_end:
                code_start_line, code_start_col = code_start.split(".")
                code_end_line, code_end_col = code_end.split(".")

                code_block = self.text.get(f"{code_start_line}.{int(code_start_col)+7}", f"{code_end_line}.{code_end_col}")

                # 在这里执行你的代码块
                print("Executing code block:")
                print(code_block)

if __name__ == "__main__":
    editor = TextEditor()