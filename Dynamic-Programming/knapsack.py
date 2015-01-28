def max(a,b):
    return a if a>b else b

def knapsack():
    for i in range(n+1):
        for j in range(w+1):
            print l[i][j]

def main():
    knapsack()
    
main()
