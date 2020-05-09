try:
    import tkinter
    from tkinter import messagebox
    from tkinter import filedialog

    def fileChooserUI():
        main = tkinter.Tk()
        main.withdraw()
        main.sourceFolder = ''
        main.sourceFile = ''
        main.sourceFile = filedialog.askopenfilename(
            parent=main, initialdir="/", title='Please select a directory')
        main.destroy()
        main.mainloop()
        return main.sourceFile

    def folderChooserUI():
        main = tkinter.Tk()
        main.withdraw()
        main.sourceFolder = ''
        main.sourceFile = ''
        main.sourceFolder = filedialog.askdirectory(
            parent=main, initialdir="/", title='Please select a directory')
        main.destroy()
        main.mainloop()
        return main.sourceFolder
except ImportError as e:
    """Tkinter or Tk or Tk bindings not installed \n
        enter the file path by text\n
        or install tkinter"""
    print("Tkinter or Tk or Tk bindings not installed \n \
          enter the file path by text\n \
          or install tkinter")
