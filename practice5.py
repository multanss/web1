cabinet = {3:"둘리", 5:"또치"}
print(cabinet[3])
print(cabinet[5])
print(cabinet.get(3))
print(cabinet.get(10))
print(cabinet.get(10,"할당되지 않음"))
print(3 in cabinet)
print(10 in cabinet)
# del cabinet[3]

print(cabinet.keys())
print(cabinet.values())
print(cabinet.items())
cabinet.clear()
print(cabinet)