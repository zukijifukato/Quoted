import tkinter as tk
import requests
from secrets import randbelow
import pyperclip
import tkinter.messagebox
import webbrowser

from PIL import Image
from PIL import ImageTk

s = requests.Session()

def fetchQuoteList():
	global quoteList, quoteListLen
	r = s.get('https://zenquotes.io/api/quotes')
	quoteList = r.json()
	quoteListLen = len(quoteList)

def fetchQuote():
	global quoteText, quoteAuthor
	randnum = randbelow(quoteListLen)
	quoteText = quoteList[randnum]["q"]
	quoteAuthor = quoteList[randnum]["a"]
	quoteLabel.config(text='"'+quoteText+'"')
	authorLabel.config(text='~ '+quoteAuthor)

def fetchNewList():
	fetchQuoteList()
	fetchQuote()

def fontHeader(label):
	label.config(font='Arial 20 bold', bg='#fff', justify='left', wraplength=580)

def fontNormal(label):
	label.config(font='Arial 12 italic', bg='#fff', justify='left', wraplength=580)

def copyToClipboard():
	pyperclip.copy('"'+quoteText+'"'+"\n\n~"+quoteAuthor)

def openlink(url):
	webbrowser.open_new(url)

def about():
	about = tk.Toplevel()
	about.geometry("350x250")
	about.title("About | Quoted")
	about.resizable(False, False)

	aboutFrame = tk.Frame(about)

	header = tk.Label(aboutFrame, text="Quoted", font='Arial 20 bold')
	header.grid(row=0, column=0, columnspan=2)

	img = Image.open("icon.png")
	img = img.resize((100, 100), Image.ANTIALIAS)
	logo = ImageTk.PhotoImage(img)
	logoLabel = tk.Label(aboutFrame, image=logo)
	logoLabel.grid(row=1, column=0, columnspan=2)

	description = tk.Label(aboutFrame, text="A simple inspirational and motivational quotes feed in Python using Tkinter.", font='Arial 12', wraplength=320)
	description.grid(row=2, column=0, columnspan=2)

	authorLabel = tk.Label(aboutFrame, text="Author: ", font='Arial 12')
	authorLabel.grid(row=3, column=0)

	authorLink = tk.Label(aboutFrame, text="zukijifukato", fg="#00f", cursor="hand2", font='Arial 12 underline')
	authorLink.grid(row=3, column=1, sticky=tk.W)
	authorLink.bind("<Button-1>", lambda e: openlink("https://github.com/zukijifukato"))

	githubLabel = tk.Label(aboutFrame, text="Github: ", font='Arial 12')
	githubLabel.grid(row=4, column=0)

	githubLink = tk.Label(aboutFrame, text="https://github.com/zukijifukato/Quoted", fg="#00f", cursor="hand2", font='Arial 12 underline')
	githubLink.grid(row=4, column=1, sticky=tk.W)
	githubLink.bind("<Button-1>", lambda e: openlink("https://github.com/zukijifukato/Quoted"))

	aboutFrame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

	aboutFrame.grid_rowconfigure(2, minsize=40)

	about.mainloop()

fetchQuoteList()

window = tk.Tk()
window.title("Quoted")
window.geometry("600x480")
window.configure(bg='#fff')
window.iconphoto(True, tk.PhotoImage(file="icon.png"))
# window.resizable(False, False)

menubar = tk.Menu(window, borderwidth=0)

filemenu = tk.Menu(menubar, tearoff=0, borderwidth=0)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="File", menu=filemenu)

helpmenu = tk.Menu(menubar, tearoff=0, borderwidth=0)
helpmenu.add_command(label="About", command=about)
menubar.add_cascade(label='Help', menu=helpmenu)

topFrame = tk.Frame(window, bg='#fff')
bottomFrame = tk.Frame(window, bg='#fff')

quoteText = ""
quoteAuthor = ""

quoteLabel = tk.Label(topFrame, text=quoteText)
fontHeader(quoteLabel)
authorLabel = tk.Label(topFrame, text=quoteAuthor)
fontNormal(authorLabel)

fetchButton = tk.Button(bottomFrame, text="New Quote", command=fetchQuote)
fetchNewListButton = tk.Button(bottomFrame,text="New List", command=fetchNewList)
copyButton = tk.Button(bottomFrame, text='Copy to Clipboard', command=copyToClipboard)

fetchQuote()

quoteLabel.grid(row=0, column=0, columnspan=2)
authorLabel.grid(row=2, column=0, columnspan=2, stick=tk.W)

fetchButton.grid(row=0, column=0)
fetchNewListButton.grid(row=0, column=1)
copyButton.grid(row=0, column=2)

topFrame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
bottomFrame.pack(side=tk.BOTTOM)

topFrame.grid_rowconfigure(1, minsize=20)

window.config(menu=menubar)
window.mainloop()