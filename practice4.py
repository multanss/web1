subway = [10,20,30]
print(subway)

subway = ["철수","영희","마이콜"]
print(subway)

#영희는 몇번째 칸에 타고 있는가?
print(subway.index("영희"))

subway.append("둘리")
print(subway)

subway.insert(2,"도우너")
print(subway)

print(subway.pop())
subway.append("철수")
print(subway)
print(subway.count("철수"))

a = [1,4,3,2,5]
# a.sort()
# print(a)

# a.reverse()
# print(a)

# a.clear()
# print(a)
b = ["a","b","e","g","f"]
a.extend(b)
print(a)

