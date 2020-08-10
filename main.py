# Health Management System
# 3 client -  Harry Rohan and Hammad
# Total 6 Files
# Write Function Which Take Client Name As Input
# Press 1 For Rohan
# Press 2 For Harry
# Ask For Logging Activities
# Press 1 To Log Diet
# Press 2 To Log Exercise

def getdate():
    import datetime
    return datetime.datetime.now()


def askuserchoice():
    print("Who Is Using The System?\n"
          "Press 1 - For Rohan\n"
          "Press 2 - For Harry\n"
          "Press 3 - For Hammad\n")
    print("Your Choice: ")
    userchoice = int(input())
    return userchoice

def loggingsystem(f):
    print("What Do You Want To Log?\n")
    print("Press 1 To Log Diet\n"
          "Press 2 To Log Exercise\n")
    print("Your Choice: ")
    logchoice = int(input())

    if(logchoice == 1):

        print("Enter Your Diet: ")
        f.write("Diet:")
        f.write(" ")
        f.write(str(getdate()))
        f.write(" ")
        dietentered = input()
        dietentered = dietentered + "\n"
        f.write(dietentered)

    elif(logchoice == 2):
        print("Enter Your Exercise: ")
        f.write("Exercise:")
        f.write(" ")
        f.write(str(getdate()))
        f.write(" ")
        exentered = input()
        exentered = exentered + "\n"
        f.write(exentered)

def retrivalsystem(f):
    content = f.read()
    print(content)

loop = True

while(loop == True):
    print("-----********------\n"
          "Press 1 To Log\n"
          "Press 2 To Retrieve\n"
          "Press 3 To Exit The Program\n"
          "-----********------")
    print("Your Choice: ",end="")
    choice = int(input())

    if(choice == 1):
        print("Logging Service Working")
        userchoice = askuserchoice()
        if userchoice == 1:
            print("Working for Rohan")
            f = open("Rohan.txt","a")
            loggingsystem(f)
            f.close()
        elif userchoice == 2:
            print("working for harry")
            f = open("Harry.txt", "a")
            loggingsystem(f)
            f.close()
        else:
            print("working for hammad")
            f = open("Hammad.txt", "a")
            loggingsystem(f)
            f.close()
    elif(choice == 2):
        print("Retrieval Service Working")
        userchoice = askuserchoice()
        if (userchoice == 1):
            print("Working for Rohan")
            f = open("Rohan.txt", "r")
            retrivalsystem(f)
            f.close()
        elif(userchoice == 2):
            print("working for harry")
            f = open("Harry.txt", "r")
            retrivalsystem(f)
            f.close()

        else:
            print("working for hammad")
            f = open("Hammad.txt", "r")
            retrivalsystem(f)
            f.close()
    else:
        loop = False




