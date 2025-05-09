from tkinter import *
from PIL import Image,ImageTk 
from tkinter import ttk,messagebox
# import pymysql
import sqlite3
import os


class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration Window")
        self.root.geometry("1500x800+0+0")
        self.root.config(bg="black")
       
       
        #==left image==
        self.bg=ImageTk.PhotoImage(file="images\\img3.jpg")
        bg=Label(self.root,image=self.bg).place(x=0,y=10,relwidth=1,relheight=1)


        #==Register Frame==
        frame1=Frame(self.root,bg="white")
        frame1.place(x=480,y=180,width=700,height=500)

        title=Label(frame1,text="REGISTER HERE",font=("ALGERIAN",28,"bold"),bg="Green").place(x=50,y=30)
        #=====Row 1
    
        f_name=Label(frame1,text="First Name",font=("times new roman",15,"bold")).place(x=50,y=100)
        self.txt_fname=Entry(frame1,font=("times new roman",15),bg="light grey",)
        self.txt_fname.place(x=50,y=130,width=250)

        
        l_name=Label(frame1,text="Last Name",font=("times new roman",15,"bold")).place(x=370,y=100)
        self.txt_lname=Entry(frame1,font=("times new roman",15),bg="light grey")
        self.txt_lname.place(x=370,y=130,width=250)

        #===contact & Email===Row 2
        contact=Label(frame1,text="Contact No.",font=("times new roman",15,"bold")).place(x=50,y=170)
        self.txt_contact=Entry(frame1,font=("times new roman",15),bg="light grey")
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame1,text="Email",font=("times new roman",15,"bold")).place(x=370,y=170)
        self.txt_email=Entry(frame1,font=("times new roman",15),bg="light grey")
        self.txt_email.place(x=370,y=200,width=250)

        #===security ===Row 3
        question=Label(frame1,text="Security Question",font=("times new roman",15,"bold")).place(x=50,y=240)

        self.cmb_quest=ttk.Combobox(frame1,font=("times new roman",13),state='readonly',justify=CENTER)
        self.cmb_quest['values']=("Select","Your First Teacher Name","Your Birth Place","Your best friend Name")
        self.cmb_quest.place(x=50,y=270,width=250)
        self.cmb_quest.current(0)

        answer=Label(frame1,text="Answer",font=("times new roman",15,"bold")).place(x=370,y=240)
        self.txt_answer=Entry(frame1,font=("times new roman",15),bg="light grey")
        self.txt_answer.place(x=370,y=270,width=250)

        #=====Password====Row 4

        Pswd=Label(frame1,text="Password",font=("times new roman",15,"bold")).place(x=50,y=310)
        self.txt_pswd=Entry(frame1,font=("times new roman",15),bg="light grey")
        self.txt_pswd.place(x=50,y=340,width=250)

        
        cpswd=Label(frame1,text="Confirm Password",font=("times new roman",15,"bold")).place(x=370,y=310)
        self.txt_cpswd=Entry(frame1,font=("times new roman",15),bg="light grey")
        self.txt_cpswd.place(x=370,y=340,width=250)


        #===Terms and condition===
        self.var_chk=IntVar()
        chk=Checkbutton(frame1,text="I Agree the terms and Condition",variable=self.var_chk,onvalue=1,offvalue=0,font=("times new roman",12),bg="light grey").place(x=50,y=380)

        #===Button====

        btn_register=Button(frame1,text="Register Now",bd=2,cursor="hand2",command=self.register_data,font=("ALGERIAN",20),bg="Green").place(x=50,y=420)

        btn_login=Button(frame1,text="Sign In",bd=2,cursor="hand2",command=self.login_window,font=("ALGERIAN",20),bg="Sky blue").place(x=370,y=420)
    
    def login_window(self):
        self.root.destroy()
        os.system("python login.py")



    def register_data(self):
        if self.txt_fname.get()=="" or self.txt_contact.get()=="" or self.txt_email.get()=="" or self.cmb_quest.get()=="Select" or self.txt_answer.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        elif self.txt_pswd.get()!=self.txt_cpswd.get():
            messagebox.showerror("Error","Password And Confirm Password should be same",parent=self.root)
        elif self.var_chk.get()==0:
             messagebox.showerror("Error","Please Agree Our Terms And Condition",parent=self.root)

        else:
            try:
                con=sqlite3.connect(database="rms.db")
                cur=con.cursor()
                cur.execute("select * from emp2 where email =?",(self.txt_email.get(),))
                row=cur.fetchone()
                #print (row)
                if row!=None:
                    messagebox.showerror("Error","User already Exist ,Please try with another email",parent=self.root)
                else:
                    cur.execute("insert into emp2(f_name,l_name,contact,email,question,answer,password) values(?,?,?,?,?,?,?)",
                             (self.txt_fname.get(),
                             self.txt_lname.get(),
                             self.txt_contact.get(),
                             self.txt_email.get(),
                             self.cmb_quest.get(),
                             self.txt_answer.get(),
                             self.txt_pswd.get()
                             ))
                
                con.commit()
                con.close()
                messagebox.showinfo("Success","Register Successful",parent=self.root)
                
                self.login_window()



            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)

root=Tk()
obj=Register(root)
root.mainloop()
