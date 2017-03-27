games_cart=["Call of Duty","GTA 5","Resident Evil","FIFA 17","PES 2017","F12017","Need for Speed"]
user = [0,1,2]
name = ["Admin","Jefferson","Sheila"]
email =["admin@email.com","Jeffersonimmanuel5@gmail.com","sheilakanishta@gmail.com"]
contact = [123,9962627568,9941441689]
def null():
        test()
def order():
    pass
def new_user():
    while True:
        user1 = raw_input("Enter the ID you want must be less than 100:  ")
        try:
            if (user1.isaplha()) or (user1 == '') or (user1 < 100):
                raise Warning("!!!!!!")
        except Exception,ValueError:
            print "ID must be less than 100 empty/characters not allowed"
            continue
        else:
            user.append(user1)
            break
    while True:
        name1 = raw_input("Enter your name: ")
    
        try:
            if(name1 == int) or (name1 == '') or (name >= str(10)):
                raise Warning("!!!!!")
        except Exception:
            print "Name should not be number and empty.\n""Should be less than 10 characters"
            continue
        else:
            name.append(name1)
            break
                
    
    while True:   
        email1 = raw_input("Enter your email id:")
    
        try:
            if(email1 == ''):
                raise Warning("!!!!!")
        except Exception:
            print "Email should not be empty."
            continue
        else:
            email.append(email1)
            break
    while True:    
        contact1 = raw_input("Enter your contact number:")
    
        try:
            if(contact1 == '') or (contact1 == str) or (contact1 > str(11)):
                raise Warning("!!!!!")
        except Exception:
            print "Contact number should be 10 digits."
            continue
        else:
            contact.append(contact1)
            break
def User():
    print "Type 1 if you are an existing user or 2 for user creation"
    type = raw_input("Enter your choice 1 or 2: ")
    if (type == str(1)):
            test()
    elif (type == str(2)):
            new_user()
    else:
            (id is '') or (id <=0) or (id == str)
            print "Invalid entry"
            User()   
            
        
def test():
        id = int(raw_input("Enter the ID for verification: "))
        try:
            if (id is '') or (id <= 0) or (id > 100):
                print"Please enter your correct ID\n"
                print "Dont enter 0 or negative numbers"
                raise Exception
        except Exception as e:
            print "Please enter the valid ID..Thanks"
            null()
        else:
            for i in user:
                if (i == str(id)):
                    validation = user.index(i)
                    print "Welcome to the shop:",(name[validation])
                    print "Your registered email id is :",(email[validation])
                    print "Your registered contact number is: ",(contact[validation])
                    order()
User()
test()
