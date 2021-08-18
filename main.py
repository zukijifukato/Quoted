import tkinter as tk
import requests
from secrets import randbelow
import pyperclip

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
	label.config(font=('Arial bold', 20), bg='#fff', justify='left', wraplength=580)

def fontNormal(label):
	label.config(font=('Arial italic', 12), bg='#fff', justify='left', wraplength=580)

def copyToClipboard():
	pyperclip.copy(quoteText)
	print(quoteText)

fetchQuoteList()

window = tk.Tk()
window.title("Quoted")
window.geometry("600x480")
window.configure(bg='#fff')
window.iconphoto(True, tk.PhotoImage(file="icon.png"))

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

window.mainloop()