from re import U
import time
import datetime
import csv 

def user():
    # user data storing csv file format 
    # user id ,user name ,password ,email,mobile number ,user type 
    # file name = user.csv
    


    def sign_in():
        f = open('user.csv','r')   # opening file 
        r = csv.reader(f)   # reader object 
        username = input('enter username : ')
        password = input("enter password : ")
        s = 0 
        for i in r :
            if i[1] == username and i[2] == password :
                print ("successfull sign in ! ")
                s = 0
            elif i[1] == username :
                print("invalid password for the user !")
                s = 1
            else :
                print("user not found please register !")
                s = 2
        
        f.close()

    def register(usertype):
        # user data storing csv file format 
        # user id ,user name ,password ,email,mobile number ,user type 
        # file name = user.csv
        f = open('user.csv','a')   # opening file 
        w = csv.writer(f)   # writer  object 
        user_id  = input('enter user id : ')
        username = input('enter username : ')
        password = input("enter password : ")
        email = input("enter your email id : ")
        mobile_number = input("enter your mobile number : ")
        L = [user_id,username,password,email,mobile_number,usertype]
        w.writerow(f)

        print("user registered successfully !")
        f.close()


    def sign_out():
        s = 3
        print("user signed out successfully !")
        

    def update():
        # user data storing csv file format 
        # user id ,user name ,password ,email,mobile number ,user type 
        # file name = user.csv
        f = open('user.csv','r')   # opening file 
        r = csv.reader(f)   # reader object 
        user_id = input("enter the user id whos details u want to update : ")
        c = 0
        for i in r:
            c+=1
            if i[0] == user_id :
                break 
        f.close ()
        # user data storing csv file format 
        # user id ,user name ,password ,email,mobile number ,user type 
        # file name = user.csv
        f = open('user.csv','r')   # opening file 
        r = csv.writer(f)   # reader object 
        data = []
        for i in r :
            data.append(i)
        f.close()
        # user data storing csv file format 
        # user id ,user name ,password ,email,mobile number ,user type 
        # file name = user.csv
        f = open('user.csv','w')   # opening file 
        w = csv.writer(f)   # writer  object 
        update = data[c-1]
        print("details of the user that u are about to update :")
        print(f'user id = {update[0]}, username = {update[1]} , user type = {update[-1]} ')
        what = input('''
        choose what do u want to update :
            [1] email
            [2] mobile number 
            [3] usertype 

        ''')
        if what == 1 :
            email = input ("enter email : ")
            data [c-1,3] = email
            print("updated successfully ! ")
            
            

        f.close()
    def display_details():
        pass
    def search ():
        pass

    pass 

def student():
    def issue():
        pass
    def renew ():
        pass
    def returnn ():
        pass
    
    pass
def staff():
    def issue():
        pass
    def renew ():
        pass
    def returnn ():
        pass

    pass
def librarian ():
    def add_book():
        pass
    def delete_book():
        pass
    def update_books():
        pass


    pass
def account():
    pass
def book ():
    pass


# main program 

# f = open ('account.csv','a' )
# w = csv.writer (f)
# f.close()