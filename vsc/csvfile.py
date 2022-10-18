import csv

#with 구문과 같이 사용하면 close() 처리를 자동으로 해줌
lines = None
with open('member.csv','r',encoding='cp949') as csvfile:
    lines=csv.reader(csvfile, quotechar="'",quoting=csv.QUOTE_NONNUMERIC)
    for line in lines:
        print (line[0:2])        #이름과 나이만 출력
        print(line[:])             # 전체 출력