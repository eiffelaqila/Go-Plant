# Import Modules
import mysql.connector as sql
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import modules.approvalPageUI

class stockManagementUI():
    # Attribute
    # root: Tk
    # idTanaman : integer
    # namaTanaman : string
    # stok : integer
    # harga : integer
    # imgPath : string

    # Constructor
    def __init__(self, root, db, frame):
        from modules.loginUI import loginUI
        self.root = root
        self.db = db
        self.currentIdx = 0
        frame.destroy()

        # Stock Management Frame
        self.stockManagementFrame = Frame(self.root, bg="#FFFFFF")
        self.stockManagementFrame.place(x = 0, y = 0, width = 1280, height = 720)

        # *** HEADER FRAME ***
        # Header
        headerFrame = Frame(self.stockManagementFrame, bg = "#FFFFFF")
        headerFrame.place(x = 0, y = 0, width = 1280, height = 110)

        # Logo
        global logo
        logo = ImageTk.PhotoImage(Image.open('./img/GoPlant.png').resize((186,60)))
        headerLogo = Button(headerFrame, image = logo, bg = "#FFFFFF", relief=FLAT, borderwidth=0, highlightthickness=0, command=lambda: loginUI(self.root, self.stockManagementFrame, self.db))
        headerLogo.place(x = 80, y = 20, anchor = "nw")

        adminLabel = Label(headerFrame, text="Admin Mode", font="Montserrat 12", bg="#FFFFFF")
        adminLabel.place(x=275, y=63, anchor="nw")

        global btnStockManagement_image
        btnStockManagement_image = ImageTk.PhotoImage(Image.open("./img/btnStockManagement.png"))
        btnStockManagement = Button(headerFrame, image=btnStockManagement_image, borderwidth=0, highlightthickness=0, command=lambda: print("btnStockManagement clicked"), relief="flat")
        btnStockManagement.place(x=1027.0, y=31.0, width=186.0, height=55.0)

        global btnApprovalPage_image
        btnApprovalPage_image = ImageTk.PhotoImage(Image.open("./img/btnApprovalPage.png"))
        btnApprovalPage = Button(headerFrame, image=btnApprovalPage_image, borderwidth=0, highlightthickness=0, command=lambda:modules.approvalPageUI.approvalPageUI(self.root, self.db, self.stockManagementFrame), relief="flat")
        btnApprovalPage.place(x=830.0, y=31.0, width=186.0, height=55.0)

        global btnSearch_image
        btnSearch_image = ImageTk.PhotoImage(Image.open("./img/btnSearch.png"))
        btnSearch = Button(headerFrame, image=btnSearch_image, borderwidth=0, highlightthickness=0, command=lambda: print("btnSearch clicked"), relief="flat")
        btnSearch.place(x=632.0, y=31.0, width=185.0, height=55.0)

        # Label
        stockManagementLabel = Label(self.stockManagementFrame, text="Stock Management Page", bg="#FFFFFF", font="Montserrat 18 bold", width=200)
        stockManagementLabel.place(relx=0.5, y=120, anchor="center")

        # Pull database
        mycon = sql.connect(host=self.db.host, port=self.db.port, user=self.db.username, password=self.db.password, database='goplant')
        cur = mycon.cursor()
        cur.execute('SELECT nama_tanaman, stok, harga, img_path FROM Tanaman')
        datas = cur.fetchall()

        # Add new stock button
        newStockButton = Button(self.stockManagementFrame, text="Add new stock", font = "Montserrat 10 bold", padx=50, activebackground="#FFFFFF", fg = "#FFFFFF", bg = "#216869", command=self.addNewStock)
        newStockButton.place(relx=0.5, y=690, anchor="center")

        # Left Button
        leftButton = Button(self.stockManagementFrame, text="<", font = "Montserrat 18 bold", activebackground="#FFFFFF", fg = "#FFFFFF", bg = "#216869", command=lambda:self.moveLeft(datas))
        leftButton.place(x=100, rely=0.57, anchor="center")

        # Right Button
        rightButton = Button(self.stockManagementFrame, text=">", font = "Montserrat 18 bold", activebackground="#FFFFFF", fg = "#FFFFFF", bg = "#216869", command=lambda:self.moveRight(datas))
        rightButton.place(x=1180, rely=0.57, anchor="center")
        
        self.displayItemFrames(self.stockManagementFrame, datas, 0)

    # Large Item Frame
    def displayItemFrames(self, mainFrame, datas, curIdx):   
        largeItemFrame = Frame(mainFrame)
        largeItemFrame.place(relx=0.5, rely=0.58, anchor="center", width=800, height=475)
        position = 70

        if(curIdx <= len(datas) - 1):
            global img1
            img1 = ImageTk.PhotoImage(Image.open(str(datas[curIdx + 0][3])).resize((50, 50)))

            # Item Frame
            itemFrame1 = Frame(largeItemFrame, bg = "#CFE6DB", highlightbackground="#0A750F", highlightthickness=2)
            itemFrame1.place(relx=0.5, y = position, anchor="center", width=750, height=100)

            # Image Tanaman
            logoPlant1 = Label(itemFrame1, image=img1)
            logoPlant1.place(x=50, rely=0.5, anchor="center")

            # Name Label
            nameLabel1 = Label(itemFrame1, text="Nama: " + datas[curIdx + 0][0], font="Montserrat 12", bg="#CFE6DB", fg="black")
            nameLabel1.place(x=100, rely=0.15)

            # Stock Label
            stockLabel1 = Label(itemFrame1, text="Stock: " + str(datas[curIdx + 0][1]), font="Montserrat 12", bg="#CFE6DB", fg="black")
            stockLabel1.place(x=100, rely=0.4)

            # Price Label
            priceLabel1 = Label(itemFrame1, text="Harga: " + str(datas[curIdx + 0][2]), font="Montserrat 12", bg="#CFE6DB", fg="black")
            priceLabel1.place(x=100, rely=0.65)

            # Delete Button
            deleteButton1 = Button(itemFrame1, text="Delete", font = "Montserrat 10 bold", activebackground="#FFFFFF", fg = "#FFFFFF", bg = "#216869", command=lambda:self.deleteTanaman(datas[curIdx + 0][0]))
            deleteButton1.place(relx=0.573, rely=0.65)

            # Rename Button
            renameButton1 = Button(itemFrame1, text="Rename", font = "Montserrat 10 bold", activebackground="#FFFFFF", fg = "#FFFFFF", bg = "#216869", command=lambda:self.renameTanaman(datas[curIdx + 0][0]))
            renameButton1.place(relx=0.653, rely=0.65)

            # Add Stock Button
            addStockButton1 = Button(itemFrame1, text="Add Stock", font = "Montserrat 10 bold", activebackground="#FFFFFF", fg = "#FFFFFF", bg = "#216869", command=lambda:self.addStock(datas[curIdx + 0][0]))
            addStockButton1.place(relx=0.747, rely=0.65)

            # Update Price Button
            updatePriceButton1 = Button(itemFrame1, text="Update Price", font = "Montserrat 10 bold", activebackground="#FFFFFF", fg = "#FFFFFF", bg = "#216869", command=lambda:self.updatePrice(datas[curIdx + 0][0]))
            updatePriceButton1.place(relx=0.86, rely=0.65)

            position += 110
            if (curIdx <= len(datas) - 2):
                global img2
                img2 = ImageTk.PhotoImage(Image.open(str(datas[curIdx + 1][3])).resize((50, 50)))

                # Item Frame
                itemFrame2 = Frame(largeItemFrame, bg = "#CFE6DB", highlightbackground="#0A750F", highlightthickness=2)
                itemFrame2.place(relx=0.5, y = position, anchor="center", width=750, height=100)

                # Image Tanaman
                logoPlant2 = Label(itemFrame2, image=img2)
                logoPlant2.place(x=50, rely=0.5, anchor="center")

                # Name Label
                nameLabel2 = Label(itemFrame2, text="Nama: " + datas[curIdx + 1][0], font="Montserrat 12", bg="#CFE6DB", fg="black")
                nameLabel2.place(x=100, rely=0.15)

                # Stock Label
                stockLabel2 = Label(itemFrame2, text="Stock: " + str(datas[curIdx + 1][1]), font="Montserrat 12", bg="#CFE6DB", fg="black")
                stockLabel2.place(x=100, rely=0.4)

                # Price Label
                priceLabel2 = Label(itemFrame2, text="Harga: " + str(datas[curIdx + 1][2]), font="Montserrat 12", bg="#CFE6DB", fg="black")
                priceLabel2.place(x=100, rely=0.65)

                # Delete Button
                deleteButton2 = Button(itemFrame2, text="Delete", font = "Montserrat 10 bold", activebackground="#FFFFFF", fg = "#FFFFFF", bg = "#216869", command=lambda:self.deleteTanaman(datas[curIdx + 1][0]))
                deleteButton2.place(relx=0.573, rely=0.65)

                # Rename Button
                renameButton2 = Button(itemFrame2, text="Rename", font = "Montserrat 10 bold", activebackground="#FFFFFF", fg = "#FFFFFF", bg = "#216869", command=lambda:self.renameTanaman(datas[curIdx + 1][0]))
                renameButton2.place(relx=0.653, rely=0.65)

                # Add Stock Button
                addStockButton2 = Button(itemFrame2, text="Add Stock", font = "Montserrat 10 bold", activebackground="#FFFFFF", fg = "#FFFFFF", bg = "#216869", command=lambda:self.addStock(datas[curIdx + 1][0]))
                addStockButton2.place(relx=0.747, rely=0.65)

                # Update Price Button
                updatePriceButton2 = Button(itemFrame2, text="Update Price", font = "Montserrat 10 bold", activebackground="#FFFFFF", fg = "#FFFFFF", bg = "#216869", command=lambda:self.updatePrice(datas[curIdx + 1][0]))
                updatePriceButton2.place(relx=0.86, rely=0.65)

                position += 110
                if (curIdx <= len(datas) - 3):
                    global img3
                    img3 = ImageTk.PhotoImage(Image.open(str(datas[curIdx + 2][3])).resize((50, 50)))

                    # Item Frame
                    itemFrame3 = Frame(largeItemFrame, bg = "#CFE6DB", highlightbackground="#0A750F", highlightthickness=2)
                    itemFrame3.place(relx=0.5, y = position, anchor="center", width=750, height=100)

                    # Image Tanaman
                    logoPlant3 = Label(itemFrame3, image=img3)
                    logoPlant3.place(x=50, rely=0.5, anchor="center")

                    # Name Label
                    nameLabel3 = Label(itemFrame3, text="Nama: " + datas[curIdx + 2][0], font="Montserrat 12", bg="#CFE6DB", fg="black")
                    nameLabel3.place(x=100, rely=0.15)

                    # Stock Label
                    stockLabel3 = Label(itemFrame3, text="Stock: " + str(datas[curIdx + 2][1]), font="Montserrat 12", bg="#CFE6DB", fg="black")
                    stockLabel3.place(x=100, rely=0.4)

                    # Price Label
                    priceLabel3 = Label(itemFrame3, text="Harga: " + str(datas[curIdx + 2][2]), font="Montserrat 12", bg="#CFE6DB", fg="black")
                    priceLabel3.place(x=100, rely=0.65)

                    # Delete Button
                    deleteButton3 = Button(itemFrame3, text="Delete", font = "Montserrat 10 bold", activebackground="#FFFFFF", fg = "#FFFFFF", bg = "#216869", command=lambda:self.deleteTanaman(datas[curIdx + 2][0]))
                    deleteButton3.place(relx=0.573, rely=0.65)

                    # Rename Button
                    renameButton3 = Button(itemFrame3, text="Rename", font = "Montserrat 10 bold", activebackground="#FFFFFF", fg = "#FFFFFF", bg = "#216869", command=lambda:self.renameTanaman(datas[curIdx + 2][0]))
                    renameButton3.place(relx=0.653, rely=0.65)

                    # Add Stock Button
                    addStockButton3 = Button(itemFrame3, text="Add Stock", font = "Montserrat 10 bold", activebackground="#FFFFFF", fg = "#FFFFFF", bg = "#216869", command=lambda:self.addStock(datas[curIdx + 2][0]))
                    addStockButton3.place(relx=0.747, rely=0.65)

                    # Update Price Button
                    updatePriceButton3 = Button(itemFrame3, text="Update Price", font = "Montserrat 10 bold", activebackground="#FFFFFF", fg = "#FFFFFF", bg = "#216869", command=lambda:self.updatePrice(datas[curIdx + 2][0]))
                    updatePriceButton3.place(relx=0.86, rely=0.65)

                    position += 110
                    if (curIdx <= len(datas) - 4):
                        global img4
                        img4 = ImageTk.PhotoImage(Image.open(str(datas[curIdx + 3][3])).resize((50, 50)))

                        # Item Frame
                        itemFrame4 = Frame(largeItemFrame, bg = "#CFE6DB", highlightbackground="#0A750F", highlightthickness=2)
                        itemFrame4.place(relx=0.5, y = position, anchor="center", width=750, height=100)

                        # Image Tanaman
                        logoPlant4 = Label(itemFrame4, image=img4)
                        logoPlant4.place(x=50, rely=0.5, anchor="center")

                        # Name Label
                        nameLabel4 = Label(itemFrame4, text="Nama: " + datas[curIdx + 3][0], font="Montserrat 12", bg="#CFE6DB", fg="black")
                        nameLabel4.place(x=100, rely=0.15)

                        # Stock Label
                        stockLabel4 = Label(itemFrame4, text="Stock: " + str(datas[curIdx + 3][1]), font="Montserrat 12", bg="#CFE6DB", fg="black")
                        stockLabel4.place(x=100, rely=0.4)

                        # Price Label
                        priceLabel4 = Label(itemFrame4, text="Harga: " + str(datas[curIdx + 3][2]), font="Montserrat 12", bg="#CFE6DB", fg="black")
                        priceLabel4.place(x=100, rely=0.65)

                        # Delete Button
                        deleteButton4 = Button(itemFrame4, text="Delete", font = "Montserrat 10 bold", activebackground="#FFFFFF", fg = "#FFFFFF", bg = "#216869", command=lambda:self.deleteTanaman(datas[curIdx + 3][0]))
                        deleteButton4.place(relx=0.573, rely=0.65)

                        # Rename Button
                        renameButton4 = Button(itemFrame4, text="Rename", font = "Montserrat 10 bold", activebackground="#FFFFFF", fg = "#FFFFFF", bg = "#216869", command=lambda:self.renameTanaman(datas[curIdx + 3][0]))
                        renameButton4.place(relx=0.653, rely=0.65)

                        # Add Stock Button
                        addStockButton4 = Button(itemFrame4, text="Add Stock", font = "Montserrat 10 bold", activebackground="#FFFFFF", fg = "#FFFFFF", bg = "#216869", command=lambda:self.addStock(datas[curIdx + 3][0]))
                        addStockButton4.place(relx=0.747, rely=0.65)

                        # Update Price Button
                        updatePriceButton4 = Button(itemFrame4, text="Update Price", font = "Montserrat 10 bold", activebackground="#FFFFFF", fg = "#FFFFFF", bg = "#216869", command=lambda:self.updatePrice(datas[curIdx + 3][0]))
                        updatePriceButton4.place(relx=0.86, rely=0.65)

                        position += 110

    def deleteTanaman(self, name):
        # New Confirmation Window
        confirmationWindow = Toplevel(self.root)
        confirmationWindow.geometry("200x100+500+300")

        # Warning text
        warningLabel = Label(confirmationWindow, text="Are you sure you want to delete?", font="Montserrat 10")
        warningLabel.place(relx=0.5, y=5, anchor="n")

        def deleteFromDB(name):
            mycon = sql.connect(host=self.db.host, port=self.db.port, user=self.db.username, password=self.db.password, database='goplant')
            cur = mycon.cursor()
            cur.execute('DELETE FROM goplant.Tanaman WHERE nama_tanaman = %s', (name, ))
            mycon.commit()
            stockManagementUI(self.root, self.db)
            confirmationWindow.destroy()
            confirmationWindow.update()

        def cancelCommand():
            confirmationWindow.destroy()
            confirmationWindow.update()

        # Delete Button
        deleteButton = Button(confirmationWindow, text="Delete", font="Montserrat 10 bold", activebackground="#FFFFFF", fg = "#FFFFFF", bg = "#216869", command=lambda:deleteFromDB(name))
        deleteButton.place(relx=0.3, y=50, anchor="n")

        # Cancel Button
        cancelButton = Button(confirmationWindow, text="Cancel", font="Montserrat 10 bold", activebackground="#FFFFFF", fg = "#FFFFFF", bg = "#216869", command=cancelCommand)
        cancelButton.place(relx=0.7, y=50, anchor="n")

    def renameTanaman(self, oldName):
        # New Input Window
        inputWindow = Toplevel(self.root)
        inputWindow.geometry("200x100+500+300")

        # Label
        inputLabel = Label(inputWindow, text="Enter the new name:", font="Montserrat 10")
        inputLabel.place(relx=0.5, y=5, anchor="n")
        
        # New Entry
        inputEntry = Entry(inputWindow, bd=1, relief=GROOVE)
        inputEntry.place(relx=0.5, y=25, anchor="n")
        def getEntryInput(oldName):
            newName = inputEntry.get()
            mycon = sql.connect(host=self.db.host, port=self.db.port, user=self.db.username, password=self.db.password, database='goplant')
            cur = mycon.cursor()
            cur.execute('UPDATE goplant.Tanaman SET nama_tanaman = %s WHERE nama_tanaman = %s', (newName, oldName,))
            mycon.commit()
            stockManagementUI(self.root, self.db)
            inputWindow.destroy()
            inputWindow.update()

        # Button
        renameButton = Button(inputWindow, text="Rename", font="Montserrat 10 bold", activebackground="#FFFFFF", fg = "#FFFFFF", bg = "#216869", command=lambda:getEntryInput(oldName))
        renameButton.place(relx=0.5, y=50, anchor="n")
    
    def addStock(self, oldName):
        # New Input Window
        inputWindow = Toplevel(self.root)
        inputWindow.geometry("200x100+500+300")

        # Label
        inputLabel = Label(inputWindow, text="Enter the new stock count:", font="Montserrat 10")
        inputLabel.place(relx=0.5, y=5, anchor="n")
        
        # New Entry
        inputEntry = Entry(inputWindow, bd=1, relief=GROOVE)
        inputEntry.place(relx=0.5, y=25, anchor="n")
        def getEntryInput(oldName):
            newStock = inputEntry.get()
            mycon = sql.connect(host=self.db.host, port=self.db.port, user=self.db.username, password=self.db.password, database='goplant')
            cur = mycon.cursor()
            cur.execute('UPDATE goplant.Tanaman SET stok = %s WHERE nama_tanaman = %s', (newStock, oldName,))
            mycon.commit()
            stockManagementUI(self.root, self.db)
            inputWindow.destroy()
            inputWindow.update()

        # Button
        addStockButton = Button(inputWindow, text="Add Stock", font="Montserrat 10 bold", activebackground="#FFFFFF", fg = "#FFFFFF", bg = "#216869", command=lambda:getEntryInput(oldName))
        addStockButton.place(relx=0.5, y=50, anchor="n")
    
    def updatePrice(self, oldName):
        # New Input Window
        inputWindow = Toplevel(self.root)
        inputWindow.geometry("200x100+500+300")
        
        # Label
        inputLabel = Label(inputWindow, text="Enter the new price:", font="Montserrat 10")
        inputLabel.place(relx=0.5, y=5, anchor="n")

        # New Entry
        inputEntry = Entry(inputWindow, bd=1, relief=GROOVE)
        inputEntry.place(relx=0.5, y=25, anchor="n")
        def getEntryInput(oldName):
            newPrice = inputEntry.get()
            mycon = sql.connect(host=self.db.host, port=self.db.port, user=self.db.username, password=self.db.password, database='goplant')
            cur = mycon.cursor()
            cur.execute('UPDATE goplant.Tanaman SET harga = %s WHERE nama_tanaman = %s', (newPrice, oldName,))
            mycon.commit()
            stockManagementUI(self.root, self.db)
            inputWindow.destroy()
            inputWindow.update()

        # Button
        addStockButton = Button(inputWindow, text="Update Price", font="Montserrat 10 bold", activebackground="#FFFFFF", fg = "#FFFFFF", bg = "#216869", command=lambda:getEntryInput(oldName))
        addStockButton.place(relx=0.5, y=50, anchor="n")

    def addNewStock(self):
        mycon = sql.connect(host=self.db.host, port=self.db.port, user=self.db.username, password=self.db.password, database='goplant')
        cur = mycon.cursor()
        # New Window
        inputWindow = Toplevel(self.root)
        inputWindow.geometry("400x325+500+300")

        # Label
        infoLabel = Label(inputWindow, text="Enter new plant data", font="Montserrat 10")
        infoLabel.place(relx=0.5, y=5, anchor="n")

        # Plant name
        nameLabel = Label(inputWindow, text="Name: ", font="Montserrat 10")
        nameLabel.place(relx=0.3, y=35, anchor="n")

        # Name entry
        nameEntry = Entry(inputWindow, bd=1, relief=GROOVE)
        nameEntry.place(relx=0.7, y=35, anchor="n")

        # Plant stock count
        stockLabel = Label(inputWindow, text="Stock: ", font="Montserrat 10")
        stockLabel.place(relx=0.3, y=65, anchor="n")

        # Stock entry
        stockEntry = Entry(inputWindow, bd=1, relief=GROOVE)
        stockEntry.place(relx=0.7, y=65, anchor="n")

        # Plant price
        priceLabel = Label(inputWindow, text="Price: ", font="Montserrat 10")
        priceLabel.place(relx=0.3, y=95, anchor="n")

        # Price entry
        priceEntry = Entry(inputWindow, bd=1, relief=GROOVE)
        priceEntry.place(relx=0.7, y=95, anchor="n")

        # Optional label
        optionalLabel = Label(inputWindow, text="Optional", font="Montserrat 10")
        optionalLabel.place(relx=0.5, y=125, anchor="n")

        # Plant description
        descLabel = Label(inputWindow, text="Description: ", font="Montserrat 10")
        descLabel.place(relx=0.3, y=155, anchor="n")

        # Description entry
        descEntry = Text(inputWindow, bd=1, relief=GROOVE, height=3, width=15)
        descEntry.place(relx=0.7, y=155, anchor="n")

        # Plant image
        imageLabel = Label(inputWindow, text="Image file (with extension): ", font="Montserrat 10")
        imageLabel.place(relx=0.3, y=220, anchor="n")

        # Price entry
        imageEntry = Entry(inputWindow, bd=1, relief=GROOVE)
        imageEntry.place(relx=0.7, y=220, anchor="n")
        # Show Message

        def showMessage(message):
            messagebox.showinfo("Alert!", message)
        
        def getEntryInput(cur, mycon):
            name = nameEntry.get()
            desc = descEntry.get("1.0", 'end-1c')
            stock = stockEntry.get()
            price = priceEntry.get()
            image = imageEntry.get()
            if (name == ""):
                showMessage("Enter name!")
            if (stock == ""):
                showMessage("Enter stock count!")
            if (price == ""):
                showMessage("Enter price!")

            formatImage = "./img/" + image
                
            cur.execute('INSERT IGNORE INTO goplant.Tanaman (nama_tanaman, deskripsi_tanaman, stok, harga, img_path) VALUES (%s, %s, %s, %s, %s)', (name, desc, stock, price, formatImage))
            mycon.commit()
            stockManagementUI(self.root, self.db)
            inputWindow.destroy()
            inputWindow.update()

        # Button
        addStockButton = Button(inputWindow, text="Add New Stock", font="Montserrat 10 bold", activebackground="#FFFFFF", fg = "#FFFFFF", bg = "#216869", command=lambda:getEntryInput(cur, mycon))
        addStockButton.place(relx=0.5, y=250, anchor="n")

    def moveLeft(self, datas):
        if (self.currentIdx > 4):
            self.displayItemFrames(self.stockManagementFrame, datas, self.currentIdx - 4)
            self.currentIdx = self.currentIdx - 4
        else:
            self.currentIdx = 0
            self.displayItemFrames(self.stockManagementFrame, datas, self.currentIdx)

    def moveRight(self, datas):
        if (self.currentIdx + 4 < len(datas)):
            self.displayItemFrames(self.stockManagementFrame, datas, self.currentIdx + 4)
            self.currentIdx = self.currentIdx + 4
        else:
            self.displayItemFrames(self.stockManagementFrame, datas, self.currentIdx)