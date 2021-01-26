import random

##  단어장의 제목 형식: "1.txt"
number_of_section=input("시험 볼 단원?")

if number_of_section=="all":
    a=open("c:/Users/jshjs/OneDrive/바탕 화면/단어장/all.txt",'w',encoding='UTF-8')
    

path="c:/Users/jshjs/OneDrive/바탕 화면/단어장/"+number_of_section+".txt"
f=open(path,"r",encoding='UTF-8')
dictionary=[]       ##  2열짜리 행렬 

while True:
    line=f.readline()
    if not line:
        break
    temp=line.split("/")
    dictionary.append(temp)
f.close()

test=int(input("시험 볼 문제 수:1~"+str(len(dictionary))+"\n"))

test_dictionary=random.sample(dictionary,test)
answer_count=0
for word in test_dictionary:
    print(word[0])
    answer=input()
    if answer in word[1]:
        print("정답!")
        answer_count+=1
    else:
        print("오답!")
        print("답은: "+word[1])
print("맞은 개수:"+str(answer_count)+"/"+str(test))


