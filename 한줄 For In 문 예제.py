#기존 리스트에 100을 추가하여 리스트를 그대로 만들어보자
# 학생 = [1,2,3,4,5]
# 학생 = [i+100 for i in 학생]
# print(학생)

#여기서 나오는 각줄의 끝에 @, #, %의 순서를 예상해보고 이해하기
# for i in range(2,10):
#     for j in range(1,10):
#         print( i*j, end="@")
#     print("#")
# print("%")


#학생 이름을 길이로 변환
# 학생 = ["둘리","마이콜","마이클조던","샘"]
# 학생 = [len(i) for i in 학생]
# print(학생)

#학생 이름을 대문자 소문자로 변환
# student = ["richard","sam","mickal","braed"]
# student = [i.upper() for i in student]
# print(student)
# student = [i.lower() for i in student]
# print(student)