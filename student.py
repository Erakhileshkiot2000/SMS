import os
import platform

global Studentlist  # Making ListStd As Super Global Variable
Studentlist = ["Akhilesh Yadav", "Shalesh Yadav",
           "Neelesh Yadav", "Abhinandan Yadav"]  # List Of Students


def manageStudent():  # Function For The Student Management System

    x = "#" * 30
    y = "=" * 28
    global bye  # Making Bye As Super Global Variable
    # Will Print GoodBye Message
    bye = "\n {}\n# {} #\n# ===>Thanks for vissitiing us <===  #\n# ===>I hope you will visit again<===  #\n# {} #\n {}".format(
        x, y, y, x)

    # Printing Welcome Message And options For This Program
    print(""" 
Enter 1 : To View Student's List 
Enter 2 : To Add New Student 
Enter 3 : To Search Student 
Enter 4 : To Remove Student 
		
		""")

    try:  # Using Exceptions For Validation
        # Will Take Input From User
        userInput = int(input("Please Select An Above Option to go ahead : "))
    except ValueError:
        exit("\nOye hello please enter on the basis of given option fields")  # Error Message
    else:
        print("\n")  # Print New Line

    # Checking Using Option
    if(userInput == 1):  # This Option Will Print List Of Students
        print("List of Students are :  \n")
        for students in Studentlist:
            print("  -----> {}".format(students))

    elif(userInput == 2):  # This Option Will Add New Student In The List
        newstudent = input("please Enter New Student: ")
        if(newstudent in Studentlist):  # This Condition Checking The New Student Is Already In List Ur Not
            print("\nThis Student {} Already Exists".format(
                newstudent))  # Error Message
        else:
            Studentlist.append(newstudent)
            print("\n=> New Student {} Successfully Add \n".format(newstudent))
            for students in Studentlist:    #this will print already existing as wel as newely added student
                print("=> {}".format(students))

    elif(userInput == 3):  # This Option Will Search Student From The student List
        searchstudent = input("please Enter Student Name To Search: ")
        if(searchstudent in Studentlist):  # This Condition Searching The Student
            print("\n=> Record Found Of Student {}".format(searchstudent))
        else:
            print("\n=> No Record Found Of Student {}".format(
                searchstudent))  # Error Message

    elif(userInput == 4):  # This Option Will Remove Student From The List
        removestudent = input("Enter Student Name To Remove: ")
        if(removestudent in Studentlist):  # This Condition Removing The Student From The List
            Studentlist.remove(removestudent)
            print("\n=> Student {} Successfully Deleted \n".format(removestudent))
            for students in Studentlist:
                print("=> {}".format(students))
        else:
            # Error Message
            print("\n=> No Record Found of This Student {}".format(removestudent))

    elif(userInput < 1 or userInput > 4):  # Validating User Option
        print("Please Enter Valid Option")  # Error Message

manageStudent()


def runAgain():  # Making Runable Problem1353
    runAgn = input("\nwant To Run Again Y/n: ")
    if(runAgn.lower() == 'y'):
        if(platform.system() == "Windows"):  # Checking User OS For Clearing The Screen
            print(os.system('cls'))
        else:
            print(os.system('clear'))
        manageStudent()
        runAgain()
    else:
        quit(bye)  # Print GoodBye Message And Exit The Program


runAgain()
