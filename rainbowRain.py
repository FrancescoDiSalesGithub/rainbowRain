import sys
import sqlite3
import yaml
import databaseobj
import json


if __name__ == "__main__":
    
        con = sqlite3.connect("rainbowtables.db")

        if(sys.argv[1] == "md5"):
            for row in con.execute("SELECT * from md5 where hash = ?",(sys.argv[2],)):
                print(row)

        if(sys.argv[1] == "sha512"):
            for row in con.execute("SELECT * from sha512 where hash = ?",(sys.argv[2],)):
                print(row)

        con.close()
   
    



