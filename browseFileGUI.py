    
# importing askopenfile function 
# from class filedialog 
from tkinter.filedialog import askopenfile 
from tkinter.filedialog import asksaveasfile
from tkinter.filedialog import askdirectory

def openFileTxt(): 
    file = askopenfile(mode ='r', filetypes =[('Text file', '*.txt')]) 
    return file

def openFileJson(): 
    file = askopenfile(mode ='r', filetypes =[('JSON file', '*.json')]) 
    return file

def openFileJpeg(): 
    file = askopenfile(mode ='r', filetypes =[('JPEG file', '*.jpg')]) 
    return file

def save(): 
    files = [('All Files', '*.*'),  
             ('Python Files', '*.py'), 
             ('Text Document', '*.txt')] 
    file = asksaveasfile(filetypes = files, defaultextension = files)
    return file

def openDir(): 
    # global dirname
    directory = askdirectory()
    # dirname = StringVar()
    # dirname.set(dirname)
    return directory
