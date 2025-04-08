def semester_gpa():
    #determination of no. of courses chosen by the user 
    courses = int (input ("\nplease, enter the number of courses\t"))
    #taking inputs from user to calculate gpa depending on choosen no. of courses
    if (courses == 1):
        c  = float (input("\nplease, enter the grade of your course\t"))
        ch = float (input ("\nplease, enter the credit hours of your first course\t"))
        gpa = (c)
    else:
        gp, sum = 0.0, 0.0
        grade = []
        list_length = courses
        chour = [] 
        list_length = courses
        for counter in range(list_length):
            c = float (input("\nplease enter the grade you scored\t"))
            ch = float (input("\nplease enter the credit hours of that course\t"))
            grade.append(c)
            chour.append(ch)
            sum += chour[counter]
            gp += grade[counter]*chour[counter]
        gpa = gp / sum
    #giving the output to tha user with different ways according to his/her gpa 
    if (gpa >= 3):
        print("\nthis semster you scored", float (gpa),",\nwhat an effort you did!\ncongratulations!")
    elif (3 > gpa >= 2):
        print("\nthis semster you scored",float (gpa),",\ncongratulations!\nkeep going!")
    else:
        print("\nthis semster you scored",float (gpa),"better luck next semester")

def cummulative_gpa(): 
    #taking inputs from user and assigning them to each variable according to no. of semesters chosen by user 
    #then calculating it in the if-condition entered then giving the user the output
    prev_gpa = float (input("please, enter your last cumm. gpa"))
    prev_ch = float (input("please, enter your previous total credit hours"))
    cur_gpa = float (input("please, enter your current gpa"))
    cur_ch = float (input("please, enter your current semester credit hours"))
    cum_gpa = ((prev_gpa*prev_ch) + (cur_gpa*cur_ch)) / (prev_ch + cur_ch) 
    print("\nyour cummulative gpa = ",cum_gpa)
    if (cum_gpa >= 3):
        print("\nwhat an effort you are doing!\ncongratulations!")
    elif (3 > cum_gpa >= 2):
        print("\ncongratulations!\nkeep going!")
    else:
        print("\nstill got a chance\ndon't give up, warrior")

def target_gpa():
    cur_gpa = float (input ("\nplease, enter your current cummulative gpa\t"))
    cur_ch  = float (input ("\nplease, enter your current credit hours\t"))
    target_gpa  = float (input ("\nplease, enter the cummulative gpa you want to achieve\t"))
    extra_ch    = float (input ("\nplease, enter the additional credit hours you will take\t"))
    needed_gpa  = ((target_gpa * ( cur_ch + extra_ch )) - (cur_gpa * cur_ch)) / extra_ch
    print("\nyou need to score", needed_gpa ,"in the next semester, goodluck!")

#the main func. where the user choose a function from the three given to perform and check if user wants to use the program again 
def main_function ():
    print ("Welcome,")
    print ("Main Menu :")
    print("\t1. semester gpa")
    print("\t2. cummulative gpa")
    print("\t3. target gpa")
    choice = float (input ("choose one of the previous options:\t"))
    if (choice == 1):
        semester_gpa()
    elif (choice == 2):
        cummulative_gpa()
    elif (choice == 3):
        target_gpa()
    else:
        print("\nplease, enter a valid choice\n")
        main_function()
    try_again = float (input ("\ndo you want to calculate anything again\n for 'yes' press 1\n for 'no' press any number\t"))
    if ( try_again == 1):
        main_function()
    else:
        print("we were happy to help you")
main_function()
