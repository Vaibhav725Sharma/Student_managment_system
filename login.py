from tkinter import *
from PIL import Image,ImageTk 
import sqlite3
from tkinter import ttk,messagebox
import os


class Login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login Window")
        self.root.geometry("1500x800+0+0")
        self.root.config(bg="white")
       
       
        #==Background==
        self.bg=ImageTk.PhotoImage(file="images\\img3.jpg")
        bg=Label(self.root,image=self.bg).place(x=0,y=10,relwidth=1,relheight=1)


        #==Register Frame==
        frame2=Frame(self.root,bg="white")
        frame2.place(x=480,y=180,width=700,height=500)

        title=Label(frame2,text="LOGIN HERE",font=("ALGERIAN",28,"bold"),bg="white",fg="sky blue").place(x=250,y=40)
        
        email=Label(frame2,text="EMAIL ADDRESS",font=("ALGERIAN",20,"bold"),bg="white").place(x=150,y=100)
        self.txt_email=Entry(frame2,font=("times new roman",15),bg="light grey")
        self.txt_email.place(x=150,y=150,width=350,height=35)

        pass_=Label(frame2,text="PASSWORD",font=("ALGERIAN",20,"bold"),bg="white").place(x=150,y=200)
        self.txt_pass_=Entry(frame2,font=("times new roman",15),bg="light grey")
        self.txt_pass_.place(x=150,y=250,width=350,height=35)

        btn_reg=Button(frame2,text="Register New Account?",command=self.register_window,font=("times new roman",20),bg="white",bd=0,fg="#B00857",cursor="hand2").place(x=150,y=300)
        
        btn_forget=Button(frame2,text="Forget Password?",command=self.forget_password_window,font=("times new roman",20),bg="white",bd=0,fg="#B00857",cursor="hand2").place(x=150,y=350)

        btn_login=Button(frame2,text="LOGIN",command=self.login,font=("ALGERIAN",20,"bold"),bg="green",fg="white",cursor="hand2").place(x=270,y=400,width=200,height=45)
    

    def reset(self):
        self.cmb_quest.current(0)
        self.txt_new_password.delete(0,END)
        self.txt_answer.delete(0,END)
        self.txt_pass_.delete(0,END)
        self.txt_email.delete(0,END)
        



    def forget_password(self):
        if self.cmb_quest.get()=="Select" or self.txt_answer.get()=="" or self.txt_new_password.get()=="":
            messagebox.showerror("Error","All Fields are Required",parent=self.root2)
        else:
            try:
                con=sqlite3.connect(database="rms.db")
                cur=con.cursor()
                cur.execute("select * from emp2 where email=? and question=? and answer=?" ,(self.txt_email.get(),self.txt_pass_.get(),self.txt_answer.get()))
                row=cur.fetchone()
                
                if row==None:
                    messagebox.showerror("Error","Please Select The Correct Security Question / Enter the Answer",parent=self.root2) 
                else:
                    cur.execute("update emp2 set password=? where email=?",(self.txt_email.get(),self.txt_new_password.get()))
                    row=cur.fetchone()
                    con.commit()
                    con.close()
                    messagebox.showerror("Sussess","Your Password has been Reset Please login with New Password",parent=self.root2)
                    
                    self.reset()
                    self.root2.destroy()
                     

                     
                
                
            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)


    
    
    
    #====Forget Password===
    def forget_password_window(self):
        if self.txt_email.get()=="":
            messagebox.showerror("Error","Please Enter The Email Address And Password",parent=self.root)
        else:
            try:
                con=sqlite3.connect(database="rms.db")
                cur=con.cursor()
                cur.execute("select * from emp2 where email=?",(self.txt_email.get(),))
                row=cur.fetchone()
                
                if row==None:
                    messagebox.showerror("Error","Please Enter The Valid Email Address to Reset Your Password",parent=self.root) 
                else:
                    con.close()
                    self.root2=Toplevel()
                    self.root2.title("Forget Password")
                    self.root2.geometry("400x400+495+150")
                    self.root2.config(bg="white")
                    self.root2.focus_force()
                    self.root2.grab_set()

                    t=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),bg="white",fg="#B00857").place(x=0,y=10,relwidth=1)
        

                    question=Label(self.root2,text="Security Question",font=("times new roman",15,"bold")).place(x=50,y=70)

                    self.cmb_quest=ttk.Combobox(self.root2,font=("times new roman",13),state='readonly',justify=CENTER)
                    self.cmb_quest['values']=("Select","Your First Teacher Name","Your Birth Place","Your best friend Name")
                    self.cmb_quest.place(x=50,y=100,width=250)
                    self.cmb_quest.current(0)

                    answer=Label(self.root2,text="Answer",font=("times new roman",15,"bold")).place(x=50,y=150)
                    self.txt_answer=Entry(self.root2,font=("times new roman",15),bg="light grey")
                    self.txt_answer.place(x=50,y=180,width=250)

                    new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold")).place(x=50,y=230)
                    self.txt_new_password=Entry(self.root2,font=("times new roman",15),bg="light grey")
                    self.txt_new_password.place(x=50,y=260,width=250)


                    btn_change_password=Button(self.root2,text="Reset Password",command=self.forget_password,bg="green",fg="white",font=("times new roman",20,"bold")).place(x=85,y=310)
                
                con.close()
                  

            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)


    def register_window(self):
        self.root.destroy()
        import register
    
  
    
    def login(self):
        if self.txt_email.get()=="" or self.txt_pass_.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)

        else:
            try:
                con=sqlite3.connect(database="rms.db")
                cur=con.cursor()
                cur.execute("select * from emp2 where email=? and password=?",(self.txt_email.get(),self.txt_pass_.get()))
                row=cur.fetchone()
                
                if row==None:
                    messagebox.showerror("Error","Invalid Username And Password",parent=self.root)
                  
                else:
                    messagebox.showinfo("Success",f"Welcome : {self.txt_email.get()}",parent=self.root)
                    self.root.destroy()
                    os.system("python dashboard.py")
                con.close()
                
                  
            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)


root=Tk()
obj=Login_window(root)
root.mainloop()


