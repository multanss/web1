set = {1,4,6,2,1,1,7}
print(set)
java = {"둘리","또치","마이콜"}
python = {"철수","영희","마이콜"}

#교집합
print(java & python)
print(java.intersection(python))

#합집합
print(java | python)
print(java.union(python))

#차집합
print(java - python)
print(java.difference(python))

#인자 추가
python.add("희동이")
print(python)

#인자 제거
python.remove("철수")