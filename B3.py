# Khởi tạo danh sách sinh viên ban đầu
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

# ==============================================================================
# PHẦN 1: CÁC HÀM PHỤ TRỢ (HELPER FUNCTIONS)
# ==============================================================================

def find_student_by_id(student_list, id_check):
    """
    Hàm phụ trợ: Tìm vị trí (index) của sinh viên qua ID.
    Trả về: Vị trí index nếu tìm thấy, ngược lại trả về -1
    """
    # Tạo danh sách chứa tất cả các ID hiện có để so sánh nhanh
    list_id = [student['student_id'] for student in student_list]
    if id_check in list_id:
        return list_id.index(id_check)
    return -1


def get_rank(average_score):
    """
    Hàm phụ trợ: Xếp loại học lực dựa trên điểm trung bình.
    Trả về: Chuỗi ký tự xếp loại (Giỏi, Khá, Trung bình, Yếu)
    """
    if average_score >= 8:
        return "Giỏi"
    elif average_score >= 6.5:
        return "Khá"
    elif average_score >= 5:
        return "Trung bình"
    else:
        return "Yếu"


def validate_score(prompt_message):
    """
    Hàm phụ trợ mới: Yêu cầu nhập điểm và kiểm tra tính hợp lệ (0 -> 10).
    Giúp giảm lặp code ở hàm thêm và cập nhật sinh viên.
    """
    while True:
        try:
            score = float(input(prompt_message))
            if 0 <= score <= 10:
                return score # Điểm hợp lệ, thoát hàm và trả về giá trị
            print("Điểm không hợp lệ! Vui lòng nhập trong khoảng từ 0 đến 10.")
        except ValueError:
            print("Vui lòng nhập đúng kiểu dữ liệu số!")

# ==============================================================================
# PHẦN 2: CÁC HÀM CHỨC NĂNG CHÍNH (MAIN FUNCTIONS)
# ==============================================================================

def display_students(student_list):
    """Chức năng 1: Hiển thị danh sách sinh viên hiện tại"""
    if not student_list:
        print("Danh sách hiện đang trống!")
        return
        
    for index, student in enumerate(student_list):
        # Sử dụng formatting :<25 để căn lề trái cho đẹp mắt
        print(f"{index + 1}. Mã: {student['student_id']:<10} | Tên: {student['name']:<20} | Toán: {student['math_score']:<5} | Anh: {student['english_score']}")


def add_student(student_list):
    """Chức năng 2: Thêm học viên mới vào danh sách"""
    # 1. Kiểm tra trùng mã ID
    while True:
        id_input = input("Nhập mã sinh viên: ").strip().upper()
        if find_student_by_id(student_list, id_input) != -1:
            print("Mã sinh viên đã tồn tại! Vui lòng nhập lại.")
        else:
            break
            
    name_input = input("Mời bạn nhập tên sinh viên: ").strip()
    
    # 2. Sử dụng hàm helper để nhập điểm gọn gàng hơn
    add_math_score = validate_score("Mời bạn nhập điểm toán: ")
    add_english_score = validate_score("Mời bạn nhập điểm anh: ")
    
    # 3. Tiến hành thêm dictionary mới vào list
    student_list.append({
        "student_id" : id_input,
        "name" : name_input,
        "math_score" : add_math_score,
        "english_score" : add_english_score
    })
    print(f"Thêm sinh viên {name_input} thành công!")
    

def update_score(student_list):
    """Chức năng 3: Cập nhật thông tin sinh viên theo mã học viên"""
    input_id = input("Mời bạn nhập vào mã sinh viên cần sửa: ").strip().upper()
    index = find_student_by_id(student_list, input_id)

    # Nếu không tìm thấy vị trí của ID trong list thì dừng hàm
    if index == -1:
        print("Không tìm thấy mã sinh viên!")
        return
    
    # Nếu tìm thấy, tiến hành cập nhật lại các thông tin mới
    name_input = input("Mời bạn nhập tên sinh viên mới: ").strip()
    add_math_score = validate_score("Mời bạn nhập điểm toán mới: ")
    add_english_score = validate_score("Mời bạn nhập điểm anh mới: ")

    # Ghi đè dữ liệu mới vào vị trí index đã tìm thấy
    student_list[index]['name'] = name_input
    student_list[index]['math_score'] = add_math_score
    student_list[index]['english_score'] = add_english_score
    print(f"Cập nhật sinh viên với id: {input_id} thành công!")


def evaluate_students(student_list):
    """Chức năng 4: Đánh giá học lực toàn bộ học viên (Đã sửa lỗi vòng lặp)"""
    if not student_list:
        print("Không có dữ liệu sinh viên để đánh giá!")
        return

    # Duyệt tuần tự qua từng sinh viên, tính điểm và in trực tiếp
    for index, student in enumerate(student_list):
        # Tính toán điểm trung bình
        total = (student['math_score'] + student['english_score']) / 2
        # Gọi hàm helper để lấy chuỗi xếp loại
        level = get_rank(total)
        
        print(f"{index + 1}. Mã: {student['student_id']:<10} | Tên: {student['name']:<20} | Điểm TB: {total:<5.2f} | Xếp loại: {level}")
                    
# ==============================================================================
# PHẦN 3: LUỒNG ĐIỀU KHIỂN CHƯƠNG TRÌNH (MENU LOOP)
# ==============================================================================
while True:
    try:
        choice = int(input('''
===== HỆ THỐNG QUẢN LÝ ĐIỂM THI RIKKEI ACADEMY =====
1. Hiển thị danh sách học viên
2. Thêm học viên mới
3. Cập nhật điểm thi theo mã học viên
4. Đánh giá học lực của toàn bộ học viên
5. Thoát chương trình
Mời bạn nhập lựa chọn: '''))
        
        if choice <= 0 or choice > 5:
            print("Menu không tồn tại! Vui lòng chọn từ 1 đến 5.")
            continue # Bỏ qua đoạn dưới, chạy lại vòng lặp menu

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
                print("Cảm ơn bạn đã sử dụng chương trình!")
                break # Thoát khỏi vòng lặp vô hạn, đóng chương trình

    except ValueError:
        print("Vui lòng nhập đúng kiểu dữ liệu số nguyên!")