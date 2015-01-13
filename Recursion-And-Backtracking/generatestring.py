def Binary(n):
    if n<1:
        print A # Printing the whole string
    else:
        A[n-1] = 0
        Binary(n-1)
        A[n-1] = 1
        Binary(n-1)

n = input("Enter the number of bits. \n")

A = [0 for x in range(n)] # Generating an empty list.

Binary(n) # Calling the function to generate the Binary
