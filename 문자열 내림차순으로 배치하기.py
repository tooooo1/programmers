def solution(s):
    sList = list(s)
    sList.sort(reverse=True)
    return ''.join(sList)