def maxCrossingSum(arr, l, m, h) :
    sm = 0
    left_sum = 0
     
    for i in range(m, l-1, -1) :
        sm = sm + arr[i]
         
        if (sm > left_sum) :
            left_sum = sm
     
    sm = 0
    right_sum = 0
    for i in range(m + 1, h + 1) :
        sm = sm + arr[i]
         
        if (sm > right_sum) :
            right_sum = sm
     
    return left_sum + right_sum;
 
 
# Returns sum of maxium sum subarray in aa[l..h]
def maxSubArraySum(arr, l, h) :
     
    # Base Case: Only one element
    if (l == h) :
        return arr[l]
 
    else:
        m = (l + h) // 2

        return max(maxSubArraySum(arr, l, m),
               maxSubArraySum(arr, m+1, h),
               maxCrossingSum(arr, l, m, h))