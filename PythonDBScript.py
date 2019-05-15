import sqlite3

conn = sqlite3.connect('my_Python.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_PythonDocs( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_document TEXT \
        )")
    conn.commit()
conn.close()


fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')
for file in fileList:
    if file.endswith(".txt"):
        conn = sqlite3.connect('my_Python.db')
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_PythonDocs(col_document) VALUES(?)", (file, ))
        conn.commit()
        conn.close()
        print(file)

    

path = '.\Python_projects'



    
