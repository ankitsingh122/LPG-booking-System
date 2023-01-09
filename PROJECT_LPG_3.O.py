from tkinter import*
from tkinter import font
import mysql.connector
from tkinter.font import BOLD
from tkinter import messagebox
class mainwindow:
    def __init__(self):
        self.root=Tk()
        self.c=Canvas(self.root,height=700,width=1124,bg='Maroon',bd=10)
        self.bg=PhotoImage(file='A:\python\lpg6.png')
        self.la=Label(self.root,image=self.bg)
        self.la.place(x=40,y=40)
        self.c.pack()
        self.root.title('Welcome to LPG world')
    def add_frame(self):
        self.f=Frame(self.root,width=700,height=590,bg='Orange')
        self.f.place(x=220,y=70,)
        self.img=PhotoImage(file='A:\python\logo.png')
        self.l1=Label(self.f,image=self.img,bd=5,bg='maroon')
        self.l1.place(x=300,y=10)
        self.img1=PhotoImage(file='A:\python\Fire.png')
        self.l5=Label(self.f,image=self.img1)
        self.l5.place(x=30,y=445)
        self.l2=Label(self.f,text='Welcome to LPG World',font=('Verdana',25,BOLD),fg='Maroon',bg='orange')
        self.l2.place(x=140,y=160)
        self.l4=Label(self.f,text='Want A New Connection',font=('Times',22),fg='Maroon',bg='orange')
        self.l4.place(x=195,y=230)
        self.b2=Button(self.f,text='New Connection',width=8,font=('Arial',16,BOLD),bd=6,fg='Maroon',command=self.continuesignup)
        self.b2.place(x=238,y=270,width=200,height=40)
        self.l3=Label(self.f,text='Want to Book a Refill',font=('Times',22),fg='Maroon',bg='orange')
        self.l3.place(x=210,y=350)
        self.b1=Button(self.f,text='Refill',width=8,font=('Arial',16,BOLD),bd=6,fg='Maroon',command=self.continuelogin)
        self.b1.place(x=265,y=390,width=140,height=40)
        
        self.root.mainloop()

    def continuelogin(self):
        self.root.destroy()
        y=login()
        y.add_frame()

    def continuesignup(self):
        self.root.destroy()
        a=SignUp()
        a.add_frame()

class login:
    def __init__(self):
        self.root1=Tk()
        self.c=Canvas(self.root1,height=600,width=1100,bg='black')
        self.bg=PhotoImage(file='A:\python\lpg13.png')
        self.la=Label(self.root1,image=self.bg)
        self.la.place(x=690,y=28)
        self.c.pack()
        self.root1.title('Welcome to login page')

    def add_frame(self):
        self.f=Frame(self.root1,width=650,height=550,bg='orange')
        self.f.place(x=20,y=28)
        self.img=PhotoImage(file='A:\python\lpg8.png')
        self.l1=Label(self.f,image=self.img,bd=6,bg='maroon')
        self.l1.place(x=235,y=15)
        self.l2=Label(self.f,text='To Refil Login',font=('Times',25,BOLD),fg='maroon',bg='orange')
        self.l2.place(x=215,y=170)
        self.l3=Label(self.f,text='Enter Username :',font=('MS Serif',12,BOLD),fg='maroon')
        self.l4=Label(self.f,text='Enter Password :',font=('MS Serif',12,BOLD),fg='maroon')
        self.l3.place(x=150,y=220)
        self.l4.place(x=152,y=260)
        self.e1=Entry(self.f,font=('MS Serif',11,BOLD),fg='maroon')
        self.e2=Entry(self.f,font=('MS Serif',11,BOLD),fg='maroon',show='*')
        self.e1.place(x=290,y=220,height=25)
        self.e2.place(x=287,y=260,height=25)
        self.b1=Button(self.f,text='Login',width=8,font=('Arial',16,BOLD),bd=6,bg='dark orange', command=self.login)
        self.b1.place(x=260,y=300,height=35)
        self.img1=PhotoImage(file='A:\python\lpg9.png')
        self.l7=Label(self.f,image=self.img1,bd=6,bg='maroon')
        self.l7.place(x=65,y=350)
        self.root1.mainloop()
    def login(self):
        s1=self.e1.get()
        s2=self.e2.get()
        if s1=='':
            messagebox.showinfo('Alert!','Enter Username')
        elif s2=='':
            messagebox.showinfo('Alert!','Enter Password')
        else:
            mydb = mysql.connector.connect(host='localhost',
                                           user='root',
                                           password='1422',
                                           port='3306',
                                           database='lpg')
            mycursor = mydb.cursor()
            mycursor.execute('Select * from lpg where Username = %s and Password = %s',(s1,s2))
            row = mycursor.fetchone()
            if row:
                messagebox.showinfo('congrachulation','Login sucessfull')
                
                mycursor.execute('SELECT Name FROM lpg where Username=%s and Password=%s;',(s1,s2))
                uname=mycursor.fetchone()
                mycursor.execute('SELECT Address FROM lpg where Username=%s and Password=%s;',(s1,s2))
                uaddress=mycursor.fetchone()
                mycursor.execute('SELECT LPG_Booked FROM lpg where Username=%s and Password=%s;',(s1,s2))
                ulpg=mycursor.fetchone()
                self.f1=Frame(self.root1,width=325,height=280,bg='orange')
                self.f1.place(x=720,y=60)
                self.l8=Label(self.f1,text='Name : %s'%uname,font=('MS Serif',18),fg='maroon',bg='orange')
                self.l8.place(x=5,y=5)
                self.l9=Label(self.f1,text='Address :- \n%s'%uaddress,font=('MS Serif',18),fg='maroon',bg='orange')
                self.l9.place(x=5,y=40)
                self.l10=Label(self.f1,text='No. of LPG Booked : %s'%ulpg,font=('MS Serif',15),fg='maroon',bg='orange')
                self.l10.place(x=5,y=100)

                self.var1=IntVar()
                self.var2=StringVar()
        
                self.s11=Spinbox(self.f1,from_=0, to = 3,textvariable=self.var1,font=('Arial',14))
                self.s22=Spinbox(self.f1,values=('Domestic Use 12Kg','commercial Use 6Kg','commercial Use 12Kg','commercial Use 16Kg','Domestic Use 6Kg'),textvariable=self.var2,font=('Times',14))

                self.s11.place(x=115,y=130,width=100)
                self.s22.place(x=60,y=170)

                self.b2=Button(self.f1,text='continue',font=15,command=self.dis)
                self.b2.place(x=120,y=210,height=30)
                
            else:
                messagebox.showinfo('oh!','invalid')
                self.root1.destroy()
    def dis(self):  
        self.root1.destroy()

class SignUp:
    def __init__(self):
        self.root2=Tk()
        self.c=Canvas(self.root2,height=620,width=700,bg='Orange')
        self.c.pack()
        self.root2.title('Welcome to SignUp page')

    def add_frame(self):
        self.f=Frame(self.root2,width=650,height=570,bg='Black')
        self.f.place(x=28,y=27)
        self.img=PhotoImage(file='A:\python\LPG.png')
        self.l1=Label(self.f,image=self.img,bd=6)
        self.l1.place(x=230,y=10)
        self.l2=Label(self.f,text='New Connection',font=('Times',25,BOLD),fg='orange')
        self.l2.place(x=200,y=140,height=35,width=260)
        self.l3=Label(self.f,text='Enter Name :',font=(1),fg='Maroon')
        self.l4=Label(self.f,text='Enter Username :',font=(1),fg='Maroon')
        self.l5=Label(self.f,text='Enter Password :',font=(1),fg='Maroon')
        self.l6=Label(self.f,text='Enter Address :',font=(1),fg='Maroon')
        self.l3.place(x=140,y=200)
        self.l4.place(x=115,y=240)
        self.l5.place(x=115,y=280)
        self.l6.place(x=130,y=320)
        self.e1=Entry(self.f,font=(1),fg='maroon')
        self.e2=Entry(self.f,font=(1),fg='maroon')
        self.e3=Entry(self.f,font=(1),fg='maroon')
        self.e4=Entry(self.f,font=(1),fg='maroon')
        self.e1.place(x=280,y=201)
        self.e2.place(x=295,y=241)
        self.e3.place(x=295,y=281)
        self.e4.place(x=290,y=321)
        self.b1=Button(self.f,text='SignUp',width=8,font=('Arial',16,BOLD),bd=6,bg='dark orange', command=self.SignUp)
        self.b1.place(x=265,y=365,height=35)
        self.img1=PhotoImage(file='A:\python\lpg7.png')
        self.l7=Label(self.f,image=self.img1)
        self.l7.place(x=175,y=415)
        self.root2.mainloop()
  
  
    def SignUp(self):
        s1=self.e1.get()
        s2=self.e2.get()
        s3=self.e3.get()
        s4=self.e4.get()
        if s1=='':
            messagebox.showinfo('Alert!','Enter Name')
        elif s2=='':
            messagebox.showinfo('Alert!','Enter Username')
        elif s3=='':
            messagebox.showinfo('Alert!','Enter Password')
        elif s4=='':
            messagebox.showinfo('Alert!','Enter Address\nor Else Your LPG Might be missplaced')
        else:
            mydb = mysql.connector.connect(host='localhost',
                                           user='root',
                                           password='1422',
                                           port='3306',
                                           database='lpg')
            mycursor = mydb.cursor()
            sql='INSERT INTO lpg (Name,Username,Password,Address) values(%s,%s,%s,%s)'
            val=(s1,s2,s3,s4)
            mycursor.execute(sql,val)
            mydb.commit()
            messagebox.showinfo('congrachulation','sign Up sucessfull')
            self.root2.destroy()
            y=login()
            y.add_frame()
if __name__=='__main__':
    x=mainwindow()
    x.add_frame()