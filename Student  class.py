class student :
    def __init__(self) :
        self.numberOfStudents = 100 
        print("Total Students in school: ", self.numberOfStudents)

    def newComers (self) :  
        newStudents = float (input("What is the number of new students coming in this year? ")) 
        self.numberOfStudents =  self.numberOfStudents + newStudents
        print("Your new number of students are: ", self.numberOfStudents)  

    def withdrawFromSchool (self) :
        leftSchool = float (input("What is the amount of students who dropped out this year? "))
        if self.numberOfStudents >= leftSchool:
            self.numberOfStudents = self.numberOfStudents - leftSchool
            print("These students have left school: ", leftSchool) 
        else:
            print(" You don’t have enough students to leave")
    def display (self) :
        print ("The total amount of students are: ", self.numberOfStudents)

k = student()
k.newComers()
k.withdrawFromSchool()
k.display()