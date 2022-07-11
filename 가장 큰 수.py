# try 1
from itertools import permutations

def solution(numbers):
    comNumbers = list(permutations(numbers, len(numbers)))
    
    comNumberList = []
    
    for c in comNumbers:
        temp=list(map(str, c))
        comNumberList.append(''.join(temp))
        
    return str(max(comNumberList))



# try 2
# def solution(numbers):
#     strNumbers = list(map(str, numbers))
#     strNumbers.sort(reverse=True)
#     return ''.join(strNumbers)

# try 3
# def ZeroCase(hidden):
#     zeroCase = len(hidden)
#     if zeroCase == hidden.count(0):
#         return True

# def solution(numbers):
#     if ZeroCase(numbers):
#         return "0"
    
#     strNumbers = list(map(str, numbers))
#     strNumbers.sort(key=lambda x: x*3, reverse=True)
#     return ''.join(strNumbers)