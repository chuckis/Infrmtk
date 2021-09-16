# Q1: Write a function that returns a string of numbers from 0 to 100, "0123456789101112...".

def string_of_hundred():
    return ''.join([str(i) for i in range(0, 101)])

# Q2: Write a function that makes a list with unique items from a list with duplicate items. 
# Example: [1, 1, 2, 3, 3] -> [1, 2, 3].

# Q3: Make a list of prime numbers from the range (1, 100) using Python.

# Q4: Write a program that prints the numbers from 1 to 20. 
# But for multiples of three print “Fizz” instead of the number and for the multiples of five
#  print “Buzz”. For numbers that are multiples of both three and five print “FizzBuzz”.

# Q5: How to convert a string to a number that consists of letters ASCII code. 
# Example: 'abcd' -> 979899100. Write a function to do this.

# Q6: How to remove empty lines from a list of lines (with a length of 0). 
# Write a function to do this.

# Q7: Write a function that counts all distinct pairs with a difference equal to k.

if __name__ == '__main__':
    print(string_of_hundred())