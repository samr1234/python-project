from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
import datetime
from tkcalendar import *
from PIL import Image,ImageTk
# splash_root=Tk()
# splash_root.title("new splash")
# splash_root.geometry("300x200")

root=Tk()
root.geometry("1370x740")
# root.wm_iconbitmap("3.ico")
root.title("Attendance form ")

# -------------------------------------------------------------------------------------------------------------------------
#  TODO FIRST PAGE 

def show1():
    f2=Frame()
    f2.place(x=0,y=0,width=1370,height=740)
    global bg
    global bg_image
    global bg_image1
    global bg1
    bg=ImageTk.PhotoImage(file="back1.jpg")
    bg_image=Label(f2,image=bg).place(x=0,y=0,width=1370,height=740)
    Frame_login1=Frame(f2,bg="white")
    Frame_login1.place(x=300,y=150,height=440,width=700)
    bg1=ImageTk.PhotoImage(file="green1.png")
    bg_image1=Label(Frame_login1,image=bg1).place(x=0,y=0,relwidth=1,relheight=1)
    f5=Frame(f2,borderwidth=4,relief=SUNKEN)
    f5.pack(fill=X)
    label_1=Label(f5,text=" STUDENT PANEL",font="HELSINKI  15 bold",fg="blue")
    label_1.pack(padx=40)
    button=Button(f2,text="<-",borderwidth=5,command=show,fg="purple")
    button.place(x=3,y=3)


    #TODO BUTTONS OF ROOT

    b2=Button(Frame_login1,text="MARK ATTENDANCE",padx=120,font=("Goudy old style",20,"bold"),fg="white",bg="#F38809",activebackgroun="#F38809",command=student_panel)
    b2.place(x=155,y=90,width=370)
    b3=Button(Frame_login1,text=" TASK ASSIGNED ",padx=100,font=("Goudy old style",20,"bold"),fg="white",bg="#F38809",activebackgroun="#F38809",command=task_assigned)
    b3.place(x=155,y=250,width=370)
     #   for students to check assigned task
def task_assigned():
        
    global bg55
    global bg_image55
    global bg556
    global bg_image556
    global bg557
    global bg_image557
    # frame=Frame()
    # frame.place(x=0,y=0,width=1370,height=740)
    bg55=ImageTk.PhotoImage(file="st3.jpg")
    bg_image55=Label(image=bg55).place(x=0,y=0,width=1370,height=740)
    f5=Frame(bg_image55,borderwidth=4,relief=SUNKEN)
    f5.place(x=0,y=0,width=1370,height=45)
    label=Label(f5,text=" TASKS ASSIGNED ",font="HELSINKI  15 bold",fg="ORANGE")
    label.place(x=530,y=5)
    bg557=ImageTk.PhotoImage(file="fram.png")
    bg_image557=Label(image=bg557).place(x=245,y=100)
    frame1=Frame()
    frame1.place(x=300,y=150,height=540,width=700)

    bg556=ImageTk.PhotoImage(file="questi1.jpg")
    bg_image556=Label(frame1,image=bg556).place(x=0,y=0,height=540,width=700)
    # ------------------------
    b3=Button(frame1,text="MATHEMATICS",padx=100,font=("Goudy old style",15,"bold"),fg="white",bg="#AD25C5",command=question1)
    b3.place(x=210,y=50,width=240,height=30)
    b4=Button(frame1,text="SCIENCE",padx=120,font=("Goudy old style",15,"bold"),fg="white",bg="#AD25C5",command=question2)
    b4.place(x=210,y=110,width=240,height=30)
    b4=Button(frame1,text="ENGLISH",padx=120,font=("Goudy old style",15,"bold"),fg="white",bg="#AD25C5",command=question3)
    b4.place(x=210,y=170,width=240,height=30)
    b4=Button(frame1,text="CHEMISTRY",padx=120,font=("Goudy old style",15,"bold"),fg="white",bg="#AD25C5",command=question4)
    b4.place(x=210,y=230,width=240,height=30)
    b4=Button(frame1,text="PROGRAMMING",padx=120,font=("Goudy old style",15,"bold"),fg="white",bg="#AD25C5",command=question5)
    b4.place(x=210,y=290,width=240,height=30)
    b4=Button(frame1,text="ENVIRONMENT",padx=120,font=("Goudy old style",15,"bold"),fg="white",bg="#AD25C5",command=question6)
    b4.place(x=210,y=350,width=240,height=30)
  
    button=Button(bg_image55,text="<-",command=show1,borderwidth=5,fg="black",bg="white")
    button.place(x=10,y=10)
    
def question1():
    global listbox1
    frame=Frame(bg="grey")
    frame.place(x=160,y=200,height=350,width=950)    
    listbox1=Listbox(frame)
    listbox1.place(x=12,y=12,width=925,height=325)
    # listbox1.insert(2,"QUESTION ")
    #listbox1.delete(1,END)
    button=Button(listbox1,text="TASK ",command=get_question1,font="HELSINKI  15 bold",fg="white",bg="#5189C8")
    button.place(x=750,y=270)
    button=Button(listbox1,text="CLOSE",command=task_assigned,fg="white",bg="#5189C8")
    button.place(x=840,y=15)
    
def question2():
    global listbox2
    frame=Frame(bg="grey")
    frame.place(x=160,y=200,height=350,width=950)    
    listbox2=Listbox(frame)
    listbox2.place(x=12,y=12,width=925,height=325)
    button=Button(listbox2,text="TASK ",command=get_question2,font="HELSINKI  15 bold",fg="white",bg="#5189C8")
    button.place(x=750,y=270)
    button=Button(listbox2,text="CLOSE",command=task_assigned,fg="white",bg="#5189C8")
    button.place(x=840,y=15)
    

def question3():
    global listbox3
    frame=Frame(bg="grey")
    frame.place(x=160,y=200,height=350,width=950)    
    listbox3=Listbox(frame)
    listbox3.place(x=12,y=12,width=925,height=325)
    button=Button(listbox3,text="TASK ",command=get_question3,font="HELSINKI  15 bold",fg="white",bg="#5189C8")
    button.place(x=750,y=270)
    button=Button(listbox3,text="CLOSE",command=task_assigned,fg="white",bg="#5189C8")
    button.place(x=840,y=15)
    

def question4():
    global listbox4
    frame=Frame(bg="grey")
    frame.place(x=160,y=200,height=350,width=950)    
    listbox4=Listbox(frame)
    listbox4.place(x=12,y=12,width=925,height=325)
    button=Button(listbox4,text="TASK ",command=get_question4,font="HELSINKI  15 bold",fg="white",bg="#5189C8")
    button.place(x=750,y=270)
    button=Button(listbox4,text="CLOSE",command=task_assigned,fg="white",bg="#5189C8")
    button.place(x=840,y=15)
    
def question5():
    global listbox5
    frame=Frame(bg="grey")
    frame.place(x=160,y=200,height=350,width=950)    
    listbox5=Listbox(frame)
    listbox5.place(x=12,y=12,width=925,height=325)
    button=Button(listbox5,text="TASK ",command=get_question5,font="HELSINKI  15 bold",fg="white",bg="#5189C8")
    button.place(x=750,y=270)
    button=Button(listbox5,text="CLOSE",command=task_assigned,fg="white",bg="#5189C8")
    button.place(x=840,y=15)
    
def question6():
    global listbox6
    frame=Frame(bg="grey")
    frame.place(x=160,y=200,height=350,width=950)    
    listbox6=Listbox(frame)
    listbox6.place(x=12,y=12,width=925,height=325)  
    button=Button(listbox6,text="TASK ",command=get_question6,font="HELSINKI  15 bold",fg="white",bg="#5189C8")
    button.place(x=750,y=270)
    button=Button(listbox6,text="CLOSE",command=task_assigned,fg="white",bg="#5189C8")
    button.place(x=840,y=15)
    

def get_question1():
    
   
    # studentidvalue=StringVar()
    con=mysql.connect(host="localhost",user="root",password="9463617001",database="attendance_sheet") 
    cursor=con.cursor()
    cursor.execute("select * from task_assign1")
    rows=cursor.fetchall()
   
    for row in rows:
        insertdata="GIVEN BY:  " +str(row[0])+ '        POSTED ON   '+str(row[2])
        insertdata1="TASK:   "+ str(row[1])
        insertdata2=" "
        listbox1.insert(END, insertdata,insertdata1,insertdata2)
       
    con.close()
def get_question2():
    
   
    # studentidvalue=StringVar()
    con=mysql.connect(host="localhost",user="root",password="9463617001",database="attendance_sheet") 
    cursor=con.cursor()
    cursor.execute("select * from task_assign2")
    rows=cursor.fetchall()
   
    for row in rows:
        insertdata="GIVEN BY:  " +str(row[0])+ '        POSTED ON   '+str(row[2])
        insertdata1="TASK:   "+ str(row[1])
        insertdata2=" "
        listbox2.insert(END, insertdata,insertdata1,insertdata2)
       
    con.close()
def get_question3():
    
   
    # studentidvalue=StringVar()
    con=mysql.connect(host="localhost",user="root",password="9463617001",database="attendance_sheet") 
    cursor=con.cursor()
    cursor.execute("select * from task_assign3")
    rows=cursor.fetchall()
   
    for row in rows:
        insertdata="GIVEN BY:  " +str(row[0])+ '        POSTED ON   '+str(row[2])
        insertdata1="TASK:   "+ str(row[1])
        insertdata2=" "
        listbox3.insert(END, insertdata,insertdata1,insertdata2)
       
    con.close()
def get_question4():
    
   
    # studentidvalue=StringVar()
    con=mysql.connect(host="localhost",user="root",password="9463617001",database="attendance_sheet") 
    cursor=con.cursor()
    cursor.execute("select * from task_assign4")
    rows=cursor.fetchall()
   
    for row in rows:
        insertdata="GIVEN BY:  " +str(row[0])+ '        POSTED ON   '+str(row[2])
        insertdata1="TASK:   "+ str(row[1])
        insertdata2=" "
        listbox4.insert(END, insertdata,insertdata1,insertdata2)
       
    con.close()
def get_question5():
    
   
    # studentidvalue=StringVar()
    con=mysql.connect(host="localhost",user="root",password="9463617001",database="attendance_sheet") 
    cursor=con.cursor()
    cursor.execute("select * from task_assign5")
    rows=cursor.fetchall()
   
    for row in rows:
        
        insertdata="GIVEN BY:  " +str(row[0])+ '        POSTED ON   '+str(row[2])
        insertdata1="TASK:   "+ str(row[1])
        insertdata2=" "
        listbox5.insert(END, insertdata,insertdata1,insertdata2)
       
    con.close()
def get_question6():
    
   
    # studentidvalue=StringVar()
    con=mysql.connect(host="localhost",user="root",password="9463617001",database="attendance_sheet") 
    cursor=con.cursor()
    cursor.execute("select * from task_assign6")
    rows=cursor.fetchall()
   
    for row in rows:
        
        insertdata="GIVEN BY:  " +str(row[0])+ '        POSTED ON   '+str(row[2])
        insertdata1="TASK:   "+ str(row[1])
        insertdata2=" "
        listbox6.insert(END, insertdata,insertdata1,insertdata2)
    con.close()
                   
    #---------------------------------------------------------   
def show2():
    try:    
        f2=Frame()
        f2.place(x=0,y=0,width=1370,height=740)
        global bg
        global bg_image
        global bg_image1
        global bg1
        bg=ImageTk.PhotoImage(file="back1.jpg")
        bg_image=Label(f2,image=bg).place(x=0,y=0,width=1370,height=740)
        Frame_login1=Frame(f2,bg="white")
        Frame_login1.place(x=300,y=150,height=440,width=700)
        bg1=ImageTk.PhotoImage(file="green1.png")
        bg_image1=Label(Frame_login1,image=bg1).place(x=0,y=0,relwidth=1,relheight=1)
        f5=Frame(f2,bg="grey",borderwidth=8,relief=SUNKEN)
        f5.pack(fill=X)
        label_1=Label(f5,text="ADMIN PANEL",font="HELSINKI  15 bold",fg="purple")
        label_1.pack(padx=40)
        button=Button(f2,text="<-",borderwidth=5,command=show,fg="purple")
        button.place(x=10,y=10)


        #TODO BUTTONS OF ROOT

        # b1=Button(Frame_login1,text="STUDENT PANEL",padx=110,font=("Goudy old style",15,"bold"),fg="white",bg="#5189C8",activebackground="#5189C8",command=student_panel)
        # b1.pack(pady=180)
        b2=Button(Frame_login1,text="ATTENDANCE RECORD",padx=120,font=("Goudy old style",20,"bold"),fg="white",bg="#F38809",activebackgroun="purple",command=admin)
        b2.place(x=147,y=90,width=380)
        b3=Button(Frame_login1,text="POST A QUESTION",padx=100,font=("Goudy old style",20,"bold"),fg="white",bg="#F38809",activebackgroun="purple",command=task)
        b3.place(x=147,y=250,width=380)
    except Exception as e:
        print(e)    
# -------------------------------------------------------------------------------------------------------------
#  TODO STUDENT PANEL 
def student_panel():
    global bg
    global bg_image
    f3=Frame()
    f3.place(x=0,y=0,width=1370,height=740) 
    global bg500
    global bg_image500
   
    bg500=ImageTk.PhotoImage(file="stud.jpg")
    bg_image500=Label(f3,image=bg500).place(x=0,y=0,width=1370,height=740)
    # bg=ImageTk.PhotoImage(file="bgphoto.jpg")
    # bg_image=Label(f3,image=bg).place(x=0,y=0,width=1370,height=740)
    # f5=Frame(f3,bg="white",borderwidth=8,relief=SUNKEN)
    # f5.pack(fill=X)
    f5=Frame(bg_image500,borderwidth=4,relief=SUNKEN)
    f5.place(x=0,y=0,width=1370,height=45)
    label=Label(f5,text=" ATTENDANCE ",font="HELSINKI  15 bold",fg="ORANGE")
    label.place(x=530,y=5)
    Frame_login2=Frame(f3,bg="green")
    Frame_login2.place(x=300,y=150,height=540,width=700)
    bg=ImageTk.PhotoImage(file="school.jpg")
    bg_image=Label(Frame_login2,image=bg).place(x=0,y=0,relwidth=1,relheight=1)
   

    b3=Button(Frame_login2,text="MATHEMATICS ",padx=100,font=("Goudy old style",15,"bold"),fg="white",bg="#5189C8",command=subject1)
    b3.place(x=195,y=130,width=300,height=30)
    b4=Button(Frame_login2,text="SCIENCE",padx=120,font=("Goudy old style",15,"bold"),fg="white",bg="#5189C8",command=subject2)
    b4.place(x=195,y=180,width=300,height=30)
    b4=Button(Frame_login2,text="ENGLISH",padx=120,font=("Goudy old style",15,"bold"),fg="white",bg="#5189C8",command=subject3)
    b4.place(x=195,y=230,width=300,height=30)
    b4=Button(Frame_login2,text="CHEMISTRY",padx=120,font=("Goudy old style",15,"bold"),fg="white",bg="#5189C8",command=subject4)
    b4.place(x=195,y=280,width=300,height=30)
    b4=Button(Frame_login2,text="PROGRAMMING",padx=120,font=("Goudy old style",15,"bold"),fg="white",bg="#5189C8",command=subject5)
    b4.place(x=195,y=330,width=300,height=30)
    b5=Button(Frame_login2,text="ENVIRONMENT",padx=120,font=("Goudy old style",15,"bold"),fg="white",bg="#5189C8",command=subject6)
    b5.place(x=195,y=380,width=300,height=30)

    button=Button(f5,text="<-",borderwidth=5,command=show1,fg="purple")
    button.place(x=0,y=0)

#  -----------------------------------------------------------------------   
    # for marking attendence
def subject1():
    global namevalue
    global studentidvalue
    global nameentry
    global student_identry
    global checkbuttonvalue
    global checkbutton
    global bg_image
    global bg
    global bg_image2
    global bg2
    f2=Frame(bg="lightgrey")
    f2.place(x=0,y=0,width=1370,height=740)
    # bg=PhotoImage(file="bg.png")
    # label=Label(f2,image=bg)
    # label.place(x=0,y=0,width=1370,height=740)
   
    bg=ImageTk.PhotoImage(file="hfhf1.jpg")
    bg_image=Label(f2,image=bg).place(x=0,y=0,relwidth=1,relheight=1)
    # frame=Frame(f2,bg="#A52F16")
    # frame.place(x=400,y=160,height=480,width=603)
    # Frame_login2=Frame(f2)
    # Frame_login2.place(x=450,y=200,height=400,width=500)


    f3=Frame(f2,borderwidth=8,relief=SUNKEN,padx=20)
    f3.grid(row=1,column=5,ipadx=400)


    label4=Label(f3,text="MATHEMATICS",font="HELSINKI  15 bold",fg="orange")
    label4.grid(row=1,column=4,padx=500)
    # bg2=ImageTk.PhotoImage(file="picture1.png")
    # bg_image2=Label(f2,image=bg2).place(x=100,y=100,width=362,height=662)
    
    
    # TODO CREATING PARAMETERS
    label11=Label(f2,text="MARK YOUR ATTENDANCE",font="HELSINKI  15 bold")
    label11.place(x=400,y=220)
    label5=Label(f2,text="STUDENT NAME",font="HELSINKI  15 bold")
    label5.place(x=450,y=280)
    label6=Label(f2,text="STUDENT ID",font="HELSINKI  15 bold")
    label6.place(x=450,y=370)    
    #TODO CREATING ENTRIES

    namevalue=StringVar()
    studentidvalue=StringVar()
    checkbuttonvalue=StringVar()

    nameentry=Entry(f2,textvariable=namevalue,font=("times new roman",15),bg="lightgrey")
    student_identry=Entry(f2,textvariable=studentidvalue,font=("times new roman",15),bg="lightgrey")
    nameentry.place(x=650,y=280,height=30,width=200)
    student_identry.place(x=650,y=370,height=30,width=200)
    # TODO CHECKBUTTON FOR ATTENDENCE
    checkbutton=Checkbutton(f2,text="PRESENT",variable=checkbuttonvalue,onvalue="PRESENT",offvalue="ABSENT",font=("times new roman",  15 ),activebackground="#5C8AD6")
    checkbutton.deselect()
    checkbutton.place(x=650,y=430)
    
    button=Button(f2,text="<-",borderwidth=5,command=student_panel)
    
    button.place(x=10,y=10)
    button6=Button(f2,text="SUBMIT",command=Subject1,font=("times new roman",10),fg="white",bg="#5C8AD6",activebackground="#5C8AD6")
    button6.place(x=640,y=500)    
def subject2():
    global namevalue1
    global studentidvalue1
    global nameentry1
    global student_identry1
    global checkbuttonvalue1
    global checkbutton1
    global bg34
    global bg_image34
    f2=Frame()
    f2.place(x=0,y=0,width=1370,height=740)
    # bg=PhotoImage(file="bg.png")
    # label=Label(f2,image=bg)
    # label.place(x=0,y=0,width=1370,height=740)
    bg34=ImageTk.PhotoImage(file="sci.jpg")
    bg_image34=Label(f2,image=bg34).place(x=0,y=0,relwidth=1,relheight=1)
    f3=Frame(f2,borderwidth=8,relief=SUNKEN,padx=20)
    f3.grid(row=1,column=5,ipadx=400)
    label4=Label(f3,text="SCIENCE",font="HELSINKI  15 bold",fg="orange")
    label4.grid(row=1,column=4,padx=500)
    
    
    # TODO CREATING PARAMETERS
    
    label5=Label(f2,text="STUDENT NAME",font="HELSINKI  15 bold")
    label5.place(x=450,y=280)
    label6=Label(f2,text="STUDENT ID",font="HELSINKI  15 bold")
    label6.place(x=450,y=370)    
    #TODO CREATING ENTRIES

    namevalue1=StringVar()
    studentidvalue1=StringVar()
    checkbuttonvalue1=StringVar()

    nameentry1=Entry(f2,textvariable=namevalue1,font="HELSINKI  15 ")
    student_identry1=Entry(f2,textvariable=studentidvalue1,font="HELSINKI  15 ")
    nameentry1.place(x=650,y=280,height=30,width=200)
    student_identry1.place(x=650,y=370,height=30,width=200)
    # TODO CHECKBUTTON FOR ATTENDENCE
    checkbutton1=Checkbutton(f2,text="PRESENT",variable=checkbuttonvalue1,onvalue="PRESENT",offvalue="ABSENT",font="HELSINKI  10 ",activebackground="#5C8AD6")
    checkbutton1.deselect()
    checkbutton1.place(x=650,y=430)
    
    button=Button(f2,text="<-",borderwidth=5,command=show1)
    
    button.place(x=10,y=10)
    button6=Button(f2,text="SUBMIT",command=Subject2,font="HELSINKI  10 bold",bg="#5C8AD6",activebackground="#5C8AD6")
    button6.place(x=640,y=500)      
def subject3():
    global namevalue2
    global studentidvalue2
    global nameentry2
    global student_identry2
    global checkbuttonvalue2
    global checkbutton2
    global bg35
    global bg_image35
    f2=Frame()
    f2.place(x=0,y=0,width=1370,height=740)
    bg35=ImageTk.PhotoImage(file="english2.jpg")
    bg_image35=Label(f2,image=bg35).place(x=0,y=0,relwidth=1,relheight=1)
    # bg=PhotoImage(file="bg.png")
    # label=Label(f2,image=bg)
    # label.place(x=0,y=0,width=1370,height=740)
    f3=Frame(f2,borderwidth=4,relief=SUNKEN,padx=20)
    f3.grid(row=1,column=5,ipadx=400)
    label4=Label(f3,text="ENGLISH",font="HELSINKI  15 bold",fg="orange")
    label4.grid(row=1,column=4,padx=500)
    
    
    # TODO CREATING PARAMETERS
    
    label5=Label(f2,text="STUDENT NAME",font="HELSINKI  15 bold")
    label5.place(x=450,y=280)
    label6=Label(f2,text="STUDENT ID",font="HELSINKI  15 bold")
    label6.place(x=450,y=370)    
    #TODO CREATING ENTRIES

    namevalue2=StringVar()
    studentidvalue2=StringVar()
    checkbuttonvalue2=StringVar()

    nameentry2=Entry(f2,textvariable=namevalue2,font="HELSINKI  15 ")
    student_identry2=Entry(f2,textvariable=studentidvalue2,font="HELSINKI  15 ")
    nameentry2.place(x=650,y=280,height=30,width=200)
    student_identry2.place(x=650,y=370,height=30,width=200)
    # TODO CHECKBUTTON FOR ATTENDENCE
    checkbutton2=Checkbutton(f2,text="PRESENT",variable=checkbuttonvalue2,onvalue="PRESENT",offvalue="ABSENT",font="HELSINKI  10 ",activebackground="#5C8AD6")
    checkbutton2.deselect()
    checkbutton2.place(x=650,y=430)
    
    button=Button(f2,text="<-",borderwidth=5,command=show1)
    
    button.place(x=10,y=10)
    button6=Button(f2,text="SUBMIT",command=Subject3,font="HELSINKI  10 bold",bg="#5C8AD6",activebackground="#5C8AD6")
    button6.place(x=640,y=500)    
def subject4():
    global namevalue3
    global studentidvalue3
    global nameentry3
    global student_identry3
    global checkbuttonvalue3
    global checkbutton3
    global bg36
    global bg_image36
    f2=Frame()
    f2.place(x=0,y=0,width=1370,height=740)
    # bg=PhotoImage(file="bg.png")
    # label=Label(f2,image=bg)
    # label.place(x=0,y=0,width=1370,height=740)
    bg36=ImageTk.PhotoImage(file="chemistry.jpg")
    bg_image36=Label(f2,image=bg36).place(x=0,y=0,relwidth=1,relheight=1)
    f3=Frame(f2,bg="grey",borderwidth=8,relief=SUNKEN,padx=20)
    f3.grid(row=1,column=5,ipadx=400)
    label4=Label(f3,text="CHEMISTRY",font="HELSINKI  15 bold",fg="orange")
    label4.grid(row=1,column=4,padx=500)
    
    
    # TODO CREATING PARAMETERS
    
    label5=Label(f2,text="STUDENT NAME",font="HELSINKI  15 bold")
    label5.place(x=450,y=280)
    label6=Label(f2,text="STUDENT ID",font="HELSINKI  15 bold")
    label6.place(x=450,y=370)    
    #TODO CREATING ENTRIES

    namevalue3=StringVar()
    studentidvalue3=StringVar()
    checkbuttonvalue3=StringVar()

    nameentry3=Entry(f2,textvariable=namevalue3,font="HELSINKI  15 ")
    student_identry3=Entry(f2,textvariable=studentidvalue3,font="HELSINKI  15 ")
    nameentry3.place(x=650,y=280,height=30,width=200)
    student_identry3.place(x=650,y=370,height=30,width=200)
    # TODO CHECKBUTTON FOR ATTENDENCE
    checkbutton3=Checkbutton(f2,text="PRESENT",variable=checkbuttonvalue3,onvalue="PRESENT",offvalue="ABSENT",font="HELSINKI  10 ",activebackground="#5C8AD6")
    checkbutton3.deselect()
    checkbutton3.place(x=650,y=430)
    
    button=Button(f2,text="<-",borderwidth=5,command=show1)
    
    button.place(x=10,y=10)
    button6=Button(f2,text="SUBMIT",command=Subject4,font="HELSINKI  10 bold",bg="#5C8AD6",activebackground="#5C8AD6")
    button6.place(x=640,y=500)
def subject5():
    global namevalue4
    global studentidvalue4
    global nameentry4
    global student_identry4
    global checkbuttonvalue4
    global checkbutton4
    global bg38
    global bg_image38
    f2=Frame()
    f2.place(x=0,y=0,width=1370,height=740)
    # bg=PhotoImage(file="bg.png")
    # label=Label(f2,image=bg)
    # label.place(x=0,y=0,width=1370,height=740)
    bg38=ImageTk.PhotoImage(file="prog.jpg")
    bg_image38=Label(f2,image=bg38).place(x=0,y=0,relwidth=1,relheight=1)
    f3=Frame(f2,bg="grey",borderwidth=8,relief=SUNKEN,padx=20)
    f3.grid(row=1,column=5,ipadx=400)
    label4=Label(f3,text="PROGRAMMING",font="HELSINKI  15 bold",fg="orange")
    label4.grid(row=1,column=4,padx=500)
    
    
    # TODO CREATING PARAMETERS
    
    label5=Label(f2,text="STUDENT NAME",font="HELSINKI  15 bold")
    label5.place(x=450,y=280)
    label6=Label(f2,text="STUDENT ID",font="HELSINKI  15 bold")
    label6.place(x=450,y=370)    
    #TODO CREATING ENTRIES

    namevalue4=StringVar()
    studentidvalue4=StringVar()
    checkbuttonvalue4=StringVar()

    nameentry4=Entry(f2,textvariable=namevalue4,font="HELSINKI  15 ")
    student_identry4=Entry(f2,textvariable=studentidvalue4,font="HELSINKI  15 ")
    nameentry4.place(x=650,y=280,height=30,width=200)
    student_identry4.place(x=650,y=370,height=30,width=200)
    # TODO CHECKBUTTON FOR ATTENDENCE
    checkbutton4=Checkbutton(f2,text="PRESENT",variable=checkbuttonvalue4,onvalue="PRESENT",offvalue="ABSENT",font="HELSINKI  10 ",activebackground="#5C8AD6")
    checkbutton4.deselect()
    checkbutton4.place(x=650,y=430)
    
    button=Button(f2,text="<-",borderwidth=5,command=show1)
    
    button.place(x=10,y=10)
    button6=Button(f2,text="SUBMIT",command=Subject5,font="HELSINKI  10 bold",bg="#5C8AD6",activebackground="#5C8AD6")
    button6.place(x=640,y=500)
def subject6():
    global namevalue5
    global studentidvalue5
    global nameentry5
    global student_identry5
    global checkbuttonvalue5
    global checkbutton5
    global bg39
    global bg_image39
    f2=Frame()
    f2.place(x=0,y=0,width=1370,height=740)
    # bg=PhotoImage(file="bg.png")
    # label=Label(f2,image=bg)
    # label.place(x=0,y=0,width=1370,height=740)
    bg39=ImageTk.PhotoImage(file="mountains1.jpg")
    bg_image39=Label(f2,image=bg39).place(x=0,y=0,relwidth=1,relheight=1)
    f3=Frame(f2,bg="grey",borderwidth=8,relief=SUNKEN,padx=20)
    f3.grid(row=1,column=5,ipadx=400)
    label4=Label(f3,text="ENVIRONMENT",font="HELSINKI  15 bold",fg="orange")
    label4.grid(row=1,column=4,padx=500)
    
    
    # TODO CREATING PARAMETERS
    
    label5=Label(f2,text="STUDENT NAME",font="HELSINKI  15 bold")
    label5.place(x=300,y=200)
    label6=Label(f2,text="STUDENT ID",font="HELSINKI  15 bold",)
    label6.place(x=300,y=280)    
    #TODO CREATING ENTRIES

    namevalue5=StringVar()
    studentidvalue5=StringVar()
    checkbuttonvalue5=StringVar()

    nameentry5=Entry(f2,textvariable=namevalue5,font="HELSINKI  15 ")
    student_identry5=Entry(f2,textvariable=studentidvalue5,font="HELSINKI  15 ")
    nameentry5.place(x=600,y=205,height=25,width=160)
    student_identry5.place(x=600,y=285,height=25,width=160)
    # TODO CHECKBUTTON FOR ATTENDENCE
    checkbutton5=Checkbutton(f2,text="PRESENT",variable=checkbuttonvalue5,onvalue="PRESENT",offvalue="ABSENT",font="HELSINKI  15 ",activebackground="#5C8AD6")
    checkbutton5.deselect()
    checkbutton5.place(x=580,y=340)
    
    button=Button(f2,text="<-",borderwidth=5,command=show1)
    
    button.place(x=10,y=10)
    button6=Button(f2,text="SUBMIT",command=Subject6,font="HELSINKI  10 bold",fg="white",bg="#5C8AD6",activebackground="#5C8AD6")
    button6.place(x=580,y=400)    
#TODO  TODO TODO INSERTING DATA     DATA BASE CONNECTIVITY ONLY 
def Subject1():
      Name=namevalue.get()
      Student_id=studentidvalue.get() 
      nameentry.delete(0,END)
      student_identry.delete(0,END)   
      attendence=checkbuttonvalue.get()
      checkbutton.deselect()
      Date=datetime.datetime.now()
      if (Name=="" or Student_id==""):
        MessageBox.showinfo("insert status","all fields are required")
      else:
        con=mysql.connect(host="localhost",user="root",password="9463617001",database="attendance_sheet") 
        cursor=con.cursor()
        sql=''' insert into subject1(name,student_id,attendance,datetime) values (%s,%s,%s,%s) '''

        val=(Name,Student_id,attendence,Date)   
        cursor.execute(sql,val)
        con.commit()

        MessageBox.showinfo("insert status","your responce has been recorded")
        con.close()          
def Subject2(): 
    try: 
      Name=namevalue1.get()
      Student_id=studentidvalue1.get() 
      nameentry1.delete(0,END)
      student_identry1.delete(0,END)   
      attendence=checkbuttonvalue1.get()
      checkbutton1.deselect()
      Date=datetime.datetime.now()
      if (Name=="" or Student_id==""):
        MessageBox.showinfo("insert status","all fields are required")
      else:
        con=mysql.connect(host="localhost",user="root",password="9463617001",database="attendance_sheet") 
        cursor=con.cursor()
        sql=''' insert into subject2(name,student_id,attendance,datetime) values (%s,%s,%s,%s) '''

        val=(Name,Student_id,attendence,Date)   
        cursor.execute(sql,val)
        con.commit()
    except Exception as e:
        print("exception occur",e)    
def  Subject3():
      Name=namevalue2.get()
      Student_id=studentidvalue2.get() 
      nameentry2.delete(0,END)
      student_identry2.delete(0,END)   
      attendence=checkbuttonvalue2.get()
      checkbutton2.deselect()
      Date=datetime.datetime.now()
      if (Name=="" or Student_id==""):
        MessageBox.showinfo("insert status","all fields are required")
      else:
        con=mysql.connect(host="localhost",user="root",password="9463617001",database="attendance_sheet") 
        cursor=con.cursor()
        sql=''' insert into subject3(name,student_id,attendance,datetime) values (%s,%s,%s,%s) '''

        val=(Name,Student_id,attendence,Date)   
        cursor.execute(sql,val)
        con.commit()
def Subject4():
      Name=namevalue3.get()
      Student_id=studentidvalue3.get() 
      nameentry3.delete(0,END)
      student_identry3.delete(0,END)   
      attendence=checkbuttonvalue3.get()
      checkbutton3.deselect()
      Date=datetime.datetime.now()
      if (Name=="" or Student_id==""):
        MessageBox.showinfo("insert status","all fields are required")
      else:
        con=mysql.connect(host="localhost",user="root",password="9463617001",database="attendance_sheet") 
        cursor=con.cursor()
        sql=''' insert into subject4(name,student_id,attendance,datetime) values (%s,%s,%s,%s) '''

        val=(Name,Student_id,attendence,Date)   
        cursor.execute(sql,val)
        con.commit()
def Subject5():
      Name=namevalue4.get()
      Student_id=studentidvalue4.get() 
      nameentry4.delete(0,END)
      student_identry4.delete(0,END)   
      attendence=checkbuttonvalue4.get()
      checkbutton4.deselect()
      Date=datetime.datetime.now()
      if (Name=="" or Student_id==""):
        MessageBox.showinfo("insert status","all fields are required")
      else:
        con=mysql.connect(host="localhost",user="root",password="9463617001",database="attendance_sheet") 
        cursor=con.cursor()
        sql=''' insert into subject5(name,student_id,attendance,datetime) values (%s,%s,%s,%s) '''

        val=(Name,Student_id,attendence,Date)   
        cursor.execute(sql,val)
        con.commit()
def Subject6():
      Name=namevalue5.get()
      Student_id=studentidvalue5.get() 
      nameentry5.delete(0,END)
      student_identry5.delete(0,END)   
      attendence=checkbuttonvalue5.get()
      checkbutton5.deselect()
      Date=datetime.datetime.now()
      if (Name=="" or Student_id==""):
        MessageBox.showinfo("insert status","all fields are required")
      else:
        con=mysql.connect(host="localhost",user="root",password="9463617001",database="attendance_sheet") 
        cursor=con.cursor()
        sql=''' insert into subject6(name,student_id,attendance,datetime) values (%s,%s,%s,%s) '''

        val=(Name,Student_id,attendence,Date)   
        cursor.execute(sql,val)
        con.commit()        
def sign_up():
    
      user=email1.get()
      txt_user.delete(0,END)
      password1=password.get()
      txt_pass.delete(0,END)          
      if (user=="" or password1==""):
        MessageBox.showinfo("insert status","all fields are required")
      else:
        con=mysql.connect(host="localhost",user="root",password="9463617001",database="attendance_sheet") 
        cursor=con.cursor()
        sql=''' insert into user(email,pas) values (%s,%s) '''

        val=(user,password1)   
        cursor.execute(sql,val)
        con.commit()

        MessageBox.showinfo("insert status","your responce has been recorded")
        con.close()
try:        
    def login():
       
        user=email1.get()
        password1=password.get()
        
        if (user=="" or password==""):
                MessageBox.showinfo("insert status","all fields are required")

        else:
                con=mysql.connect(host="localhost",user="root",password="9463617001",database="attendance_sheet") 
                cursor=con.cursor()
                sql="select email , pas from user "
                cursor.execute(sql)
                for (email,pas) in cursor:
                    global login
                    if user=="admin@gmail.com" and password1=="12345":
                        show2()
                        break
                        
                    elif user==email and password1==pas:
                        login =True
                        break
                    
                    else:
                        login=False
                if login==True:
                
                    show1()
                elif(login==False):
                    MessageBox.showinfo("insert status","wrong password or username")   
                # con.commit()
                # cursor.close()

                con.close()
except:
        print("error occured")
# task page         
    
def task():
    global bg_image59
    global bg59
    global bg60
    global bg_image60
    frame=Frame()
    frame.place(x=0,y=0,width=1370,height=740) 
    bg60=ImageTk.PhotoImage(file="laptopj.jpg")

    bg_image60=Label(frame,image=bg60).place(x=0,y=0)
    f5=Frame(bg_image60,borderwidth=4,relief=SUNKEN)
    f5.place(x=0,y=0,width=1370,height=45)
    label=Label(f5,text=" ASSIGNED A TASK  ",font="HELSINKI  15 bold",fg="PURPLE")
    label.place(x=530,y=5)
    frame1=Frame(bg="lightgrey")
    frame1.place(x=235,y=80,height=458,width=900)
    bg59=ImageTk.PhotoImage(file="fram3.png")
    bg_image59=Label(frame1,image=bg59).place(x=0,y=0)
    # ------------------------
    b3=Button(frame1,text="MATHEMATICS ",padx=100,font=("Goudy old style",15,"bold"),fg="white",bg="#941FB7",command=post_task1)
    b3.place(x=360,y=120,width=180,height=30)
    b4=Button(frame1,text="SCIENCE",padx=120,font=("Goudy old style",15,"bold"),fg="white",bg="#941FB7",command=post_task2)
    b4.place(x=360,y=170,width=180,height=30)
    b4=Button(frame1,text="ENGLISH",padx=120,font=("Goudy old style",15,"bold"),fg="white",bg="#941FB7",command=post_task3)
    b4.place(x=360,y=220,width=180,height=30)
    b4=Button(frame1,text="CHEMISTRY",padx=120,font=("Goudy old style",15,"bold"),fg="white",bg="#941FB7",command=post_task4)
    b4.place(x=360,y=270,width=180,height=30)
    b4=Button(frame1,text="PROGRAMMING",padx=120,font=("Goudy old style",15,"bold"),fg="white",bg="#941FB7",command=post_task5)
    b4.place(x=360,y=320,width=180,height=30)
    b4=Button(frame1,text="ENVIRONMENT",padx=120,font=("Goudy old style",15,"bold"),fg="white",bg="#941FB7",command=post_task6)
    b4.place(x=360,y=370,width=180,height=30)
  
    button=Button(f5,text="<-",borderwidth=5,command=show2,fg="purple")
    button.place(x=5,y=5)
    # TODO ADMIN BLOCK----------------------------------------------
    # data base work 
def post1():
    Name= label9value.get()
    task= label91value.get() 
    label9entry.delete(0,END)
    label91entry.delete(0,END)   
  
    Date=datetime.datetime.now()
    if (Name=="" or task==""):
        MessageBox.showinfo("insert status","all fields are required")
    else:
        con=mysql.connect(host="localhost",user="root",password="9463617001",database="attendance_sheet") 
        cursor=con.cursor()
        sql=''' insert into task_assign1(teacher,task,Date_time) values (%s,%s,%s) '''

        val=(Name,task,Date)   
        cursor.execute(sql,val)
        con.commit()

        MessageBox.showinfo("insert status","your responce has been recorded")
        con.close()    
def post2():
    Name= label9value.get()
    task= label91value.get() 
    label9entry.delete(0,END)
    label91entry.delete(0,END)   
  
    Date=datetime.datetime.now()
    if (Name=="" or task==""):
        MessageBox.showinfo("insert status","all fields are required")
    else:
        con=mysql.connect(host="localhost",user="root",password="9463617001",database="attendance_sheet") 
        cursor=con.cursor()
        sql=''' insert into task_assign2(teacher,task,Date_time) values (%s,%s,%s) '''

        val=(Name,task,Date)   
        cursor.execute(sql,val)
        con.commit()

        MessageBox.showinfo("insert status","your responce has been recorded")
        con.close()  
def post3():
    Name= label9value.get()
    task= label91value.get() 
    label9entry.delete(0,END)
    label91entry.delete(0,END)   
  
    Date=datetime.datetime.now()
    if (Name=="" or task==""):
        MessageBox.showinfo("insert status","all fields are required")
    else:
        con=mysql.connect(host="localhost",user="root",password="9463617001",database="attendance_sheet") 
        cursor=con.cursor()
        sql=''' insert into task_assign3(teacher,task,Date_time) values (%s,%s,%s) '''

        val=(Name,task,Date)   
        cursor.execute(sql,val)
        con.commit()

        MessageBox.showinfo("insert status","your responce has been recorded")
        con.close()
def post4():
    Name= label9value.get()
    task= label91value.get() 
    label9entry.delete(0,END)
    label91entry.delete(0,END)   
  
    Date=datetime.datetime.now()
    if (Name=="" or task==""):
        MessageBox.showinfo("insert status","all fields are required")
    else:
        con=mysql.connect(host="localhost",user="root",password="9463617001",database="attendance_sheet") 
        cursor=con.cursor()
        sql=''' insert into task_assign4(teacher,task,Date_time) values (%s,%s,%s) '''

        val=(Name,task,Date)   
        cursor.execute(sql,val)
        con.commit()

        MessageBox.showinfo("insert status","your responce has been recorded")
        con.close()
def post5():
    Name= label9value.get()
    task= label91value.get() 
    label9entry.delete(0,END)
    label91entry.delete(0,END)   
  
    Date=datetime.datetime.now()
    if (Name=="" or task==""):
        MessageBox.showinfo("insert status","all fields are required")
    else:
        con=mysql.connect(host="localhost",user="root",password="9463617001",database="attendance_sheet") 
        cursor=con.cursor()
        sql=''' insert into task_assign5(teacher,task,Date_time) values (%s,%s,%s) '''

        val=(Name,task,Date)   
        cursor.execute(sql,val)
        con.commit()

        MessageBox.showinfo("insert status","your responce has been recorded")
        con.close()
def post6():
    Name= label9value.get()
    task= label91value.get() 
    label9entry.delete(0,END)
    label91entry.delete(0,END)   
  
    Date=datetime.datetime.now()
    if (Name=="" or task==""):
        MessageBox.showinfo("insert status","all fields are required")
    else:
        con=mysql.connect(host="localhost",user="root",password="9463617001",database="attendance_sheet") 
        cursor=con.cursor()
        sql=''' insert into task_assign6(teacher,task,Date_time) values (%s,%s,%s) '''

        val=(Name,task,Date)   
        cursor.execute(sql,val)
        con.commit()

        MessageBox.showinfo("insert status","your responce has been recorded")
        con.close()                                                          
def post_task1():
    global label9entry
    global label91entry

    global  label9value
    global   label91value
    frame=Frame(bg="lightgrey")
    frame.place(x=200,y=190,height=450,width=930)
    label11=Label(frame,text="ASSIGNED A TASK ",font="HELSINKI  15 bold",fg="#216963",bg="lightgrey")
    label11.place(x=30,y=40)
    label9=Label(frame,text="TEACHER NAME",font="HELSINKI  15 bold",fg="blue",bg="lightgrey")
    label9.place(x=40,y=100)
    label91=Label(frame,text="TASK ",font="HELSINKI  15 bold",fg="blue",bg="lightgrey")
    label91.place(x=40,y=180)
    button=Button(frame,text="POST ASSIGNMENT ",command=post1,font="HELSINKI  15 bold",fg="black",bg="#57DFBC")
    button.place(x=110,y=250)
    button=Button(frame,text="CLOSE ",command=task,font="HELSINKI  15 bold",fg="black",bg="#57DFBC")
    button.place(x=830,y=15)

    label9value=StringVar()
    label91value=StringVar()
    label9entry=Entry(frame,textvariable= label9value,font="HELSINKI  15 ")
    label9entry.place(x=240,y=100)
    label91entry=Entry(frame,textvariable=label91value,font="HELSINKI  15 ")
    label91entry.place(x=240,y=180,width=450) 
def post_task2():
    global label9entry
    global label91entry

    global  label9value
    global   label91value
    frame=Frame(bg="lightgrey")
    frame.place(x=200,y=190,height=450,width=930)
    label11=Label(frame,text="ASSIGNED A TASK ",font="HELSINKI  15 bold",fg="#216963",bg="lightgrey")
    label11.place(x=30,y=40)
    label9=Label(frame,text="TEACHER NAME",font="HELSINKI  15 bold",fg="blue",bg="lightgrey")
    label9.place(x=40,y=100)
    label91=Label(frame,text="TASK ",font="HELSINKI  15 bold",fg="blue",bg="lightgrey")
    label91.place(x=40,y=180)
    button=Button(frame,text="POST ASSIGNMENT ",command=post2,font="HELSINKI  15 bold",fg="black",bg="#57DFBC")
    button.place(x=110,y=250)
    button=Button(frame,text="CLOSE ",command=task,font="HELSINKI  15 bold",fg="black",bg="#57DFBC")
    button.place(x=830,y=15)

    label9value=StringVar()
    label91value=StringVar()
    label9entry=Entry(frame,textvariable= label9value,font="HELSINKI  15 ")
    label9entry.place(x=240,y=100)
    label91entry=Entry(frame,textvariable=label91value,font="HELSINKI  15 ")
    label91entry.place(x=240,y=180,width=450) 
def post_task3():
    global label9entry
    global label91entry

    global  label9value
    global   label91value
    frame=Frame(bg="lightgrey")
    frame.place(x=200,y=190,height=450,width=930)
    label11=Label(frame,text="ASSIGNED A TASK ",font="HELSINKI  15 bold",fg="#216963",bg="lightgrey")
    label11.place(x=30,y=40)
    label9=Label(frame,text="TEACHER NAME",font="HELSINKI  15 bold",fg="blue",bg="lightgrey")
    label9.place(x=40,y=100)
    label91=Label(frame,text="TASK ",font="HELSINKI  15 bold",fg="blue",bg="lightgrey")
    label91.place(x=40,y=180)
    button=Button(frame,text="POST ASSIGNMENT ",command=post3,font="HELSINKI  15 bold",fg="black",bg="#57DFBC")
    button.place(x=110,y=250)
    button=Button(frame,text="CLOSE ",command=task,font="HELSINKI  15 bold",fg="black",bg="#57DFBC")
    button.place(x=830,y=15)

    label9value=StringVar()
    label91value=StringVar()
    label9entry=Entry(frame,textvariable= label9value,font="HELSINKI  15 ")
    label9entry.place(x=240,y=100)
    label91entry=Entry(frame,textvariable=label91value,font="HELSINKI  15 ")
    label91entry.place(x=240,y=180,width=450) 
def post_task4():
    global label9entry
    global label91entry

    global  label9value
    global   label91value
    frame=Frame(bg="lightgrey")
    frame.place(x=200,y=190,height=450,width=930)
    label11=Label(frame,text="ASSIGNED A TASK ",font="HELSINKI  15 bold",fg="#216963",bg="lightgrey")
    label11.place(x=30,y=40)
    label9=Label(frame,text="TEACHER NAME",font="HELSINKI  15 bold",fg="blue",bg="lightgrey")
    label9.place(x=40,y=100)
    label91=Label(frame,text="TASK ",font="HELSINKI  15 bold",fg="blue",bg="lightgrey")
    label91.place(x=40,y=180)
    button=Button(frame,text="POST ASSIGNMENT ",command=post4,font="HELSINKI  15 bold",fg="black",bg="#57DFBC")
    button.place(x=110,y=250)
    button=Button(frame,text="CLOSE ",command=task,font="HELSINKI  15 bold",fg="black",bg="#57DFBC")
    button.place(x=830,y=15)

    label9value=StringVar()
    label91value=StringVar()
    label9entry=Entry(frame,textvariable= label9value,font="HELSINKI  15 ")
    label9entry.place(x=240,y=100)
    label91entry=Entry(frame,textvariable=label91value,font="HELSINKI  15 ")
    label91entry.place(x=240,y=180,width=450) 
def post_task5():
    global label9entry
    global label91entry

    global  label9value
    global   label91value
    frame=Frame(bg="lightgrey")
    frame.place(x=200,y=190,height=450,width=930)
    label11=Label(frame,text="ASSIGNED A TASK ",font="HELSINKI  15 bold",fg="#216963",bg="lightgrey")
    label11.place(x=30,y=40)
    label9=Label(frame,text="TEACHER NAME",font="HELSINKI  15 bold",fg="blue",bg="lightgrey")
    label9.place(x=40,y=100)
    label91=Label(frame,text="TASK ",font="HELSINKI  15 bold",fg="blue",bg="lightgrey")
    label91.place(x=40,y=180)
    button=Button(frame,text="POST ASSIGNMENT ",command=post5,font="HELSINKI  15 bold",fg="black",bg="#57DFBC")
    button.place(x=110,y=250)
    button=Button(frame,text="CLOSE ",command=task,font="HELSINKI  15 bold",fg="black",bg="#57DFBC")
    button.place(x=830,y=15)

    label9value=StringVar()
    label91value=StringVar()
    label9entry=Entry(frame,textvariable= label9value,font="HELSINKI  15 ")
    label9entry.place(x=240,y=100)
    label91entry=Entry(frame,textvariable=label91value,font="HELSINKI  15 ")
    label91entry.place(x=240,y=180,width=450) 
def post_task6():
    global label9entry
    global label91entry

    global  label9value
    global   label91value
    frame=Frame(bg="lightgrey")
    frame.place(x=200,y=190,height=450,width=930)
    label11=Label(frame,text="ASSIGNED A TASK ",font="HELSINKI  15 bold",fg="#216963",bg="lightgrey")
    label11.place(x=30,y=40)
    label9=Label(frame,text="TEACHER NAME",font="HELSINKI  15 bold",fg="blue",bg="lightgrey")
    label9.place(x=40,y=100)
    label91=Label(frame,text="TASK ",font="HELSINKI  15 bold",fg="blue",bg="lightgrey")
    label91.place(x=40,y=180)
    button=Button(frame,text="POST ASSIGNMENT ",command=post6,font="HELSINKI  15 bold",fg="black",bg="#57DFBC")
    button.place(x=110,y=250)
    button=Button(frame,text="CLOSE ",command=task,font="HELSINKI  15 bold",fg="black",bg="#57DFBC")
    button.place(x=830,y=15)

    label9value=StringVar()
    label91value=StringVar()
    label9entry=Entry(frame,textvariable= label9value,font="HELSINKI  15 ")
    label9entry.place(x=240,y=100)
    label91entry=Entry(frame,textvariable=label91value,font="HELSINKI  15 ")
    label91entry.place(x=240,y=180,width=450)                     

def admin():
    global studentidvalue
    global listbox
    global studententry
    global f4
    global cal
    global bg10
    global bg_image11
    global bg101
    global bg_image101
    f4=Frame()
    f4.place(x=0,y=0,width=1370,height=740)
    bg101=ImageTk.PhotoImage(file="laptopj.jpg")

    bg_image101=Label(f4,image=bg101).place(x=0,y=0)
    bg10=ImageTk.PhotoImage(file="ipad.jpg")
    bg_image11=Label(f4,image=bg10).place(x=730,y=220)
    # bg101=ImageTk.PhotoImage(file="laptop.jpeg")

    # bg_image101=Label(f4,image=bg101).place(x=160,y=80)
    listbox=Listbox(f4)
   
    listbox.place(x=764,y=251,width=340,height=227)
   
    listbox.insert(END,"   NAME          ATTENDANCE             DATE & TIME")
    listbox.delete(1,END)
    cal=Calendar(f4,background="black",disabledbackground="black", bordercolor="black", 
               headersbackground="black", normalbackground="black", foreground='white', 
               normalforeground='white', headersforeground='white',selectmode="day")
    cal.place(x=235,y=72)
  
    f6=Frame(f4,borderwidth=8,relief=SUNKEN,padx=125)
    f6.place(x=0,y=0,width=1370,height=55) 
    
    label7=Label(f6,text="ADMIN PANEL",font="HELSINKI  15 bold",fg="orange")
    label7.place(x=450,y=5)
  #  label8=Label(top,text="enter value to get student details")
    #label8.grid(row=2,column=0)

    label9=Label(f4,text="STUDENT ID",font="HELSINKI  15 bold",fg="blue",background="white")
    label9.place(x=240,y=315)
    studentidvalue=StringVar()
    studententry=Entry(f4,textvariable=studentidvalue,font="HELSINKI  15 ",borderwidth=5)
    studententry.place(x=410,y=315)
   
    button4=Button(f4,text="MATHEMATICS RECORD ",font="HELSINKI  10 bold",fg="white",command=subject1_record,bg="#5189C8")
    button4.place(x=240,y=365,width=180,)
    button5=Button(f4,text="SCIENCE RECORD",font="HELSINKI  10 bold",fg="white",command=subject2_record,bg="#5189C8")
    button5.place(x=240,y=415,width=180,)
    button6=Button(f4,text="ENGLISH",font="HELSINKI  10 bold",fg="white",command=subject3_record,bg="#5189C8")
    button6.place(x=240,y=470,width=180,)
    button7=Button(f4,text="CHEMISTRY",font="HELSINKI  10 bold",fg="white",command=subject4_record,bg="#5189C8")
    button7.place(x=500,y=365,width=180,)
    button8=Button(f4,text="PROGRAMMING",font="HELSINKI  10 bold",fg="white",command=subject5_record,bg="#5189C8")
    button8.place(x=500,y=415,width=180)
    button9=Button(f4,text=" ENVIRONMENT",font="HELSINKI  10 bold",fg="white",command=subject6_record,bg="#5189C8")
    button9.place(x=500,y=465,width=180)
    button=Button(f4,text="<-",borderwidth=5,command=show2,fg="purple")
    button.place(x=10,y=10)
    button5=Button(f4,text="clear",font="HELSINKI  8 bold",fg="white",bg="#5189C8",command=delete)
    button5.place(x=1040,y=452,width=60)
    button11=Button(f4,text="Present Date",font="HELSINKI  8 bold",fg="white",bg="#AD25C5",command=get_date1)
    button11.place(x=300,y=260,width=80)
    Label(f4,text="PRESENT DATE",font="HELSINKI  8 bold",bg="white").place(x=500,y=80)
def delete():
    
    listbox.delete(1,END)
    # todo get calendar date
def get_date1():
  

    

    my_label=Label(text="",font=("times new roman",15),fg="black",bg="white")
    my_label.place(x=500,y=100)
    my_label.config(text=cal.get_date())
# all subject records ---------------------------------------------------- for admin     
def subject1_record():
    
   
    # studentidvalue=StringVar()
    con=mysql.connect(host="localhost",user="root",password="9463617001",database="attendance_sheet") 
    cursor=con.cursor()
    cursor.execute("select * from subject1 where student_id='" + studentidvalue.get() + "'")
    rows=cursor.fetchall()
    studententry.delete(0,END)
    for row in rows:
        insertdata= "   "+str(row[0])+"                 "+  row[2]+'                     '+str(row[3])
        listbox.insert(END, insertdata)
       
    con.close() 
def subject2_record():
    
   
    # studentidvalue=StringVar()
    con=mysql.connect(host="localhost",user="root",password="9463617001",database="attendance_sheet") 
    cursor=con.cursor()
    cursor.execute("select * from subject2 where student_id='" + studentidvalue.get() + "'")
    rows=cursor.fetchall()
    studententry.delete(0,END)
    for row in rows:
        insertdata= "   "+str(row[0])+"                 "+  row[2]+'                     '+str(row[3])
        listbox.insert(END, insertdata)
       
    con.close()     
def subject3_record():
    
   
    # studentidvalue=StringVar()
    con=mysql.connect(host="localhost",user="root",password="9463617001",database="attendance_sheet") 
    cursor=con.cursor()
    cursor.execute("select * from subject3 where student_id='" + studentidvalue.get() + "'")
    rows=cursor.fetchall()
    studententry.delete(0,END)
    for row in rows:
        insertdata= "   "+str(row[0])+"                 "+  row[2]+'                     '+str(row[3])
        listbox.insert(END, insertdata)
       
    con.close()         
def subject4_record():
    
   
    # studentidvalue=StringVar()
    con=mysql.connect(host="localhost",user="root",password="9463617001",database="attendance_sheet") 
    cursor=con.cursor()
    cursor.execute("select * from subject4 where student_id='" + studentidvalue.get() + "'")
    rows=cursor.fetchall()
    studententry.delete(0,END)
    for row in rows:
        insertdata= "   "+str(row[0])+"                 "+  row[2]+'                     '+str(row[3])
        listbox.insert(END, insertdata)
       
    con.close()   
def subject5_record():
    
   
    # studentidvalue=StringVar()
    con=mysql.connect(host="localhost",user="root",password="9463617001",database="attendance_sheet") 
    cursor=con.cursor()
    cursor.execute("select * from subject5 where student_id='" + studentidvalue.get() + "'")
    rows=cursor.fetchall()
    studententry.delete(0,END)
    for row in rows:
        insertdata= "   "+str(row[0])+"                 "+  row[2]+'                     '+str(row[3])
        listbox.insert(END, insertdata)
       
    con.close()            
def subject6_record():
    
   
    # studentidvalue=StringVar()
    con=mysql.connect(host="localhost",user="root",password="9463617001",database="attendance_sheet") 
    cursor=con.cursor()
    cursor.execute("select * from subject5 where student_id='" + studentidvalue.get() + "'")
    rows=cursor.fetchall()
    studententry.delete(0,END)
    for row in rows:
        insertdata= "   "+str(row[0])+"                 "+  row[2]+'                     '+str(row[3])
        listbox.insert(END, insertdata)
       
    con.close()                
try:            
    def show():
        global email1
        global password
        global  txt_user
        global     txt_pass
        root.resizable(False,False)
        #         #========bg=========
        root.title("Login System")
        global bg_image
        global bg
        bg=ImageTk.PhotoImage(file="photo1.png")
        bg_image=Label(root,image=bg).place(x=0,y=0,relwidth=1,relheight=1)
        # root.attributes('-alpha',0.5)    

                #==========Login Frame=======
        Frame_login=Frame(root,bg="white")
        Frame_login.place(x=150,y=150,height=340,width=500)
        # root.attributes(Frame_login,'-alpha',0.5)  

        title=Label(Frame_login,text="Login here",font=("Impact",35,"bold"),fg="#d77337",bg="white").place(x=90,y=30)
        desc=Label(Frame_login,text="Student/Admin Login",font=("Goudy old style",15,"bold"),fg="#d25d17",bg="white").place(x=90,y=100)

        email1=StringVar()
        password=StringVar()

        lbl_user=Label(Frame_login,text="Email",font=("Goudy old style",15,"bold"),fg="grey",bg="white").place(x=90,y=140)
        txt_user=Entry(Frame_login,textvariable=email1,font=("times new roman",15),bg="lightgrey")
        txt_user.place(x=90,y=170,width=350,height=35)


        lbl_pass=Label(Frame_login,text="Password",font=("Goudy old style",15,"bold"),fg="grey",bg="white").place(x=90,y=210)
        txt_pass=Entry(Frame_login,textvariable=password,show="*",font=("times new roman",15),bg="lightgrey")
        txt_pass.place(x=90,y=240,width=350,height=35)
        global forget_btn
        global Login_btn
        global sign_up
        global login_btn
        global img_label
       
        forget_btn=Button(Frame_login,text="Forget Password?",cursor="hand2",bg="white",fg="#d77337",bd=0,font=("times new roman",12)).place(x=90,y=280)
        Login_btn=Button(root,cursor="hand2",command=login,text="Login",fg="white",bg="#d77337",font=("times new roman",20)).place(x=230,y=470,width=170,height=40)
        sign_up=Button(root,cursor="hand2",command=sign_up,text="Sign up",fg="white",bg="#d77337",font=("times new roman",20)).place(x=415,y=470,width=160,height=40)
    show()
except Exception as e:
    print(e)



root.mainloop()
