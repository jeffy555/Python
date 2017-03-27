Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> shop_cart=["Call of Duty","WWE","FIFA","PES 2017","Resident evil","Splinter Cell","Hitman"]
#user = {469899:["Jefferson","jeffersonimmanuel5@gmail.com",9962627568],469878:["Angela","Angela@gmail.com",9941441689]}
#testing
user = [0,1,2]
name = ["Admin","Jefferson","Sheila"]
email =["admin@email.com","Jeffersonimmanuel5@gmail.com","sheilakanishta@gmail.com"]
contact = (123,9962627568,9941441689)
def null():
        test()
def order():
    pass
def test():
        id = int(raw_input("Enter the ID for verification: "))
        try:
            if (id is '') or (id <= 0) or (id > 3):
                print"Please enter your correct ID\n"
                print "Dont enter 0 or negative numbers"
                raise Exception
        except Exception as e:
            print "Please enter the valid ID..Thanks"
            null()
        else:
            for i in user:
                if (id == i):
                    print "Welcome to the shop:",(name[id])
                    print "Your registered email id is :",(email[id])
                    print "Your registered contact number is: ",(contact[id])
                    order()
test()





