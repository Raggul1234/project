

def Update_Function(StudentIds,Names,Ages,Genders,Heights,Weights,Activitytypes,Activitys,Extras):
    def clear_fielads():
        Name1.delete(0 ,tk.END)
        Age1.delete(0 ,tk.END)
        Gender1.delete(0 ,tk.END)
        Height1.delete(0 ,tk.END)
        Weight1.delete(0 ,tk.END)
        StudentId1.delete(0 ,tk.END)
        Activitytype1.delete(0 ,tk.END)
        Activity1.delete(0 ,tk.END)
        Extra1.delete(0 ,tk.END)
    while True:
        
            if len(Names)==0:
                messagebox.showinfo("Tkinter", "Name cannot be empty")
                break
            elif len(Ages)==0:
                messagebox.showinfo("Tkinter", "Age cannot be empty")
                break
            elif len(Genders)==0:
                messagebox.showinfo("Tkinter", "Genders cannot be empty")
                break
            elif len(StudentIds)==0:
                messagebox.showinfo("Tkinter", "StudentId cannot be empty")
                break
            elif len(Names)==0 and len(Ages)==0 and len(Gender)==0 and len(StudentIds)==0:
                messagebox.showinfo("Tkinter", "Atleast Name,Age,Gender and StudentId must be given!!")
                break
            try:
                
                
                int(Names)
                messagebox.showinfo("Tkinter", "Name must be string")
                break
            except ValueError:
                try:
                    cursor.execute("""delete Students
                            where StudentId = (?)
                            """,(StudentIds))
                    conn.commit()
                    cursor.execute("""delete Activities
                                where StudentId = (?)
                                """,(StudentIds))
                    
                    conn.commit()
                    
                                             
                    cursor.execute("""
                    INSERT INTO Students(studentId,name,age,gender,height,weight)
                    VALUES (?,?,?,?,?,?)""",(StudentIds,Names,Ages,Genders,Heights,Weights))
                    conn.commit()
                    cursor.execute("""
                    INSERT INTO Activities(studentId,name,activity_type,activity,extra_activity)
                    VALUES (?,?,?,?,?)
                    """,(StudentIds,Names,Activitytypes,Activitys,Extras))
                    conn.commit()
                    clear_fields()
                        
                    messagebox.showinfo("Tkinter", "Updated successfully!")
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

                                  
                            cursor.execute("""
                            INSERT INTO Students(studentId,name,age,gender,height,weight)
                            VALUES (?,?,?,?,?,?)""",(StudentIds,Names,Ages,Genders,Heights,Weights))
                            conn.commit()
                            cursor.execute("""
                            INSERT INTO Activities(studentId,name,activity_type,activity,extra_activity)
                            VALUES (?,?,?,?,?)
                            """,(StudentIds,Names,Activitytypes,Activitys,Extras))
                            conn.commit()
                            clear_fields()
                        
                            messagebox.showinfo("Tkinter", "Updated successfully!")
                            break
                           

                        except pyodbc.DataError:
                            try:
                                int(Genders)
                                messagebox.showinfo("Tkinter", "enter m for male and f for female")
                                break
                            except ValueError:
                                try:
                                    cursor.execute("""delete Students
                                            where StudentId = (?)
                                            """,(StudentIds))
                                    conn.commit()
                                    cursor.execute("""delete Activities
                                                where StudentId = (?)
                                                """,(StudentIds))
                                    
                                    conn.commit()
                                    
                                                             
                                    cursor.execute("""
                                    INSERT INTO Students(studentId,name,age,gender,height,weight)
                                    VALUES (?,?,?,?,?,?)""",(StudentIds,Names,Ages,Genders,Heights,Weights))
                                    conn.commit()
                                    cursor.execute("""
                                    INSERT INTO Activities(studentId,name,activity_type,activity,extra_activity)
                                    VALUES (?,?,?,?,?)
                                    """,(StudentIds,Names,Activitytypes,Activitys,Extras))
                                    conn.commit()
                                    clear_fields()
                                        
                                    messagebox.showinfo("Tkinter", "Updated successfully!")
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

                                                  
                                            cursor.execute("""
                                            INSERT INTO Students(studentId,name,age,gender,height,weight)
                                            VALUES (?,?,?,?,?,?)""",(StudentIds,Names,Ages,Genders,Heights,Weights))
                                            conn.commit()
                                            cursor.execute("""
                                            INSERT INTO Activities(studentId,name,activity_type,activity,extra_activity)
                                            VALUES (?,?,?,?,?)
                                            """,(StudentIds,Names,Activitytypes,Activitys,Extras))
                                            conn.commit()
                                            clear_fields()
                                        
                                            messagebox.showinfo("Tkinter", "Updated successfully!")
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

                                                          
                                                    cursor.execute("""
                                                    INSERT INTO Students(studentId,name,age,gender,height,weight)
                                                    VALUES (?,?,?,?,?,?)""",(StudentIds,Names,Ages,Genders,Heights,Weights))
                                                    conn.commit()
                                                    cursor.execute("""
                                                    INSERT INTO Activities(studentId,name,activity_type,activity,extra_activity)
                                                    VALUES (?,?,?,?,?)
                                                    """,(StudentIds,Names,Activitytypes,Activitys,Extras))
                                                    conn.commit()
                                                    clear_fields()
                                                
                                                    messagebox.showinfo("Tkinter", "Updated successfully!")
                                                    break
                                                except pyodbc.DataError:
                                                    try:
                                                        int(StudentIds)
                                                        break
                                                    except :
                                                        messagebox.showinfo("Tkinter", "StudentId must be integer")
                                                        break
                                                    else:
                                                        try:

                                                                  
                                                            cursor.execute("""
                                                            INSERT INTO Students(studentId,name,age,gender,height,weight)
                                                            VALUES (?,?,?,?,?,?)""",(StudentIds,Names,Ages,Genders,Heights,Weights))
                                                            conn.commit()
                                                            cursor.execute("""
                                                            INSERT INTO Activities(studentId,name,activity_type,activity,extra_activity)
                                                            VALUES (?,?,?,?,?)
                                                            """,(StudentIds,Names,Activitytypes,Activitys,Extras))
                                                            conn.commit()
                                                            clear_fields()
                                                        
                                                            messagebox.showinfo("Tkinter", "Updated successfully!")
                                                            break
                                                        except pyodbc.DataError:
                                                            try:
                
                
                                                                int(Activtytypes)
                                                                messagebox.showinfo("Tkinter", "Activity type must be string")
                                                                break
                                                            except ValueError:
                                                                try:
                                                                    cursor.execute("""delete Students
                                                                            where StudentId = (?)
                                                                            """,(StudentIds))
                                                                    conn.commit()
                                                                    cursor.execute("""delete Activities
                                                                                where StudentId = (?)
                                                                                """,(StudentIds))
                                                                    
                                                                    conn.commit()
                                                                    
                                                                                             
                                                                    cursor.execute("""
                                                                    INSERT INTO Students(studentId,name,age,gender,height,weight)
                                                                    VALUES (?,?,?,?,?,?)""",(StudentIds,Names,Ages,Genders,Heights,Weights))
                                                                    conn.commit()
                                                                    cursor.execute("""
                                                                    INSERT INTO Activities(studentId,name,activity_type,activity,extra_activity)
                                                                    VALUES (?,?,?,?,?)
                                                                    """,(StudentIds,Names,Activitytypes,Activitys,Extras))
                                                                    conn.commit()
                                                                    clear_fields()
                                                                        
                                                                    messagebox.showinfo("Tkinter", "Updated successfully!")
                                                                    break

                                                                          
                                                                except pyodbc.DataError:
                                                                    try:
                
                
                                                                        int(Activitys)
                                                                        messagebox.showinfo("Tkinter", "Activity must be string")
                                                                        break
                                                                    except ValueError:
                                                                        try:
                                                                            cursor.execute("""delete Students
                                                                                    where StudentId = (?)
                                                                                    """,(StudentIds))
                                                                            conn.commit()
                                                                            cursor.execute("""delete Activities
                                                                                        where StudentId = (?)
                                                                                        """,(StudentIds))
                                                                            
                                                                            conn.commit()
                                                                            
                                                                                                     
                                                                            cursor.execute("""
                                                                            INSERT INTO Students(studentId,name,age,gender,height,weight)
                                                                            VALUES (?,?,?,?,?,?)""",(StudentIds,Names,Ages,Genders,Heights,Weights))
                                                                            conn.commit()
                                                                            cursor.execute("""
                                                                            INSERT INTO Activities(studentId,name,activity_type,activity,extra_activity)
                                                                            VALUES (?,?,?,?,?)
                                                                            """,(StudentIds,Names,Activitytypes,Activitys,Extras))
                                                                            conn.commit()
                                                                            clear_fields()
                                                                                
                                                                            messagebox.showinfo("Tkinter", "Updated successfully!")
                                                                            break

                                                                                  
                                                                        except pyodbc.DataError:
                                                                            try:
                
                
                                                                                int(Extras)
                                                                                messagebox.showinfo("Tkinter", "Extra must be string")
                                                                                break
                                                                            except ValueError:
                                                                                try:
                                                                                    cursor.execute("""delete Students
                                                                                            where StudentId = (?)
                                                                                            """,(StudentIds))
                                                                                    conn.commit()
                                                                                    cursor.execute("""delete Activities
                                                                                                where StudentId = (?)
                                                                                                """,(StudentIds))
                                                                                    
                                                                                    conn.commit()
                                                                                    
                                                                                                             
                                                                                    cursor.execute("""
                                                                                    INSERT INTO Students(studentId,name,age,gender,height,weight)
                                                                                    VALUES (?,?,?,?,?,?)""",(StudentIds,Names,Ages,Genders,Heights,Weights))
                                                                                    conn.commit()
                                                                                    cursor.execute("""
                                                                                    INSERT INTO Activities(studentId,name,activity_type,activity,extra_activity)
                                                                                    VALUES (?,?,?,?,?)
                                                                                    """,(StudentIds,Names,Activitytypes,Activitys,Extras))
                                                                                    conn.commit()
                                                                                    clear_fields()
                                                                                        
                                                                                    messagebox.showinfo("Tkinter", "Updated successfully!")
                                                                                    break
                                                                                except:
                                                                                    pass

                                                                                          
                                                                                
                                            
                                            
                        
    

        
    





def Delete():
        x=StudentId.get()
        cursor.execute("""
        DELETE FROM Students
        WHERE StudentId = (?)""",(x))
        conn.commit()
        cursor.execute("""
        DELETE FROM Activities
        WHERE StudentId = (?)""",(x))
        conn.commit()
        clearfields()
        messagebox.showinfo("Tkinter", "Deleted successfully!")


def clearfields():
    Name.delete(0 ,tk.END)
    Age.delete(0 ,tk.END)
    G1.deselect()
    G2.deselect()
    Height.delete(0 ,tk.END)
    Weight.delete(0 ,tk.END)
    StudentId.delete(0 ,tk.END)
    Activitytype.delete(0 ,tk.END)
    Activity.delete(0 ,tk.END)
    Extra.delete(0 ,tk.END)



























