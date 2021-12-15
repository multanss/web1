#url = "http://www.naver.com"
url2 = "http://www.daum.net"
my_str = url2.replace("http://www.","")
my_str = my_str[:my_str.index(".")]
my_str = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
password = my_str
 
#print("{0}의 비밀번호는 {1}입니다".format(url,password))
print("{0}의 비밀번호는 {1}입니다.".format(url2,password))

