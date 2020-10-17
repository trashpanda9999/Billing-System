from tkinter import*
import tkinter.messagebox
import cstDatabase_BackEnd
#Frontend


class customer:
    
    def __init__(self, root):
        self.root = root
        self.root.title("eZ Billing System")
        self.root.geometry("1350x750+0+0")
        self.root.config(bg="cadet blue")
        self.frame = Frame(self.root,bg='cadet blue')
        self.frame.pack()
        
        CID = StringVar()
        Product = StringVar()
        Qty = StringVar()
        Price = StringVar()
        Dsc = StringVar()
        Gst = StringVar()
        Amt = StringVar()
        
        
        #=================================================================Function=====================================================
        
        def iExit():
            iExit = tkinter.messagebox.askyesno("eZ Billing System","Confirm Exit?")
            if iExit > 0:
                root.destroy()
                return
        
        def clearData():
            self.txtCID.delete(0,END)
            self.txtProduct.delete(0,END)
            self.txtQty.delete(0,END)
            self.txtPrice.delete(0,END)
            self.txtDsc.delete(0,END)
            self.txtGst.delete(0,END)
            self.txtAmt.delete(0,END)
        
        def addData():
            if(len(CID.get())!=0):
                cstDatabase_BackEnd.addCstRec(CID.get() ,Product.get() ,Qty.get(), Price.get(), Dsc.get(), Gst.get(),Amt.get())
                customerlist.delete(0,END)
                customerlist.insert(END,(CID.get() ,Product.get() ,Qty.get(), Price.get(), Dsc.get(), Gst.get(),\
                                    Amt.get()))
        
        def CustomerRec(event):
            global sd
            searchCST = customerlist.curselection()[0]
            sd = customerlist.get(searchCST)
            
            self.txtCID.delete(0,END)
            self.txtCID.insert(END,sd[1])
            self.txtProduct.delete(0,END)
            self.txtProduct.insert(END,sd[2])
            self.txtQty.delete(0,END)
            self.txtQty.insert(END,sd[3])
            self.txtPrice.delete(0,END)
            self.txtPrice.insert(END,sd[4])
            self.txtDsc.delete(0,END)
            self.txtDsc.insert(END,sd[5])
            self.txtGst.delete(0,END)
            self.txtGst.insert(END,sd[6])
            self.txtAmt.delete(0,END)
            self.txtAmt.insert(END,sd[7])
            
        def DisplayData():
            customerlist.delete(0,END)
            for row in cstDatabase_BackEnd.viewData():
             customerlist.insert(END,row,str(""))
            
        def DeleteData():
            if(len(CID.get())!=0):
                cstDatabase_BackEnd.deleteRec(sd[0])
                clearData()
                DisplayData()
        def update():
            if(len(CID.get())!=0):
                cstDatabase_BackEnd.deleteRec(sd[0])
            if(len(CID.get())!=0):
                cstDatabase_BackEnd.addCstRec(CID.get() ,Product.get() ,Qty.get(), Price.get(), Dsc.get(), Gst.get(),Amt.get())
                customerlist.delete(0,END)
                customerlist.insert(END,(CID.get() ,Product.get() ,Qty.get(), Price.get(), Dsc.get(), Gst.get(),\
                                    Amt.get()))
            
            
            
            
        #===================================================================Frame=======================================================
        MainFrame = Frame(self.frame, bg="cadet blue")
        MainFrame.grid()
        
        TitFrame = Frame(MainFrame, bd=2 ,padx=450, pady=8,bg="Ghost White",relief = RIDGE)
        TitFrame.pack(side=TOP)
        
        self.lblTit = Label(TitFrame , font=('arial',47,'bold'),text="eZ Billing System",bg="Ghost White")
        self.lblTit.grid()
        
        ButtonFrame = Frame(MainFrame, bd=2 ,width=1350,height=70,padx=18,pady=10,bg="Ghost White",relief = RIDGE)
        ButtonFrame.pack(side=BOTTOM)
        
        DataFrame = Frame(MainFrame, bd=1 ,width=1300,height=400,padx=20,pady=20,bg="cadet blue",relief = RIDGE)
        DataFrame.pack(side=BOTTOM)
        
        DataFrameLEFT = LabelFrame(DataFrame, bd=1 ,width=1000,height=600,padx=20,bg="Ghost White",relief = RIDGE,
                               font=('arial',20,'bold'),text="Bill Details")
        DataFrameLEFT.pack(side=LEFT)
        
        DataFrameRIGHT = LabelFrame(DataFrame, bd=1 ,width=450,height=300,padx=31,pady=3,bg="Ghost White",relief = RIDGE,
                               font=('arial',20,'bold'),text="Details")
        DataFrameRIGHT.pack(side=RIGHT)

        #==========================================Label and Entry Widget=======================
        self.lblCID = Label(DataFrameLEFT , font=('arial',20,'bold'),text="Customer ID:",padx=2,pady=2,bg="Ghost White")
        self.lblCID.grid(row=0,column=0,sticky=W)
        self.txtCID = Entry(DataFrameLEFT , font=('arial',20,'bold'),textvariable=CID,width=39)
        self.txtCID.grid(row=0,column=1)
        
        self.lblProduct = Label(DataFrameLEFT , font=('arial',20,'bold'),text="Product:",padx=2,pady=2,bg="Ghost White")
        self.lblProduct.grid(row=1,column=0,sticky=W)
        self.txtProduct = Entry(DataFrameLEFT , font=('arial',20,'bold'),textvariable=Product,width=39)
        self.txtProduct.grid(row=1,column=1)
        
        self.lblQty = Label(DataFrameLEFT , font=('arial',20,'bold'),text="Quantity:",padx=2,pady=2,bg="Ghost White")
        self.lblQty.grid(row=2,column=0,sticky=W)
        self.txtQty = Entry(DataFrameLEFT , font=('arial',20,'bold'),textvariable=Qty,width=39)
        self.txtQty.grid(row=2,column=1)
        
        self.lblPrice = Label(DataFrameLEFT , font=('arial',20,'bold'),text="Price:",padx=2,pady=2,bg="Ghost White")
        self.lblPrice.grid(row=3,column=0,sticky=W)
        self.txtPrice = Entry(DataFrameLEFT , font=('arial',20,'bold'),textvariable=Price,width=39)
        self.txtPrice.grid(row=3,column=1)
        
        self.lblDsc = Label(DataFrameLEFT , font=('arial',20,'bold'),text="Discount:",padx=2,pady=2,bg="Ghost White")
        self.lblDsc.grid(row=4,column=0,sticky=W)
        self.txtDsc = Entry(DataFrameLEFT , font=('arial',20,'bold'),textvariable=Dsc,width=39)
        self.txtDsc.grid(row=4,column=1)
        
        self.lblGst = Label(DataFrameLEFT , font=('arial',20,'bold'),text="GST:",padx=2,pady=2,bg="Ghost White")
        self.lblGst.grid(row=5,column=0,sticky=W)
        self.txtGst = Entry(DataFrameLEFT , font=('arial',20,'bold'),textvariable=Gst,width=39)
        self.txtGst.grid(row=5,column=1)
        
        self.lblAmt = Label(DataFrameLEFT , font=('arial',20,'bold'),text="Grand Total:",padx=2,pady=2,bg="Ghost White")
        self.lblAmt.grid(row=6,column=0,sticky=W)
        self.txtAmt = Entry(DataFrameLEFT , font=('arial',20,'bold'),textvariable=Amt,width=39)
        self.txtAmt.grid(row=6,column=1)
        
        #========================================================ListBox and ScrollBar Widget===================================================
        
        scrollbar = Scrollbar(DataFrameRIGHT)
        scrollbar.grid(row=0,column=1,sticky='ns')
        
        customerlist = Listbox(DataFrameRIGHT,width=41,height=16,font=('arial',12,'bold'), yscrollcommand=scrollbar.set)
        customerlist.bind('<<ListboxSelect>>',CustomerRec)
        customerlist.grid(row=0,column=0,padx=8)
        scrollbar.config(command = customerlist.yview)
        
        
        #================================================================Button Widget==========================================================

        self.btnAddData = Button(ButtonFrame,text="Add New",font=('arial',20,'bold'),width=10,height=1,bd=4,command=addData)
        self.btnAddData.grid(row=0,column=0)
        
        self.btnDisplayData = Button(ButtonFrame,text="Display",font=('arial',20,'bold'),width=10,height=1,bd=4,command=DisplayData)
        self.btnDisplayData.grid(row=0,column=1) 
        
        self.btnClearData = Button(ButtonFrame,text="Clear",font=('arial',20,'bold'),width=10,height=1,bd=4,command=clearData)
        self.btnClearData.grid(row=0,column=2) 
        
        self.btnDeleteData = Button(ButtonFrame,text="Delete",font=('arial',20,'bold'),width=10,height=1,bd=4,command=DeleteData)
        self.btnDeleteData.grid(row=0,column=3) 
        
#        self.btnSearchData = Button(ButtonFrame,text="Search",font=('arial',20,'bold'),width=10,height=1,bd=4)
#        self.btnSearchData.grid(row=0,column=4) 
        
        self.btnUpdateData = Button(ButtonFrame,text="Update",font=('arial',20,'bold'),width=10,height=1,bd=4,command=update)
        self.btnUpdateData.grid(row=0,column=4) 
        
        self.btnExitData = Button(ButtonFrame,text="Exit",font=('arial',20,'bold'),width=10,height=1,bd=4,command=iExit)
        self.btnExitData.grid(row=0,column=5) 

        


if __name__=='__main__':
    root = Tk()
    application = customer(root)
    root.mainloop()