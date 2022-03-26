# importing tkinter libraries
from tkinter import * 
import tkinter as tk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import datetime
import tkinter

class LibraryManagementSystem:
    def __init__(self,root):
        self.root = root
        self.root.title("LibraryManagementSystem")
        self.root.geometry("1550x800+0+0")
        
        ########### Declaring variables ###########3
        self.member_var = StringVar()
        self.prn_var = StringVar()
        self.id_var = StringVar()
        self.firstname_var = StringVar()
        self.lastname_var = StringVar()
        self.address1_var = StringVar()
        self.address2_var = StringVar()
        self.postcode_var = StringVar()
        self.mobile_var = StringVar()
        self.bookid_var = StringVar()
        self.title_var = StringVar()
        self.author_var = StringVar()
        self.dateborrowed_var = StringVar()
        self.datedue_var = StringVar()
        self.daysonbook_var = StringVar()
        self.latereturnfine_var = StringVar()
        self.dateoverdue_var = StringVar()
        self.price_var = StringVar()
        
        
        
        lbltitle = Label(self.root,text = "Library Management System",bg = "black",fg = "white",bd = 20,relief = RIDGE,font=("times new roman",50,"bold"),padx = 2,pady = 6)
        lbltitle.pack(side = TOP,fill=X)
        
        frame = Frame(self.root,bd = 12,relief = RIDGE,padx = 12,bg = "light green")
        frame.place(x=0,y=130,height = 400,width = 1530)

        # data frame left side and creating labels and entry box for member registration

        DataFrameLeft = LabelFrame(frame,text = "Book Issue Details",bg = "light green",fg = "blue",bd = 12,relief = RIDGE,font=("times new roman",15,"bold"))
        DataFrameLeft.place(x =0,y=5,width =860,height=360)
        
        lblMember = Label(DataFrameLeft,bg = "light green",text = "Member Type",font=("times new roman",12,"bold"),padx = 2,pady = 6)
        lblMember.grid(row =0,column =0,sticky=W)
        
        lblentry = ttk.Combobox(DataFrameLeft,textvariable = self.member_var,font=("times new roman",12,"bold"),width = 27,state = "readonly")
        lblentry["value"] = ("Student","Faculty","Admin Staff")
        lblentry.grid(row=0,column=1)
        
        lblPRN = Label(DataFrameLeft,font=("times new roman",12,"bold"),text = "PRN NO.",padx=2,bg = "light green")
        lblPRN.grid(row = 1,column = 0,sticky = W)
        lblPRNEntry = Entry(DataFrameLeft,textvariable = self.prn_var,font=("times new roman",12,"bold"),width = 29)
        lblPRNEntry.grid(row=1,column=1)
        
        lblID = Label(DataFrameLeft,font=("times new roman",12,"bold"),text = "ID NO.",padx=2,pady=4,bg = "light green")
        lblID.grid(row =2,column = 0,sticky = W)
        lblIDEntry = Entry(DataFrameLeft,textvariable = self.id_var,font=("times new roman",12,"bold"),width = 29)
        lblIDEntry.grid(row=2,column=1)
        
         
        lblFirstName = Label(DataFrameLeft,font=("times new roman",12,"bold"),text = "FirstName",padx=2,pady=6,bg = "light green")
        lblFirstName.grid(row = 3,column = 0,sticky = W)
        lblFirstNameEntry = Entry(DataFrameLeft,textvariable=self.firstname_var,font=("times new roman",12,"bold"),width = 29)
        lblFirstNameEntry.grid(row=3,column=1)
        
        lblLastName = Label(DataFrameLeft,font=("times new roman",12,"bold"),text = "LastName",padx=2,pady=6,bg = "light green")
        lblLastName.grid(row = 4,column = 0,sticky = W)
        lblLastNameEntry = Entry(DataFrameLeft,textvariable = self.lastname_var ,font=("times new roman",12,"bold"),width = 29)
        lblLastNameEntry.grid(row=4,column=1)
        
        
        lblAdd1 = Label(DataFrameLeft,font=("times new roman",12,"bold"),text = "Address1",padx=2,pady=6,bg = "light green")
        lblAdd1.grid(row = 5,column = 0,sticky = W)
        lblAdd1Entry = Entry(DataFrameLeft,textvariable=self.address1_var,font=("times new roman",12,"bold"),width = 29)
        lblAdd1Entry.grid(row=5,column=1)
        
        lblAdd2 = Label(DataFrameLeft,font=("times new roman",12,"bold"),text = "Address2",padx=2,pady=6,bg = "light green")
        lblAdd2.grid(row = 6,column = 0,sticky = W)
        lblAdd2Entry = Entry(DataFrameLeft,textvariable = self.address2_var,font=("times new roman",12,"bold"),width = 29)
        lblAdd2Entry.grid(row=6,column=1)
        
        lblPost = Label(DataFrameLeft,font=("times new roman",12,"bold"),text = "PostCode",padx=2,pady=6,bg = "light green")
        lblPost.grid(row = 7,column = 0,sticky = W)
        lblPostEntry = Entry(DataFrameLeft,textvariable = self.postcode_var,font=("times new roman",12,"bold"),width = 29)
        lblPostEntry.grid(row=7,column=1)
       
        lblMob = Label(DataFrameLeft,font=("times new roman",12,"bold"),text = "Mobile",padx=2,pady=6,bg = "light green")
        lblMob.grid(row = 8,column = 0,sticky = W)
        lblMobEntry = Entry(DataFrameLeft,textvariable=self.mobile_var,font=("times new roman",12,"bold"),width = 29)
        lblMobEntry.grid(row=8,column=1)
        
        
        lblBookId = Label(DataFrameLeft,font=("times new roman",12,"bold"),text = "Book ID",padx=2,bg = "light green")
        lblBookId.grid(row = 0,column = 2,sticky = W)
        lblBookIdEntry = Entry(DataFrameLeft,textvariable = self.bookid_var,font=("times new roman",12,"bold"),width = 29)
        lblBookIdEntry.grid(row=0,column=3)
        
        lblBookTitle = Label(DataFrameLeft,font=("times new roman",12,"bold"),text = "Book Title",padx=2,pady=6,bg = "light green")
        lblBookTitle.grid(row = 1,column = 2,sticky = W)
        lblBookTitleEntry = Entry(DataFrameLeft,textvariable = self.title_var,font=("times new roman",12,"bold"),width = 29)
        lblBookTitleEntry.grid(row=1,column=3)
        
        lblAuthor = Label(DataFrameLeft,font=("times new roman",12,"bold"),text = "Author Name",padx=2,pady=6,bg = "light green")
        lblAuthor.grid(row = 2,column = 2,sticky = W)
        lblAuthorEntry = Entry(DataFrameLeft,textvariable = self.author_var,font=("times new roman",12,"bold"),width = 29)
        lblAuthorEntry.grid(row=2,column=3)
        
        lblDateBorrowed = Label(DataFrameLeft,font=("times new roman",12,"bold"),text = "Date Borrowed",padx=2,pady=6,bg = "light green")
        lblDateBorrowed.grid(row = 3,column = 2,sticky = W)
        lblDateBorrowedEntry = Entry(DataFrameLeft,textvariable = self.dateborrowed_var,font=("times new roman",12,"bold"),width = 29)
        lblDateBorrowedEntry.grid(row=3,column=3)
        
        lblDateDue = Label(DataFrameLeft,font=("times new roman",12,"bold"),text = "Date Due",padx=2,pady=6,bg = "light green")
        lblDateDue.grid(row = 4,column = 2,sticky = W)
        lblDateDueEntry = Entry(DataFrameLeft,textvariable = self.datedue_var,font=("times new roman",12,"bold"),width = 29)
        lblDateDueEntry.grid(row=4,column=3)
        
        lblDaysOnBook= Label(DataFrameLeft,font=("times new roman",12,"bold"),text = "Days on Book",padx=2,pady=6,bg = "light green")
        lblDaysOnBook.grid(row = 5,column = 2,sticky = W)
        lblDaysOnBookEntry = Entry(DataFrameLeft,textvariable = self.daysonbook_var,font=("times new roman",12,"bold"),width = 29)
        lblDaysOnBookEntry.grid(row=5,column=3)
        
        lblLateReturnFine= Label(DataFrameLeft,font=("times new roman",12,"bold"),text = "Late Return Fine",padx=2,pady=6,bg = "light green")
        lblLateReturnFine.grid(row = 6,column = 2,sticky = W)
        lblLateReturnFineEntry = Entry(DataFrameLeft,textvariable = self.latereturnfine_var,font=("times new roman",12,"bold"),width = 29)
        lblLateReturnFineEntry.grid(row=6,column=3)
        
        lblDateOverDue= Label(DataFrameLeft,font=("times new roman",12,"bold"),text = "Date Over Due",padx=2,pady=6,bg = "light green")
        lblDateOverDue.grid(row = 7,column = 2,sticky = W)
        lblDateOverDueEntry = Entry(DataFrameLeft,textvariable = self.dateoverdue_var,font=("times new roman",12,"bold"),width = 29)
        lblDateOverDueEntry.grid(row=7,column=3)
        
        lblPrice= Label(DataFrameLeft,font=("times new roman",12,"bold"),text = "Price",padx=2,pady=6,bg = "light green")
        lblPrice.grid(row = 8,column = 2,sticky = W)
        lblPriceEntry = Entry(DataFrameLeft,textvariable = self.price_var,font=("times new roman",12,"bold"),width = 29)
        lblPriceEntry.grid(row=8,column=3)
        
        
        
        # data frame right side and creating labels to show available books
        DataFrameRight = LabelFrame(frame,text = "Available Books",bg = "light green",fg = "blue",bd = 12,relief = RIDGE,font=("times new roman",15,"bold"))
        DataFrameRight.place(x =875,y=5,width =600,height=360)
        
        self.txtBox = Text(DataFrameRight,font=("times new roman",15,"bold"),width = 37,height = 13,padx=3,pady=6)
        self.txtBox.grid(row = 0,column = 2)
        
        listScrollBar = Scrollbar(DataFrameRight)
        listScrollBar.grid(row = 0,column =1,sticky = "ns")
        
       #  creating list of books and defining select book function so that after selecting any book entry field will automatically got filled
        listBooks = ['Cracking the Coding Interview','Algorithms','The Algorithm Design Manual','Introduction to Algorithms','Algorithm Design',
                  'Advanced Data Structures','Purely Functional Data Structures','Higher Order Perl','Randomized Algorithms and Probabilistic Analysis',
                  'Computation','An Introduction to Computational Learning Theory','Operating System Concepts','Algorithmic Game Theory',
                  'Operating Systems: Three Easy Pieces','Windows Internals','Modern Processor Design','Readings in Computer Architecture','Algorithmic Game Theory']

        def SelectBook(event=""):
              val = str(listBox.get(listBox.curselection()))
              x = val
        
              if (x == "Cracking the Coding Interview"):
                
                self.bookid_var.set("BKID01")
                self.title_var.set("Cracking the Coding Interview")
                self.author_var.set("McDowell")
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days = 15)
                d3 = d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set("15")
                self.latereturnfine_var.set("50")
                self.dateoverdue_var.set("NA")
                self.price_var.set("600")  

              elif (x == "Algorithms"):
                
                self.bookid_var.set("BKID02")
                self.title_var.set("Algorithms")
                self.author_var.set("Dasgupta, Papadimitriou, and Vazirani")
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days = 15)
                d3 = d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set("15")
                self.latereturnfine_var.set("50")
                self.dateoverdue_var.set("NA")
                self.price_var.set("500")   

              elif (x == "The Algorithm Design Manual"):
                
                self.bookid_var.set("BKID03")
                self.title_var.set("The Algorithm Design Manual")
                self.author_var.set("Skiena")
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days = 15)
                d3 = d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set("15")
                self.latereturnfine_var.set("50")
                self.dateoverdue_var.set("NA")
                self.price_var.set("550")

              elif (x == "Introduction to Algorithms"):
                
                self.bookid_var.set("BKID04")
                self.title_var.set("Introduction to Algorithms")
                self.author_var.set("CLRS")
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days = 15)
                d3 = d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set("15")
                self.latereturnfine_var.set("50")
                self.dateoverdue_var.set("NA")
                self.price_var.set("750") 

              elif (x == "Algorithm Design"):
                
                self.bookid_var.set("BKID05")
                self.title_var.set("Algorithm Design")
                self.author_var.set("Kleinberg & Tardos")
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days = 15)
                d3 = d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set("15")
                self.latereturnfine_var.set("50")
                self.dateoverdue_var.set("NA")
                self.price_var.set("788") 

              elif (x == "Advanced Data Structures"):
                
                self.bookid_var.set("BKID06")
                self.title_var.set("Advanced Data Structures")
                self.author_var.set("Demaine")
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days = 15)
                d3 = d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set("15")
                self.latereturnfine_var.set("50")
                self.dateoverdue_var.set("NA")
                self.price_var.set("890") 

              elif (x == "Purely Functional Data Structures"):
                
                self.bookid_var.set("BKID07")
                self.title_var.set("Purely Functional Data Structures")
                self.author_var.set("Okasaki")
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days = 15)
                d3 = d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set("15")
                self.latereturnfine_var.set("50")
                self.dateoverdue_var.set("NA")
                self.price_var.set("1500") 

              elif (x == "Higher Order Perl"):
                
                self.bookid_var.set("BKID08")
                self.title_var.set("Higher Order Perl")
                self.author_var.set("Dominus")
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days = 15)
                d3 = d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set("15")
                self.latereturnfine_var.set("50")
                self.dateoverdue_var.set("NA")
                self.price_var.set("1200") 

              elif (x == "Randomized Algorithms and Probabilistic Analysis"):
                
                self.bookid_var.set("BKID09")
                self.title_var.set("Randomized Algorithms and Probabilistic Analysis")
                self.author_var.set("Mitzenmacher & Upfal")
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days = 15)
                d3 = d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set("15")
                self.latereturnfine_var.set("50")
                self.dateoverdue_var.set("NA")
                self.price_var.set("1600") 

              elif (x == "An Introduction to Computational Learning Theory"):
                
                self.bookid_var.set("BKID10")
                self.title_var.set("An Introduction to Computational Learning Theory")
                self.author_var.set("Sipser")
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days = 15)
                d3 = d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set("15")
                self.latereturnfine_var.set("50")
                self.dateoverdue_var.set("NA")
                self.price_var.set("900")

        # creating listbox to contain books
        listBox = Listbox(DataFrameRight,font=("times new roman",12,"bold"),width = 20,height = 16)
        listBox.bind("<<ListboxSelect>>",SelectBook)
        listBox.grid(row = 0,column = 0,padx = 4)
        listScrollBar.config(command = listBox.yview)
        
        for item in listBooks:
            listBox.insert(END,item) 

        
        # buttons frame to do the operations such AS add,update,delete,exit,delete and reset
        FrameButton = Frame(self.root,bd = 12,relief = RIDGE,padx = 20,bg = "light green")
        FrameButton.place(x=0,y=530,height = 70,width = 1530)
        
        btnAddData = Button(FrameButton,text = "Add",command = self.add_data,font=("times new roman",12,"bold"),width = 23,bg="light grey",padx=2,pady=2)
        btnAddData.grid(row=0,column=0)
        
        btnshowData = Button(FrameButton,text = "Show",command = self.show_data,font=("times new roman",12,"bold"),width = 23,bg="light grey",padx=2,pady=2)
        btnshowData.grid(row=0,column=1)
        
        btnupdateData = Button(FrameButton,text = "Update",command = self.update,font=("times new roman",12,"bold"),width = 23,bg="light grey")
        btnupdateData.grid(row=0,column=2)
        
        btndelData = Button(FrameButton,text = "Delete",command = self.deletes,font=("times new roman",12,"bold"),width = 23,bg="light grey")
        btndelData.grid(row=0,column=3)
        
        btnresetData = Button(FrameButton,text = "Reset",command = self.reset,font=("times new roman",12,"bold"),width = 23,bg="light grey")
        btnresetData.grid(row=0,column=4)
        
        btnexitData = Button(FrameButton,text = "Exit",command = self.exits,font=("times new roman",12,"bold"),width = 23,bg="light grey")
        btnexitData.grid(row=0,column=5)
        
        # information frame to show the data in database
        FrameDetails = Frame(self.root,bd = 12,relief = RIDGE,padx = 20,bg = "light green")
        FrameDetails.place(x=0,y=600,height = 190,width = 1530)
        
        tableFrame = Frame(FrameDetails,bd = 6,relief = RIDGE,bg = "light green")
        tableFrame.place(x = 0,y=2,width=1470,height = 160)
        
        xscroll = ttk.Scrollbar(tableFrame,orient = HORIZONTAL)
        yscroll = ttk.Scrollbar(tableFrame,orient = VERTICAL)
        
        # creating dummy variables to fetch data from database
        self.lib_table = ttk.Treeview(tableFrame,column = ("Member Type","PRN NO.","ID NO.","FirstName","LastName","Address1",
                                      "Address2","PostCode","Mobile","Book ID","Book Title","Author Name","Date Borrowed",
                                      "Date Due","Days on Book", "Late Return Fine","Date Over Due","Price"),xscrollcommand = xscroll.set,yscrollcommand = yscroll.set)
        
        # adding scrollbars
        xscroll.pack(side = BOTTOM,fill=X)
        yscroll.pack(side = RIGHT,fill=Y)
        
        xscroll.config(command =self.lib_table.xview)
        yscroll.config(command =self.lib_table.yview)
        
        self.lib_table.heading("Member Type",text = "Member Type")
        self.lib_table.heading("PRN NO.",text = "PRN NO.")
        self.lib_table.heading("ID NO.",text = "ID NO.")
        self.lib_table.heading("FirstName",text = "First Name")
        self.lib_table.heading("LastName",text = "Last Name")
        self.lib_table.heading("Address1",text = "Address 1")
        self.lib_table.heading("Address2",text = "Address 2")
        self.lib_table.heading("PostCode",text = "Post Code")
        self.lib_table.heading("Mobile",text = "Mobile")
        self.lib_table.heading("Book ID",text = "Book ID")
        self.lib_table.heading("Book Title",text = "Book Title")
        self.lib_table.heading("Author Name",text = "Author Name")
        self.lib_table.heading("Date Borrowed",text = "Date Borrowed")
        self.lib_table.heading("Date Due",text = "Date Due")
        self.lib_table.heading("Days on Book",text = "Days on Book")
        self.lib_table.heading("Late Return Fine",text = "Late Return Fine")
        self.lib_table.heading("Date Over Due",text = "Date Over Due")
        self.lib_table.heading("Price",text = "Price")
        
        
        self.lib_table["show"] = "headings"
        self.lib_table.pack(fill=BOTH,expand=1)
        
        # reducing the width of column
        self.lib_table.column("Member Type",width = 100)
        self.lib_table.column("PRN NO.",width = 100)
        self.lib_table.column("ID NO.",width = 100)
        self.lib_table.column("FirstName",width = 100)
        self.lib_table.column("LastName",width = 100)
        self.lib_table.column("Address1",width = 100)
        self.lib_table.column("Address2",width = 100)
        self.lib_table.column("PostCode",width = 100)
        self.lib_table.column("Mobile",width = 100)
        self.lib_table.column("Book ID",width = 100)
        self.lib_table.column("Book Title",width = 100)
        self.lib_table.column("Author Name",width = 100)
        self.lib_table.column("Date Borrowed",width = 100)
        self.lib_table.column("Date Due",width = 100)
        self.lib_table.column("Days on Book",width = 100)
        self.lib_table.column("Late Return Fine",width = 100)
        self.lib_table.column("Date Over Due",width = 100)
        self.lib_table.column("Price",width = 100)

        self.fetch_data()
        self.lib_table.bind("<ButtonRelease-1>",self.get_cursor)

        
   
    # function to add data in database
    def add_data(self):
        conn = mysql.connector.connect(host = "localhost",user = "root",password = "password",database = "mydatabase")
        my_cursor = conn.cursor()
        my_cursor.execute("insert into library values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                          ( self.member_var.get(), 
                            self.prn_var.get(),
                            self.id_var .get(),
                            self.firstname_var.get(),
                            self.lastname_var.get(), 
                            self.address1_var.get(),
                            self.address2_var.get(), 
                            self.postcode_var.get(), 
                            self.mobile_var.get(),
                            self.bookid_var.get(), 
                            self.title_var.get(),
                            self.author_var.get(), 
                            self.dateborrowed_var.get(),
                            self.datedue_var.get(),
                            self.daysonbook_var.get(), 
                            self.latereturnfine_var.get(),
                            self.dateoverdue_var.get(), 
                            self.price_var.get() ))
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Success","Member added successfully")

# function to update data in database
    def update(self):
        conn = mysql.connector.connect(host = "localhost",user = "root",password = "password",database = "mydatabase")
        my_cursor = conn.cursor()
        my_cursor.execute("update library set Member=%s,ID=%s,FirstName=%s,LastName=%s,Address1=%s,Address2=%s,PostId=%s,Mobile=%s,BookId=%s,BookTitle=%s,Author=%s,DateBorrowed=%s,DateDue=%s,LateReturnFine=%s,DateoverDue=%s,Price=%s,DaysOnBook=%s,PRN_NO=%s",
                            (self.member_var.get(), 
                            self.id_var .get(),
                            self.firstname_var.get(),
                            self.lastname_var.get(), 
                            self.address1_var.get(),
                            self.address2_var.get(), 
                            self.postcode_var.get(), 
                            self.mobile_var.get(),
                            self.bookid_var.get(), 
                            self.title_var.get(),
                            self.author_var.get(), 
                            self.dateborrowed_var.get(),
                            self.datedue_var.get(),
                            self.latereturnfine_var.get(),
                            self.dateoverdue_var.get(), 
                            self.price_var.get(),
                            self.daysonbook_var.get(), 
                            self.prn_var.get())
                         )
        conn.commit()
        self.fetch_data()
        self.reset()
        conn.close()
        messagebox.showinfo("Success","Member updated successfully")    
        
 # function to fetch data from mysql workbench to our GUI by giving our workbench user and password and name of database
 
    def fetch_data(self):
            conn = mysql.connector.connect(host = "localhost",user = "root",password = "password",database = "mydatabase")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from library")
            rowsVal = my_cursor.fetchall()

            if len(rowsVal)>0:
                self.lib_table.delete(*self.lib_table.get_children())
                for val in rowsVal:
                    self.lib_table.insert("",END,values = val)
                conn.commit()    
            conn.close()    

  # function to fill the entry field and to show thw information when any row is selected 
    def get_cursor(self,event=""):
      self.reset()
      cursor_row = self.lib_table.focus()
      contents = self.lib_table.item(cursor_row)
      row = contents['values']

      self.member_var.set(row[0])
      self.prn_var.set(row[1])
      self.id_var.set(row[1])
      self.firstname_var.set(row[3])
      self.lastname_var.set(row[4])
      self.address1_var.set(row[5])
      self.address2_var.set(row[6])
      self.postcode_var.set(row[7])
      self.mobile_var.set(row[8])
      self.bookid_var.set(row[9])
      self.title_var.set(row[10])
      self.author_var.set(row[11])
      self.dateborrowed_var.set(row[12])
      self.datedue_var.set(row[13])
      self.daysonbook_var.set(row[14])
      self.latereturnfine_var.set(row[15])
      self.dateoverdue_var.set(row[16])
      self.price_var.set(row[17])

    # function to show data of selected member in right side       
    def show_data(self):
      self.txtBox.insert(END,"Member Type \t\t"+ self.member_var.get()+ "\n")
      self.txtBox.insert(END,"PRN NO. \t\t"+ self.prn_var.get()+ "\n")
      self.txtBox.insert(END,"ID NO. \t\t"+ self.id_var.get()+ "\n")
      self.txtBox.insert(END,"First Name \t\t"+ self.firstname_var.get()+ "\n")
      self.txtBox.insert(END,"Last Name \t\t"+ self.lastname_var.get()+ "\n")
      self.txtBox.insert(END,"Address 1 \t\t"+ self.address1_var.get()+ "\n")
      self.txtBox.insert(END,"Address 2 \t\t"+ self.address2_var.get()+ "\n")
      self.txtBox.insert(END,"Post Code \t\t"+ self.postcode_var.get()+ "\n")
      self.txtBox.insert(END,"Mobile  \t\t"+ self.mobile_var.get()+ "\n")
      self.txtBox.insert(END,"Book ID \t\t"+ self.bookid_var.get()+ "\n")
      self.txtBox.insert(END,"Title \t\t"+ self.title_var.get()+ "\n")
      self.txtBox.insert(END,"Author \t\t"+ self.author_var.get()+ "\n")
      self.txtBox.insert(END,"Date Borrowed \t\t"+ self.dateborrowed_var.get()+ "\n")
      self.txtBox.insert(END,"Date Due \t\t"+ self.datedue_var.get()+ "\n")
      self.txtBox.insert(END,"Days on Book \t\t"+ self.daysonbook_var.get()+ "\n")
      self.txtBox.insert(END,"Late Return fine \t\t"+ self.latereturnfine_var.get()+ "\n")
      self.txtBox.insert(END,"Overdue\t\t"+ self.dateoverdue_var.get()+ "\n")
      self.txtBox.insert(END,"Price \t\t"+ self.price_var.get()+ "\n")

 # function to reset the entry fields to empty
    def reset(self):
      self.member_var.set("")
      self.prn_var.set("")
      self.id_var.set("")
      self.firstname_var.set("")
      self.lastname_var.set("")
      self.address1_var.set("")
      self.address2_var.set("")
      self.postcode_var.set("")
      self.mobile_var.set("")
      self.bookid_var.set("")
      self.title_var.set("")
      self.author_var.set("")
      self.dateborrowed_var.set("")
      self.datedue_var.set("")
      self.daysonbook_var.set("")
      self.latereturnfine_var.set("")
      self.dateoverdue_var.set("")
      self.price_var.set("")
    #  self.txtbox.delete("1.0",END)

 # function to exit the GUI
    def exits(self):
      exits = tkinter.messagebox.askyesno("Library Management System","Do You want to exit ?")
      if exits>0:
        self.root.destroy()
        return
 
   # function to delete the row in database when any row is selected
    def deletes(self):
      if self.prn_var.get() == "" or self.id_var.get()=="":
        messagebox.showerror("Error","Deleting without selecting any member")

      else:
        conn = mysql.connector.connect(host = "localhost",user = "root",password = "password",database = "mydatabase")
        my_cursor = conn.cursor()
       # my_cursor.execute("delete from library where PRN_NO=%s",self.prn_var.get())
        query = ("delete from library where PRN_NO=%s")
        value = (self.prn_var.get(),)
        my_cursor.execute(query,value)


        conn.commit()
        self.fetch_data()
        self.reset()
        conn.close()

        messagebox.showinfo("Success","Member has been deleted successfully")

                
 # MAIN FUNCTION CALLING      

if __name__ == "__main__":
    root = Tk()
    obj = LibraryManagementSystem(root)
    root.mainloop()        
   