import sys


def frame(): # 데이터 출력시 기본 인덱스 및 틀
    print("Student\t\t\tName\t\t\tMidterm\t\tFinal\t\tAverage\t\tGrade")
    print("----------------------------------------------------------------------------------------------------------")


def show(data): # 전체학생 데이터 출력
    frame()
    data.sort(key=lambda e: e[4], reverse=True)
    for s_info in data:
        for y in s_info:
            print(y, end='\t\t')
        print('')
    print('')


def search(data): # 특정학생 검색
    s_id = input("Student ID: ")

    for s_info in data:
        if str(s_info[0]).strip() == str(s_id).strip():
            frame()
            for x in s_info:
                print(x, end='\t\t')
            print('')
            break
        else:
            print("NO SUCH PERSON.")
            break


def changescore_data(s_id, new_score,data,check_m_f):# 점수 수정 데이터변경 부분
    frame()

    for n in range(len(data)):
        if data[n][0] == s_id:
            for sin in data[n]:
                print(sin, end='\t\t')

    for x in range(len(data)):
        if data[x][0] == s_id:
            if check_m_f =='mid':
                data[x][2] = new_score
            else:
                data[x][3] = new_score
            data[x][4] = Mean(data[x][2], data[x][3])
            data[x][5] = grade(data[x][4])
            print('')
            print("Score changed.")

    for n in range(len(data)):
        if data[n][0] == s_id:
            for sin in data[n]:
                print(sin, end='\t\t')
    print('')


def changescore(data): # 점수 수정조건부분
    s_id = input("Student ID: ")
    cnt=0

    for s_info in data:
        if str(s_info[0]).strip() == str(s_id).strip():
            cnt+=1
            check_m_f = input("MID/Final? ")
            if check_m_f == ('mid' or 'final'):
                new_score = input("Input new score: ")

                if int(new_score) < 0 and int(new_score) > 100:
                    break
                elif int(new_score) >= 0 and int(new_score) <= 100:
                    changescore_data(s_id, new_score,data,check_m_f)
                    break
                else:
                    break

            else:
                break
    if  cnt ==0:
        print("NO SUCH PERSON")
        print("")

def searchgrade(data): # 특정 학점 학생 출력 함수
    find_grade = []
    sc_grade = input("Grade to search: ")
    if sc_grade == ("A" or "B" or "C" or "D" or "F"):

        for std in range(len(data)):
            if data[std][5] == sc_grade:
                find_grade.append(std)

        if find_grade == [] :
            print("NO RESULTS.")
        else:
            frame()
            for x in find_grade:
                for s_data in data[x]:
                    print(s_data, end='\t\t')
                print('')


def add_data(s_add,data,len_max): # 학생 추가 데이터입력및 계산부분
    add_name = input("Name: ")
    add_mid = input("Midterm Score: ")
    add_fin = input("Final Score: ")
    add_avg = Mean(add_mid, add_fin)
    add_grd = grade(add_avg)
    if len(add_name) >len_max:
        len_max =len(add_name)
    add_data = [s_add, add_name + ((len_max - len(add_name)) * ' '), add_mid, add_fin, add_avg, add_grd]
    data.append(add_data)
    print("Student added.")


def add(data,len_max): # 학생 추가 조건 부분
    cnt=0
    s_add = input("Student ID: ")
    for s_info in data:
        if str(s_info[0]).strip() == str(s_add).strip():
            print("ALREADY EXISTS.")
            cnt+=1
            break
    if cnt!=1:
        add_data(s_add,data,len_max)

def Remove(data): # 학생 데이터 삭제 부분
    cnt=0
    if len(data) == 0:
        print("List is empty.")
    else:
        s_id = input("Studen ID: ")
        for s_info in data:
            if str(s_id).strip() == s_info[0]:
                data.remove(s_info)
                print("Student removed.")
                cnt+=1
        if cnt !=1 :
            print("NO SUCH PERSON.")


def quit(data): # 프로그램 종료 부분
    save_data = input("Save data?[yes/no] ")

    if save_data == 'yes':
        new_fname = input("File name: ")
        with open("%s" % new_fname, "w") as file_write:
            for line_data in data:
                for x in line_data:
                    file_write.write(str(x).strip())
                    file_write.write("\t")
                file_write.write('\n')


def Mean(mid, final): # 학생의 평균 계산
    mn = (int(mid) + int(final)) / 2
    return round(mn, 1)


def grade(a): #학생의 학점 계산
    if float(a) >= 90:
        grd = 'A'
    elif float(a) >= 80:
        grd = 'B'
    elif float(a) >= 70:
        grd = 'C'
    elif float(a) >= 60:
        grd = 'D'
    else:
        grd = 'F'
    return grd


def main():
    data = [] # 학생 데이터를 저장 할 데이터 리스트 선언
    len_max = 0 # 학생 데이터 출력시 가독성을 위한 이름 길이 저장 변수 선언
    if len(sys.argv) == 2:# argv 갯수를 입력받아 읽어올 파일 이름 선택
        data_file = sys.argv[1]
    else:
        data_file = "students.txt"

    with open("%s" % data_file, "r") as file_read: # 데이터 읽는 부분
        for line in file_read:
            s_info = list(map(str, line.split('\t')))
            s_info[3] = (s_info[3])[0:2]
            data.append(s_info)

    for x in range(len(data)):  #학생 이름 최대 길이 저장
        if len(data[x][1]) > len_max:
            len_max = len(data[x][1])
    for x in range(len(data)):  # 학생 최대 이름길이를 기준으로 이름+공백으로 데이터 변경
        if len(data[x][1]) < len_max:
            data[x][1] += ' ' * (len_max - len(data[x][1]))
    for mean in range(len(data)):
        data[mean].append(Mean(data[mean][2], data[mean][3]))
        data[mean].append(grade(data[mean][4]))


    show(data)

    while (True):  # 명령어 받는 부분
        a = input().strip().lower()
        if a == "show":
            show(data)
        elif a == "search":
            search(data)
        elif a == "changescore":
            changescore(data)
        elif a == "add":
            add(data,len_max)
        elif a == "remove":
            Remove(data)
        elif a == "quit":
            quit(data)
            break
        elif a == "searchgrade":
            searchgrade(data)

if __name__ == "__main__":
    main()
