'''
Created on Mar 30, 2019

@author: ITAUser
'''
import json 
answer = 'yes'
while answer != 'no':
    with open("assignment_list.json", "r") as f_r:
        data = json.load(f_r)
    print ("\n\n Here are the assignments below...")
    for i in data:
            print ("\n" + i)
            
    ans = input("1, Check what's the due date. \n2 Add new assignment \n\n")
    if ans == "1":
        assignment = input("Enter assignment: ")
        print("The assignment for {} is {}".format(assignment, data.get(assignment, "not in our database")))
    elif ans == "2":
        n = int(input("How many assignments do you want to add? (max 3 at a time"))
        i = 0
        while i<n:
            print("\n Add assignment", i+1)
            new_assignment = input("Enter the assignment: ")
            new_duedate = input("Enter in due date (dd/mm/yyyy):")
            data[new_assignment] = new_duedate
            with open("assignment_list.json", "w")as f_w:
                json.dump(data, f_w)
            print("Assignment Added!")
            i += 1
    else:
        print("\n Invalid Input!")
    answer = input("\n Do you want to use the assignment list again (yes/no):")