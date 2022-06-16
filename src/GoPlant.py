from tkinter import *
from PIL import ImageTk, Image
from modules.loginUI import *
from databases.database import *

class GoPlant:
    """
    This class will check if database is already connected,
    if connected, open loginUI, otherwise, open databaseConnectorUI
    """
    def __init__(self, root):
        self.root = root

        # Create Root Frame
        rootFrame = Frame(self.root, bg = "#DCE1DE")
        rootFrame.place(x = 0, y = 0, width = 1280, height = 720)

        # *** HEADER FRAME ***
        # Header
        headerFrame = Frame(rootFrame, bg = "#FFFFFF")
        headerFrame.place(x = 0, y = 0, width = 1280, height = 110)

        # Logo
        global logo
        logo = ImageTk.PhotoImage(Image.open('./img/GoPlant.png').resize((186,60)))
        headerLogo = Label(headerFrame, image = logo, bg = "#FFFFFF")
        headerLogo.place(relx = 0.5, y = 20, anchor = "n")


        # *** MASCOT ***
        # GoPlant Mascot
        global mascot
        mascot = ImageTk.PhotoImage(Image.open('./img/GoPlantBg.png').resize((454,363)))
        mascotImg = Label(rootFrame, image = mascot, bg = "#DCE1DE")
        mascotImg.place(x = 172, y = 186)

        # Tagline
        tagLabel = Label(rootFrame, text = "Sewa Mudah Hanya di", font = "Montserrat 16 bold", bg = "#DCE1DE", fg = "#000000")
        tagLabel.place(x = 218, y = 587)

        # Logo Input2
        global logo2
        logo2 = ImageTk.PhotoImage(Image.open('./img/GoPlant.png').resize((99,32)))
        logo2_ = Label(rootFrame, image = logo2, bg = "#DCE1DE")
        logo2_.place(x = 473, y = 580, anchor = "nw")


        # Attribute
        self.host = StringVar()
        self.port = StringVar()
        self.username = StringVar()
        self.password = StringVar()

        # *** MySQL SETUP FRAME ***
        mySQLSetupFrame = Frame(rootFrame, bg = "#FFFFFF")
        mySQLSetupFrame.place(x = 720, y = 160, height = 480, width = 400)

        # MySQL Setup title
        mySQLSetupTitle = Label(mySQLSetupFrame, text = "MySQL Setup", font = "Montserrat 24 bold", bg = "#FFFFFF", fg = "#216669")
        mySQLSetupTitle.place(relx = 0.5, y = 40, anchor = "n")

        # Host Input
        hostLabel = Label(mySQLSetupFrame, text = "Host Name", font = "Montserrat 10 bold", bg = "#FFFFFF", fg = "#216669")
        hostLabel.place(x = 39, y = 120, anchor = "nw")
        hostEntry = Entry(mySQLSetupFrame, bd = 1, bg = "#FFFFFF", relief = GROOVE, width = 52, textvariable = self.host)
        hostEntry.place(x = 40, y = 142)

        # Port Input
        portLabel = Label(mySQLSetupFrame, text = "Port", font = "Montserrat 10 bold", bg = "#FFFFFF", fg = "#216669")
        portLabel.place(x = 39, y = 180, anchor = "nw")
        portEntry = Entry(mySQLSetupFrame, bd = 1, bg = "#FFFFFF", relief = GROOVE, width = 52, textvariable = self.port)
        portEntry.place(x = 40, y = 201)

        # Username Input
        usernameLabel = Label(mySQLSetupFrame, text = "Username", font = "Montserrat 10 bold", bg = "#FFFFFF", fg = "#216669")
        usernameLabel.place(x = 39, y = 239, anchor = "nw")
        usernameEntry = Entry(mySQLSetupFrame, bd = 1, bg = "#FFFFFF", relief = GROOVE, width = 52, textvariable = self.username)
        usernameEntry.place(x = 40, y = 260)

        # Password Input
        passwordLabel = Label(mySQLSetupFrame, text = "Password", font = "Montserrat 10 bold", bg = "#FFFFFF", fg = "#216669")
        passwordLabel.place(x = 39, y = 298, anchor = "nw")
        passwordEntry = Entry(mySQLSetupFrame, show = "*", bd = 1, bg = "#FFFFFF", relief = GROOVE, width = 52, textvariable = self.password)
        passwordEntry.place(x = 40, y = 319)
        
        # Button
        submitButton = Button(mySQLSetupFrame, text = "Submit", font = "Montserrat 10 bold", activebackground = "#FFFFFF", fg = "#FFFFFF", bg = "#216869", padx=10, pady=2, relief=FLAT, width=10, command = lambda:self.dbinit(root, rootFrame, self.host.get(), self.port.get(), self.username.get(), self.password.get()))
        submitButton.place(relx = 0.5, y = 400, anchor = "n")

    # Setting up database
    def dbinit(self, root, frame, host, port, username, password):
        if (host == ""):
            self.showMessage("Enter host!")
        elif (port == ""):
            self.showMessage("Enter port!")
        elif (username == ""):
            self.showMessage("Enter username!")
        elif (password == ""):
            self.showMessage("Enter password!")
        else:
            # Setup database
            db = database(host, int(port), username, password)

            # Jump to login page
            loginUI(root, frame, db)

    # Show Message
    def showMessage(self, message):
        messagebox.showinfo("Alert!", message)


# MAIN PROGRAM
if __name__ == '__main__':
    # Root window
    root = Tk()
    root.title("Go Plant")
    root.geometry("1280x720+100+50")
    root.config(bg = "#DCE1DE")
    GoPlant(root)

    # Main Loop
    root.mainloop()