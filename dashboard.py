import sqlite3
from tkinter import *
from PIL import Image, ImageTk  # Updated usage here
from course import CourseClass
from student import studentClass
from result import resultClass
from report import reportClass
from tkinter import messagebox
import os

class RMS:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1520x800+0+0")
        self.root.config(bg="white")

        #====icon=====
        self.logo_dash = ImageTk.PhotoImage(file="images/logo_p.png")

        #====title====
        title = Label(self.root, text="Student Result Management System", padx=10, compound=LEFT,
                      image=self.logo_dash, font=("goudy old style", 20, "bold"),
                      bg="#033054", fg="white")
        title.place(x=0, y=0, relwidth=1, height=50)

        #====menu====
        M_Frame = LabelFrame(self.root, text="Menus", font=("times new roman", 15, "bold"), bg="white")
        M_Frame.place(x=10, y=70, width=1510, height=80)

        #====menu buttons====
        Button(M_Frame, text="Course", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white",
               cursor="hand2", command=self.add_course).place(x=20, y=5, width=200, height=40)
        Button(M_Frame, text="Student", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white",
               cursor="hand2", command=self.add_student).place(x=270, y=5, width=200, height=40)
        Button(M_Frame, text="Result", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white",
               cursor="hand2", command=self.add_result).place(x=520, y=5, width=200, height=40)
        Button(M_Frame, text="View Student Result", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white",
               cursor="hand2", command=self.add_report).place(x=770, y=5, width=200, height=40)
        Button(M_Frame, text="Logout", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white",
               cursor="hand2", command=self.logout).place(x=1020, y=5, width=200, height=40)
        Button(M_Frame, text="Exit", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white",
               cursor="hand2", command=self.exit).place(x=1280, y=5, width=200, height=40)

        #====content window====
        self.bg_img = Image.open("images/bg.png")
        self.bg_img = self.bg_img.resize((920, 350), Image.Resampling.LANCZOS)  # ✅ Updated here
        self.bg_img = ImageTk.PhotoImage(self.bg_img)
        Label(self.root, image=self.bg_img).place(x=400, y=180, width=920, height=350)

        #====update details====
        self.lbl_course = Label(self.root, text="Total Courses\n[ 0 ]", font=("goudy old style", 20),
                                bd=10, relief=RIDGE, bg="red", fg="white")
        self.lbl_course.place(x=400, y=530, width=300, height=100)

        self.lbl_student = Label(self.root, text="Total Students\n[ 0 ]", font=("goudy old style", 20),
                                 bd=10, relief=RIDGE, bg="green", fg="white")
        self.lbl_student.place(x=710, y=530, width=300, height=100)

        self.lbl_result = Label(self.root, text="Total Results\n[ 0 ]", font=("goudy old style", 20),
                                bd=10, relief=RIDGE, bg="blue", fg="white")
        self.lbl_result.place(x=1020, y=530, width=300, height=100)

        #====footer====
        footer = Label(self.root,
                       text="SRMS:-Student Result Management System\nContact Us For Any Technical Issue: 72528**551 or vaibhav.sharma@gmail.com",
                       font=("goudy old style", 15), bg="#262626", fg="white")
        footer.pack(side=BOTTOM, fill=X)

        self.update_details()

    def update_details(self):
        con = sqlite3.connect(database="RMS.db")
        cur = con.cursor()
        try:
            cur.execute("select * from course")
            cr = cur.fetchall()
            self.lbl_course.config(text=f"Total Courses\n[{str(len(cr))}]")

            cur.execute("select * from student")
            cr = cur.fetchall()
            self.lbl_student.config(text=f"Total Students\n[{str(len(cr))}]")

            cur.execute("select * from result")
            cr = cur.fetchall()
            self.lbl_result.config(text=f"Total Results\n[{str(len(cr))}]")

            self.lbl_course.after(200, self.update_details)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def add_course(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = CourseClass(self.new_win)

    def add_student(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = studentClass(self.new_win)

    def add_result(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = resultClass(self.new_win)

    def add_report(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = reportClass(self.new_win)

    def logout(self):
        op = messagebox.askyesno("Confirm", "Do you really want to logout?", parent=self.root)
        if op:
            self.root.destroy()
            os.system("python login.py")

    def exit(self):
        op = messagebox.askyesno("Confirm", "Do you really want to Exit?", parent=self.root)
        if op:
            self.root.destroy()


if __name__ == "__main__":
    root = Tk()
    obj = RMS(root)
    root.mainloop()
