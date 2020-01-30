from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
root=Tk()
root.title("unsaved note")
file=None

menubar=Menu(root)

def showabout():
    showinfo("Notepad","Faizan Mustafa")
    
def openfile():
    file=askopenfilename(initialdir="/home/faizan/Desktop",
                         defaultextension=".txt",
                         filetypes=[("all files","*.*"),("text files","")])
    if file=="":
        file=None
    else:
        root.title(file)
        text.delete(1.0,END)
        _file=open(file,"r")
        text.insert(1.0,_file.read())
        _file.close()
        
    
    
def newfile():
    root.title("unsaved note")
    file=None
    text.delete(1.0,END)
    
def savefile():
    global file
    if file==None:
        file=asksaveasfilename(initialdir="/home/faizan/Desktop",
                               initialfile="untitled.txt",
                               defaultextension=".txt",
                               filetypes=[("All Files","*.*"),("Text Files","*.txt")])
        
        if file=="":
            file=None
        else:
            _file=open(file,"w")
            _file.write(text.get(1.0,END))
            _file.close()
            root.title("saved file")
    else:
        _file=open(file,"w")
        _file.write(text.get(1.0,END))
        _file.close()
        
        
def quitapp():
    root.destroy()



filemenu=Menu(menubar,tearoff=0)
filemenu.add_command(label="New",command=newfile)
filemenu.add_command(label="Open",command=openfile)
filemenu.add_command(label="Save",command=savefile)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=quitapp)
menubar.add_cascade(label="File",menu=filemenu)

editmenu=Menu(menubar,tearoff=0)
editmenu.add_command(label="Cut",command=lambda:root.focus_get().event_generate("<<Cut>>"))
editmenu.add_command(label="Copy",command=lambda:root.focus_get().event_generate("<<Copy>>"))
editmenu.add_command(label="Paste",command=lambda:root.focus_get().event_generate("<<Paste>>"))
menubar.add_cascade(label="Edit",menu=editmenu)

helpmenu=Menu(menubar,tearoff=0)
helpmenu.add_command(label="About",command=showabout)
menubar.add_cascade(label="Help",menu=helpmenu)

root.config(menu=menubar)

text=Text(root)
text.pack()

scr_width=root.winfo_screenwidth()
scr_height=root.winfo_screenheight()
win_width=600
win_height=400

x=(scr_width//2)-(win_width//2)
y=(scr_height//2)-(win_height//2)

root.geometry("{}x{}+{}+{}".format(win_width,win_height,x,y))

root.grid_rowconfigure(0,weight=1)
root.grid_columnconfigure(0,weight=1)
text.grid(sticky="nsew")


scroll=Scrollbar(text)
scroll.pack(side=RIGHT,fill=Y)
scroll.config(command=text.yview)
text.config(yscrollcommand=scroll.set)




mainloop()