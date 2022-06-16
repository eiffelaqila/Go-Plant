import mysql.connector as sql
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from modules.ProdukUI import produkUI
from modules.currentlyRentedPageUI import currentlyRentedPageUI


class homePage():
    def __init__(self, root, frame, db, curUser):
        from modules.loginUI import loginUI
        frame.destroy()
        self.root = root
        self.db = db
        self.curUser = curUser
        
        # *** HOME FRAME ***
        home = Frame(self.root, bg = "#DCE1DD")
        home.place(x = 0, y = 0, height= 720, width= 1280)
        
        # *** HEADER FRAME ***
        # Header
        headerFrame = Frame(self.root, bg = "#FFFFFF")
        headerFrame.place(x = 0, y = 0, width = 1280, height = 110)

        # Logo
        global logo
        logo = ImageTk.PhotoImage(Image.open('./img/GoPlant.png').resize((186,60)))
        headerLogo = Button(headerFrame, image = logo, bg = "#FFFFFF", relief="flat", command=lambda: loginUI(self.root, home, self.db))
        headerLogo.place(x = 80, y = 20, anchor = "nw")

       
        # Button search
        global searchLogo
        searchLogo = ImageTk.PhotoImage(Image.open('./img/searchButton.png').resize((185,55)))
        search = Button(headerFrame, image=searchLogo, bg="#FFFFFF", borderwidth= 0, command = lambda : self.ErrorFind())
        search.place(x = 665, y = 31)

        # Button Cart
        global cartLogo
        cartLogo = ImageTk.PhotoImage(Image.open('./img/cartButton.png').resize((185,55)))
        Cart = Button(headerFrame, image=cartLogo, bg="#FFFFFF", borderwidth= 0, command = lambda : self.ErrorFind())
        Cart.place(x = 863, y = 31)
    
        # User Info
        global userInfoLogo
        userInfoLogo = ImageTk.PhotoImage(Image.open('./img/userButton.png').resize((185,55)))
        user_info = Button(headerFrame, image=userInfoLogo, bg="#FFFFFF", borderwidth= 0, command = lambda : currentlyRentedPageUI(self.root, self.curUser, self.db, frame))
        user_info.place(x = 1060, y = 31)
        
        # *** DAFTAR TANAMAN FRAME ***
        self.daftartanaman = Frame(home, bg = "#FFFFFF")
        self.daftartanaman.place(x = 40, y = 160, height= 520, width=1200)

        # Pull database
        mycon = sql.connect(host=self.db.host, port=self.db.port, user=self.db.username, password=self.db.password, database='goplant')
        cur = mycon.cursor()
        cur.execute('SELECT nama_tanaman, stok, harga, img_path FROM Tanaman')
        datas = cur.fetchall()

        # DISPLAY ITEM FRAME
        self.curIdx = 0
        self.displayItemFrames(self.daftartanaman, datas, self.db, self.curIdx)

        
    def displayItemFrames(self, frame, datas, db, curIdx):  
        # Box 1  
        if(curIdx <= len(datas) - 1):
            global img1
            img1 = ImageTk.PhotoImage(Image.open(str(datas[curIdx + 0][3])).resize((200, 200)))

            # Item Frame
            itemFrame1 = Frame(frame, bg = "#216869")
            itemFrame1.place(x = 140, y = 80, width = 200, height = 360, anchor = "nw")
            
            # Name Label
            nameLabel1 = Label(itemFrame1, text = datas[curIdx + 0][0], font="Montserrat 12 bold", bg="#216869", fg="#FFFFFF")
            nameLabel1.place(relx=0.5, y=5, anchor = "n")

            # Image Tanaman
            logoPlant1 = Button(itemFrame1, image=img1, command=lambda:produkUI(self.root, frame, db, datas[curIdx+0][0], self.curUser))
            logoPlant1.place(relx = 0.5, y = 40, anchor="n")
            
            # Price Label
            priceLabel1 = Label(itemFrame1, text="Harga: " + str(datas[curIdx + 0][2]), font="Montserrat 12 bold", bg="#216869", fg="#FFFFFF")
            priceLabel1.place(x=20, y=266, anchor = "nw")

            # Stock Label
            stockLabel1 = Label(itemFrame1, text="Stock: " + str(datas[curIdx + 0][1]), font="Montserrat 12 bold", bg="#216869", fg="#FFFFFF")
            stockLabel1.place(x=20, y=302, anchor = "nw")

        # Box 2
        if (curIdx <= len(datas) - 2):
            global img2
            img2 = ImageTk.PhotoImage(Image.open(str(datas[curIdx + 1][3])).resize((200, 200)))

            # Item Frame
            itemFrame2 = Frame(frame, bg = "#216869")
            itemFrame2.place(x = 380, y = 80, width = 200, height = 360, anchor = "nw")
            
            # Name Label
            nameLabel2 = Label(itemFrame2, text = datas[curIdx + 1][0], font="Montserrat 12 bold", bg="#216869", fg="#FFFFFF")
            nameLabel2.place(relx=0.5, y=5, anchor = "n")

            # Image Tanaman
            logoPlant2 = Button(itemFrame2, image=img2, command=lambda:produkUI(self.root, frame, db, datas[curIdx+1][0], self.curUser))
            logoPlant2.place(relx = 0.5, y = 40, anchor="n")
            
            # Price Label
            priceLabel2 = Label(itemFrame2, text="Harga: " + str(datas[curIdx + 1][2]), font="Montserrat 12 bold", bg="#216869", fg="#FFFFFF")
            priceLabel2.place(x=20, y=266, anchor = "nw")

            # Stock Label
            stockLabel2 = Label(itemFrame2, text="Stock: " + str(datas[curIdx + 1][1]), font="Montserrat 12 bold", bg="#216869", fg="#FFFFFF")
            stockLabel2.place(x=20, y=302, anchor = "nw")

        # Box 3
        if (curIdx <= len(datas) - 3):
            global img3
            img3 = ImageTk.PhotoImage(Image.open(str(datas[curIdx + 2][3])).resize((200, 200)))
            
            # Item Frame
            itemFrame3 = Frame(frame, bg = "#216869")
            itemFrame3.place(x = 620, y = 80, width = 200, height = 360, anchor = "nw")
            
            # Name Label
            nameLabel3 = Label(itemFrame3, text = datas[curIdx + 2][0], font="Montserrat 12 bold", bg="#216869", fg="#FFFFFF")
            nameLabel3.place(relx=0.5, y=5, anchor = "n")

            # Image Tanaman
            logoPlant3 = Button(itemFrame3, image=img3, command=lambda:produkUI(self.root, frame, db, datas[curIdx+2][0], self.curUser))
            logoPlant3.place(relx = 0.5, y = 40, anchor="n")
            
            # Price Label
            priceLabel3 = Label(itemFrame3, text="Harga: " + str(datas[curIdx + 2][2]), font="Montserrat 12 bold", bg="#216869", fg="#FFFFFF")
            priceLabel3.place(x=20, y=266, anchor = "nw")

            # Stock Label
            stockLabel3 = Label(itemFrame3, text="Stock: " + str(datas[curIdx + 2][1]), font="Montserrat 12 bold", bg="#216869", fg="#FFFFFF")
            stockLabel3.place(x=20, y=302, anchor = "nw")

        # Box 4
        if (curIdx <= len(datas) - 4):
            global img4
            img4 = ImageTk.PhotoImage(Image.open(str(datas[curIdx + 3][3])).resize((200, 200)))

            # Item Frame
            itemFrame4 = Frame(frame, bg = "#216869")
            itemFrame4.place(x = 860, y = 80, width = 200, height = 360, anchor = "nw")
            
            # Name Label
            nameLabel4 = Label(itemFrame4, text = datas[curIdx + 3][0], font="Montserrat 12 bold", bg="#216869", fg="#FFFFFF")
            nameLabel4.place(relx=0.5, y=5, anchor = "n")

            # Image Tanaman
            logoPlant4 = Button(itemFrame4, image=img4, command=lambda:produkUI(self.root, frame, db, datas[curIdx+3][0], self.curUser))
            logoPlant4.place(relx = 0.5, y = 40, anchor="n")
            
            # Price Label
            priceLabel4 = Label(itemFrame4, text="Harga: " + str(datas[curIdx + 3][2]), font="Montserrat 12 bold", bg="#216869", fg="#FFFFFF")
            priceLabel4.place(x=20, y=266, anchor = "nw")

            # Stock Label
            stockLabel4 = Label(itemFrame4, text="Stock: " + str(datas[curIdx + 3][1]), font="Montserrat 12 bold", bg="#216869", fg="#FFFFFF")
            stockLabel4.place(x=20, y=302, anchor = "nw")
        
        # Left Button
        leftButton = Button(frame, text="<", font = "Montserrat 18 bold", activebackground="#FFFFFF", fg = "#FFFFFF", bg = "#216869", command=lambda:self.moveLeft(datas, db))
        leftButton.place(x=80, rely=0.5, anchor="center")

        # Right Button
        rightButton = Button(frame, text=">", font = "Montserrat 18 bold", activebackground="#FFFFFF", fg = "#FFFFFF", bg = "#216869", command=lambda:self.moveRight(datas, db))
        rightButton.place(x=1120, rely=0.5, anchor="center")

    def moveLeft(self, datas, db):
        if (self.curIdx > 4):
            self.displayItemFrames(self.daftartanaman, datas, db, self.curIdx - 4)
            self.curIdx = self.curIdx - 4
        else:
            self.curIdx = 0
            self.displayItemFrames(self.daftartanaman, datas, db, self.curIdx)

    def moveRight(self, datas, db):
        if (self.curIdx + 4 < len(datas)):
            self.displayItemFrames(self.daftartanaman, datas, db, self.curIdx + 4)
            self.curIdx = self.curIdx + 4
        else:
            self.displayItemFrames(self.daftartanaman, datas, db, self.curIdx)

    def ErrorFind(self):
        messagebox.showinfo("Go To Premium !!!","Untuk menggunakan fitur ini, segara tingkatkan akun anda ke premium")
    
    # def GoToProdukUI(self, frame, idTanaman):
    #     frame.destroy()
    #     produkUIFrame = Frame(self.root, bg = )