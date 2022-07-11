# try 1
def solution(s):    
    while len(s):
        flag = True
        for i in range(len(s)):
            if s[i]+s[i] in s:
                s = s.replace(s[i]+s[i],'')
                flag = False
                break
        if flag:
            return 0
    
    return 1

# try 2
def solution(s):    
    listS = set(list(s))
    
    for _ in range(len(s)//2+1):
        for l in listS:
            while l+l in s:
                s=s.replace(l+l,'')
    
    if len(s):
        return 0
    return 1

# try 3
def solution(s):    
    stack = []
    
    for i in s:
        if not stack:
            stack.append(i)
            continue
        
        stack.pop() if stack[-1] == i else stack.append(i)
        
    if stack:
        return 0
    return 1