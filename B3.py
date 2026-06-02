students = [
    {
        "student_id": "RA001",
        "name": "Nguyễn Văn A",
        "math_score": 8.5,
        "english_score": 7.0
    },
    {
        "student_id": "RA002",
        "name": "Trần Thị B",
        "math_score": 9.0,
        "english_score": 9.5
    }
]

#Hàm in danh sách
def display_students(student_list):
    for index, student in enumerate(student_list):
        print(f"{index + 1}. {'Mã:'} {student['student_id']:<25} | Tên: {student['name']:<25} | Toán: {student['math_score']:<25} | Anh: {student['english_score']}")

#Hàm thêm sinh viên
def add_student(student_list):
    list_id = [id['student_id'] for id in student_list]
    while True:
        id_input = input("Nhập mã sinh viên: ").strip().upper()
        if id_input in list_id:
            print("Mã sinh viên đã tồn tại! Vui lòng nhập lại")
        else:
            break
    name_input = input("Mời bạn nhập tên sinh viên: ")
    
    while True:
        add_math_score = float(input("Mời bạn nhập điểm toán: "))
        if add_math_score < 0 or add_math_score > 10:
            print("Điểm không hợp lệ! ")
        else:
            break
    
    while True:
        add_english_score = float(input("Mời bạn nhập điểm anh: "))
        if add_english_score < 0 or add_english_score > 10:
            print("Điểm không hợp lệ! ")
        else:
            break
    student_list.append({
        "student_id" : id_input,
        "name" : name_input,
        "math_score" : add_math_score,
        "english_score" : add_english_score
    })
    

#Hàm phụ trợ
def find_student_by_id(student_list, id_check):
    list_id = [id['student_id'] for id in student_list]
    if id_check in list_id:
        return list_id.index(id_check)
    else:
        return -1


def update_score(student_list):
    input_id = input("Mời bạn nhập vào mã sinh viên: ").strip().upper()
    index = find_student_by_id(student_list, input_id)

    if index == -1:
        print("Không tìm thấy mã sinh viên")
        return
    
    name_input = input("Mời bạn nhập tên sinh viên: ")
    
    while True:
        add_math_score = float(input("Mời bạn nhập điểm toán: "))
        if add_math_score < 0 or add_math_score > 10:
            print("Điểm không hợp lệ! ")
        else:
            break
    
    while True:
        add_english_score = float(input("Mời bạn nhập điểm anh: "))
        if add_english_score < 0 or add_english_score > 10:
            print("Điểm không hợp lệ! ")
        else:
            break

    student_list[index]['student_id'] = input_id
    student_list[index]['name'] = name_input
    student_list[index]['math_score'] = add_math_score
    student_list[index]['english_score'] = add_english_score
    print(f"Cập nhật sinh viên với id: {input_id} Thành công!")

#Hàm thứ hạng
def get_rank(average_score):
    if average_score >= 8:
        return "Giỏi"
    elif average_score >= 6.5:
        return "Khá"
    elif average_score >= 5:
        return "Trung bình"
    else:
        return "Yếu"

#Hàm in 
def evaluate_students(student_list):
    list_math = [math['math_score'] for math in students]
    list_english = [english['english_score'] for english in students]

    for index, student in enumerate(students):
        for index, (score_math, score_english) in enumerate(zip(list_math, list_english)):
            total = 0
            total = (score_math + score_english) / 2
            level = get_rank(total)
        print(f"{index + 1}. {'Mã:'} {student['student_id']:<25} | Tên: {student['name']:<25} | Điểm trung bình: {total:<25} | Xếp loại: {level}")
                    
    
while True:
    try:
        choice = int(input('''
===== HỆ THỐNG QUẢN LÝ ĐIỂM THI RIKKEI ACADEMY =====
1. Hiển thị danh sách học viên
2. Thêm học viên mới
3. Cập nhật điểm thi theo mã học viên
4. Đánh giá học lực của toàn bộ học viên
5. Thoát chương trình
Mời bạn nhập lựa chọn: 
'''))
        if choice <= 0 or choice > 5:
            print("Menu không tồn tại!")

        match choice:
            case 1:
                display_students(students)
            
            case 2:
                add_student(students)

            case 3:
                update_score(students)

            case 4:
                evaluate_students(students)

            case 5:
                print("Cảm ơn bạn đã sử dụng chương trình!")
                    

    except ValueError:
        print("Vui lòng nhập đúng kiểu dữ liệu!")