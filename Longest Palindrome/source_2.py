# This a best way with low complexity.
s='cbbd'
left=0
max_length=0
substring=''
while left<len(s):
    right = left+1
    while right<len(s):
        temp = s[left:right+1]
        if temp==temp[::-1]:
            length=len(temp)
            if max_length<length:
                substring=''.join(temp)
                max_length=length
        right+=1
    left+=1
print(substring)
        
