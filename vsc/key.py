# # 쓰기 모드
# f = open('D:\javaedu9\KH_정보교육원\\6. 파이썬\\vsc\sample.txt','w')
# print(f.writable())
# f.write('hello!world1\n')
# f.close()

# 추가 모드
f = open('D:\javaedu9\KH_정보교육원\\6. 파이썬\\vsc\sample.txt','a')
f.write('hello~world2\n')
f.write('hello~world3\n')
f.close()

# 읽기모드
f = open('D:\javaedu9\KH_정보교육원\\6. 파이썬\\vsc\sample.txt','r')
for line in f.readlines():
    print(line.strip())
f.close()

# 읽기모드
f = open('D:\javaedu9\KH_정보교육원\\6. 파이썬\\vsc\member.csv','r')
for line in f.readlines():
    print(line.strip())
f.close()