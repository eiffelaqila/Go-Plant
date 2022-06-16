from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import mysql.connector as sql

class produkUI():
    def __init__(self, root, frame, db, namaTanaman, curUser):
        from modules.homePageUI import homePage
        from modules.currentlyRentedPageUI import currentlyRentedPageUI
        frame.destroy()
        self.root = root
        self.db = db
        self.namaTanaman = namaTanaman
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
        headerLogo = Button(headerFrame, image = logo, bg = "#FFFFFF", relief="flat", command = lambda : homePage(self.root, home, self.db, self.curUser))
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
        user_info = Button(headerFrame, image=userInfoLogo, bg="#FFFFFF", borderwidth= 0, command = lambda : currentlyRentedPageUI(self.root, self.curUser, self.db, home))
        user_info.place(x = 1060, y = 31)
        
        # pull databases
        mycon = sql.connect(host=self.db.host, port=self.db.port, user=self.db.username, password=self.db.password, database='goplant')
        cur = mycon.cursor()
        cur.execute('SELECT deskripsi_tanaman, harga, img_path, id_tanaman FROM Tanaman WHERE nama_tanaman = %s', (self.namaTanaman,))
        datas = cur.fetchall()
        
        # *** Description Frame *** #
        DescriptionFrame = Frame(home, bg = "#FFFFFF")
        DescriptionFrame.place(x = 40, y = 160, height=520, width=1200)
        
        # Foto Tanaman
        foto = Frame(DescriptionFrame, bg = "#216669")
        foto.place(x = 84, y = 49, height= 439, width= 465)
        
        headerGambar = Label(foto, text= "Gambar Tanaman",font = ('Comic Sans Ms', 16, 'bold'), fg="#FFFFFF", bg="#216669")
        headerGambar.place(relx = 0.5, y = 25, anchor= 'n')
        
        global fotoTanaman
        fotoTanaman = ImageTk.PhotoImage(Image.open(str(datas[0][2])).resize((411,313)))
        TanamanImage = Label(foto, image=fotoTanaman, bg = "#216669")
        TanamanImage.place(relx = 0.5, y = 84, anchor= 'n')
        
        #teks deskripsi
        deskripsi = Frame(DescriptionFrame, bg = "#216669")
        deskripsi.place(x = 676, y = 49, height= 300, width= 413)
        
        headerDeskripsi = Label(deskripsi, text= "Deskripsi Tanaman",font = ('Comic Sans Ms', 16, 'bold'), fg="#FFFFFF", bg="#216669")
        headerDeskripsi.place(relx = 0.5, y = 20, anchor='n')
        
        teks = Label(deskripsi, text= datas[0][0],font = ('Comic Sans Ms', 12), fg="#FFFFFF", bg="#216669", wraplength=400)
        teks.place(relx = 0.5, y = 60, anchor='n')
        
        #Harga
        harga = Frame(DescriptionFrame, bg = "#216669")
        harga.place(x = 753, y = 352, height=70, width=260)
        
        headerHarga = Label(harga, text= "Harga",font = ('Comic Sans Ms', 16, 'bold'), fg="#FFFFFF", bg="#216669")
        headerHarga.place(relx=0.5, y = 5, anchor= 'n')
        
        jumlahHarga = Label(harga, text="Rp." + str(datas[0][1]), font = ('Comic Sans Ms', 12), fg="#FFFFFF", bg="#216669")
        jumlahHarga.place(relx=0.5, y = 34, anchor='n')
        
        #AddToCartButtton
        global addToCartButton
        addToCartButton = ImageTk.PhotoImage(Image.open('./img/AddToCartButton.png').resize((213,39)))
        addToCart = Button(DescriptionFrame, image= addToCartButton, bg = "#FFFFFF", borderwidth= 0, command=lambda: self.addToCart(home, datas[0][3]))
        addToCart.place(x = 773, y = 450)

    def ErrorFind(self):
        messagebox.showinfo("Go To Premium !!!","Untuk menggunakan fitur ini, segara tingkatkan akun anda ke premium")

    def addToCart(self, home, id_tanaman):
        mycon = sql.connect(host=self.db.host, port=self.db.port, user=self.db.username, password=self.db.password, database='goplant')
        cur = mycon.cursor()
        # New Window
        inputWindow = Toplevel(self.root)
        inputWindow.geometry("400x325+500+300")

        # Label
        infoLabel = Label(inputWindow, text="Enter your order :", font="Montserrat 10")
        infoLabel.place(relx=0.5, y=5, anchor="n")

        # Jumlah sewa
        jumlahLabel = Label(inputWindow, text="Jumlah: ", font="Montserrat 10")
        jumlahLabel.place(relx=0.3, y=35, anchor="n")

        # entry jumlah
        jumlahEntry = Entry(inputWindow, bd=1, relief=GROOVE)
        jumlahEntry.place(relx=0.7, y=35, anchor="n")

        # tgl awal label
        tglAwalLabel = Label(inputWindow, text="Tanggal Awal: ", font="Montserrat 10")
        tglAwalLabel.place(relx=0.3, y=65, anchor="n")

        # tgl awal entry
        tglAwalEntry = Entry(inputWindow, bd=1, relief=GROOVE)
        tglAwalEntry.place(relx=0.7, y=65, anchor="n")

        # tgl Akhir label
        tglAkhirLabel = Label(inputWindow, text="Tanggal Akhir: ", font="Montserrat 10")
        tglAkhirLabel.place(relx=0.3, y=95, anchor="n")

        # tgl Akhir entry
        tglAkhirEntry = Entry(inputWindow, bd=1, relief=GROOVE)
        tglAkhirEntry.place(relx=0.7, y=95, anchor="n")

        
        # Show Message

        def showMessage(message):
            messagebox.showinfo("Alert!", message)
        
        def getEntryInput(cur, mycon, home, id_tanaman):
            jumlah = jumlahEntry.get()
            tglAwal = tglAwalEntry.get()
            tglAkhir = tglAkhirEntry.get()
            if (jumlah == ""):
                showMessage("Enter jumlah!")
            if (tglAwal == ""):
                showMessage("Enter tanggal awal!")
            if (tglAkhir == ""):
                showMessage("Enter tanggal akhir!")
                
            cur.execute('INSERT INTO goplant.orderlist (id_pelanggan, id_tanaman, jumlah_sewa, tanggal_awal, tanggal_akhir, status) VALUES (%s, %s, %s, %s, %s, %s)', (self.curUser.id_pelanggan, id_tanaman, jumlah, tglAwal, tglAkhir, 0))
            mycon.commit()
            showMessage("Added to cart!")
            produkUI(self.root, home, self.db, self.namaTanaman, self.curUser)
            inputWindow.destroy()
            inputWindow.update()

        addtoCartButton = Button(inputWindow, text="Add To Cart", font="Montserrat 10 bold", activebackground="#FFFFFF", fg = "#FFFFFF", bg = "#216869", command=lambda:getEntryInput(cur, mycon, home, id_tanaman))
        addtoCartButton.place(relx=0.5, y=150, anchor="n")