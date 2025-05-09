from tkinter import *
from PIL import Image, ImageTk  
from tkinter import ttk, messagebox
import sqlite3

class studentClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

        # Title
        title = Label(self.root, text="Manage Student Details", font=("goudy old style", 20, "bold"), bg="#033054", fg="white")
        title.grid(row=0, column=0, columnspan=4, pady=10)

        # Student Labels
        self.create_labels()

        # Variables for student details
        self.create_variables()

        # Entry Fields
        self.create_entries()

        # Buttons
        self.create_buttons()

        # Search Panel
        self.create_search_panel()

        # Content Frame
        self.create_content_frame()

        # Fetch courses
        self.fetch_course()

        # Show all students in the table
        self.show()

    def create_labels(self):
        labels = [
            ("Roll No", 10, 60),
            ("Name", 10, 100),
            ("Email", 10, 140),
            ("Gender", 10, 180),
            ("State", 10, 220),
            ("City", 310, 220),
            ("Pin", 500, 220),
            ("Address", 10, 260),
            ("D.O.B", 360, 60),
            ("Contact", 360, 100),
            ("Admission", 360, 140),
            ("Course", 360, 180)
        ]
        for label in labels:
            Label(self.root, text=label[0], font=("goudy old style", 15, "bold"), bg="white").place(x=label[1], y=label[2])

    def create_variables(self):
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_email = StringVar()
        self.var_dob = StringVar()
        self.var_gender = StringVar()
        self.var_contact = StringVar()
        self.var_course = StringVar()
        self.var_a_date = StringVar()
        self.var_state = StringVar()
        self.var_city = StringVar()
        self.var_pin = StringVar()
        self.var_search = StringVar()

    def create_entries(self):
        self.txt_roll = Entry(self.root, textvariable=self.var_roll, font=("goudy old style", 15, "bold"), bg="lightyellow")
        self.txt_roll.place(x=150, y=60, width=200)

        self.txt_name = Entry(self.root, textvariable=self.var_name, font=("goudy old style", 15, "bold"), bg="lightyellow")
        self.txt_name.place(x=150, y=100, width=200)

        self.txt_email = Entry(self.root, textvariable=self.var_email, font=("goudy old style", 15, "bold"), bg="lightyellow")
        self.txt_email.place(x=150, y=140, width=200)

        self.txt_state = Entry(self.root, textvariable=self.var_state, font=("goudy old style", 15, "bold"), bg="lightyellow")
        self.txt_state.place(x=150, y=220, width=150)

        self.txt_city = Entry(self.root, textvariable=self.var_city, font=("goudy old style", 15, "bold"), bg="lightyellow")
        self.txt_city.place(x=380, y=220, width=100)

        self.txt_pin = Entry(self.root, textvariable=self.var_pin, font=("goudy old style", 15, "bold"), bg="lightyellow")
        self.txt_pin.place(x=560, y=220, width=120)

        self.txt_gender = ttk.Combobox(self.root, textvariable=self.var_gender, values=("Male", "Female", "Other"), font=("goudy old style", 15, "bold"), state="readonly", justify=CENTER)
        self.txt_gender.place(x=150, y=180, width=200)
        self.txt_gender.current(0)

        self.txt_address = Text(self.root, font=("goudy old style", 15, "bold"), bg="lightyellow")
        self.txt_address.place(x=150, y=260, width=530, height=100)

        self.txt_dob = Entry(self.root, textvariable=self.var_dob, font=("goudy old style", 15, "bold"), bg="lightyellow")
        self.txt_dob.place(x=480, y=60, width=200)

        self.txt_contact = Entry(self.root, textvariable=self.var_contact, font=("goudy old style", 15, "bold"), bg="lightyellow")
        self.txt_contact.place(x=480, y=100, width=200)

        self.txt_a_date = Entry(self.root, textvariable=self.var_a_date, font=("goudy old style", 15, "bold"), bg="lightyellow")
        self.txt_a_date.place(x=480, y=140, width=200)

        self.txt_course = ttk.Combobox(self.root, textvariable=self.var_course, values=self.course_list, font=("goudy old style", 15, "bold"), state="readonly", justify=CENTER)
        self.txt_course.place(x=480, y=180, width=200)
        self.txt_course.set("Select")

    def create_buttons(self):
        Button(self.root, text="Save", font=("goudy old style", 15, "bold"), bg="blue", fg="white", cursor="hand2", command=self.add).place(x=150, y=400, width=110, height=40)
        Button(self.root, text="Update", font=("goudy old style", 15, "bold"), bg="green", fg="white", cursor="hand2", command=self.update).place(x=270, y=400, width=110, height=40)
        Button(self.root, text="Delete", font=("goudy old style", 15, "bold"), bg="red", fg="white", cursor="hand2", command=self.delete).place(x=390, y=400, width=110, height=40)
        Button(self.root, text="Clear", font=("goudy old style", 15, "bold"), bg="#607d8b", fg="white", cursor="hand2", command=self.clear).place(x=510, y=400, width=110, height=40)

    def create_search_panel(self):
        Label(self.root, text="Roll No :-", font=("goudy old style", 15, "bold"), bg="white").place(x=720, y=60)
        Entry(self.root, textvariable=self.var_search, font=("goudy old style", 15, "bold"), bg="lightyellow").place(x=870, y=60, width=180)
        Button(self.root, text="Search", font=("goudy old style", 15, "bold"), bg="lightgreen", fg="white", cursor="hand2", command=self.search).place(x=1070, y=60, width=120, height=28)

    def create_content_frame(self):
        self.C_Frame = Frame(self.root, bd=2, relief=RIDGE)
        self.C_Frame.place(x=720, y=100, width=470, height=340)

        Scrolly = Scrollbar(self.C_Frame, orient=VERTICAL)
        Scrollx = Scrollbar(self.C_Frame, orient=HORIZONTAL)

        self.CourseTable = ttk.Treeview(self.C_Frame, columns=("roll", "name", "email", "gender", "dob", "contact", "admission", "course", "state", "city", "pin", "address"),
                                        xscrollcommand=Scrollx.set, yscrollcommand=Scrolly.set)

        Scrollx.pack(side=BOTTOM, fill=X)
        Scrolly.pack(side=RIGHT, fill=Y)

        Scrollx.config(command=self.CourseTable.xview)
        Scrolly.config(command=self.CourseTable.yview)

        self.CourseTable.heading("roll", text="Roll No")
        self.CourseTable.heading("name", text="Name")
        self.CourseTable.heading("email", text="Email")
        self.CourseTable.heading("gender", text="Gender")
        self.CourseTable.heading("dob", text="D.O.B")
        self.CourseTable.heading("contact", text="Contact")
        self.CourseTable.heading("admission", text="Admission")
        self.CourseTable.heading("course", text="Course")
        self.CourseTable.heading("state", text="State")
        self.CourseTable.heading("city", text="City")
        self.CourseTable.heading("pin", text="Pin")
        self.CourseTable.heading("address", text="Address")

        self.CourseTable["show"] = "headings"

        self.CourseTable.column("roll", width=100)
        self.CourseTable.column("name", width=100)
        self.CourseTable.column("email", width=100)
        self.CourseTable.column("gender", width=100)
        self.CourseTable.column("dob", width=100)
        self.CourseTable.column("contact", width=100)
        self.CourseTable.column("admission", width=100)
        self.CourseTable.column("course", width=100)
        self.CourseTable.column("state", width=100)
        self.CourseTable.column("city", width=100)
        self.CourseTable.column("pin", width=100)
        self.CourseTable.column("address", width=200)

        self.CourseTable.pack(fill=BOTH, expand=1)
        self.CourseTable.bind("<ButtonRelease-1>", self.get_data)

    def connect_db(self):
        return sqlite3.connect(database="rms.db")

    def clear(self):
        self.show()
        self.var_roll.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("")
        self.var_dob.set("")
        self.var_contact.set("")
        self.var_a_date.set("")
        self.var_course.set("")
        self.var_state.set("")
        self.var_city.set("")
        self.var_pin.set("")
        self.txt_address.delete("1.0", END)
        self.txt_roll.config(state=NORMAL)
        self.var_search.set("")

    def delete(self):
        con = self.connect_db()
        cur = con.cursor()
        try:
            if self.var_roll.get() == "":
                messagebox.showerror("Error", "Roll No. should be required", parent=self.root)
            else:
                cur.execute("select * from student where roll=?", (self.var_roll.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Please select student from the list first", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)
                    if op == TRUE:
                        cur.execute("delete from student where roll=?", (self.var_roll.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Student record deleted successfully", parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            con.close()
def update(self):
    con = self.connect_db()
    cur = con.cursor()
    try:
        if self.var_roll.get() == "" or self.var_name.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            cur.execute("select * from student where roll=?", (self.var_roll.get(),))
            row = cur.fetchone()
            if row is None:
                messagebox.showerror("Error", "Please select student from the list first", parent=self.root)
            else:
                cur.execute("""update student set name=?, email=?, gender=?, dob=?, contact=?, admission=?, course=?, state=?, city=?, pin=?, address=? where roll=?""",
                            (self.var_name.get(), self.var_email.get(), self.var_gender.get(), self.var_dob.get(), self.var_contact.get(),
                             self.var_a_date.get(), self.var_course.get(), self.var_state.get(), self.var_city.get(), self.var_pin.get(),
                             self.txt_address.get("1.0", END), self.var_roll.get()))
                con.commit()
                messagebox.showinfo("Update", "Student record updated successfully", parent=self.root)
                self.clear()
    except Exception as ex:
        messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
    finally:
        con.close()
def show(self):
    con = self.connect_db()
    cur = con.cursor()
    try:
        cur.execute("select * from student")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert("", END, values=row)
            con.commit()
    except Exception as ex:
        messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
    finally:
        con.close()

def search(self):
    con = self.connect_db()
    cur = con.cursor()
    try:
        cur.execute("select * from student where roll=?", (self.var_search.get(),))
        row = cur.fetchone()
        if row:
            self.var_roll.set(row[0])
            self.var_name.set(row[1])
            self.var_email.set(row[2])
            self.var_gender.set(row[3])
            self.var_dob.set(row[4])
            self.var_contact.set(row[5])
            self.var_a_date.set(row[6])
            self.var_course.set(row[7])
            self.var_state.set(row[8])
            self.var_city.set(row[9])
            self.var_pin.set(row[10])
            self.txt_address.delete("1.0", END)
            self.txt_address.insert("1.0", row[11])
        else:
            messagebox.showerror("Error", "No record found", parent=self.root)
    except Exception as ex:
        messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
    finally:
        con.close()

def fetch_course(self):
    con = self.connect_db()
    cur = con.cursor()
    try:
        cur.execute("select * from course")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.course_list = [row[1] for row in rows]
    except Exception as ex:
        messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
    finally:
        con.close()

def add(self):
    con = self.connect_db()
    cur = con.cursor()
    try:
        if self.var_roll.get() == "" or self.var_name.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            cur.execute("select * from student where roll=?", (self.var_roll.get(),))
            row = cur.fetchone()
            if row:
                messagebox.showerror("Error", "Student already exists", parent=self.root)
            else:
                cur.execute("""insert into student(roll, name, email, gender, dob, contact, admission, course, state, city, pin, address)
                               values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                             (self.var_roll.get(), self.var_name.get(), self.var_email.get(), self.var_gender.get(),
                              self.var_dob.get(), self.var_contact.get(), self.var_a_date.get(), self.var_course.get(),
                              self.var_state.get(), self.var_city.get(), self.var_pin.get(), self.txt_address.get("1.0", END)))
                con.commit()
                messagebox.showinfo("Success", "Student added successfully", parent=self.root)
                self.clear()
    except Exception as ex:
        messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
    finally:
        con.close()

def get_data(self, ev):
    f = self.CourseTable.focus()
    content = self.CourseTable.item(f)
    row = content["values"]
    self.var_roll.set(row[0])
    self.var_name.set(row[1])
    self.var_email.set(row[2])
    self.var_gender.set(row[3])
    self.var_dob.set(row[4])
    self.var_contact.set(row[5])
    self.var_a_date.set(row[6])
    self.var_course.set(row[7])
    self.var_state.set(row[8])
    self.var_city.set(row[9])
    self.var_pin.set(row[10])
    self.txt_address.delete("1.0", END)
    self.txt_address.insert("1.0", row[11])

if __name__ == "__main__":
    root = Tk()
    obj = studentClass(root)
    root.mainloop()
