#function 1:

def sumofdigits(number):
    # Calculate the sum of digits in the given number
    return sum(int(digit) for digit in str(number))

#function 2:

def ispal(number):
    # Check if the given number is a palindrome
    num_str = str(number)
    return num_str == num_str[::-1]

if __name__ == "__main__":
    raise RuntimeError("This module should not be run independently.")