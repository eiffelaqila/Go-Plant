# Import Modules
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from modules.homePageUI import *
from modules.stockManagementUI import *
import mysql.connector as sql
from databases.database import *
from modules.user import *

class validationController():
    # Attributes
    # root: Tk
    # db: db_init

    def __init__(self, root, db):
        self.root = root
        self.db = db
        self.currentUser = None

    def verifyLoginAdmin(self, frame, username, password):
        # Verify Login Admin
        mycon = sql.connect(host=self.db.host, port=self.db.port, user=self.db.username, password=self.db.password, database='goplant')
        cur = mycon.cursor()
        cur.execute('SELECT username, password FROM Admin')
        datas = cur.fetchall()
        mycon.close()

        countUsernameOccurrences = 0
        if username and password:
            for data in datas:
                if username == data[0]:
                    countUsernameOccurrences += 1
                    if password == data[1]:
                        stockManagementUI(self.root, self.db, frame)
                    else:
                        if (countUsernameOccurrences == 1):
                            self.sendMessage("Wrong password!")
            if countUsernameOccurrences == 0:
                self.sendMessage("Username is not registered. Please register!")

    def verifyLoginCustomer(self, frame, username, password):
        # Verify Login Customer
        mycon = sql.connect(host=self.db.host, port=self.db.port, user=self.db.username, password=self.db.password, database='goplant')
        cur = mycon.cursor()
        cur.execute('SELECT username, password, id_pelanggan FROM Pelanggan')
        datas = cur.fetchall()
        mycon.close()

        countUsernameOccurrences = 0
        if username and password:
            for data in datas:
                if username == data[0]:
                    countUsernameOccurrences += 1
                    if password == data[1]:
                        self.currentUser = user(data[2])
                        homePage(self.root, frame, self.db, self.currentUser)
                    else:
                        if (countUsernameOccurrences == 1):
                            self.sendMessage("Wrong password!")
            if countUsernameOccurrences == 0:
                self.sendMessage("Username is not registered. Please register!")
    
    def validate(self, frame, username, password, alamat):
        # Validate Register
        mycon = sql.connect(host=self.db.host, port=self.db.port, user=self.db.username, password=self.db.password, database='goplant')
        cur = mycon.cursor()
        cur.execute('SELECT username, password FROM Pelanggan')
        datas = cur.fetchall()

        countUsernameOccurrences = 0
        if username and password:
            for data in datas:
                if username == data[0]:
                    countUsernameOccurrences += 1
                    if (countUsernameOccurrences == 1):
                        self.sendMessage("Username is registered!")
            if countUsernameOccurrences == 0:
                # Insert customers
                cur.execute('INSERT INTO goplant.Pelanggan (username, password, alamat) VALUES (%s, %s, %s)', (username, password, alamat))
                mycon.commit()
                self.sendMessage("Account registered successfully!")

                # Back to login UI
                from modules.loginUI import loginUI
                frame.destroy()
                loginUI(self.root, frame, self.db)
        
        mycon.close()

    def sendMessage(self, message):
        # 
        messagebox.showinfo("Alert!", message)