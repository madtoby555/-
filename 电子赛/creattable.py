import sqlite3
conn = sqlite3.connect('data.db')
cursor  = conn.cursor()
cursor.execute("CREATE TABLE"+' USER '+
                '''(
                    NAME             TEXT  NOT NULL , 
                    HEALTH           INT  NOT NULL,
                    TIME            text  NOT NUll,
                    TEMP             REAL NOT NULL ,
                    ID INT PRIMARY KEY NOT NULL
                );''')
conn.commit()
conn.close()