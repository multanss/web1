
결석한학생 = [2,5]
책안가져온학생 = [7]
for 학생 in range(1,11):
    if 학생 in 결석한학생 :
        continue  #continue는 반복문에 등장할시에 continue이하의 문장은 스킵하고 다시 반복문 다음시작으로 돌아감
    elif 학생 in 책안가져온학생 :
        print("{0}는 수업 끝나고 교무실로 따라와!".format(학생))
        break #break는 반복문에서 등장할시에 반복문을 그 즉시 종료시킨다
    print("{0}아 책좀 읽어볼래?".format(학생))
    