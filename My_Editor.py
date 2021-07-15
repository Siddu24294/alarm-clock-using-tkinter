import tkinter as tk
from tkinter import *
from tkinter import messagebox
import time,winsound

global testStr,checkWindow
testStr = "SID"
"""checker section"""


def drawCheckWindow(alarmMeassage):
	global checkWindow
	checkWindow = tk.Tk()
	checkWindow.title(alarmMeassage)
	checkWindow.geometry("200x150")
	checkWindow.attributes("-topmost",True)
	drawBasics(alarmMeassage)
	checkWindow.protocol("WM_DELETE_WINDOW", on_closing)
	checkWindow.mainloop()



def on_closing():
	messagebox.showinfo("Not permitted","you are not allowed to close this window without correctly answering the question")
# creating widget for check window
def drawBasics(alarmMessage):

	message=Label(checkWindow,text=
	f"ALARM LABELLED\n{alarmMessage}\n IS PLAYING!!!")
	message.grid(row=0,column=0)

	checkText = Label(checkWindow, text=f"Enter this text below:{testStr}")
	checkText.grid(row=1, column=0)

	global captchaBox
	captchaBox = Entry(checkWindow, width=15)
	captchaBox.grid(row=2, column=0)

	global checkButton
	checkButton = Button(checkWindow, text="Check!", command=check)
	checkButton.grid(row=3, column=0)


def check():
	global captchaBox,checkButton,label3
	if captchaBox.get()==testStr:
		winsound.PlaySound("*", winsound.SND_ASYNC)
		messagebox.showinfo("test passed!!!", "Click on ok to exit")
		checkWindow.destroy()
		label3.config(text="NO ALARM DUE")

	else:
		messagebox.showinfo("wrong answer", "retry after clicking ok")


"""alarm clock section"""


# creating widget for main window
def createWidgets():

	label1=Label(root,text="Enter the time in 24hr HH:MM format:")
	label1.grid(row=0, column=0, padx=5,pady=5)

	global entry1
	entry1=Entry(root,width=15)
	entry1.grid(row=0,column=1)

	label2=Label(root,text="Enter the message of alarm:")
	label2.grid(row=1, column=0, padx=5,pady=5)

	global entry2
	entry2=Entry(root,width=15)
	entry2.grid(row=1,column=1)

	but=Button(root,text="Submit",width=10,command=submit)
	but.grid(row=2,column=1)

	global label3
	label3=Label(root,text="")
	label3.grid(row=3,column=1)

	exitButton=Button(root,text="EXIT",command=checkExit)
	exitButton.grid(row=2,column=2)

	note=Label(root,text="          WARNING              \n"
	                     "WHEN THE ALARM PLAYS, DON'T CLOSE\n"
	                     "THE CHECKING WINDOW WITHOUT CORRECTLY\n"
	                     " ANSWERING THE QUESTION...OR ELSE THE\n"
	                     "ALARM SOUND WILL KEEP ON PLAYING FOREVER\n"
	                     " UNTIL U REBOOT THE MACHINE...")
	note.grid(row=4,column=0)


def checkExit():
	global exitWin
	exitWin=tk.Tk()
	exitWin.title("ARE YOU SURE?")
	exitWin.geometry("200x100")

	question=Label(exitWin,text="Are you sure you wanna exit?")
	question.grid(row=0,column=0)

	yes=Button(exitWin,text="YES",command=kill)
	yes.grid(row=1,column=0)
	no=Button(exitWin,text="NO",command=exitWin.destroy)
	no.grid(row=1,column=1)
	exitWin.mainloop()


def kill():root.destroy();exitWin.destroy()


def message1():
	global entry1,label3
	alarmtimelabel=entry1.get()
	label3.config(text="The alarm is  counting...")
	messagebox.showinfo("Alarm Clock",f"The Alarm time is: {alarmtimelabel}")


def submit():
	global entry1,entery2,label3
	alarmtime=entry1.get()
	message1()
	currenttime=time.strftime("%H:%M")
	while alarmtime!=currenttime:
		currenttime= time.strftime("%H:%M")
		time.sleep(1)
	if alarmtime==currenttime:
		winsound.PlaySound('C:/Windows/Media/notify.wav', winsound.SND_LOOP + winsound.SND_ASYNC)
		label3.config(text="Alarm playing....")
		drawCheckWindow(entry2.get())


if __name__=="__main__":
	root=tk.Tk()
	root.title("Annoying Alarm Clock")
	root.geometry("500x210")
	createWidgets()
	root.mainloop()