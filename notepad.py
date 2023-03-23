import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import colorchooser
import sys
import pyperclip as pyclip

class App:
    def __init__(self):
        self.filename = ""
        self.font_size = 10

    def drawing(self):
        self.root = tk.Tk()
        self.root.geometry("500x300")
        self.root.title("NotePad")

        self.frame_notepad = tk.Frame(self.root)
        self.frame_notepad.pack(expand=True, fill=tk.BOTH)

        self.cv_notepad = tk.Canvas(self.frame_notepad, width=500, height=300)
        self.cv_notepad.pack(expand=True, fill=tk.BOTH)
        self.textbox = tk.Text(self.cv_notepad, font=("", 10))
        self.textbox.place(x=0, y=0, relwidth=1, relheight=1)

        self.notebook = ttk.Notebook(self.cv_notepad)
        self.tab = tk.Frame(self.notebook)
        self.notebook.add(self.tab, text="新規タブ")
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)
        self.menu_file = tk.Menu(self.root)
        self.menu_bar.add_cascade(label="ファイル", menu=self.menu_file)
        self.menu_file.add_command(label="新規作成", command=self.create_new)
        self.menu_file.add_command(label="開く", command=self.open_file)
        self.menu_file.add_separator()
        self.menu_file.add_command(label="保存", command=self.overwrite_save)
        self.menu_file.add_command(label="名前をつけて保存", command=self.named_save)
        self.menu_file.add_separator()
        self.menu_file.add_command(label="終了", command=self.com_exit)
        self.menu_edit = tk.Menu(self.root)
        self.menu_bar.add_cascade(label="編集", menu=self.menu_edit)
        self.menu_edit.add_command(label="全てコピー", command=self.copy_contents)
        self.menu_show = tk.Menu(self.root)
        self.menu_bar.add_cascade(label="表示", menu=self.menu_show)
        self.menu_show.add_command(label="拡大", command=lambda:self.change_font_size(10))
        self.menu_show.add_command(label="縮小", command=lambda:self.change_font_size(-10))
        self.menu_show.add_command(label="ダークテーマ", command=self.change_theme)
        self.menu_show.add_separator()
        self.menu_show.add_command(label="文字色の変更", command=lambda:self.custom_color("fg"))
        self.menu_show.add_command(label="背景色の変更", command=lambda:self.custom_color("bg"))

        self.root.mainloop()

    def create_new(self):
        self.ask_save = messagebox.askyesnocancel("確認", "未保存内容は失われます。保存しますか?")
        if self.ask_save == True:
            self.overwrite_save()
        elif False:
            pass
        else:
            return
        self.textbox.delete(0.0, tk.END)
        self.filename = ""

    def open_file(self):
        self.ask_save = messagebox.askyesnocancel("確認", "未保存内容は失われます。保存しますか?")
        if self.ask_save == True:
            self.overwrite_save()
        elif False:
            pass
        else:
            return
        self.textbox.delete(0.0, tk.END)
        self.filename = filedialog.askopenfilename(title="開く", filetypes=[("TEXT", ".txt")])
        if self.filename:
            self.opening_file = open(self.filename, "r", encoding="utf-8")
            self.textbox.insert(tk.END, self.opening_file.read())

    def save_file(self, filename):
        self.file = open(filename, "w", encoding="utf-8")
        self.file.write(self.input_contents)
        self.file.close()

    def overwrite_save(self):
        if self.filename:
            self.input_contents = self.textbox.get(0.0, tk.END)
            self.save_file(self.filename)
        else:
            self.named_save()

    def named_save(self):
        self.input_contents = self.textbox.get(0.0, tk.END)
        self.filename = filedialog.asksaveasfilename(title="名前をつけて保存", defaultextension=".txt", filetypes=[("TEXT", ".txt")])
        if self.filename:
            self.save_file(self.filename)

    def copy_contents(self):
        self.input_contents = self.textbox.get(0.0, tk.END)
        pyclip.copy(self.input_contents)
        messagebox.showinfo("NotePad", "コンテンツはクリップボードにコピーされました。")

    def change_font_size(self, event):
        self.font_size += event
        self.textbox.config(font=("", self.font_size))

    def change_theme(self):
        self.textbox.config(background="black", foreground="white")

    def custom_color(self, position):
        self.color = colorchooser.askcolor()
        if position == "fg":
            self.textbox.config(foreground=self.color[1])
        elif position == "bg":
            self.textbox.config(background=self.color[1])

    def com_exit(self):
        self.ask_save = messagebox.askyesnocancel("確認", "未保存内容は失われます。保存しますか?")
        if self.ask_save == True:
            self.overwrite_save()
        elif self.ask_save == False:
            pass
        else:
            return
        sys.exit()


if __name__ == "__main__":
    app = App()
    app.drawing()