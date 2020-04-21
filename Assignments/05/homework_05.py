

def q1():
    # 1 POINT
    # If i want to pass a command line argument to a program, what module and function do you need to use?
    your_answer = ""
    print("Question 1")
    print(your_answer)


def q2():
    # 1 POINT
    # What is a random seed and why would you want to use one?
    your_answer = ""
    print("Question 2")
    print(your_answer)


def q3():
    # 1 POINT
    # Numpy arrays and regular python lists have many similarities and differences. List 3 of each.
    your_answer = ""
    print("Question 3")
    print(your_answer)


def q4():
    # 1 POINT
    # What is the differences between the two blocks of code below:
    import math
    x = [1, 2, 3, 4, 5]
    y = math.fsum(x)

    import numpy as np
    x = np.array([1, 2, 3, 4, 5])
    y = x.sum()

    your_answer = ""
    print("Question 4")
    print(your_answer)


def q5():
    # 2 POINTS
    A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
    B = None
    C = None
    D = None
    E = None
    # change the definitions of B, C, D, and E to generate the results described below
    # B = a tuple containing the number of rows and columns in A
    # C = only column 0 from array A
    # D = only row 2 from column A
    # E = array A converted into a single 12-element array instead of a matrix of rows and columns
    your_answer = ""
    print("Question 5")
    print("A: ", A)
    print("B: ", B)
    print("C: ", C)
    print("D: ", D)
    print("E: ", E)


def q6():
    # 2 POINTS
    # np.dot() computes the sum of the products of the elements in two arrays, i.e. dot = x1*y1 + x2*y2 + ... + xn*yn
    # Compute the dot product of the two arrays below using np.dot().
    # In addition, write a function (defined at the global level so you can call it inside this function) that computes
    # the dot product using loops that iterate over the array.
    A = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
    B = np.array([3, 4, 6, 2, 3, 8, 6, 5, 10])
    your_answer = ""
    print("Question 6")
    print(your_answer)


def q7():
    # 2 POINTS
    # use the time module to compare the time it takes your computer to compute the dot product using the two methods
    # from the previous question. Print out the results.
    loop_time = 0
    numpy_time = 0
    # your code here
    print("Question 7")
    print("Loop Method Time:", loop_time)
    print("Numpy Method time:", numpy_time)


def q8():
    # 3 POINTS
    # write a function called "generate_data()" (defined at the global level and called inside this function) that takes
    # two input arguments: num_students, and num_assignments. this function should create a numpy matrix with
    # num_students as the number of rows, and num_assignments as the number of columns. This matrix should be filled
    # with randomly generated data that has a mean of 80, a standard deviation of 10, and with no values that
    # are < 0 or > 100. have the function return this data matrix. call the function from inside this q8 function, pass
    # it two values, and receive the resulting matrix. Print out the shape of the matrix, and the average value in the
    # matrix calculated using the numpy function for getting a mean.

    your_answer = ""
    print("Question 8")
    print(your_answer)


def q9():
    # 3 POINTS
    # write a function called "calculate_means()" that takes two input arguments, a data matrix generated by the
    # function created in the previous question, and a string called "which_means" which can be set to either "students"
    # or "assignments". If which_stats == "students", the function should return a numpy array of length num_students,
    # that contains each student's average grade. if which_stats == "assignments", the function should return a numpy
    # array of length "num_assignments", showing the average score on each assignment. The code for this function should
    # not contain any loops! Inside this q9 function, call both the "generate_data()" function and the
    # "calculate_stats()" function, and print out the returned value of the "calculate_stats()" function.
    num_students = 20
    num_assignments = 10
    which_stats = "students"

    your_answer = ""
    print("Question 9")
    print(your_answer)


def q10():
    # 4 POINTS
    # finish the lab_05_03.py. Dont paste the code here
    your_answer = ""
    print("Question 10")
    print(your_answer)


def main():

    q1()
    q2()
    q3()
    q4()
    q5()
    q6()
    q7()
    q8()
    q9()
    q10()


main()