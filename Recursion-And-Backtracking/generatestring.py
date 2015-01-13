A = [1,2,3,4,5]

def Binary(n):
    if n<1:
        print A
    else:
        A[n-1] = 0
        Binary(n-1)
        A[n-1] = 1
        Binary(n-1)

Binary(5)
