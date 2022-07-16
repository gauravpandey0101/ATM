from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter import PhotoImage

object=Tk()
object.title("Home_Page")
object.geometry("1300x700")
object.iconbitmap("Designcontest-Ecommerce-Business-Atm-money.ico")
object.configure(bg="blue")

def Submit():
    entry=entry1_1_1.get()
    entry1=entry1_2_2.get()
    import mysql.connector as atm
    object=atm.connect(host='localhost',user='root',password='rekhagaurav123@',database='atm')
    print("Connect Success")
    object1=object.cursor()
    object1.execute('create table if not exists atm (username varchar(20),password varchar(20),cash integer(10))')
    #object1.execute('insert into atm(cash) values(15)')
    object1.execute('select * from atm where username= %s and password= %s',(entry,entry1))
    result=object1.fetchone()
    if result:
        messagebox.showinfo("","login Success !!!!")
        print('DBMS SUCCESS')
        def balance():
            username="gaurav123";
            object1.execute('select * from atm where username = %s',(username))
            result=object1.fetchone()
            if result:
                messagebox.showinfo("Success")
        def cash():
            pass
        def exit():
            pass

        button2_1=Button(f2,text="CHECK BALANCE",command=balance,bg="black",fg="yellow",bd=5,width=20,font="arial 12 bold").grid(row=2,column=0,padx=10)
        button2_2=Button(f2,text="CASH_WITHDRAW",bg="black",fg="yellow",bd=5,width=20,font="arial 12 bold").grid(row=3,column=0,padx=10)
        button2_3=Button(f2,text=" EXIT ",bg="black",fg="yellow",bd=5,width=20,font="arial 12 bold").grid(row=4,column=0,padx=10)
    else:
        messagebox.showwarning("","Something Wrong..Try again")
    
    object.commit()
    print("Connect Success")
def Clear():
    entry1_1_1.set("")
    entry1_2_2.set("")
    
f1=Frame(object,bg="grey",borderwidth=5,relief=SUNKEN)
f1.pack(side=LEFT,fill=Y)

label1_0=Label(f1,text="SBI ATM",fg="gold",bg="blue",width=17,font="arial 15 bold",bd=5,relief=SUNKEN)
label1_0.pack()
photo = ImageTk.PhotoImage(file="Designcontest-Ecommerce-Business-Atm-money.ico")
label1_1=Label(f1,image=photo,width="205",height="180")
label1_1.pack(padx=1,pady=1)
label1_2=Label(f1,text="WELCOME_OFFICIAL_ACCOUNT",font="arial 10 bold",bd=3,bg="blue",fg="gold",relief=SUNKEN)
label1_2.pack()
Label(f1,text="\n",bg="grey").pack()
label1_3=Label(f1,text="Account_Holder",font="arial 10 bold",bd=5,bg="blue",fg="gold",relief=SUNKEN)
label1_3.pack()
entry1_1_1=StringVar()
entry1_1=Entry(f1,bd=3,textvariable=entry1_1_1).pack()
label1_4=Label(f1,text="Password",font="arial 10 bold",bd=5,bg="blue",fg="gold",relief=SUNKEN)
label1_4.pack()
entry1_2_2=StringVar()
entry1_2=Entry(f1,bd=3,textvariable=entry1_2_2).pack()
Label(f1,text="\n",bg="grey").pack()
button1_1=Button(f1,text="SUBMIT",command=Submit,bd=5,bg="black",fg="gold").pack()
button1_1=Button(f1,text="CLEAR",command=Clear,bd=5,bg="black",fg="gold").pack()
Label(f1,text="\n",bg="grey").pack()
button1_2=Button(f1,text="I CAN HELP YOU ?",bd=3,bg="black",fg="gold",relief=SUNKEN).pack()

f2=Frame(object,bg="pink",borderwidth=5,relief=SUNKEN)
f2.pack(fill=X)
label2_1=Label(f2,text="SELECT YOUR CHOICE GIVEN BELLOW STATEMENT",font="arial 15 bold",height="2")
label2_1.grid(row=0,column=0,padx=50)
pic=ImageTk.PhotoImage(file="Graphicloads-Flat-Finance-Atm.ico")
label2_2=Label(f2,image=pic,width="200",height="200").grid(row=0,column=6,padx=30)


object.mainloop()