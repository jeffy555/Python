games_cart=["Call of Duty","GTA 5","Resident Evil","FIFA 17","PES 2017","F12017","Need for Speed"]
cost=[]
user = [0,1,2]
name = ["Admin","Jefferson","Sheila"]
email =["admin@email.com","Jeffersonimmanuel5@gmail.com","sheilakanishta@gmail.com"]
contact = [123,9962627568,9941441689]
def null():
        test()
def order():
    print games_cart
    while True:
        choice = raw_input("Please choose one item from the games cart: ")
        for game in games_cart:
            if (choice == '') or (choice.isdigit()):
                print "Enter an item from cart"
                continue
            elif (choice == game):
                value = games_cart.index(choice)
                print "You order is :",(games_cart[value])
                break
            else:
                print "Game unavailable"
                req = raw_input("Enter yes if you want to request :"+choice)
                if (req == yes):
                    request()
                else:
                        print "Please input the available items from the games_cart"
                        continue
            
def new_user():
    while True:
        user1 = raw_input("Enter the ID you want must be less than 100:  ")
        try:
            for i in user:
                if (user1 == str(i)) or user1.isalpha() or (user1 == '') or (user1 < 100):
                    raise Warning("!!!!!!")
        except Exception,ValueError:
            print "ID must be less than 100 empty/characters not allowed"
        else:
            user.append(user1)
            break
    while True:
        name1 = raw_input("Enter your name: ")
        try:
            for n in name:
                if (name1 == str(n)) or name1.isdigit() or (name1 == ''):
                        raise Warning("!!!!!")
                        continue
        except Exception:
            print "Name should not be number and empty.\n""Should be less than 10 characters"
            continue
        else:
            name.append(name1)
            break
                
    
    while True:   
        email1 = raw_input("Enter your email id:")
    
        try:
            for e in email:
                if(email1 == '') or (email1 == str(e)):
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
            for c in contact:
                if(contact1 == '') or contact1.isalpha() or (contact1 == str(c)):
                    raise Warning("!!!!!")
        except Exception:
            print "Contact number should be 10 digits."
            continue
        else:
            contact.append(contact1)
            break
def User():
    print "Type 1 if you are an existing user or 2 for user creation"
    while True:
        type = raw_input("Enter your choice 1 or 2: ")
        if (type == str(1)):
                test()
        elif (type == str(2)):
                new_user()
        else:
            (id is '') or (id <=0) or (id == str)
            print "Invalid entry"
              
            
        
def test():
        id = int(raw_input("Enter the ID for verification: "))
        try:
            if (id is '') or (id <= 0):
                print"Please enter your correct ID\n"
                print "Dont enter 0 or negative numbers"
                raise Exception
        except Exception as e:
            print "Please enter the valid ID..Thanks"
            null()
        else:
            for i in user:
                if (id == i):
                    validation = user.index(i)
                    print "Welcome to the shop:",(name[validation])
                    print "Your registered email id is :",(email[validation])
                    print "Your registered contact number is: ",(contact[validation])
                    order()
User()
test()
