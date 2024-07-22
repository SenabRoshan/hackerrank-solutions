# Challenge: HourglassSum - Find the maximum hourglassSum
#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    # Write your code here
    
    start_middle = 1
    
    max_total = -100
    
    
    while (start_middle <= len(arr) - 2):
        for i in range(1, 5):
            total = arr[start_middle][i] + arr[start_middle+1][i] + arr[start_middle-1][i] + arr[start_middle+1][i+1] + arr[start_middle+1][i-1] + arr[start_middle-1][i-1] + arr[start_middle-1][i+1]
            
            if (total > max_total):
                max_total = total
                
        start_middle += 1
        
    return (max_total)
    
arr = []

for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))

result = hourglassSum(arr)

print(result)