
import hashlib
import sqlite3

class hashcontroller:
    def __init__(self,file) -> None:
        self.file = file
        pass

    def generate_md5_sql(self):
        

                file_md5=open(self.file,"r",encoding='utf-8',errors='ignore')
                file_md5_sql=open("md5toinsert.sql","w",errors='ignore')

                for value in file_md5:
                    md5 = hashlib.md5()
                
                    md5.update(value.encode(encoding='utf-8'))
                    hashdone = md5.hexdigest()
                    file_md5_sql.write("\n")
                    file_md5_sql.write("insert into md5 values ('{}','{}');".format(str(hashdone),str(value).rstrip()))
                
                file_md5_sql.close()
                file_md5.close()
                print("export done! Check md5toinsert.sql")


    def generate_sha512_sql(self):

        file_sha512 = open(self.file,"r",encoding='utf-8',errors='ignore')
        file_sha512_sql = open("sha512toinsert.sql","w",errors='ignore')

        for value in file_sha512:
            sha512 = hashlib.sha512()
            sha512.update(value.encode(encoding='utf-8'))
            sha512done = sha512.hexdigest()

            file_sha512_sql.write("\n")
            file_sha512_sql.write("insert into sha512 values ('{}','{}');\n".format(str(sha512done),str(sha512done).rstrip()))

        file_sha512_sql.close()
        file_sha512.close()
        print("export done! Check sha512toinsert.sql")

        

    def generate_sha256_sql(self):
        file_sha256 = open(self.file,"r",encoding='utf-8',errors='ignore')
        file_sha256_sql = open("sha256toinsert.sql","w",errors='ignore')
        
        for value in file_sha256:
            sha256 = hashlib.sha256()
            sha256.update(value.encode(encoding='utf-8'))
            sha256done = sha256.hexdigest()

            file_sha256_sql.write("\n")
            file_sha256_sql.write("insert into sha256 values ('{}','{}');\n".format(str(sha256done),str(value).rstrip()))

        file_sha256_sql.close()
        file_sha256.close()
        print("export done! Check sha256toinsert.sql")

    def import_md5_sql(self):
        file_md5 = open(self.file,"r",encoding='utf-8',errors='ignore')
        db_connection = sqlite3.connect("rainbowtables.db")

        for value in file_md5:
            value.encode('utf-8',errors='ignore')
            db_connection.execute(value)
            db_connection.commit()
            
        db_connection.close()
        file_md5.close()
        print("import done!")

    def import_sha256_sql(self):
        file_sha256 = open(self.file,"r",encoding='utf-8',errors='ignore')
        db_connection = sqlite3.connect("rainbowtables.db")

        for value in file_sha256:
            value.encode('utf-8',errors='ignore')
            db_connection.execute(value)
            db_connection.commit()
            
        db_connection.close()
        file_sha256.close()
        print("import done!")


    def import_sha512_sql(self):
        file_sha512 = open(self.file,"r",encoding='utf-8',errors='ignore')
        db_connection = sqlite3.connect("rainbowtables.db")

        for value in file_sha512:
            value.encode('utf-8',errors='ignore')
            db_connection.execute(str(value))
            db_connection.commit()
            
        db_connection.close()
        file_sha512.close()
        print("import done!")
