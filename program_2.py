# Program #2: Math Quiz
# Write a program that gives simple math quizzes.  The program should display two random numbers to be added, such as

#   247
# + 129
# ------

# The program should allow the student to enter the answer.  
# If the answer is correct, a message of congratulations should be displayed.  
# If the answer is incorrect a message showing the correct answer should be displayed.  
# The program must use a function that accomplishes part of the needed tasks.

def check_answer(answer, solution):
    if answer == solution:
        print("Correct")
    else:
        print("Incorrect the correct answer was", solution)


if __name__ == '__main__':
    # Find random number 1 and 2 and save them
    import random
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    solution = num1 + num2
    # print equation
    print("\t ",num1)
    print("\t+", num2)
    print('___________')
    answer = int(input("Enter Solution:"))

    # function to display message based on input
    check_answer(answer, solution)
