#   Rainier Pamintuan Agcaoili
#   Andrew ID: ragcaoil

#   Function to reverse string
def stringreverse(str):
    reversed = ""

#   Looping through last element in string and then going down, capturing the str
#   In the index position
    for i in range(len(str) - 1, -1, -1):
        reversed += str[i] 

    return reversed

#   Function that finds 2 numbers in list that add up to the goal
#   It returns the indices of the values in the list
def twosum(nums, goal):

#   Looping through each combination of number
    for i in range(1, len(nums)):
        for x in range(len(nums)):

#           Checking if numbers in list == to goal
            if nums[i] + nums[x] == goal:

#               Returning the indexes in ascending order
                if i > x:
                    return [x, i]
                else:
                    return [i,x]

#   Own programming language that i found outside of the list
#   FizzBuzz, Prints integers 1 to n, if divisible by 3 then
#   Return Fizz, if 5 then return Buzz, if both return FizzBuzz
def fizzbuzz(lastnum):
    for i in range(lastnum):
        str = ""

#       If divisible by, 3 add Fizz to string, if 5
#       Add Buzz to string, if empty not divisible so
#       Just return the value of the num
        if i % 3 == 0:
            str += "Fizz"

        if i % 5 == 0:
            str += "Buzz"

        if str == "":
            str = i

        print(str)

    