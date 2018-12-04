from tkinter import *

root = Tk()

root.title("Banner Workaround")

scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill = Y )

line1 = Canvas(root, width=400, height=2,bd=0, highlightthickness=0)
line1.configure(bg="grey")

line2 = Canvas(root, width=400, height=2,bd=0, highlightthickness=0)
line2.configure(bg="grey")

line3 = Canvas(root, width=400, height=2,bd=0, highlightthickness=0)
line3.configure(bg="grey")

line4 = Canvas(root, width=400, height=2,bd=0, highlightthickness=0)
line4.configure(bg="grey")

line5 = Canvas(root, width=400, height=2,bd=0, highlightthickness=0)
line5.configure(bg="grey")

line6 = Canvas(root, width=400, height=2,bd=0, highlightthickness=0)
line6.configure(bg="grey")

line7 = Canvas(root, width=400, height=2,bd=0, highlightthickness=0)
line7.configure(bg="grey")

line8 = Canvas(root, width=400, height=2,bd=0, highlightthickness=0)
line8.configure(bg="grey")

line9 = Canvas(root, width=400, height=2,bd=0, highlightthickness=0)
line9.configure(bg="grey")

line10 = Canvas(root, width=400, height=2,bd=0, highlightthickness=0)
line10.configure(bg="grey")

line11 = Canvas(root, width=400, height=2,bd=0, highlightthickness=0)
line11.configure(bg="grey")

greetingLbl1 = Label(root, text = "Welcome to the hours logger!")
greetingLbl2 = Label(root, text = "For SPU employees who don't want to use banner.")
nameInpLbl = Label(root, text = "Please enter your SPU username:")
passInpLbl = Label(root, text = "Please enter your SPU password:")
submitLbl = Label(root, text = "Submit Hours:")

hoursLbl = Label(root, text = "Please enter the time you clocked in and the time you clocked out")
hours2Lbl = Label(root, text = "on each day that you worked (leave each day you did not work blank).")
monAmLbl = Label(root, text = "Monday (AM):")
monPmLbl = Label(root, text = "Monday (PM):")
tueAmLbl = Label(root, text = "Tuesday (AM):")
tuePmLbl = Label(root, text = "tuesday (PM):")
wedAmLbl = Label(root, text = "Wednesday (AM):")
wedPmLbl = Label(root, text = "Wednesday (PM):")
thrAmLbl = Label(root, text = "Thursday (AM):")
thrPmLbl = Label(root, text = "Thursday (PM):")
friAmLbl = Label(root, text = "Friday (AM):")
friPmLbl = Label(root, text = "Friday (PM):")
satAmLbl = Label(root, text = "Saturday (AM):")
satPmLbl = Label(root, text = "Saturday (PM):")
#Lbl = Label(root, text = "")

enterName = Entry(root)
enterPass = Entry(root)
amMon = Entry(root)
pmMon = Entry(root)
amTue = Entry(root)
pmTue = Entry(root)
amWed = Entry(root)
pmWed = Entry(root)
amThr = Entry(root)
pmThr = Entry(root)
amFri = Entry(root)
pmFri = Entry(root)
amSat = Entry(root)
pmSat = Entry(root)

submitBtn = Button(text = "Submit")

space1 = Label(root, text = "")
space2 = Label(root, text = "")
space3 = Label(root, text = "")
space4 = Label(root, text = "")
space5 = Label(root, text = "")
space6 = Label(root, text = "")
space7 = Label(root, text = "")
space8 = Label(root, text = "")
space9 = Label(root, text = "")
space10 = Label(root, text = "")
space11 = Label(root, text = "")
space12 = Label(root, text = "")
space13 = Label(root, text = "")
space14 = Label(root, text = "")
space15 = Label(root, text = "")
space16 = Label(root, text = "")
space17 = Label(root, text = "")
space18 = Label(root, text = "")
space19 = Label(root, text = "")
space20 = Label(root, text = "")

greetingLbl1.config(font = ("Courier", 24))
greetingLbl2.config(font = ("Courier", 14))

greetingLbl1.pack(fill = X)	# Displasy greeting
greetingLbl2.pack(fill = X)
space1.pack()

nameInpLbl.pack(fill = X)	# Asks for username
enterName.pack(fill = Y)
space2.pack()

passInpLbl.pack(fill = X)	# Asks for pass
enterPass.pack(fill = Y)
space3.pack()
line1.pack()
space4.pack()

hoursLbl.pack()		# Displays message
hours2Lbl.pack()
space5.pack()
line2.pack()
space6.pack()

thrAmLbl.pack()		# Thursday
amThr.pack()
thrPmLbl.pack()
pmThr.pack()
space13.pack()
line6.pack()
space14.pack()

friAmLbl.pack()		# Friday
amFri.pack()
friPmLbl.pack()
pmFri.pack()
space15.pack()
line7.pack()
space16.pack()

satAmLbl.pack()		# Saturday
amSat.pack()
satPmLbl.pack()
pmSat.pack()
space17.pack()
line8.pack()
space18.pack()

submitLbl.pack()	# Submit
space19.pack()
submitBtn.pack()
space20.pack()

root.mainloop()