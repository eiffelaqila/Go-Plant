# Import Modules
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from modules.validationController import *

class registerUI():
    # Attribute
    # root: Tk
    # valControl: validationController
    # username: String
    # password: String
    # alamat: String

    # Constructor
    def __init__(self, root, frame, valControl, db):
        self.root = root
        self.valControl = valControl
        self.db = db
        frame.destroy()


        # Create Register Frame
        regFrame = Frame(root, bg = "#DCE1DE")
        regFrame.place(x = 0, y = 0, width = 1280, height = 720)


        # *** HEADER FRAME ***
        # Header
        headerFrame = Frame(self.root, bg = "#FFFFFF")
        headerFrame.place(x = 0, y = 0, width = 1280, height = 110)

        # Logo
        global logo
        logo = ImageTk.PhotoImage(Image.open('./img/GoPlant.png').resize((186,60)))
        headerLogo = Label(headerFrame, image = logo, bg = "#FFFFFF")
        headerLogo.place(relx = 0.5, y = 20, anchor = "n")

        # Background
        global regBg
        regBg = ImageTk.PhotoImage(Image.open('./img/GoPlantRegisterBg.png').resize((661,486)))
        regBgImage = Label(regFrame, image = regBg, bg = "#DCE1DE")
        regBgImage.place(relx = 0.5, y = 168, anchor = "n")


        # *** REGISTER ATTRIBUTE ***
        self.username = StringVar()
        self.password = StringVar()
        self.alamat = StringVar()


        # *** REGISTER FRAME ***
        registerFrame = Frame(regFrame, bg = "#FFFFFF")
        registerFrame.place(x = 440, y = 200, width = 400, height = 440)

        # Label
        registerLabel = Label(registerFrame, text = "Sign Up", font = "Montserrat 24 bold", bg = "#FFFFFF", fg = "#216869")
        registerLabel.place(relx = 0.5, y = 40, anchor = "n")

        # Username Input
        usernameLabel = Label(registerFrame, text = "Username/Email", font = "Montserrat 10", bg = "#FFFFFF", fg = "#1F2421")
        usernameLabel.place(x = 39, y = 120)
        usernameEntry = Entry(registerFrame, bd = 1, bg = "#FFFFFF", relief = GROOVE, width = 52, textvariable = self.username)
        usernameEntry.place(x = 40, y = 141)

        # Password Input
        passwordLabel = Label(registerFrame, text = "Password", font = "Montserrat 10", bg = "#FFFFFF", fg = "#1F2421")
        passwordLabel.place(x = 39, y = 180)
        passwordEntry = Entry(registerFrame, show = "*", bd = 1, bg = "#FFFFFF", relief = GROOVE, width = 52, textvariable = self.password)
        passwordEntry.place(x = 40, y = 201)

        # Alamat Input
        alamatLabel = Label(registerFrame, text = "Alamat (optional)", font = "Montserrat 10", bg = "#FFFFFF", fg = "#1F2421")
        alamatLabel.place(x = 39, y = 240)
        alamatEntry = Text(registerFrame, bd = 1, bg = "#FFFFFF", relief = GROOVE, width = 39, height = 4)
        alamatEntry.place(x = 40, y = 261)
        self.alamat = alamatEntry

        # Button
        registerButton = Button(registerFrame, text = "Sign Up", font = "Montserrat 10 bold", activebackground = "#FFFFFF", fg = "#FFFFFF", bg = "#216869", padx=15, pady=5, relief=FLAT, width=10, command = lambda:self.requestRegister(regFrame))
        registerButton.place(relx = 0.5, y = 360, anchor = "n")


    # Request Register
    def requestRegister(self, frame):
        if (self.getUsername() == ""):
            self.showMessage("Enter username!")
        elif (self.getPassword() == ""):
            self.showMessage("Enter password!")
        else:
            self.valControl.validate(frame, self.getUsername(), self.getPassword(), self.getAlamat())


    # Show Message
    def showMessage(self, message):
        messagebox.showinfo("Alert!", message)
        
    # Getter - Setter
    def getUsername(self):
        return self.username.get()
    
    def getPassword(self):
        return self.password.get()

    def getAlamat(self):
        return self.alamat.get("1.0", 'end-1c')