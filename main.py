import tkinter
from tkinter import ttk
from tkinter import *
import mysql.connector
import random
from datetime import datetime
from tkinter import messagebox


class Store:
    def __init__(self,root):
        self.root=root
        self.root.title("Touch mobile store")
        self.root.geometry("1540x800+0+0")

        self.type=StringVar()
        self.FamilyBrand = StringVar()
        self.Brand=StringVar()
        self.DateOfBuy=StringVar()
        self.DateOfSale=StringVar()
        self.price=StringVar()
        self.isSold=StringVar()
        self.soldPrice=StringVar()
        self.Id=StringVar()


        lbtitle=Label(self.root,bd=20,relief=RIDGE,text="TOUCH Mobile Store",fg="black",font=("times new roman",50,"bold"))
        lbtitle.pack(side=TOP,fill=X)


        Dataframe=Frame(self.root,bd=20,relief=RIDGE)
        Dataframe.place(x=0,y=130,width=1530,height=400)

        DataframeLeft=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,font=("times new roman",12,"bold"),text="objects")
        DataframeLeft.place(x=0,y=5,width=980,height=350)

        DataframeRight = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10, font=("times new roman", 12, "bold"),text="information")
        DataframeRight.place(x=990, y=5, width=460, height=350)

        ButtonFrame = Frame(self.root, bd=20, relief=RIDGE)
        ButtonFrame.place(x=0, y=530, width=1530, height=70)

        Detailsframe = Frame(self.root, bd=20, relief=RIDGE)
        Detailsframe.place(x=0, y=600, width=1530, height=190)

        lblNameTablet=Label(DataframeLeft,text="Types of stuff  *",font=("times new roman", 12, "bold"),padx=2,pady=6)
        lblNameTablet.grid(row=0,column=0)

        comNametablet=ttk.Combobox(DataframeLeft,textvariable=self.type,state="readonly",font=("times new roman",12,"bold"),width=33)
        comNametablet["values"]=("glass","adaptor","cable","back cover","airpod","handsfree","headphone","machine lighter sharger","speaker","watch","neack handsfree")
        comNametablet.grid(row=0,column=1)

        #----------------------DataFrameLeft--------------------------------------


        lblFamilyBrand = Label(DataframeLeft, text="Family Brand", font=("times new roman", 12, "bold"), padx=2,
                              pady=6)
        lblFamilyBrand.grid(row=1, column=0)

        comFamilyBrand = ttk.Combobox(DataframeLeft, textvariable=self.FamilyBrand, state="readonly",
                                     font=("times new roman", 12, "bold"), width=33)
        comFamilyBrand["values"] = ("Apple","Samsung","Xiaomi","Sony")
        comFamilyBrand.grid(row=1, column=1)


        lblbuy = Label(DataframeLeft, font=("arial", 12, "bold"), text="Date of Buy   *", padx=2,pady=4)
        lblbuy.grid(row=2, column=0, sticky=W)
        textbuy = Entry(DataframeLeft, font=("arial", 12, "bold"),textvariable=self.DateOfBuy, width=35)
        textbuy.grid(row=2, column=1)

        lblprice = Label(DataframeLeft, font=("arial", 12, "bold"), text="price    *", padx=2,pady=6)
        lblprice.grid(row=3, column=0, sticky=W)
        textprice = Entry(DataframeLeft, font=("arial", 12, "bold"),textvariable=self.price, width=35)
        textprice.grid(row=3, column=1)

        lblSale = Label(DataframeLeft, font=("arial", 12, "bold"), text="Date of Sale", padx=2,pady=6)
        lblSale.grid(row=4, column=0, sticky=W)
        textSale = Entry(DataframeLeft, font=("arial", 12, "bold"),textvariable=self.DateOfSale, width=35)
        textSale.grid(row=4, column=1)

        lblIsSold = Label(DataframeLeft, font=("arial", 12, "bold"), text="is sold", padx=2,pady=6)
        lblIsSold.grid(row=5, column=0, sticky=W)
        textIsSold = Entry(DataframeLeft, font=("arial", 12, "bold"),textvariable=self.isSold, width=35)
        textIsSold.grid(row=5, column=1)

        lblSoldPrice = Label(DataframeLeft, font=("arial", 12, "bold"), text="sold price", padx=2,pady=6)
        lblSoldPrice.grid(row=5, column=0, sticky=W)
        textSoldPrice = Entry(DataframeLeft, font=("arial", 12, "bold"),textvariable=self.soldPrice, width=35)
        textSoldPrice.grid(row=5, column=1)

        lblBrand = Label(DataframeLeft, font=("arial", 12, "bold"), text="Brand", padx=2,pady=6)
        lblBrand.grid(row=6, column=0, sticky=W)
        textBrand = Entry(DataframeLeft, font=("arial", 12, "bold"), textvariable=self.Brand,width=35)
        textBrand.grid(row=6, column=1)

        lblIsSold = Label(DataframeLeft, font=("arial", 12, "bold"), text="is Sold?   *", padx=2, pady=6)
        lblIsSold.grid(row=7, column=0, sticky=W)
        textIsSold = Entry(DataframeLeft, font=("arial", 12, "bold"), textvariable=self.isSold, width=35)
        textIsSold.grid(row=7, column=1)

        lblId = Label(DataframeLeft, font=("arial", 12, "bold"), text="Id", padx=2, pady=6)
        lblId.grid(row=8, column=0, sticky=W)
        textId = Entry(DataframeLeft, font=("arial", 12, "bold"),textvariable=self.Id, state="readonly", width=35)
        textId.grid(row=8, column=1)


        #---------------------------DataFrameRight----------------------------------------------
        self.txtInformation=Text(DataframeRight,font=("arial", 12, "bold"),width=47,height=16,padx=2,pady=6)
        self.txtInformation.grid(row=0,column=0)

        #----------------------------Buttons----------------------------------------------
        btnRead=Button(ButtonFrame,text="Read",command=self.read,bg='green',fg='white',font=("arial", 12, "bold"),width=20,padx=2,pady=6)
        btnRead.grid(row=0,column=0)

        btnSearch = Button(ButtonFrame, text="Search", command=self.search, bg='green', fg='white',
                           font=("arial", 12, "bold"),
                           width=20, padx=2, pady=6)
        btnSearch.grid(row=0, column=1)

        btnInsertData = Button(ButtonFrame, text="Insert data",command=self.insert, bg='green', fg='white', font=("arial", 12, "bold"),
                                 width=20, padx=2, pady=6)
        btnInsertData.grid(row=0, column=2)

        btnUpdate = Button(ButtonFrame, text="Update",command=self.update, bg='green', fg='white', font=("arial", 12, "bold"),
                                 width=20, padx=2, pady=6)
        btnUpdate.grid(row=0, column=3)

        btnDelete = Button(ButtonFrame, text="Delete",command=self.delete, bg='green', fg='white', font=("arial", 12, "bold"),
                                 width=20, padx=2, pady=6)
        btnDelete.grid(row=0, column=4)

        btnClear = Button(ButtonFrame, text="Clear",command=self.clear, bg='green', fg='white', font=("arial", 12, "bold"),
                                 width=20, padx=2, pady=6)
        btnClear.grid(row=0, column=5)

        btnExit = Button(ButtonFrame, text="Exit",command=self.exit, bg='green', fg='white', font=("arial", 12, "bold"),
                                 width=20, padx=2, pady=6)
        btnExit.grid(row=0, column=6)




        #----------------------------------table--------------------------
        #---------------------------------Scrollbar-----------------------
        scroll_x=ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Detailsframe,orient=VERTICAL)

        self.store_table=ttk.Treeview(Detailsframe,column=("id","Date of Buy","price","sold price","is sold","Date of Sale","family brand","type","brand"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)


        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x=ttk.Scrollbar(command=self.store_table.xview)
        scroll_x=ttk.Scrollbar(command=self.store_table.yview)

        self.store_table.heading("id",text="id")
        self.store_table.heading("Date of Buy",text="Date of Buy")
        self.store_table.heading("price", text="price")
        self.store_table.heading("sold price", text="sold price")
        self.store_table.heading("is sold", text="is sold")
        self.store_table.heading("Date of Sale", text="Date of Sale")
        self.store_table.heading("family brand", text="family brand")
        self.store_table.heading("type", text="type")
        self.store_table.heading("brand", text="brand")

        self.store_table["show"]="headings"
        self.store_table.column("id",width=100)
        self.store_table.column("Date of Buy",width=100)
        self.store_table.column("price",width=100)
        self.store_table.column("sold price",width=100)
        self.store_table.column("is sold",width=100)
        self.store_table.column("Date of Sale",width=100)
        self.store_table.column("family brand",width=100)
        self.store_table.column("type",width=100)
        self.store_table.column("brand",width=100)

        self.store_table.pack(fill=BOTH,expand=1)
        self.store_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.read()
    #---------------------------Functionality Declaration------------------------
    def insert(self):
        if self.type.get()=="" or self.DateOfBuy.get()=="" or self.price.get()=="" or self.isSold.get()=="":
            messagebox.showerror("error","All fields are required")
        else:
            date_of_buy=datetime.strptime(self.DateOfBuy.get(), '%Y-%m-%d').date()
            date_of_sale=None
            if self.DateOfSale.get()!="":
                date_of_sale=datetime.strptime(self.DateOfSale.get(), '%Y-%m-%d').date()
            sold_price=None
            if self.soldPrice.get()!="":
                sold_price=int(self.soldPrice.get())
            is_sold=0
            if self.isSold.get()=="yes":
                is_sold=1
            try:
                conn = mysql.connector.connect(host="localhost", username="hooman", password="8585honarvar",
                                               database="Touch_mobile")
                my_cursor = conn.cursor()
                try:

                    my_cursor.execute(
                        "insert into stuff_1 (`Date of Buy`,`price`,`sold price`,`is sold`,`Date of Sale`,`Family Brand`,`type`,`brand`) values(%s,%s,%s,%s,%s,%s,%s,%s)",
                        (date_of_buy, int(self.price.get()), sold_price, is_sold, date_of_sale, self.FamilyBrand.get(),
                         self.type.get(), self.Brand.get()))
                    messagebox.showinfo("Insert", "Record has been Inserted Successfully")

                except:
                    messagebox.showerror("error", "unable to insert data")
                conn.commit()
                conn.close()
            except:
                messagebox.showerror("error", "unable connect to database")
        self.read()


    def read(self):
        conn=None
        my_cursor=None
        try:
            conn = mysql.connector.connect(host="localhost", username="hooman", password="8585honarvar",
                                           database="Touch_mobile")
            my_cursor = conn.cursor()
        except:
            messagebox.showerror("error", "unable connect to database")

        my_cursor.execute("select * from stuff_1")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.store_table.delete(*self.store_table.get_children())
            for i in rows:
                self.store_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.store_table.focus()
        content=self.store_table.item(cursor_row)
        row=content["values"]
        self.type.set(row[7])
        self.FamilyBrand.set(row[6])
        self.DateOfBuy.set(row[1])
        self.price.set(row[2])
        self.DateOfSale.set(row[5])
        self.soldPrice.set(row[3])
        self.Brand.set(row[8])
        self.isSold.set(row[4])
        self.Id.set(row[0])


    def update(self):

        date_of_buy = datetime.strptime(self.DateOfBuy.get(), '%Y-%m-%d').date()
        date_of_sale = ""
        if self.DateOfSale.get() != "":
            date_of_sale = datetime.strptime(self.DateOfSale.get(), '%Y-%m-%d').date()
        sold_price = None
        if self.soldPrice.get() != "":
            sold_price = int(self.soldPrice.get())
        conn=None
        my_cursor=None
        try:
            conn = mysql.connector.connect(host="localhost", username="hooman", password="8585honarvar",
                                           database="Touch_mobile")
            my_cursor = conn.cursor()

        except:
            messagebox.showerror("error", "unable connect to database")
        try:
            my_cursor.execute(
                "update stuff_1  set `Date of Buy`=%s , `price`=%s,`sold price`=%s,`is sold`=%s,`Date of Sale`=%s,`Family Brand`=%s,`type`=%s,`brand`=%s where `idstuff` =%s",
                (date_of_buy, int(self.price.get()), sold_price, int(self.isSold.get()), date_of_sale, self.FamilyBrand.get(),
                 self.type.get(), self.Brand.get(),int(self.Id.get())))
            messagebox.showinfo("Update", "Record has been updated Successfully")
            conn.commit()
            conn.close()
            self.read()

        except:
            messagebox.showerror("error", "unable to update data")

    def delete(self):
        conn = None
        my_cursor = None
        try:
            conn = mysql.connector.connect(host="localhost", username="hooman", password="8585honarvar",
                                           database="Touch_mobile")
            my_cursor = conn.cursor()

        except:
            messagebox.showerror("error", "unable connect to database")
        try:
            query="delete from stuff_1 where `idstuff`=%s"
            value=(int(self.Id.get()),)
            my_cursor.execute(query,value)

            messagebox.showinfo("Delete", "Record has been Deleted Successfully")
            conn.commit()
            conn.close()
            self.read()

        except:
            messagebox.showerror("error", "unable to delete data")

    def clear(self):
        self.type.set("")
        self.FamilyBrand.set("")
        self.Brand.set("")
        self.DateOfBuy.set("")
        self.DateOfSale.set("")
        self.price.set("")
        self.isSold.set("")
        self.soldPrice.set("")
        self.Id.set("")
        self.txtInformation.delete("1.0",END)
    def exit(self):
        Iexit=messagebox.askyesno("Touch mobile","Confirm you want to exit")
        if Iexit>0:
            root.destroy()
            return



    def search(self):
        self.txtInformation.delete("1.0",END)
        conn = None
        my_cursor = None
        try:
            conn = mysql.connector.connect(host="localhost", username="hooman", password="8585honarvar",
                                           database="Touch_mobile")
            my_cursor = conn.cursor()

        except:
            messagebox.showerror("error", "unable connect to database")
        if self.isSold.get()!="" and self.type.get()=="" and self.Brand.get()=="" and self.FamilyBrand.get()=="":
            query = "select * from stuff_1 where `is sold`=%s"
            value = (int(self.isSold.get()),)
            my_cursor.execute(query, value)
            result=my_cursor.fetchall()
            count=1
            if len(result)!=0:
                for row in result:
                    self.txtInformation.insert(END,"--------------------------------------"+str(count)+"-----------------------------------------\n")
                    self.txtInformation.insert(END,"Date of Buy:\t\t\t"+str(row[1])+"\n")
                    self.txtInformation.insert(END, "price:\t\t\t" + str(row[2]) + "\n")
                    self.txtInformation.insert(END, "sold price:\t\t\t" + str(row[3]) + "\n")
                    self.txtInformation.insert(END, "is sold?:\t\t\t" + str(row[4]) + "\n")
                    self.txtInformation.insert(END, "Date of Sale:\t\t\t" + str(row[5]) + "\n")
                    self.txtInformation.insert(END, "Family Brand:\t\t\t" + str(row[6]) + "\n")
                    self.txtInformation.insert(END, "Type:\t\t\t" + str(row[7]) + "\n")
                    self.txtInformation.insert(END, "Brand:\t\t\t" + str(row[8]) + "\n")
                    count+=1
                count=1
        elif self.isSold.get()=="" and self.type.get()!="" and self.Brand.get()=="" and self.FamilyBrand.get()=="":
            query = "select * from stuff_1 where `type`=%s"
            value = (self.type.get(),)
            my_cursor.execute(query, value)
            result=my_cursor.fetchall()
            count=1
            if len(result)!=0:
                for row in result:
                    self.txtInformation.insert(END,"--------------------------------------"+str(count)+"-----------------------------------------\n")
                    self.txtInformation.insert(END,"Date of Buy:\t\t\t"+str(row[1])+"\n")
                    self.txtInformation.insert(END, "price:\t\t\t" + str(row[2]) + "\n")
                    self.txtInformation.insert(END, "sold price:\t\t\t" + str(row[3]) + "\n")
                    self.txtInformation.insert(END, "is sold?:\t\t\t" + str(row[4]) + "\n")
                    self.txtInformation.insert(END, "Date of Sale:\t\t\t" + str(row[5]) + "\n")
                    self.txtInformation.insert(END, "Family Brand:\t\t\t" + str(row[6]) + "\n")
                    self.txtInformation.insert(END, "Type:\t\t\t" + str(row[7]) + "\n")
                    self.txtInformation.insert(END, "Brand:\t\t\t" + str(row[8]) + "\n")
                    count+=1
                count=1
        elif self.isSold.get()=="" and self.type.get()=="" and self.Brand.get()!="" and self.FamilyBrand.get()=="":
            query = "select * from stuff_1 where `brnad`=%s"
            value = (self.Brand.get(),)
            my_cursor.execute(query, value)
            result=my_cursor.fetchall()
            count=1
            if len(result)!=0:
                for row in result:
                    self.txtInformation.insert(END,"--------------------------------------"+str(count)+"-----------------------------------------\n")
                    self.txtInformation.insert(END,"Date of Buy:\t\t\t"+str(row[1])+"\n")
                    self.txtInformation.insert(END, "price:\t\t\t" + str(row[2]) + "\n")
                    self.txtInformation.insert(END, "sold price:\t\t\t" + str(row[3]) + "\n")
                    self.txtInformation.insert(END, "is sold?:\t\t\t" + str(row[4]) + "\n")
                    self.txtInformation.insert(END, "Date of Sale:\t\t\t" + str(row[5]) + "\n")
                    self.txtInformation.insert(END, "Family Brand:\t\t\t" + str(row[6]) + "\n")
                    self.txtInformation.insert(END, "Type:\t\t\t" + str(row[7]) + "\n")
                    self.txtInformation.insert(END, "Brand:\t\t\t" + str(row[8]) + "\n")
                    count+=1
                count=1
        elif self.isSold.get()=="" and self.type.get()=="" and self.Brand.get()=="" and self.FamilyBrand.get()!="":
            query = "select * from stuff_1 where `Family Brand`=%s"
            value = (self.FamilyBrand.get(),)
            my_cursor.execute(query, value)
            result=my_cursor.fetchall()
            count=1
            if len(result)!=0:
                for row in result:
                    self.txtInformation.insert(END,"--------------------------------------"+str(count)+"-----------------------------------------\n")
                    self.txtInformation.insert(END,"Date of Buy:\t\t\t"+str(row[1])+"\n")
                    self.txtInformation.insert(END, "price:\t\t\t" + str(row[2]) + "\n")
                    self.txtInformation.insert(END, "sold price:\t\t\t" + str(row[3]) + "\n")
                    self.txtInformation.insert(END, "is sold?:\t\t\t" + str(row[4]) + "\n")
                    self.txtInformation.insert(END, "Date of Sale:\t\t\t" + str(row[5]) + "\n")
                    self.txtInformation.insert(END, "Family Brand:\t\t\t" + str(row[6]) + "\n")
                    self.txtInformation.insert(END, "Type:\t\t\t" + str(row[7]) + "\n")
                    self.txtInformation.insert(END, "Brand:\t\t\t" + str(row[8]) + "\n")
                    count+=1
                count=1
        elif self.isSold.get()=="" and self.type.get()=="" and self.Brand.get()!="" and self.FamilyBrand.get()!="":
            query = "select * from stuff_1 where `Family Brand`=%s and `brand`=%s"
            value = (self.FamilyBrand.get(),self.Brand.get(),)
            my_cursor.execute(query, value)
            result=my_cursor.fetchall()
            count=1
            if len(result)!=0:
                for row in result:
                    self.txtInformation.insert(END,"--------------------------------------"+str(count)+"-----------------------------------------\n")
                    self.txtInformation.insert(END,"Date of Buy:\t\t\t"+str(row[1])+"\n")
                    self.txtInformation.insert(END, "price:\t\t\t" + str(row[2]) + "\n")
                    self.txtInformation.insert(END, "sold price:\t\t\t" + str(row[3]) + "\n")
                    self.txtInformation.insert(END, "is sold?:\t\t\t" + str(row[4]) + "\n")
                    self.txtInformation.insert(END, "Date of Sale:\t\t\t" + str(row[5]) + "\n")
                    self.txtInformation.insert(END, "Family Brand:\t\t\t" + str(row[6]) + "\n")
                    self.txtInformation.insert(END, "Type:\t\t\t" + str(row[7]) + "\n")
                    self.txtInformation.insert(END, "Brand:\t\t\t" + str(row[8]) + "\n")
                    count+=1
                count=1
        elif self.isSold.get()=="" and self.type.get()!="" and self.Brand.get()=="" and self.FamilyBrand.get()!="":
            query = "select * from stuff_1 where `Family Brand`=%s and `type`=%s"
            value = (self.FamilyBrand.get(),self.type.get(),)
            my_cursor.execute(query, value)
            result=my_cursor.fetchall()
            count=1
            if len(result)!=0:
                for row in result:
                    self.txtInformation.insert(END,"--------------------------------------"+str(count)+"-----------------------------------------\n")
                    self.txtInformation.insert(END,"Date of Buy:\t\t\t"+str(row[1])+"\n")
                    self.txtInformation.insert(END, "price:\t\t\t" + str(row[2]) + "\n")
                    self.txtInformation.insert(END, "sold price:\t\t\t" + str(row[3]) + "\n")
                    self.txtInformation.insert(END, "is sold?:\t\t\t" + str(row[4]) + "\n")
                    self.txtInformation.insert(END, "Date of Sale:\t\t\t" + str(row[5]) + "\n")
                    self.txtInformation.insert(END, "Family Brand:\t\t\t" + str(row[6]) + "\n")
                    self.txtInformation.insert(END, "Type:\t\t\t" + str(row[7]) + "\n")
                    self.txtInformation.insert(END, "Brand:\t\t\t" + str(row[8]) + "\n")
                    count+=1
                count=1
        elif self.isSold.get()!="" and self.type.get()=="" and self.Brand.get()=="" and self.FamilyBrand.get()!="":
            query = "select * from stuff_1 where `Family Brand`=%s and `is sold`=%s"
            value = (self.FamilyBrand.get(),int(self.isSold.get()),)
            my_cursor.execute(query, value)
            result=my_cursor.fetchall()
            count=1
            if len(result)!=0:
                for row in result:
                    self.txtInformation.insert(END,"--------------------------------------"+str(count)+"-----------------------------------------\n")
                    self.txtInformation.insert(END,"Date of Buy:\t\t\t"+str(row[1])+"\n")
                    self.txtInformation.insert(END, "price:\t\t\t" + str(row[2]) + "\n")
                    self.txtInformation.insert(END, "sold price:\t\t\t" + str(row[3]) + "\n")
                    self.txtInformation.insert(END, "is sold?:\t\t\t" + str(row[4]) + "\n")
                    self.txtInformation.insert(END, "Date of Sale:\t\t\t" + str(row[5]) + "\n")
                    self.txtInformation.insert(END, "Family Brand:\t\t\t" + str(row[6]) + "\n")
                    self.txtInformation.insert(END, "Type:\t\t\t" + str(row[7]) + "\n")
                    self.txtInformation.insert(END, "Brand:\t\t\t" + str(row[8]) + "\n")
                    count+=1
                count=1
        elif self.isSold.get()=="" and self.type.get()!="" and self.Brand.get()!="" and self.FamilyBrand.get()!="":
            query = "select * from stuff_1 where `Family Brand`=%s and `type`=%s and `brand`=%s"
            value = (self.FamilyBrand.get(),self.type.get(),self.Brand.get(),)
            my_cursor.execute(query, value)
            result=my_cursor.fetchall()
            count=1
            if len(result)!=0:
                for row in result:
                    self.txtInformation.insert(END,"--------------------------------------"+str(count)+"-----------------------------------------\n")
                    self.txtInformation.insert(END,"Date of Buy:\t\t\t"+str(row[1])+"\n")
                    self.txtInformation.insert(END, "price:\t\t\t" + str(row[2]) + "\n")
                    self.txtInformation.insert(END, "sold price:\t\t\t" + str(row[3]) + "\n")
                    self.txtInformation.insert(END, "is sold?:\t\t\t" + str(row[4]) + "\n")
                    self.txtInformation.insert(END, "Date of Sale:\t\t\t" + str(row[5]) + "\n")
                    self.txtInformation.insert(END, "Family Brand:\t\t\t" + str(row[6]) + "\n")
                    self.txtInformation.insert(END, "Type:\t\t\t" + str(row[7]) + "\n")
                    self.txtInformation.insert(END, "Brand:\t\t\t" + str(row[8]) + "\n")
                    count+=1
                count=1
        elif self.isSold.get()!="" and self.type.get()!="" and self.Brand.get()=="" and self.FamilyBrand.get()!="":
            query = "select * from stuff_1 where `Family Brand`=%s and `type`=%s and `is sold`=%s"
            value = (self.FamilyBrand.get(),self.type.get(),int(self.isSold.get()),)
            my_cursor.execute(query, value)
            result=my_cursor.fetchall()
            count=1
            if len(result)!=0:
                for row in result:
                    self.txtInformation.insert(END,"--------------------------------------"+str(count)+"-----------------------------------------\n")
                    self.txtInformation.insert(END,"Date of Buy:\t\t\t"+str(row[1])+"\n")
                    self.txtInformation.insert(END, "price:\t\t\t" + str(row[2]) + "\n")
                    self.txtInformation.insert(END, "sold price:\t\t\t" + str(row[3]) + "\n")
                    self.txtInformation.insert(END, "is sold?:\t\t\t" + str(row[4]) + "\n")
                    self.txtInformation.insert(END, "Date of Sale:\t\t\t" + str(row[5]) + "\n")
                    self.txtInformation.insert(END, "Family Brand:\t\t\t" + str(row[6]) + "\n")
                    self.txtInformation.insert(END, "Type:\t\t\t" + str(row[7]) + "\n")
                    self.txtInformation.insert(END, "Brand:\t\t\t" + str(row[8]) + "\n")
                    count+=1
                count=1
        elif self.isSold.get()!="" and self.type.get()!="" and self.Brand.get()!="" and self.FamilyBrand.get()!="":
            query = "select * from stuff_1 where `Family Brand`=%s and `type`=%s and `brand`=%s and `is sold`=%s"
            value = (self.FamilyBrand.get(),self.type.get(),self.Brand.get(),int(self.isSold.get()),)
            my_cursor.execute(query, value)
            result=my_cursor.fetchall()
            count=1
            if len(result)!=0:
                for row in result:
                    self.txtInformation.insert(END,"--------------------------------------"+str(count)+"-----------------------------------------\n")
                    self.txtInformation.insert(END,"Date of Buy:\t\t\t"+str(row[1])+"\n")
                    self.txtInformation.insert(END, "price:\t\t\t" + str(row[2]) + "\n")
                    self.txtInformation.insert(END, "sold price:\t\t\t" + str(row[3]) + "\n")
                    self.txtInformation.insert(END, "is sold?:\t\t\t" + str(row[4]) + "\n")
                    self.txtInformation.insert(END, "Date of Sale:\t\t\t" + str(row[5]) + "\n")
                    self.txtInformation.insert(END, "Family Brand:\t\t\t" + str(row[6]) + "\n")
                    self.txtInformation.insert(END, "Type:\t\t\t" + str(row[7]) + "\n")
                    self.txtInformation.insert(END, "Brand:\t\t\t" + str(row[8]) + "\n")
                    count+=1
                count=1
        elif self.isSold.get()=="" and self.type.get()!="" and self.Brand.get()!="" and self.FamilyBrand.get()=="":
            query = "select * from stuff_1 where `brand`=%s and `type`=%s"
            value = (self.Brand.get(),self.type.get(),)
            my_cursor.execute(query, value)
            result=my_cursor.fetchall()
            count=1
            if len(result)!=0:
                for row in result:
                    self.txtInformation.insert(END,"--------------------------------------"+str(count)+"-----------------------------------------\n")
                    self.txtInformation.insert(END,"Date of Buy:\t\t\t"+str(row[1])+"\n")
                    self.txtInformation.insert(END, "price:\t\t\t" + str(row[2]) + "\n")
                    self.txtInformation.insert(END, "sold price:\t\t\t" + str(row[3]) + "\n")
                    self.txtInformation.insert(END, "is sold?:\t\t\t" + str(row[4]) + "\n")
                    self.txtInformation.insert(END, "Date of Sale:\t\t\t" + str(row[5]) + "\n")
                    self.txtInformation.insert(END, "Family Brand:\t\t\t" + str(row[6]) + "\n")
                    self.txtInformation.insert(END, "Type:\t\t\t" + str(row[7]) + "\n")
                    self.txtInformation.insert(END, "Brand:\t\t\t" + str(row[8]) + "\n")
                    count+=1
                count=1
        elif self.isSold.get()!="" and self.type.get()!="" and self.Brand.get()=="" and self.FamilyBrand.get()=="":
            query = "select * from stuff_1 where `is sold`=%s and `type`=%s"
            value = (int(self.isSold.get()),self.type.get(),)
            my_cursor.execute(query, value)
            result=my_cursor.fetchall()
            count=1
            if len(result)!=0:
                for row in result:
                    self.txtInformation.insert(END,"--------------------------------------"+str(count)+"-----------------------------------------\n")
                    self.txtInformation.insert(END,"Date of Buy:\t\t\t"+str(row[1])+"\n")
                    self.txtInformation.insert(END, "price:\t\t\t" + str(row[2]) + "\n")
                    self.txtInformation.insert(END, "sold price:\t\t\t" + str(row[3]) + "\n")
                    self.txtInformation.insert(END, "is sold?:\t\t\t" + str(row[4]) + "\n")
                    self.txtInformation.insert(END, "Date of Sale:\t\t\t" + str(row[5]) + "\n")
                    self.txtInformation.insert(END, "Family Brand:\t\t\t" + str(row[6]) + "\n")
                    self.txtInformation.insert(END, "Type:\t\t\t" + str(row[7]) + "\n")
                    self.txtInformation.insert(END, "Brand:\t\t\t" + str(row[8]) + "\n")
                    count+=1
                count=1
        elif self.isSold.get()!="" and self.type.get()=="" and self.Brand.get()!="" and self.FamilyBrand.get()=="":
            query = "select * from stuff_1 where `brand`=%s and `is sold`=%s"
            value = (self.Brand.get(),int(self.isSold.get()),)
            my_cursor.execute(query, value)
            result=my_cursor.fetchall()
            count=1
            if len(result)!=0:
                for row in result:
                    self.txtInformation.insert(END,"--------------------------------------"+str(count)+"-----------------------------------------\n")
                    self.txtInformation.insert(END,"Date of Buy:\t\t\t"+str(row[1])+"\n")
                    self.txtInformation.insert(END, "price:\t\t\t" + str(row[2]) + "\n")
                    self.txtInformation.insert(END, "sold price:\t\t\t" + str(row[3]) + "\n")
                    self.txtInformation.insert(END, "is sold?:\t\t\t" + str(row[4]) + "\n")
                    self.txtInformation.insert(END, "Date of Sale:\t\t\t" + str(row[5]) + "\n")
                    self.txtInformation.insert(END, "Family Brand:\t\t\t" + str(row[6]) + "\n")
                    self.txtInformation.insert(END, "Type:\t\t\t" + str(row[7]) + "\n")
                    self.txtInformation.insert(END, "Brand:\t\t\t" + str(row[8]) + "\n")
                    count+=1
                count=1
        elif self.isSold.get()!="" and self.type.get()!="" and self.Brand.get()!="" and self.FamilyBrand.get()=="":
            query = "select * from stuff_1 where `type`=%s and `brand`=%s and `is sold`=%s"
            value = (self.type.get(),self.Brand.get(),int(self.isSold.get()),)
            my_cursor.execute(query, value)
            result=my_cursor.fetchall()
            count=1
            if len(result)!=0:
                for row in result:
                    self.txtInformation.insert(END,"--------------------------------------"+str(count)+"-----------------------------------------\n")
                    self.txtInformation.insert(END,"Date of Buy:\t\t\t"+str(row[1])+"\n")
                    self.txtInformation.insert(END, "price:\t\t\t" + str(row[2]) + "\n")
                    self.txtInformation.insert(END, "sold price:\t\t\t" + str(row[3]) + "\n")
                    self.txtInformation.insert(END, "is sold?:\t\t\t" + str(row[4]) + "\n")
                    self.txtInformation.insert(END, "Date of Sale:\t\t\t" + str(row[5]) + "\n")
                    self.txtInformation.insert(END, "Family Brand:\t\t\t" + str(row[6]) + "\n")
                    self.txtInformation.insert(END, "Type:\t\t\t" + str(row[7]) + "\n")
                    self.txtInformation.insert(END, "Brand:\t\t\t" + str(row[8]) + "\n")
                    count+=1
                count=1
        elif self.isSold.get()!="" and self.type.get()=="" and self.Brand.get()!="" and self.FamilyBrand.get()!="":
            query = "select * from stuff_1 where `Family Brand`=%s and `brand`=%s and `is sold`=%s"
            value = (self.FamilyBrand.get(),self.Brand.get(),int(self.isSold.get()),)
            my_cursor.execute(query, value)
            result=my_cursor.fetchall()
            count=1
            if len(result)!=0:
                for row in result:
                    self.txtInformation.insert(END,"--------------------------------------"+str(count)+"-----------------------------------------\n")
                    self.txtInformation.insert(END,"Date of Buy:\t\t\t"+str(row[1])+"\n")
                    self.txtInformation.insert(END, "price:\t\t\t" + str(row[2]) + "\n")
                    self.txtInformation.insert(END, "sold price:\t\t\t" + str(row[3]) + "\n")
                    self.txtInformation.insert(END, "is sold?:\t\t\t" + str(row[4]) + "\n")
                    self.txtInformation.insert(END, "Date of Sale:\t\t\t" + str(row[5]) + "\n")
                    self.txtInformation.insert(END, "Family Brand:\t\t\t" + str(row[6]) + "\n")
                    self.txtInformation.insert(END, "Type:\t\t\t" + str(row[7]) + "\n")
                    self.txtInformation.insert(END, "Brand:\t\t\t" + str(row[8]) + "\n")
                    count+=1
                count=1









root=Tk()
ob=Store(root)
root.mainloop()