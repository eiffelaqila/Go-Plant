# Import Modules
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from modules.registerUI import *
from modules.validationController import *

class loginUI():
    # Attribute
    # root: Tk
    # valControl: validationController
    # usernameAdmin: String
    # passwordAdmin: String
    # usernameCustomer: String
    # passwordCustomer: String

    # Constructor
    def __init__(self, root, frame, db):
        self.root = root
        self.db = db
        self.valControl = validationController(self.root, self.db)

        frame.destroy()

        # Create Login Frame
        loginFrame = Frame(self.root, bg = "#DCE1DE")
        loginFrame.place(x = 0, y = 0, width = 1280, height = 720)

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
        global loginBg
        loginBg = ImageTk.PhotoImage(Image.open('./img/GoPlantLoginBg.png').resize((496,396)))
        loginBgImage = Label(loginFrame, image = loginBg, bg = "#DCE1DE")
        loginBgImage.place(relx = 0.5, y = 191, anchor = "n")


        # *** LOGIN ATTRIBUTES ***
        self.usernameAdmin = StringVar()
        self.passwordAdmin = StringVar()
        self.usernameCustomer = StringVar()
        self.passwordCustomer = StringVar()


        # *** LOGIN AS ADMIN FRAME ***
        loginAdminFrame = Frame(loginFrame, bg = "#FFFFFF")
        loginAdminFrame.place(x = 160, y = 200, width = 400, height = 360)

        # Label
        loginAdminLabel = Label(loginAdminFrame, text = "Login as Admin", font = "Montserrat 24 bold", bg = "#FFFFFF", fg = "#216869")
        loginAdminLabel.place(relx = 0.5, y = 40, anchor = "n")

        # Username Input
        usernameAdminLabel = Label(loginAdminFrame, text = "Username", font = "Montserrat 10", bg = "#FFFFFF", fg = "#1F2421")
        usernameAdminLabel.place(x = 39, y = 120)
        usernameAdminLabel = Entry(loginAdminFrame, bd = 1, bg = "#FFFFFF", relief = GROOVE, width = 52, textvariable = self.usernameAdmin)
        usernameAdminLabel.place(x = 40, y = 141)

        # Password Input
        passwordAdminLabel = Label(loginAdminFrame, text = "Password", font = "Montserrat 10", bg = "#FFFFFF", fg = "#1F2421")
        passwordAdminLabel.place(x = 39, y = 180)
        passwordAdminLabel = Entry(loginAdminFrame, show = "*", bd = 1, bg = "#FFFFFF", relief = GROOVE, width = 52, textvariable = self.passwordAdmin)
        passwordAdminLabel.place(x = 40, y = 201)

        # Button
        loginAdminButton = Button(loginAdminFrame, text = "Log In", font = "Montserrat 10 bold", activebackground = "#FFFFFF", fg = "#FFFFFF", bg = "#216869", padx=15, pady=5, relief=FLAT, width=10, command = lambda:self.requestLoginAsAdmin(loginFrame))
        loginAdminButton.place(relx = 0.5, y = 280, anchor = "n")


        # *** LOGIN AS CUSTOMER FRAME ***
        loginCustomerFrame = Frame(loginFrame, bg = "#FFFFFF")
        loginCustomerFrame.place(x = 720, y = 200, width = 400, height = 360)

        # Label
        loginCustomerLabel = Label(loginCustomerFrame, text = "Login as Customer", font = "Montserrat 24 bold", bg = "#FFFFFF", fg = "#216869")
        loginCustomerLabel.place(relx = 0.5, y = 40, anchor = "n")

        # Username Input
        usernameCustomerLabel = Label(loginCustomerFrame, text = "Username", font = "Montserrat 10", bg = "#FFFFFF", fg = "#1F2421")
        usernameCustomerLabel.place(x = 39, y = 120)
        usernameCustomerEntry = Entry(loginCustomerFrame, bd = 1, bg = "#FFFFFF", relief = GROOVE, width = 52, textvariable = self.usernameCustomer)
        usernameCustomerEntry.place(x = 40, y = 141)

        # Password Input
        passwordCustomerLabel = Label(loginCustomerFrame, text = "Password", font = "Montserrat 10", bg = "#FFFFFF", fg = "#1F2421")
        passwordCustomerLabel.place(x = 39, y = 180)
        passwordCustomerEntry = Entry(loginCustomerFrame, show = "*", bd = 1, bg = "#FFFFFF", relief = GROOVE, width = 52, textvariable = self.passwordCustomer)
        passwordCustomerEntry.place(x = 40, y = 201)

        # Button
        loginCustomerButton = Button(loginCustomerFrame, text = "Log In", font = "Montserrat 10 bold", activebackground = "#FFFFFF", fg = "#FFFFFF", bg = "#216869", padx=15, pady=5, relief=FLAT, width=10, command = lambda:self.requestLoginAsCustomer(loginFrame))
        loginCustomerButton.place(relx = 0.5, y = 280, anchor = "n")


        # *** SIGN UP ***
        SignUpLabel = Label(loginFrame, text = "If you don't have an account, create one now", font = "Montserrat 12", bg = "#DCE1DE", fg = "#1F2421")
        SignUpLabel.place(x = 386, y = 602, anchor = "nw")

        # Button
        SignUpButton = Button(loginFrame, text = "Sign Up", font = "Montserrat 10 bold", activebackground = "#FFFFFF", fg = "#FFFFFF", bg = "#216869", padx=12, pady=2, relief=FLAT, width=10, command = lambda:registerUI(self.root, loginFrame, self.valControl, self.db))
        SignUpButton.place(x = 759, y = 600, anchor = "nw")


    # Request Login As Admin
    def requestLoginAsAdmin(self, frame):
        if (self.getUsernameAdmin() == ""):
            self.showMessage("Enter username!")
        elif (self.getPasswordAdmin() == ""):
            self.showMessage("Enter password!")
        else:
            self.valControl.verifyLoginAdmin(frame, self.getUsernameAdmin(), self.getPasswordAdmin())

    # Request Login As Customer
    def requestLoginAsCustomer(self, frame):
        if (self.getUsernameCustomer() == ""):
            self.showMessage("Enter username!")
        elif (self.getPasswordCustomer() == ""):
            self.showMessage("Enter password!")
        else:
            self.valControl.verifyLoginCustomer(frame, self.getUsernameCustomer(), self.getPasswordCustomer())


    # Show Message
    def showMessage(self, message):
        messagebox.showinfo("Alert!", message)
    

    # Getter - Setter
    def getUsernameAdmin(self):
        return self.usernameAdmin.get()
    
    def getPasswordAdmin(self):
        return self.passwordAdmin.get()

    def getUsernameCustomer(self):
        return self.usernameCustomer.get()
    
    def getPasswordCustomer(self):
        return self.passwordCustomer.get()