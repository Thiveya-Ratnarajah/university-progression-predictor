# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID : 20518970
# Date : 04/12/2023

# I hereby confirm that the codes in this document are referenced from the following sources;
# w3schools website : https://www.w3schools.com/python/
# geeksforgeeks website : https://www.geeksforgeeks.org/how-to-use-while-true-in-python/
# UOW lecture slides from week 1 to week 9; specially concerned topics: Python Exception Handling, While Loop,String formatting, Lists, User-Defined Functions, Global & Special Variables.
# Graphic.py : Python documentation, week 5 lecture slides


### Part 1 ###


# CODING FOR THE STUDENT ACCESSABLE PART OF THIS PROGRAM.

# A_Outcomes

# Get input from the student.
# B_validation: Check 'Out of range!' error and 'ValueError'.
# Validation error messages to be displayed have been customized to enhance user understandibility.
def Student():
    global Pass_credit, Defer_credit, Fail_credit
    while True:
        try:
            Pass_credit = int(input("Enter your total PASS credits: "))
            if Pass_credit not in range(0,121,20):          # Validation_1
                print("Action Blocked... \nOut of range! Your credit must be 0/20/40/60/80/100/120.")
                print("")
                continue

            Defer_credit = int(input("Enter your total DEFER credits: "))
            if Defer_credit not in range(0,121,20):          # Validation_1
                print("Action Blocked... \nOut of range! Your credit must be 0/20/40/60/80/100/120.")
                print("")
                continue

            Fail_credit = int(input("Enter your total FAIL credits: "))
            if Fail_credit not in range(0,121,20):          # Validation_1
                print("Action Blocked... \nOut of range! Your credit must be 0/20/40/60/80/100/120.")
                print("")
                continue

            return Pass_credit, Defer_credit, Fail_credit

        except ValueError:
            print("Action Blocked... \nNumber is required!")        # Validation_2 
            print("")



# B_Validation

# Check the sum of credits (Validation_3) and check progression outcome of the each student, as defined by the University regulations.
def check_progression_outcome_student():
    Total = Pass_credit + Defer_credit + Fail_credit
    while Total==120:                               
        if Pass_credit==120:
            print("PROGRESSION OUTCOME: Progress")
        elif Pass_credit==100:
            print("PROGRESSION OUTCOME: Progress (Module Trailer)")
        elif Fail_credit>=80:
            print("PROGRESSION OUTCOME: Excluded")
        else:
            print("PROGRESSION OUTCOME: Do Not Progress (Module Retriever)")
        break
    else:
        print("Action Blocked... \nTotal Incorrect! Expected total is 120.")              # Validation_3
        ValidIn = False
        while (ValidIn==False):
            print("\nDo you want to repeat the operation?")
            yes_or_no = input("Press 'Enter' key to repeat or 'Q' to quit: ")        
            if yes_or_no == "":
                print("")
                Student()
                check_progression_outcome_student()
                return True
            elif yes_or_no.upper() == "Q":
                return False
            else:
                print("Invalid Input! Please press 'Enter' or 'Q'.")
                print("")






# CODING FOR STAFF MEMBER ACCESSABLE PART OF THIS PROGRAM.

# A_Outcomes

# Initiate variables to get the count of progression outcomes.
count_of_progress = 0
count_of_trailer = 0
count_of_retriever = 0
count_of_excluded = 0
count_of_total_outcomes = 0

# List to store user input of progression outcomes.
list_of_progress = []
list_of_trailer = []
list_of_retriever = []
list_of_excluded = []


# Check the sum of credits (validation_1) and check progression outcome of the each student, as defined by the University regulations.
def check_progression_outcome_staff():
    global count_of_progress, count_of_trailer, count_of_retriever, count_of_excluded, count_of_total_outcomes
    global Valid_credits

    Valid_credits = Pass, Defer, Fail
    
    Total = Pass + Defer + Fail
    if Total==120:
        count_of_total_outcomes+=1
        if Pass==120:
            print("\nPROGRESSION OUTCOME: Progress")
            print("")
            count_of_progress+=1
            list_of_progress.append(Valid_credits)
        elif Pass==100:
            print("\nPROGRESSION OUTCOME: Progress (Module Trailer)")
            print("")
            count_of_trailer+=1
            list_of_trailer.append(Valid_credits)
        elif Fail>=80:
            print("\nPROGRESSION OUTCOME: Excluded")
            print("")
            count_of_excluded+=1
            list_of_excluded.append(Valid_credits)
        else:
            print("\nPROGRESSION OUTCOME: Do Not Progress (Module Retriever)")
            print("")
            count_of_retriever+=1
            list_of_retriever.append(Valid_credits)
    else:
        print("Action Blocked... \nTotal Incorrect! Expected total is 120.")              # Validation_3
        print("")
    




# B_Validation

# Check 'Out of range!' error and 'ValueError'.
# Validation error messages to be displayed have been customized to enhance user understandibility.
# Additional validation has been implemented to minimize or prevent the errors occurs (Validation_4 & Validation_5).
# Reference link for global variables : https://www.w3schools.com/python/python_variables_global.asp
# Reference link for infinite loop : https://www.geeksforgeeks.org/how-to-use-while-true-in-python/ 
def check_range_of_pass():
    global Pass
    while True:
        try:
            Pass = int(input("Enter your total PASS credits: "))
            if Pass not in range(0,121,20):          # Validation_1
                print("Action Blocked... \nOut of Range! Credit must be 0/20/40/60/80/100/120.")
                print("")
            else:
                return False
        except ValueError:          # Validation_2
            print("ERROR MESSAGE: Number is required!")
            print("")


def check_range_of_defer():
    global Defer
    while True:
        try:
            Defer = int(input("Enter your total DEFER credits: "))
            if Defer not in range(0,121,20):          # Validation_1
                print("Action Blocked... \nOut of Range! Credit must be 0/20/40/60/80/100/120.")
                print("")
            else:
                return False
        except ValueError:          # Validation_2
            print("ERROR MESSAGE: Number is required!")
            print("")


def check_range_of_fail():
    global Fail
    while True:
        try:
            Fail = int(input("Enter your total FAIL credits: "))
            if Fail not in range(0,121,20):          # Validation_1
                print("Action Blocked... \nOut of Range! Credit must be 0/20/40/60/80/100/120.")
                print("")
            else:
                return False
        except ValueError:          # Validation_2
            print("ERROR MESSAGE: Number is required!")
            print("")



# Validation of 'Out of Range!' error.
def Staff():
    # if below mentioned all three user-defined functions return False, then loop breaks and step into 'continue_or_quit()'.
    # function of nested if-condition: check the each condition one by one until it returns False. If not it will run the same user-defined function again.  
    while True:
        if not check_range_of_pass():
            if not check_range_of_defer():
                if not check_range_of_fail():
                    break




                
# C_Multiple Outcomes

# User input for continue or quit the program.
# Reference link for string formatting : https://www.w3schools.com/python/ref_string_lower.asp
def continue_or_quit():

    while True:
        print("Would you like to enter another set of data?")
        user_input = input("Press 'Enter' key to continue or 'q' to quit and view results: ")
        if user_input=="":
            print("")
            return True
        elif user_input.lower()=="q":  #String formatting
            chart()
            
            ### coding for Part 2 begins ###
            print("\nPart 2:")
            for record in range(len(list_of_progress)):
                print("Progress -", str(list_of_progress[record]).strip("()"))
            for record in range(len(list_of_trailer)):
                print("Progress (Module Trailer) -", str(list_of_trailer[record]).strip("()"))
            for record in range(len(list_of_retriever)):
                print("Module Retriever -", str(list_of_retriever[record]).strip("()"))
            for record in range(len(list_of_excluded)):
                print("Excluded -", str(list_of_excluded[record]).strip("()"))
            ### coding for Part 2 ends ###

            file_handling()
                
            return False
        else:
            print("Action Blocked... \nInvalid input! Please press 'Enter' or 'q'.")              # Validation_4
            print("")




            
# D_Histogram

from graphics import*

def chart():
    win = GraphWin("Histogram",400,400)
    win.setBackground("White")

    #Inserting heading
    #Reference link for text colour code in hexadecimal : https://htmlcolorcodes.com/colors/shades-of-gray/
    Heading = Text(Point(150,20),"Histogram Results")
    Heading.setFace("arial")
    Heading.setSize(20)
    Heading.setStyle("bold")
    Heading.setTextColor("#5E5452")
    Heading.draw(win)

    #Inserting a horizontal line
    aLine = Line(Point(20,330),Point(380,330))
    aLine.draw(win)
    
    #Inserting rectangles
    # Reference link for inserted colour codes in hexadecimal : https://htmlcolorcodes.com/colors/shades-of-green/
    Rectangle_description = [(30,count_of_progress,110,"#98FB98"),
                             (115,count_of_trailer,195,"#93C572"),
                             (200,count_of_retriever,280,"#8A9A5B"),
                             (285,count_of_excluded,370,"#E0BFB8")]
    for A_point, B_point, C_point, Color_code in Rectangle_description:
        Inserting_Shape(win, A_point, B_point, C_point, Color_code)
        
    #Inserting count of each outcome
    Count_data = [(str(count_of_progress),70,count_of_progress),
                  (str(count_of_trailer),155,count_of_trailer),
                  (str(count_of_retriever),245,count_of_retriever),
                  (str(count_of_excluded),325,count_of_excluded)]
    for count, a_point, b_point in Count_data:
        TEXT(win,count,a_point,(315-(15*b_point)),11)
    
    #Inserting title for each column
    Title_data = [("Progress",65),("Trailer",155),("Retriever",240),("Excluded",330)]
    for title, x_point, in Title_data:
        TEXT(win,title,x_point,345,11)

    #Inserting total outcomes
    TEXT(win,(str(count_of_total_outcomes) + " outcomes in total."),120,370,15)

    win.getMouse()
    win.close()


# Function for inserting text in the histogram
# Reference link for text colour code in hexadecimal : https://htmlcolorcodes.com/colors/shades-of-gray/
def TEXT(win,description,x,y,z):
    Topic = Text(Point(x,y),description)
    Topic.setFace("arial")
    Topic.setSize(z)
    Topic.setStyle("bold")
    Topic.setTextColor("#708090")
    Topic.draw(win)


# Function for inserting rectangles in the histogram
def Inserting_Shape(win,r,s,t,color):
    Shapes = Rectangle(Point(r,(330-15*s)),Point(t,330))
    Shapes.setFill(color)
    Shapes.draw(win)



### Part 3 begins ###
# Creating Text File (This is incomplete.)       
def file_handling():
    f = open("Progress_Outcomes_Record.txt", "w")
    f.write("\nPart 3:")
    f.close()


    f = open("Progress_Outcomes_Record.txt", "r")
    print(f.read())
### Part 3 ends ###





    
# Logical use of function
def main():
    print("Welcome! Please enter any one of the following values below to execute the program. \n\t1. I am a student. \n\t2. I am a staff member.")
    print("")
    student_or_staff = input("Enter the number 1 or 2: ")
    print("")
    while True:
        if student_or_staff == "1":
            Student()
            print("")
            check_progression_outcome_student()
            print("\nThank you! This program is successfully terminated.")
            break

        elif student_or_staff == "2":
            while True:
                Staff()
                check_progression_outcome_staff()
                print("-"*165)
                if not continue_or_quit():
                    return True
                break

        else:
            print("Please enter the correct input")              # Validation_5
            main()
            pass
            return False

    


if __name__ == "__main__":
    main()
    



    
            
            
        
            

