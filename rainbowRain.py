import sys
import sqlite3

import hashcontroller

if __name__ == "__main__":
    
           
        
            if(sys.argv[1] == "md5"):
                con = sqlite3.connect("rainbowtables.db")
                cursor = con.cursor()
                cursor.execute("SELECT * from md5 where hash = ?",(sys.argv[2],))
                rows = cursor.fetchall()

                for row in rows:
                    print(row)

                con.close()

            if(sys.argv[1] == "sha512"):
                print("argv1:"+sys.argv[1])
                print("argv2:"+sys.argv[2])

                con = sqlite3.connect("rainbowtables.db")
                cursor = con.cursor()
                cursor.execute("SELECT * from sha512 where hash = ?",(sys.argv[2],))
                rows = cursor.fetchall()

                for row in rows:
                    print(row)
                con.close()
                

            if(sys.argv[1] == "sha256"):
                con = sqlite3.connect("rainbowtables.db")
                cursor = con.cursor()
                cursor.execute("SELECT * from sha256 where hash = ?",(sys.argv[2],))
                rows = cursor.fetchall()

                for row in rows:
                    print(row)

                con.close()

            if(sys.argv[1]=="exportmd5"):
                hash_md5_export = hashcontroller.hashcontroller(str(sys.argv[2]))
                hash_md5_export.generate_md5_sql()

            if(sys.argv[1]=="exportsha256"):
                hash_sha_256_export = hashcontroller.hashcontroller(str(sys.argv[2]))
                hash_sha_256_export.generate_sha256_sql()

            if(sys.argv[1]=="exportsha512"):
                hash_sha_512_export = hashcontroller.hashcontroller(str(sys.argv[2]))
                hash_sha_512_export.generate_sha512_sql()    

            if(sys.argv[1]=="importmd5"):
                hash_md5_import = hashcontroller.hashcontroller(str(sys.argv[2]))
                hash_md5_import.import_md5_sql()

            if(sys.argv[1]=="importsha256"):
                hash_sha_256_import = hashcontroller.hashcontroller(str(sys.argv[2]))
                hash_sha_256_import.import_sha256_sql()

            if(sys.argv[1]=="importsha512"):
                hash_sha_512_import = hashcontroller.hashcontroller(str(sys.argv[2]))
                hash_sha_512_import.import_sha512_sql()






