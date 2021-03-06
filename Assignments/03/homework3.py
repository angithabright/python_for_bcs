
def q0():
    # What is the difference between an argument and a parameter? Given an example.
    your_answer = ""
    print("Question 0")
    print(your_answer)


def q1():
    # The function below is called a 'non-fruitful' because it doesnt return a value. But it actually does return a
    # value, silently. How can you see what that value is? What is it? What is an example of a function we have used
    # that is a non-fruitful function?

    def non_fruitful_function():
        print("all this function does is print me out")

    print("Question 1")
    non_fruitful_function()
    your_answer = ""
    print(your_answer)


def q2():
    # what is wrong with the code below?
    #
    # def function1():
    #     print("This is function 1")
    #
    #     def function2():
    #         print("This is function 2")
    #
    # function1()
    # function2()

    your_answer = ""
    print("Question 2")
    print(your_answer)


def q3():
    # below this function definition, there is a global variable defined. What about python's syntax makes it a
    # global variable? How would you make it a local variable to this function?

    your_answer = ""
    print("Question 3")
    print(your_answer)


x = 25


def q4():
    # What is an optional parameter in a python function, and how do you define one in a function definition?
    your_answer = ""
    print("Question 4")
    print(your_answer)


def q5():
    # What is the function below doing? The function definition returns two values, but when the function is called
    # there is only one variable to which the data is being assigned? Why is this legal? How is handling this situation?
    def get_min_max(some_list):
        minimum = some_list[0]
        maximum = some_list[1]
        for value in some_list[1:]:
            if value > maximum:
                maximum = value
            if value < minimum:
                minimum = value
        return minimum, maximum

    print("Question 5")
    your_answer = ""
    my_list = [-6, 2, 5, 5, -1, 3]
    min_max = get_min_max(my_list)
    print(min_max)
    print(your_answer)


def q6():
    # explain why it is valuable to make your code in terms functions. Give at least three specific examples from class
    # so far that take code you have written and why it would be better if it had been as a function instead of how we
    # did it originally.
    your_answer = ""
    print("Question 6")
    print(your_answer)


def q7():
    # Define a function that can take a variable number of input arguments, and if all the arguments are numbers,
    # calculates and returns the variance of those numbers. print

    print("Question 7")
    variance = 0
    print(variance)


def q8():
    # What is the problem with the code below that defines and calls a function? Type your answer where it says
    # 'your_answer. Then, uncomment and fix the code so that it does not generate an error, prints out "yes" if the
    # input argument is "dog", prints out no otherwise, and returns either "yes" or "no" when the function is complete.

    # def dog_identifier:
    #     if x == "dog":
    #         print("yes")
    #     else:
    #         print("no")
    #
    # input_string = input("Type Something: ")
    # answer = dog_identifier(input_string)

    your_answer = ""
    print("Question 8")
    print(your_answer)


def q9():
    # write a function that takes a list as an input, and calculates mean, median, and mode of those numbers,
    # and returns them.

    # your function definition here

    data = [6,7,8,9,9,9,9,10,11,12]
    mean = 0
    median = 0
    mode = 0
    # call the function here
    print("Question 9")
    print(mean, median, mode)


"""
QUESTION 10
create a main function that calls each of the other functions, and call the main function so that when this script runs,
the answers to all the questions print out
"""