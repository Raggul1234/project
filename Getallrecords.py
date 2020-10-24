



def getallrecords():
    t=tree.get_children()
    for f in t:
        tree.delete(f)
    cursor.execute("""select A.name,A.age,A.gender,A.height,A.weight,A.studentId,B.activity
    from Students A inner join Activities B on A.studentId=B.studentId""")
    records=cursor.fetchall()
    for row in records:
        tree.insert("", 3, text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
        tree.pack(side=tk.TOP,fill=tk.X)
def Search():
 
        Names= Name.get()
        Ages= Age.get()

        Heights= Height.get()
        Weights= Height.get()
        StudentIds= StudentId.get()
        Activitytypes=Activitytype.get()
        Activitys=Activity.get()
        Extras=Extra.get()

        

# clearing the tree
       
        t=tree.get_children()
        for f in t:
            tree.delete(f)
        

#Search starts
            

        if len(Names)!=0:
            cursor.execute("""select A.name,A.age,A.gender,A.height,A.weight,A.studentId,B.activity
            from Students A inner join Activities B on A.StudentId=B.StudentId where A.Name like(?)""",(Names))
            records=cursor.fetchall()
            for row in records:
                tree.insert("", 3, text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
                tree.pack(side=tk.TOP,fill=tk.X)
                    
		
        elif  len(Ages)!=0:
            cursor.execute("""select A.name,A.age,A.gender,A.height,A.weight,A.studentId,B.activity
            from Students A inner join Activities B on A.StudentId=B.StudentId where A.Age like(?)""",(Ages))
            records=cursor.fetchall()
            for row in records:
                tree.insert("", 3, text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
                tree.pack(side=tk.TOP,fill=tk.X)


        elif (M.get() == 1) and (F.get() == 0):
            cursor.execute("""select A.name,A.age,A.gender,A.height,A.weight,A.studentId,B.activity
            from Students A inner join Activities B on A.StudentId=B.StudentId where A.Gender like 'm'""")
            records=cursor.fetchall()
            for row in records:
                tree.insert("", 3, text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
                tree.pack(side=tk.TOP,fill=tk.X)
        elif (M.get() == 0) and (F.get() == 1):
            cursor.execute("""select A.name,A.age,A.gender,A.height,A.weight,A.studentId,B.activity
            from Students A inner join Activities B on A.StudentId=B.StudentId where A.Gender like 'f'""")
            records=cursor.fetchall()
            for row in records:
                tree.insert("", 3, text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
                tree.pack(side=tk.TOP,fill=tk.X)

        elif  len(Heights)!=0:
            cursor.execute("""select A.name,A.age,A.gender,A.height,A.weight,A.studentId,B.activity
            from Students A inner join Activities B on A.StudentId=B.StudentId where A.Height like(?)""",(Heights))
            records=cursor.fetchall()
            for row in records:
                tree.insert("", 3, text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
                tree.pack(side=tk.TOP,fill=tk.X)          


        elif  len(Weights)!=0:
            cursor.execute("""select A.name,A.age,A.gender,A.height,A.weight,A.studentId,B.activity
            from Students A inner join Activities B on A.StudentId=B.StudentId where A.weight like(?)""",(Weights))
            records=cursor.fetchall()
            for row in records:
                tree.insert("", 3, text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
                tree.pack(side=tk.TOP,fill=tk.X)


        elif  len(StudentIds)!=0:
            cursor.execute("""select A.name,A.age,A.gender,A.height,A.weight,A.studentId,B.activity
            from Students A inner join Sports B on A.StudentId=B.StudentId where A.StudentId like(?)""",(Rollnos))
            records=cursor.fetchall()
            for row in records:
                tree.insert("", 3, text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
                tree.pack(side=tk.TOP,fill=tk.X)


        elif  len(Activitytypes)!=0:
            cursor.execute("""select A.name,A.age,A.gender,A.height,A.weight,A.studentId,B.activity
            from Students A inner join Activities B on A.StudentId=B.StudentId where B.activitytypes like(?)""",(Activitytypes))
            records=cursor.fetchall()
            for row in records:
                tree.insert("", 3, text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
                tree.pack(side=tk.TOP,fill=tk.X)

                
        elif  len(Activitys)!=0:
            cursor.execute("""select A.name,A.age,A.gender,A.height,A.weight,A.studentId,B.activity
            from Students A inner join Activities B on A.StudentId=B.StudentId where B.activity like(?)""",(Activitys))
            records=cursor.fetchall()
            for row in records:
                tree.insert("", 3, text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
                tree.pack(side=tk.TOP,fill=tk.X)
                

        elif  len(Extras)!=0:
            cursor.execute("""select A.name,A.age,A.gender,A.height,A.weight,A.studentId,B.activity
            from Students A inner join Activities B on A.StudentId=B.StudentId where B.extra like(?)""",(estras))
            records=cursor.fetchall()
            for row in records:
                tree.insert("", 3, text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
                tree.pack(side=tk.TOP,fill=tk.X)

        else:
            
            messagebox.showinfo("Tkinter", "Atleast one search criteria must be given!")




