# 파이썬 모듈
# 모듈은 파이썬 정의와 문장을 담고 있는 파일

list = []
tuple=()
dic = {}

def add(*args):
    sum = 0
    for ele in args:
        sum +=ele
    return sum

def multi(*args):
    result = 1
    for ele in args:
        result *=ele
    return result