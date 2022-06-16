import mysql.connector as sql
from tkinter import messagebox
from pathlib import Path

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
class database:
        # host: String
        # port: integer
        # username: String
        # password: String
        # database: database
        
        def __init__(self, host, port, username, password):
                try:
                        self.host = host
                        self.port = port
                        self.username = username 
                        self.password = password
                        self.database = 'goplant'

                        # Create database
                        mycon = sql.connect(host=self.host, port=self.port, user=self.username, password=self.password)
                        cursor = mycon.cursor()
                        
                        cursor.execute("CREATE DATABASE IF NOT EXISTS `goplant`")

                        mycon.close()

                        # Setup database
                        mycon = sql.connect(host=self.host, port=self.port, user=self.username, password=self.password, database=self.database)
                        cursor = mycon.cursor()
                        
                        sqlRestored = open(relative_to_assets("GoPlant.sql")).read()
                        cursor.execute(sqlRestored, multi=True)

                        mycon.close()
                        
                except sql.Error as msg:
                        messagebox.showinfo("Gagal menggunakan basis data: ", msg)
                        exit()