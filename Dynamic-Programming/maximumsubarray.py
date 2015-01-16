def max(x,y):
	return y if (y > x) else x 
	
def maxSubArraySum(a,size):
   max_so_far = a[0]
   curr_max = a[0]
 
   for i in range(1,size):
   
        curr_max = max(a[i], curr_max+a[i])
        max_so_far = max(max_so_far, curr_max)
   
   return max_so_far 
   
n = input()
a = raw_input().split()
a = [int(i) for i in a]
print maxSubArraySum(a,len(a))

   

