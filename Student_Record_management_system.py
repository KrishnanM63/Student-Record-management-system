FILE_NAME='krish.txt'
import os


def insert_studen():
        name=input("enter your name")
        age=int(input("enter your age"))
        roll=int(input("enter your roll"))
        with open(FILE_NAME,"a") as f:
            f.writelines(f"{name},{age},{roll}\n")
            print("✅Student Add successfully")
def  view_studen():
      if not os.path.exists(FILE_NAME):
            print("⚠️Record Not fount")
            return
      with open(FILE_NAME,"r") as f:
          if not f.readline:
              print("⚠️ No records to display.\n")
      
          print("Name \t age \t roll")
          print("-"*25)
           
          for i in f:
               
                name,age,roll=i.strip().split(",")
                print(f"{name}\t{age}\t{roll}")
def search_student():
    
    search=input("enter your serach").strip()
    fount=False

        
    with open (FILE_NAME,"r") as f:
         for i in f:
             name,age,roll=i.strip().split(",")
             if search==roll:
                 print(f"name  {name}")
                 print(f"age   {age}")
                 print(f"roll  {roll}")
                 fount=True
                 break 
         if not fount:
             print("Student Not Fount⚠️")
def  update_student() :
           
    rollnum=input("enter your roll number:").strip()
    updated=False
    
    
    if not os.path.exists(FILE_NAME):
            print("⚠️Record Not fount")
            return
    

    new_record=[]
    with open(FILE_NAME,"r") as f:
        for i in f:
            name,age,roll=i.strip().split(",")
            if rollnum==roll:
                name=input("enter new name")
                age=int(input("enter your new age"))
                roll=int(input("enter your new roll"))
                new_record.append(f"{name},{age},{roll}\n")
                updated=True
               
            else:
                new_record.append(i)
    with open(FILE_NAME,"w") as f:
        f.writelines(new_record)
        if updated:
                print("✅ Student record updated.\n")
        else:
             print("❌ Student not found.\n")
             
def   delete_student() :
    del_id=input("enter your deleted id").strip()
    deleted_record=False
    
    if not os.path.exists(FILE_NAME):
            print("⚠️Record Not fount")
            return
    new_record=[]
    with open(FILE_NAME,"r") as f:
        for i in f:
            name,age,roll=i.strip().split(",")
            if del_id==roll:
                deleted_record=True
                continue
            new_record.append(i)
               
    with open(FILE_NAME,"w") as f:
        f.writelines(new_record)
        if deleted_record:
                print("✅ Student record updated.\n")
        else:
             print("❌ Student not found.\n")            
                
def menu():
    
    while True:
        print("===Student Record management system===")
        print("1.Add student ")
        print("2.view students")
        print("3.search Studen Record")
        print("4.Update Student Record")
        print("5.Delete student Record")
        print("6.Exit")
        
        
        user_input=int(input("enter your choice"))
        
        if user_input==1:
            insert_studen()
        elif user_input==2:
            view_studen() 
        elif user_input==3:
            search_student()
        elif user_input==4:
            update_student()
        elif user_input==5:
            delete_student()
            break        
                
        
menu()    
