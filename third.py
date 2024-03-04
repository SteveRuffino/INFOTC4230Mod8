for i in range(1, 101):
    # Make a blank string to hold the output
    output = ''
    
    # Output Fizz if divisible by 3
    if i % 3 == 0:
        output += 'Fizz'
    
    # Output Fizz if divisible by 3
    if i % 5 == 0:
        output += 'Buzz'
    
    # Print the number if it is not divisible by 3 or 5, otherwise print the string.
    print(output or i)