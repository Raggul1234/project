


def Save():
    Names=   (Name.get())
    Ages=    (Age.get())
    Heights= (Height.get())
    Weights= (Weight.get())
    StudentIds= (StudentId.get())
    Activitytypes=(Activitytype.get())
    Activitys=(Activity.get())
    Extras=(Extra.get())

    Validate(Names,Ages,Heights,Weights,StudentIds,Activitytypes,Activitys,Extras)
def create_new_window():
    def Search():
     
            Name1s= Name1.get()
            Age1s= Age1.get()
            Height1s= Height1.get()
            Weight1s= Weight1.get()
            StudentId1s= StudentId1.get()
            Activitytype1s=Activitytype1.get()
            Activitie1s=Activity1.get()
            Extra1s=Extra1.get()

            

    
           

            

    #Search starts
                

            if len(Name1s)!=0:
                cursor.execute("""select A.name,A.age,A.gender,A.height,A.weight,A.studentId,B.activity_type,B.activity,B.extra_activity
                from Students A inner join Activities B on A.StudentId=B.StudentId where A.Name like(?)""",(Name1s))
                records=cursor.fetchall()
                for row in records:
                    
                    Age1.insert(0,row[1])
                    
                    Gender1.insert(0,row[2])
                    Height1.insert(0,row[3])
                    Weight1.insert(0,row[4])
                    StudentId1.insert(0,row[5])
                    Activitytype1.insert(0,row[6])
                    Activity1.insert(0,row[7])
                    Extra1.insert(0,row[8])
                    
                        
                    
            elif  len(Age1s)!=0:
                cursor.execute("""select A.name,A.age,A.gender,A.height,A.weight,A.studentId,B.activity_type,B.activity,B.extra_activity
                from Students A inner join Activities B on A.StudentId=B.StudentId where A.Age like(?)""",(Age1s))
                records=cursor.fetchall()
                for row in records:
                    Name1.insert(0,row[0])
                    Gender1.insert(0,row[2])
                    Height1.insert(0,row[3])
                    Weight1.insert(0,row[4])
                    StudentId1.insert(0,row[5])
                    Activitytype1.insert(0,row[6])
                    Activity1.insert(0,row[7])
                    Extra1.insert(0,row[8])




                    
            elif  len(Gender1s)!=0:
                cursor.execute("""select A.name,A.age,A.gender,A.height,A.weight,A.studentId,B.activity_type,B.activity,B.extra_activity
                from Students A inner join Activities B on A.StudentId=B.StudentId where A.Gender like(?) """,(Gender1s))
                records=cursor.fetchall()
                for row in records:
                    Name1.insert(0,row[0])
                    Age1.insert(0,row[1])
                    Gender1.insert(0,row[2])
                    Height1.insert(0,row[3])
                    Weight1.insert(0,row[4])
                    StudentId1.insert(0,row[5])
                    Activitytype1.insert(0,row[6])
                    Activity1.insert(0,row[7])
                    Extra1.insert(0,row[8])


            elif  len(Height1s!=0):
                cursor.execute("""select A.name,A.age,A.gender,A.height,A.weight,A.studentId,B.activity_type,B.activity,B.extra_activity
                from Students A inner join Activities B on A.StudentId=B.StudentId where A.Height like(?)""",(Height1s))
                records=cursor.fetchall()
                for row in records:
                    Name1.insert(0,row[0])
                    Age1.insert(0,row[1])
                    Gender1.insert(0,row[2])
                    Weight1.insert(0,row[4])
                    StudentId1.insert(0,row[5])
                    Activitytype1.insert(0,row[6])
                    Activity1.insert(0,row[7])
                    Extra1.insert(0,row[8])          


            elif  len(Weight1s)!=0:
                cursor.execute("""select A.name,A.age,A.gender,A.height,A.weight,A.studentId,B.activity_type,B.activity,B.extra_activity
                from Students A inner join Activities B on A.StudentId=B.StudentId where A._Weight like(?)""",(Weight1s))
                records=cursor.fetchall()
                for row in records:
                    Name1.insert(0,row[0])
                    Age1.insert(0,row[1])
                    Height1.insert(0,row[3])
                    Gender1.insert(0,row[2])
                    StudentId1.insert(0,row[5])
                    Activitytype1.insert(0,row[6])
                    Activity1.insert(0,row[7])
                    Extra1.insert(0,row[8])


            elif  len(StudentId1s)!=0:
                cursor.execute("""select A.name,A.age,A.gender,A.height,A.weight,A.studentId,B.activity_type,B.activity,B.extra_activity
                from Students A inner join Sports B on A.StudentId=B.StudentId where A.StudentId like(?)""",(StudentId1s))
                records=cursor.fetchall()
                for row in records:
                    Name1.insert(0,row[0])
                    Age1.insert(0,row[1])
                    Height1.insert(0,row[3])
                    Weight1.insert(0,row[4])
                    Gender1.insert(0,row[2])
                    Activitytype1.insert(0,row[6])
                    Activity1.insert(0,row[7])
                    Extra1.insert(0,row[8])


            elif  len(Activitytype1s)!=0:
                cursor.execute("""select A.name,A.age,A.gender,A.height,A.weight,A.studentId,B.activity_type,B.activity,B.extra_activity
                from Students A inner join Activities B on A.StudentId=B.StudentId where B.Activitytypes like(?)""",(Activitytype1s))
                records=cursor.fetchall()
                for row in records:
                    Name1.insert(0,row[0])
                    Age1.insert(0,row[1])
                    Height1.insert(0,row[3])
                    Weight1.insert(0,row[4])
                    StudentId1.insert(0,row[5])
                    Gender1.insert(0,row[2])
                    Activity1.insert(0,row[7])
                    Extra1.insert(0,row[8])

                    
            elif  len(Activitie1s)!=0:
                cursor.execute("""select A.name,A.age,A.gender,A.height,A.weight,A.studentId,B.activity_type,B.activity,B.extra_activity
                from Students A inner join Activities B on A.StudentId=B.StudentId where B.Activity like(?)""",(Activitie1s))
                records=cursor.fetchall()
                for row in records:
                    Name1.insert(0,row[0])
                    Age1.insert(0,row[1])
                    Height1.insert(0,row[3])
                    Weight1.insert(0,row[4])
                    StudentId1.insert(0,row[5])
                    Activitytype1.insert(0,row[6])
                    Gender1.insert(0,row[2])
                    Extra1.insert(0,row[8])
                    

            elif  len(Extra1s)!=0:
                cursor.execute("""select A.name,A.age,A.gender,A.height,A.weight,A.studentId,B.activity_type,B.activity,B.extra_activity
                from Students A inner join Activities B on A.StudentId=B.StudentId where B.Extra like(?)""",(Estra1s))
                records=cursor.fetchall()
                for row in records:
                    Name1.insert(0,row[0])
                    Age1.insert(0,row[1])
                    Gender1.insert(0,row[2])
                    Height1.insert(0,row[3])
                    Weight1.insert(0,row[4])
                    StudentId1.insert(0,row[5])
                    Activitytype1.insert(0,row[6])
                    Activity1.insert(0,row[7])
                    

            else:
                
                messagebox.showinfo("Tkinter", "Atleast one search criteria must be given!")

    

    def Update():
        Name1s= Name1.get()
        Age1s= Age1.get()
        Height1s= Height1.get()
        Weight1s= Weight1.get()
        StudentId1s= StudentId1.get()
        Activitytype1s=Activitytype1.get()
        Activitie1s=Activity1.get()
        Extra1s=Extra1.get()
        Gender1s=Gender1.get()
        Update_Function(StudentId1s,Name1s,Age1s,Gender1s,Height1s,Weight1s,Activitytype1s,Activitie1s,Extra1s)


        
    root2=tk.Tk()
    root2.title("Class4c-update record")
    canvas2 = tk.Canvas(root2, width = 900, height = 300)
    canvas2.pack()




    Name1 = tk.Entry (root2)
    canvas2.create_window(300, 10, window=Name1)
    label1 = tk.Label(root2, text='Name:')
    label1.config(font=('helvetica', 10))
    canvas2.create_window(200, 10, window=label1)


    Age1 = tk.Entry (root2)
    canvas2.create_window(300, 40, window=Age1)
    label2 = tk.Label(root2 , text='Age:')
    label2.config(font=('helvetica', 10))
    canvas2.create_window(200, 40, window=label2)



    label31 = tk.Label(root2, text='Gender:')
    label31.config(font=('helvetica', 10))
    canvas2.create_window(200, 70, window=label31)
    Gender1 = tk.Entry (root2)
    canvas2.create_window(300, 70, window=Gender1)

    


    Height1 = tk.Entry (root2)
    canvas2.create_window(300, 100, window=Height1)
    label4 = tk.Label(root2, text='height in cm:')
    label4.config(font=('helvetica', 10))
    canvas2.create_window(195, 100, window=label4)

    Weight1 = tk.Entry (root2)
    canvas2.create_window(300, 130, window=Weight1)
    label5 = tk.Label(root2, text='weight in kg:')
    label5.config(font=('helvetica', 10))
    canvas2.create_window(195, 130, window=label5)

    StudentId1 = tk.Entry (root2)
    canvas2.create_window(300, 160, window=StudentId1)
    label6 = tk.Label(root2, text='StudentId:')
    label6.config(font=('helvetica', 10))
    canvas2.create_window(200, 160, window=label6)

    Activitytype1 = tk.Entry (root2)
    canvas2.create_window(300, 190, window=Activitytype1)
    label7 = tk.Label(root2, text='Activitytype:')
    label7.config(font=('helvetica', 10))
    canvas2.create_window(200, 190, window=label7)


    Activity1 = tk.Entry (root2)
    canvas2.create_window(500, 10, window=Activity1)
    label8 = tk.Label(root2, text='Activity:')
    label8.config(font=('helvetica', 10))
    canvas2.create_window(400, 10, window=label8)

    Extra1 = tk.Entry (root2)
    canvas2.create_window(500, 40, window=Extra1)
    label9 = tk.Label(root2, text='Extra:')
    label9.config(font=('helvetica', 10))
    canvas2.create_window(400, 40, window=label9)

    button6 = tk.Button(root2,text='get',command=Search)
    canvas2.create_window(400, 250, window=button6)

    button5 = tk.Button(root2,text='Update',command=Update)
    canvas2.create_window(350, 250, window=button5)


def Validate(Names,Ages,Heights,Weights,StudentIds,Activitytypes,Activitys,Extras):

    while True:
        
            if len(Names)==0:
                messagebox.showinfo("Tkinter", "Name cannot be empty")
                break
            elif len(Ages)==0:
                messagebox.showinfo("Tkinter", "Age cannot be empty")
                break
            elif (M.get() == 0) and (F.get() == 0):
                messagebox.showinfo("Tkinter", "Genders cannot be empty")
                break
            elif len(StudentIds)==0:
                messagebox.showinfo("Tkinter", "StudentId cannot be empty")
                break
            elif len(Names)==0 and len(Ages)==0 and (M.get()==0 and M.get()==0)  and len(StudentIds)==0:
                messagebox.showinfo("Tkinter", "Atleast Name,Age,Gender and StudentId must be given!!")
                break
            
            try:
            
                int(Names)
                messagebox.showinfo("Tkinter", "Name must be string")
                break
            except ValueError:
                try:
                    if (M.get() == 1) and (F.get() == 0):
                          
                        cursor.execute("""
                        INSERT INTO Students(studentId,name,age,gender,height,weight)
                        VALUES (?,?,?,?,?,?)""",(StudentIds,Names,Ages,'m',Heights,Weights))
                        conn.commit()
                        cursor.execute("""
                        INSERT INTO Activities(studentId,name,activity_type,activity,extra_activity)
                        VALUES (?,?,?,?,?)
                        """,(StudentIds,Names,Activitytypes,Activitys,Extras))
                        conn.commit()
                        clearfields()
                        
                        messagebox.showinfo("Tkinter", "Saved successfully!")
                        break
                    elif (M.get() == 0) and (F.get() == 1):
                          
                        cursor.execute("""
                        INSERT INTO Students(studentId,name,age,gender,height,weight)
                        VALUES (?,?,?,?,?,?)""",(StudentIds,Names,Ages,'f',Heights,Weights))
                        conn.commit()
                        cursor.execute("""
                        INSERT INTO Activities(studentId,name,activity_type,activity,extra_activity)
                        VALUES (?,?,?,?,?)
                        """,(StudentIds,Names,Activitytypes,Activitys,Extras))
                        conn.commit()
                        clearfields()
                        
                        messagebox.showinfo("Tkinter", "Saved successfully!")
                        break
                except pyodbc.DataError:
                    
                    try:
                        int(Ages)
                        break
                    except :
                        messagebox.showinfo("Tkinter", "Age must be integer")
                        break
                    else:
                        try:
                            if (M.get() == 1) and (F.get() == 0):
                                  
                                cursor.execute("""
                                INSERT INTO Students(studentId,name,age,gender,height,weight)
                                VALUES (?,?,?,?,?,?)""",(StudentIds,Names,Ages,'m',Heights,Weights))
                                conn.commit()
                                cursor.execute("""
                                INSERT INTO Activities(studentId,name,activity_type,activity,extra_activity)
                                VALUES (?,?,?,?,?)
                                """,(StudentIds,Names,Activitytypes,Activitys,Extras))
                                conn.commit()
                                clearfields()
                        
                                messagebox.showinfo("Tkinter", "Saved successfully!")
                                break
                            elif (M.get() == 0) and (F.get() == 1):
                                  
                                cursor.execute("""
                                INSERT INTO Students(studentId,name,age,gender,height,weight)
                                VALUES (?,?,?,?,?,?)""",(StudentIds,Names,Ages,'f',Heights,Weights))
                                conn.commit()
                                cursor.execute("""
                                INSERT INTO Activities(studentId,name,activity_type,activity,extra_activity)
                                VALUES (?,?,?,?,?)
                                """,(StudentIds,Names,Activitytypes,Activitys,Extras))
                                conn.commit()
                                clearfields()
                        
                                messagebox.showinfo("Tkinter", "Saved successfully!")
                                break
                        

                        except pyodbc.DataError:
                            try:
                                int(Heights)
                                break
                            except :
                                messagebox.showinfo("Tkinter", "Height must be integer")
                                break
                            else:
                                try:
                                    if (M.get() == 1) and (F.get() == 0):
                                          
                                        cursor.execute("""
                                        INSERT INTO Students(studentId,name,age,gender,height,weight)
                                        VALUES (?,?,?,?,?,?)""",(StudentIds,Names,Ages,'m',Heights,Weights))
                                        conn.commit()
                                        cursor.execute("""
                                        INSERT INTO Activities(studentId,name,activity_type,activity,extra_activity)
                                        VALUES (?,?,?,?,?)
                                        """,(StudentIds,Names,Activitytypes,Activitys,Extras))
                                        conn.commit()
                                        clearfields()
                                
                                        messagebox.showinfo("Tkinter", "Saved successfully!")
                                        break
                                    elif (M.get() == 0) and (F.get() == 1):
                                          
                                        cursor.execute("""
                                        INSERT INTO Students(studentId,name,age,gender,height,weight)
                                        VALUES (?,?,?,?,?,?)""",(StudentIds,Names,Ages,'f',Heights,Weights))
                                        conn.commit()
                                        cursor.execute("""
                                        INSERT INTO Activities(studentId,name,activity_type,activity,extra_activity)
                                        VALUES (?,?,?,?,?)
                                        """,(StudentIds,Names,Activitytypes,Activitys,Extras))
                                        conn.commit()
                                        clearfields()
                                
                                        messagebox.showinfo("Tkinter", "Saved successfully!")
                                        break
                                except pyodbc.DataError:
                                    try:
                                        int(Weights)
                                        break
                                    except :
                                        messagebox.showinfo("Tkinter", "Weight must be integer")
                                        break
                                    else:
                                        try:
                                            if (M.get() == 1) and (F.get() == 0):
                                                  
                                                cursor.execute("""
                                                INSERT INTO Students(studentId,name,age,gender,height,weight)
                                                VALUES (?,?,?,?,?,?)""",(StudentIds,Names,Ages,'m',Heights,Weights))
                                                conn.commit()
                                                cursor.execute("""
                                                INSERT INTO Activities(studentId,name,activity_type,activity,extra_activity)
                                                VALUES (?,?,?,?,?)
                                                """,(StudentIds,Names,Activitytypes,Activitys,Extras))
                                                conn.commit()
                                                clearfields()
                                        
                                                messagebox.showinfo("Tkinter", "Saved successfully!")
                                                break
                                            elif (M.get() == 0) and (F.get() == 1):
                                                  
                                                cursor.execute("""
                                                INSERT INTO Students(studentId,name,age,gender,height,weight)
                                                VALUES (?,?,?,?,?,?)""",(StudentIds,Names,Ages,'f',Heights,Weights))
                                                conn.commit()
                                                cursor.execute("""
                                                INSERT INTO Activities(studentId,name,activity_type,activity,extra_activity)
                                                VALUES (?,?,?,?,?)
                                                """,(StudentIds,Names,Activitytypes,Activitys,Extras))
                                                conn.commit()
                                                clearfields()
                                        
                                                messagebox.showinfo("Tkinter", "Saved successfully!")
                                                break
                                        except pyodbc.DataError:

                                                    try:
                                                        int(StudentIds)
                                                        break
                                                    except  :
                                                        messagebox.showinfo("Tkinter", "StudentId must be integer")
                                                        break
                                                    else:
                                                        try:
                                                            if (M.get() == 1) and (F.get() == 0):
                                                                  
                                                                cursor.execute("""
                                                                INSERT INTO Students(studentId,name,age,gender,height,weight)
                                                                VALUES (?,?,?,?,?,?)""",(StudentIds,Names,Ages,'m',Heights,Weights))
                                                                conn.commit()
                                                                cursor.execute("""
                                                                INSERT INTO Activities(studentId,name,activity_type,activity,extra_activity)
                                                                VALUES (?,?,?,?,?)
                                                                """,(StudentIds,Names,Activitytypes,Activitys,Extras))
                                                                conn.commit()
                                                                clearfields()
                                                        
                                                                messagebox.showinfo("Tkinter", "Saved successfully!")
                                                                break
                                                            elif (M.get() == 0) and (F.get() == 1):
                                                                  
                                                                cursor.execute("""
                                                                INSERT INTO Students(studentId,name,age,gender,height,weight)
                                                                VALUES (?,?,?,?,?,?)""",(StudentIds,Names,Ages,'f',Heights,Weights))
                                                                conn.commit()
                                                                cursor.execute("""
                                                                INSERT INTO Activities(studentId,name,activity_type,activity,extra_activity)
                                                                VALUES (?,?,?,?,?)
                                                                """,(StudentIds,Names,Activitytypes,Activitys,Extras))
                                                                conn.commit()
                                                                clearfields()
                                                        
                                                                messagebox.showinfo("Tkinter", "Saved successfully!")
                                                                break
                                                        except pyodbc.DataError:
                                                            try:
                                                                int(Activitytypes)
                                                                messagebox.showinfo("Tkinter", "Activitytype must be string")
                                                                break
                                                            except ValueError:
                                                                try:
                                                                    if (M.get() == 1) and (F.get() == 0):
                                                                          
                                                                        cursor.execute("""
                                                                        INSERT INTO Students(studentId,name,age,gender,height,weight)
                                                                        VALUES (?,?,?,?,?,?)""",(StudentIds,Names,Ages,'m',Heights,Weights))
                                                                        conn.commit()
                                                                        cursor.execute("""
                                                                        INSERT INTO Activities(studentId,name,activity_type,activity,extra_activity)
                                                                        VALUES (?,?,?,?,?)
                                                                        """,(StudentIds,Names,Activitytypes,Activitys,Extras))
                                                                        conn.commit()
                                                                        clearfields()
                                                                        
                                                                        messagebox.showinfo("Tkinter", "Saved successfully!")
                                                                        break
                                                                    elif (M.get() == 0) and (F.get() == 1):
                                                                          
                                                                        cursor.execute("""
                                                                        INSERT INTO Students(studentId,name,age,gender,height,weight)
                                                                        VALUES (?,?,?,?,?,?)""",(StudentIds,Names,Ages,'f',Heights,Weights))
                                                                        conn.commit()
                                                                        cursor.execute("""
                                                                        INSERT INTO Activities(studentId,name,activity_type,activity,extra_activity)
                                                                        VALUES (?,?,?,?,?)
                                                                        """,(StudentIds,Names,Activitytypes,Activitys,Extras))
                                                                        conn.commit()
                                                                        clearfields()
                                                                        
                                                                        messagebox.showinfo("Tkinter", "Saved successfully!")
                                                                        break
                                                                except pyodbc.DataError:
                                                                    try:
                                                                        int(Activitys)
                                                                        messagebox.showinfo("Tkinter", "Activity must be string")
                                                                        break
                                                                    except ValueError:
                                                                        try:
                                                                            if (M.get() == 1) and (F.get() == 0):
                                                                                  
                                                                                cursor.execute("""
                                                                                INSERT INTO Students(studentId,name,age,gender,height,weight)
                                                                                VALUES (?,?,?,?,?,?)""",(StudentIds,Names,Ages,'m',Heights,Weights))
                                                                                conn.commit()
                                                                                cursor.execute("""
                                                                                INSERT INTO Activities(studentId,name,activity_type,activity,extra_activity)
                                                                                VALUES (?,?,?,?,?)
                                                                                """,(StudentIds,Names,Activitytypes,Activitys,Extras))
                                                                                conn.commit()
                                                                                clearfields()
                                                                                
                                                                                messagebox.showinfo("Tkinter", "Saved successfully!")
                                                                                break
                                                                            elif (M.get() == 0) and (F.get() == 1):
                                                                                  
                                                                                cursor.execute("""
                                                                                INSERT INTO Students(studentId,name,age,gender,height,weight)
                                                                                VALUES (?,?,?,?,?,?)""",(StudentIds,Names,Ages,'f',Heights,Weights))
                                                                                conn.commit()
                                                                                cursor.execute("""
                                                                                INSERT INTO Activities(studentId,name,activity_type,activity,extra_activity)
                                                                                VALUES (?,?,?,?,?)
                                                                                """,(StudentIds,Names,Activitytypes,Activitys,Extras))
                                                                                conn.commit()
                                                                                clearfields()
                                                                                
                                                                                messagebox.showinfo("Tkinter", "Saved successfully!")
                                                                                break
                                                                        except pyodbc.DataError:
                                                                            try:
                                                                                int(Extra)
                                                                                messagebox.showinfo("Tkinter", "Extra must be string")
                                                                                break
                                                                            except ValueError:

                                                                                    if (M.get() == 1) and (F.get() == 0):
                                                                                          
                                                                                        cursor.execute("""
                                                                                        INSERT INTO Students(studentId,name,age,gender,height,weight)
                                                                                        VALUES (?,?,?,?,?,?)""",(StudentIds,Names,Ages,'m',Heights,Weights))
                                                                                        conn.commit()
                                                                                        cursor.execute("""
                                                                                        INSERT INTO Activities(studentId,name,activity_type,activity,extra_activity)
                                                                                        VALUES (?,?,?,?,?)
                                                                                        """,(StudentIds,Names,Activitytypes,Activitys,Extras))
                                                                                        conn.commit()
                                                                                        clearfields()
                                                                                        
                                                                                        messagebox.showinfo("Tkinter", "Saved successfully!")
                                                                                        break
                                                                                    elif (M.get() == 0) and (F.get() == 1):
                                                                                          
                                                                                        cursor.execute("""
                                                                                        INSERT INTO Students(studentId,name,age,gender,height,weight)
                                                                                        VALUES (?,?,?,?,?,?)""",(StudentIds,Names,Ages,'f',Heights,Weights))
                                                                                        conn.commit()
                                                                                        cursor.execute("""
                                                                                        INSERT INTO Activities(studentId,name,activity_type,activity,extra_activity)
                                                                                        VALUES (?,?,?,?,?)
                                                                                        """,(StudentIds,Names,Activitytypes,Activitys,Extras))
                                                                                        conn.commit()
                                                                                        clearfields()
                                                                                        
                                                                                        messagebox.showinfo("Tkinter", "Saved successfully!")
                                                                                        break




