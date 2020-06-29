While True:
    username = input("enter username: ")
    
    password = input("enter password: ")
    
    if username == "Rdog" and password == "password":
        break
    else:
        print("WRONG")
    
#Break loop print 
print("Welcome!", username)
