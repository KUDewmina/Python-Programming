l1 = [1,2,3,4]
left = 0
while left<len(l1): 
    right = left+1
    while right<len(l1):
        print("("+str(l1[left])+","+str(l1[right])+")")
        right+=1
    left+=1
