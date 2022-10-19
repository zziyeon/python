import os.path

file = 'D:\javaedu9\KH_정보교육원\\6. 파이썬\\vsc\\testresult.txt'
print( os.path.exists(file))

vocabulary = None
if not os.path.exists(file) :
    # 파일이 존재하지 않으면 신규
    vocabulary =open(file, 'w', encoding='UTF8')
    print('신규 생성')
else :
    # 파일이 존재하면 추가
    vocabulary = open(file, 'a', encoding='UTF8')
    print('기존 파일 열기')

# 파일에서 읽어오기
f = open('D:\javaedu9\KH_정보교육원\\6. 파이썬\\vsc\\testresult.txt','r', encoding='UTF8')
if f.readable():
    dic ={}
    for line in f.readlines():
        list = line.split(':')
        print(list)
        dic[list[0].strip()] = list[1].strip()
    f.close()
    print(dic)

voca = {}
# voca = {'student': '학생', 'teacher': '교사', 'classroom': '교실', 'smart': '똑똑한', 'lunch':'점심'}

flag=False
while not flag:
    print('\n[메뉴] 1.저장 2.검색 3.수정 4.삭제 5.목록 6. 통계 7.종료(x)')
    num = int(input('번호를 입력하세요 >>> '))
    # 저장
    if num==1 :
        if len(voca)<5 :
            vocaKey = input('>>> 저장할 영어 단어를 입력하세요: ')
            vocaValue = input('>>> 저장할 단어 뜻을 입력하세요: ')
            

            if vocaKey in voca :
                print('이미 등록되었습니다.')
            voca[vocaKey]=vocaValue
            continue
        else:
            print('최대 5개 단어만 저장할 수 있습니다.')
            continue
    # 검색    
    elif num==2 :
        searchWord = (input('>>> 검색할 단어를 입력하세요: ')).lower()
        x=0
        for searchKey in voca.keys():
            if searchKey.startswith(searchWord) :
                if searchKey in voca:
                    x=1
                    print('{} : {}'.format(searchKey, voca[searchKey])) 
        if x !=1:
            print('단어를 검색할 수 없습니다.')
        
        continue
        
    # 수정
    elif num==3 :
        alterKey = (input('>>> 수정할 영어 단어를 입력하세요: ')).lower()
        
        if alterKey in voca :
            alterValue = input('>>> 수정할 영어 단어 뜻을 입력하세요: ')
            voca[alterKey]=alterValue
            print('단어의 뜻을 수정 하였습니다.')
        else:
            print('단어를 검색할 수 없습니다.')
        continue
    
    # 삭제
    elif num==4 :
        deleteKey = (input('>>> 삭제할 영어 단어를 입력하세요: ')).lower()
        if deleteKey in voca :
            del voca[deleteKey]
            print('단어를 삭제 하였습니다.')
        else:
            print('단어를 검색할 수 없습니다.')
        continue
    
    # 목록
    elif num==5 :
        print('[서브메뉴] 1.오름차순 2.내림차순')
        arrayType = int(input('정렬 순서를 선택해주세요: '))
        import operator
        sortedVoca = sorted(voca.items(), key = operator.itemgetter(0))
        reversedVoca = reversed(sortedVoca)
        if arrayType == 1:
            for item in sortedVoca:
                print('{}:{}'.format(item[0], item[1]))
            
        elif arrayType == 2:
            for item in reversedVoca:
                print('{}:{}'.format(item[0], item[1]))
        continue
        
    # 통계
    elif num==6 :
        long_word =[]
        for len_word in voca.keys():
            long_word.append(len_word)
        long_word.sort(key=lambda x:(len(x),x), reverse=True)

        print('1. 저장된 단어 갯수: {}'.format(len(voca)))
        print('2. 단어의 문자수가 가장 많은 단어: {}'.format(long_word[0]))
        print('3. 단어 글자수 내림차순 출력(단어만): {}'.format(long_word))
        
        continue

    # 종료
    elif num==7 :
        print('프로그램을 종료합니다.')
        # 파일에 저장
        f = open('D:\javaedu9\KH_정보교육원\\6. 파이썬\\vsc\\testresult.txt','w', encoding='UTF8')
        if f.writable():
            for line in sortedVoca:
                f.write('{}:{}\n'.format(line[0].strip(), line[1].strip()))
            f.close()    
        break
