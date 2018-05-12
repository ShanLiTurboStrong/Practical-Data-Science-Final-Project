import csv, sqlite3

con = sqlite3.connect("irs.db")
cur = con.cursor()
cur.execute("CREATE TABLE irs (STATE,zipcode,agi_stub,N02650,A02650,N00200,A00200,N00900,A00900,N02300,A02300,N01700,A01700,N01000,A01000);")  # use your column names here

with open('../15zpallagi.txt') as f: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(f) # comma is default delimiter
    to_db = [(i['STATE'], i['zipcode'], i['agi_stub'],
              i['N02650'], i['A02650'], i['N00200'], i['A00200'],
              i['N00900'], i['A00900'], i['N02300'], i['A02300'],
              i['N01700'], i['A01700'], i['N01000'], i['A01000']) for i in dr]

cur.executemany("INSERT INTO irs (STATE,zipcode,agi_stub,N02650,A02650,N00200,A00200,N00900,A00900,N02300,A02300,N01700,A01700,N01000,A01000) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", to_db)
con.commit()
con.close()

