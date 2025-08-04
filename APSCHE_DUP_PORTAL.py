def  main_menu():
    print("------------APSCHE---------")
    print("AP EAPCET 2025 ADMISSIONS DASHBOARD :")
    print(""" 1. Student Login
          2. Registration
          3. print Verified Application
          4. Web Options Entry
          5. Seat Allotment
          6. Print Allotment Order
          7. Self Reporting
          8. Exit """)
name= ""
dob=0
hall_ticket=0
def student_login(): 
    global name,dob,hall_ticket
    name = input("Enter your name: ")
    dob= int(input("Login Credential : "))
    hall_ticket=int(input("Enter Your Hall Ticket No : "))
    college = input("Enter your college name: ")
    print("Login Credential Is DOB ")
    print("Login Mandatory for further process")
    print("Login Successful")
def registration():   
    safety=int(input("Enter Your DOB: "))
    if safety==dob :
        print("Authentication Verified")
        print("Registration Successful")
    else:
        print("Authentication Failed. Please try again.")
def print_verified_application():
    safety1= int(input("Enter your Hall Ticket Number: "))
    safety2= int(input("Enter your DOB: "))
    if safety1 == hall_ticket and safety2 == dob:
        print("Authentication Succesfully Verified")

        print("----APSCHE 2025 ADMISSIONS DASHBOARD----")
        print("----AP EAPCET 2025 APPLICATION FORM----")
        print(f"Candidate Name :{name} ")
        print(f"Date of Birth :{dob} ")
        print(f"Hall Ticket Number :{hall_ticket} ")
        print(" Student Stream Mathematics")

    else:
        print("Authentication Failed. Please try again.")
preferences_list=[]
def web_options_entry():
    global preferences_list
    safety1= int(input("Enter your Hall Ticket Number: "))
    safety2= int(input("Enter your DOB: "))
    if safety1 == hall_ticket and safety2 == dob:
        print("Authentication Succesfully Done")
        nums= int(input("Number Of Preferences : "))
        for i in range (nums) :
            pref= input(f"Enter Preference {i+1} : ")
            preferences_list.append(pref)
        print("Web Options Saved Succesfully")
        print("For Cross Checking")
        print(preferences_list)
    else:
        print("Authentication failed")
caste = "" 
course="" 
student_rank=0
allotted_college=""
multiplier=0
def seat_allotment():
    safety1= int(input("Enter your Hall Ticket Number: "))
    safety2= int(input("Enter your DOB: "))
    global caste,course,student_rank,allotted_college,multiplier
    if safety1 == hall_ticket and safety2 == dob:
        print("Authentication Succesfully Done")
        caste=input("Enter Your Caste : ")
        course=input("Enter Your Course : ")
        colleges_list=["JNTK","AUCE","GVPCE","VITAPU","SRMAPU"]
        colleges_cutoffs=[1200,600,2400,2890,3500]
        if caste=="OC" :
            multiplier=1.00
        elif caste=="EWS" :
            multiplier=1.25
        elif caste=="OBC":
            multiplier=2.00
        elif caste=="SC":
            multiplier=3.50
        elif caste=="ST":
            multiplier=4.00
        else :
            print("Invalid Caste Input")
            multiplier=0.00
        
        if course=="CSE" :
            relief= 0
        elif course=="CSM":
            relief=100
        elif course=="CSD":
            relief=200
        elif course=="ECE":
            relief=300
        elif course=="EEE":
            relief=500
        elif course=="MEC":
            relief=1000
        elif course=="CIV":
            relief=1500
        else :
            print("Invalid Course ><")
            relief=0
        
        student_rank=int(input("Enter Your APEAPCET RANK : ")) 
        for college in preferences_list:
            college_idx=colleges_list.index(college)
            college_cutoff=colleges_cutoffs[college_idx]
            extremal_cutoff=college_cutoff*multiplier 
            extremal_cutoff+=relief 
            if student_rank<=extremal_cutoff :
                    allotted_college=college 
                    print(f"Congrats , College Allotted Is {allotted_college}")
                    print("Print Allotment Order")
                    break 
        else :
                print("No College Is Allotted")
                print("Try Again In Further Rounds By Changing Web Options ")
                allotted_college=""
    else :
        print("Authentication Failed , Try Again")

def print_allotment_order():
    safety1=int(input("Enter Your  Hall  Ticket Number : "))
    safety2=int(input("Enter Your DOB : "))
    if safety1==hall_ticket and safety2==dob :
        print("Authentication Succesfuly Done")
        if allotted_college!="" :
            print("Allotment Order ")
            print(""" -------------APSCHE 2025 ------------""")
            print("----APEAPCET2025 SEAT ALLOTMENT ORDER-------")
            print(f"This Is To Order The Student {name} And Confirm")
            print("That As Per The Web Options Candidate Has Exercised")
            print(f"Is Allotted Provisionally To {allotted_college}")
            print(f"Under The Course {course}, The Candidate As Mentioned")
            print("Prior To  The Guidelines Issued By The State Government  ")
            print("The Candidate Has To Read And Abide All The Instructtions ")
            print("With Care And Prevent From Misuse Of Govt. Seat")
            print("Joining Should Be Up To date")
            print("--------------APEAPCET--APSCHE--2025----------")
        elif allotted_college=="" :
            print(f"Dear {name} , In The First Round You Havent Been Allotted A Seat ")
        else :
            print("0")     
    else :
        print("Authentication Mismatch")
def self_reporting():
    safety1=int(input("Enter Hallticket No : "))
    safety2=int(input("Enter Your  DOB : "))
    if safety1==hall_ticket and safety2==dob :
        print("Authentication Verified ")
        if allotted_college!="" :
            print("Welcome To Self Reporting Dashboard")
            print("Verify Your Details And Submit Them For College Submission")
            print("Firstly,Are You Accepting Your College")
            deci=input("Do You Accept the Allotted  College  ? :  ")
            if deci=="yes" :
                print("Submission Form Below ")
                print(f"Candidate Name : {name}")
                print(f"Candidate College Allotted : {allotted_college}")
                print(f"Candidate Hall Ticket No APEAPCET2025 : {hall_ticket}")
                print(f"Candidate Reservation :  {caste}")
                print("Date Of Birth Is Not Stored Due To Security Reasons")
                print("------------APSCHE----APEAPCET-----2025-----")
                print("---------Self Reporting Panel --------------")
                deci2=input("Are The Details Exact : ")
                if deci2=="yes":
                    print("Self Reporting Succesfully Done")
                    print("Congrats a way Ahead")
                    print("Student Sincerely APEAPCET and APSCHE Team")
                else : 
                    print("Self Reporting Failed")
            else :
                print("College Seat Floated")
        else :
            print("Authentication Failed")
def exit():
    print("-----------------APEAPCET2025----------------")
    print("ANDHRA PRADESH STATE COUNCIL OF HIGHER EDUCATION")
    print("WISH YOU THE SUCCESS ")
    print("Portal Program Terminated")

student_login()
registration()
print_verified_application()
web_options_entry()
seat_allotment()
self_reporting()
exit()
        
        
            
        






        
        
    



   






    










