import sqlite3
#backend
def customerData():
    con=sqlite3.connect("customer.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS customer(id INTEGER PRIMARY KEY, CID text, \
                                                     Product text,Qty text,Price text,Dsc text,Gst text,Amt text)")
    con.commit()
    con.close()
    
def addCstRec(CID ,Product ,Qty, Price, Dsc, Gst, Amt):
    con=sqlite3.connect("customer.db")
    cur = con.cursor()
    cur.execute("INSERT INTO customer VALUES (NULL,?,?,?,?,?,?,?)",(CID ,Product ,Qty, Price, Dsc, Gst, Amt))
    con.commit()
    con.close()
    
def viewData():
    con=sqlite3.connect("customer.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM customer")
    row = cur.fetchall()
    con.close()
    return row

def deleteRec(id):
    con=sqlite3.connect("customer.db")
    cur = con.cursor()
    cur.execute("DELETE FROM customer WHERE id=?",(id,))
    con.commit()
    con.close()
    
def dataUpdate(id,CID="",Product="" ,Qty="", Price="" ,Dsc="", Gst="", Amt=""):
    con=sqlite3.connect("customer.db")
    cur = con.cursor()
    cur.execute("UPDATE customer SET CD=?,Product=? ,Qty=?, Price=?, Dsc=?, Gst=?, Amt=?, WHERE id=?",\
                (CID ,Product ,Qty, Price, Dsc, Gst, Amt, id))
    con.commit()
    con.close()
    
    
    
customerData()