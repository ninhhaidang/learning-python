"""
Exercise 04: Control Flow - Solutions
Bài giải mẫu cho các bài tập về Control Flow
"""

import random
import datetime

def exercise_1_student_classification():
    """Bài 1: Hệ thống phân loại và thống kê học sinh"""
    print("=== BÀI 1: HỆ THỐNG PHÂN LOẠI HỌC SINH ===\n")
    
    students = [
        {"name": "Nguyễn Văn A", "age": 18, "math": 8.5, "literature": 7.5, "english": 9.0},
        {"name": "Trần Thị B", "age": 19, "math": 9.2, "literature": 8.8, "english": 8.5},
        {"name": "Lê Văn C", "age": 17, "math": 6.0, "literature": 7.0, "english": 6.5},
        {"name": "Phạm Thị D", "age": 21, "math": 9.5, "literature": 9.0, "english": 9.2},
        {"name": "Hoàng Văn E", "age": 18, "math": 5.0, "literature": 4.5, "english": 5.5}
    ]
    
    def classify_grade(avg_score):
        """Phân loại học lực"""
        if avg_score > 9:
            return "Xuất sắc"
        elif avg_score > 8:
            return "Giỏi"
        elif avg_score > 6.5:
            return "Khá"
        elif avg_score > 5:
            return "Trung bình"
        else:
            return "Yếu"
    
    def classify_age(age):
        """Phân loại độ tuổi"""
        if age < 18:
            return "Nhỏ tuổi"
        elif age <= 20:
            return "Bình thường"
        else:
            return "Lớn tuổi"
    
    def is_excellent_overall(student):
        """Kiểm tra học sinh giỏi toàn diện"""
        return all(score > 8 for score in [student["math"], student["literature"], student["english"]])
    
    # Tính điểm trung bình và phân loại
    for student in students:
        avg = (student["math"] + student["literature"] + student["english"]) / 3
        student["average"] = avg
        student["grade_level"] = classify_grade(avg)
        student["age_group"] = classify_age(student["age"])
    
    # Hiển thị danh sách chi tiết
    print("=== DANH SÁCH CHI TIẾT ===")
    for i, student in enumerate(students, 1):
        print(f"{i}. {student['name']} ({student['age']} tuổi) - "
              f"ĐTB: {student['average']:.2f} - "
              f"Học lực: {student['grade_level']} - "
              f"Độ tuổi: {student['age_group']}")
    print()
    
    # Thống kê theo học lực
    grade_stats = {}
    for student in students:
        grade = student["grade_level"]
        grade_stats[grade] = grade_stats.get(grade, 0) + 1
    
    print("=== THỐNG KÊ THEO HỌC LỰC ===")
    total_students = len(students)
    grade_order = ["Xuất sắc", "Giỏi", "Khá", "Trung bình", "Yếu"]
    
    for grade in grade_order:
        count = grade_stats.get(grade, 0)
        percentage = (count / total_students) * 100
        print(f"- {grade}: {count} học sinh ({percentage:.1f}%)")
    print()
    
    # Tìm học sinh giỏi toàn diện
    print("=== HỌC SINH GIỎI TOÀN DIỆN ===")
    excellent_students = [s for s in students if is_excellent_overall(s)]
    
    if excellent_students:
        for student in excellent_students:
            print(f"- {student['name']}: Toán {student['math']}, "
                  f"Văn {student['literature']}, Anh {student['english']}")
    else:
        print("Không có học sinh giỏi toàn diện.")
    print()
    
    # Top 3 học sinh điểm cao nhất
    print("=== TOP 3 HỌC SINH ĐIỂM CAO NHẤT ===")
    sorted_students = sorted(students, key=lambda x: x["average"], reverse=True)
    
    for i, student in enumerate(sorted_students[:3], 1):
        print(f"{i}. {student['name']} - ĐTB: {student['average']:.2f}")
    print()

def exercise_2_warehouse_management():
    """Bài 2: Quản lý kho hàng với vòng lặp"""
    print("=== BÀI 2: HỆ THỐNG QUẢN LÝ KHO HÀNG ===\n")
    
    warehouse = {}
    sales_history = []
    
    def add_product():
        """Thêm hàng hóa"""
        print("=== THÊM HÀNG HÓA ===")
        code = input("Mã hàng: ")
        name = input("Tên hàng: ")
        quantity = int(input("Số lượng: "))
        price = float(input("Giá bán: "))
        
        warehouse[code] = {
            "name": name,
            "quantity": quantity,
            "price": price,
            "sold": 0
        }
        print("Đã thêm thành công!")
    
    def sell_product():
        """Bán hàng"""
        print("=== BÁN HÀNG ===")
        code = input("Mã hàng: ")
        
        if code not in warehouse:
            print("Không tìm thấy mã hàng!")
            return
        
        quantity = int(input("Số lượng bán: "))
        product = warehouse[code]
        
        if quantity > product["quantity"]:
            print("Không đủ hàng trong kho!")
            return
        
        # Cập nhật kho
        product["quantity"] -= quantity
        product["sold"] += quantity
        
        # Tính tiền
        total = quantity * product["price"]
        sales_history.append({
            "code": code,
            "name": product["name"],
            "quantity": quantity,
            "total": total,
            "time": datetime.datetime.now()
        })
        
        print(f"Bán thành công! Tồn kho còn lại: {product['quantity']}")
        print(f"Tổng tiền: {total:,.0f} VNĐ")
        
        # Kiểm tra cảnh báo
        if product["quantity"] < 10:
            print(f"⚠️ CẢNH BÁO: {product['name']} sắp hết hàng!")
    
    def check_inventory():
        """Kiểm tra tồn kho"""
        print("=== TỒN KHO HIỆN TẠI ===")
        if not warehouse:
            print("Kho hàng trống!")
            return
        
        print(f"{'Mã':<10} {'Tên hàng':<20} {'Tồn kho':<10} {'Giá':<15}")
        print("-" * 60)
        
        low_stock = []
        for code, product in warehouse.items():
            print(f"{code:<10} {product['name']:<20} {product['quantity']:<10} {product['price']:,.0f}")
            if product['quantity'] < 10:
                low_stock.append((code, product))
        
        if low_stock:
            print("\n=== CẢNH BÁO TỒN KHO ===")
            print("Các mặt hàng sắp hết:")
            for code, product in low_stock:
                print(f"- {code}: {product['name']} (còn {product['quantity']} chiếc)")
    
    def show_statistics():
        """Thống kê kho hàng"""
        print("=== THỐNG KÊ KHO HÀNG ===")
        
        if not warehouse:
            print("Chưa có dữ liệu!")
            return
        
        # Tổng giá trị kho
        total_value = sum(p["quantity"] * p["price"] for p in warehouse.values())
        print(f"Tổng giá trị kho: {total_value:,.0f} VNĐ")
        
        # Doanh thu
        total_revenue = sum(sale["total"] for sale in sales_history)
        print(f"Tổng doanh thu: {total_revenue:,.0f} VNĐ")
        
        # Mặt hàng bán chạy nhất
        if warehouse:
            best_seller = max(warehouse.items(), key=lambda x: x[1]["sold"])
            print(f"Mặt hàng bán chạy: {best_seller[1]['name']} ({best_seller[1]['sold']} đã bán)")
    
    # Demo hệ thống (mô phỏng)
    print("=== HỆ THỐNG QUẢN LÝ KHO HÀNG ===\n")
    
    # Thêm một số sản phẩm mẫu
    warehouse = {
        "SP001": {"name": "Bút bi", "quantity": 50, "price": 5000, "sold": 15},
        "SP002": {"name": "Tập vở", "quantity": 8, "price": 12000, "sold": 12},
        "SP003": {"name": "Thước kẻ", "quantity": 25, "price": 8000, "sold": 5}
    }
    
    print("MENU CHÍNH:")
    print("1. Thêm hàng hóa")
    print("2. Bán hàng") 
    print("3. Kiểm tra tồn kho")
    print("4. Thống kê kho hàng")
    print("5. Thoát chương trình")
    print()
    
    # Mô phỏng một số thao tác
    print("Lựa chọn của bạn: 3")
    check_inventory()
    print()

def exercise_3_snake_game():
    """Bài 3: Trò chơi Rắn săn mồi (logic cơ bản)"""
    print("=== BÀI 3: SNAKE GAME LOGIC ===\n")
    
    # Khởi tạo game
    board_size = 10
    snake = [(5, 5), (5, 4), (5, 3)]  # Đầu rắn ở đầu list
    food = (3, 5)
    score = 0
    
    def print_board():
        """Hiển thị bàn chơi"""
        print(f"Điểm: {score} | Độ dài rắn: {len(snake)}")
        print()
        
        # Header với số cột
        print("  ", end="")
        for i in range(board_size):
            print(f"{i} ", end="")
        print()
        
        # Vẽ bàn chơi
        for row in range(board_size):
            print(f"{row} ", end="")
            for col in range(board_size):
                if (row, col) == food:
                    print("F ", end="")  # Food
                elif (row, col) in snake:
                    print("S ", end="")  # Snake
                else:
                    print(". ", end="")  # Empty
            print()
        print()
    
    def move_snake(direction):
        """Di chuyển rắn"""
        head_row, head_col = snake[0]
        
        # Tính vị trí mới của đầu rắn
        if direction == 'W':  # Up
            new_head = (head_row - 1, head_col)
        elif direction == 'S':  # Down
            new_head = (head_row + 1, head_col)
        elif direction == 'A':  # Left
            new_head = (head_row, head_col - 1)
        elif direction == 'D':  # Right
            new_head = (head_row, head_col + 1)
        else:
            return False, "Hướng không hợp lệ!"
        
        # Kiểm tra va chạm với tường
        if (new_head[0] < 0 or new_head[0] >= board_size or 
            new_head[1] < 0 or new_head[1] >= board_size):
            return False, "Va chạm với tường!"
        
        # Kiểm tra va chạm với thân rắn
        if new_head in snake:
            return False, "Va chạm với thân rắn!"
        
        # Di chuyển rắn
        snake.insert(0, new_head)
        
        # Kiểm tra ăn mồi
        global food, score
        if new_head == food:
            score += 10
            # Tạo mồi mới
            while True:
                new_food = (random.randint(0, board_size-1), 
                           random.randint(0, board_size-1))
                if new_food not in snake:
                    food = new_food
                    break
        else:
            # Không ăn mồi thì bỏ đuôi
            snake.pop()
        
        return True, "OK"
    
    # Demo game
    print("=== SNAKE GAME ===")
    print_board()
    
    # Mô phỏng một số nước đi
    moves = ['W', 'W', 'D', 'D']
    
    for move in moves:
        print(f"Nhập hướng di chuyển (W/A/S/D): {move}")
        success, message = move_snake(move)
        
        if not success:
            print(f"GAME OVER: {message}")
            break
        
        print_board()
    
    print(f"Điểm cuối game: {score}")
    print()

def exercise_4_sorting_algorithms():
    """Bài 4: Thuật toán sắp xếp và tìm kiếm"""
    print("=== BÀI 4: THUẬT TOÁN SẮP XẾP VÀ TÌM KIẾM ===\n")
    
    def bubble_sort(arr):
        """Bubble Sort với theo dõi các bước"""
        arr = arr.copy()
        n = len(arr)
        comparisons = 0
        steps = []
        
        for i in range(n):
            for j in range(0, n - i - 1):
                comparisons += 1
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
            
            if i < 3:  # Chỉ hiển thị 3 bước đầu
                steps.append(arr.copy())
        
        return arr, comparisons, steps
    
    def selection_sort(arr):
        """Selection Sort với theo dõi các bước"""
        arr = arr.copy()
        n = len(arr)
        comparisons = 0
        steps = []
        
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                comparisons += 1
                if arr[j] < arr[min_idx]:
                    min_idx = j
            
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            
            if i < 3:  # Chỉ hiển thị 3 bước đầu
                steps.append(arr.copy())
        
        return arr, comparisons, steps
    
    def linear_search(arr, target):
        """Tìm kiếm tuyến tính"""
        comparisons = 0
        for i, item in enumerate(arr):
            comparisons += 1
            if item == target:
                return i, comparisons
        return -1, comparisons
    
    def binary_search(arr, target):
        """Tìm kiếm nhị phân"""
        left, right = 0, len(arr) - 1
        comparisons = 0
        
        while left <= right:
            mid = (left + right) // 2
            comparisons += 1
            
            if arr[mid] == target:
                return mid, comparisons
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1, comparisons
    
    # Dữ liệu test
    numbers = [64, 34, 25, 12, 22, 11, 90, 88, 76, 50, 42]
    search_value = 22
    
    print(f"Mảng ban đầu: {numbers}")
    print()
    
    # Bubble Sort
    print("=== BUBBLE SORT ===")
    sorted_bubble, bubble_comparisons, bubble_steps = bubble_sort(numbers)
    
    for i, step in enumerate(bubble_steps, 1):
        print(f"Bước {i}: {step}")
    print("...")
    print(f"Kết quả: {sorted_bubble}")
    print(f"Số lần so sánh: {bubble_comparisons}")
    print()
    
    # Selection Sort
    print("=== SELECTION SORT ===")
    sorted_selection, selection_comparisons, selection_steps = selection_sort(numbers)
    
    for i, step in enumerate(selection_steps, 1):
        print(f"Bước {i}: {step}")
    print("...")
    print(f"Kết quả: {sorted_selection}")
    print(f"Số lần so sánh: {selection_comparisons}")
    print()
    
    # Tìm kiếm
    print("=== TÌM KIẾM ===")
    print(f"Tìm số {search_value}:")
    
    # Linear search trên mảng gốc
    linear_pos, linear_comps = linear_search(numbers, search_value)
    if linear_pos != -1:
        print(f"- Linear Search: Tìm thấy tại vị trí {linear_pos} ({linear_comps} lần so sánh)")
    else:
        print(f"- Linear Search: Không tìm thấy ({linear_comps} lần so sánh)")
    
    # Binary search trên mảng đã sắp xếp
    binary_pos, binary_comps = binary_search(sorted_bubble, search_value)
    if binary_pos != -1:
        print(f"- Binary Search: Tìm thấy tại vị trí {binary_pos} ({binary_comps} lần so sánh)")
    else:
        print(f"- Binary Search: Không tìm thấy ({binary_comps} lần so sánh)")
    print()

def exercise_5_atm_simulation():
    """Bài 5: Máy ATM mô phỏng"""
    print("=== BÀI 5: MÁY ATM MÔ PHỎNG ===\n")
    
    # Dữ liệu tài khoản mẫu
    accounts = {
        "1234567890": {
            "pin": "1234",
            "name": "Nguyễn Văn A",
            "balance": 2500000,
            "transactions": []
        }
    }
    
    current_account = None
    
    def login():
        """Đăng nhập"""
        global current_account
        
        print("=== CHÀO MỪNG ĐẾN ATM TECHBANK ===")
        print()
        
        card_number = input("Nhập số thẻ: ")
        
        if card_number not in accounts:
            print("Số thẻ không tồn tại!")
            return False
        
        # Cho phép 3 lần thử PIN
        for attempt in range(3):
            pin = input("Nhập mã PIN: ")
            
            if pin == accounts[card_number]["pin"]:
                current_account = card_number
                print(f"\nĐăng nhập thành công!")
                print(f"Xin chào, {accounts[card_number]['name']}")
                return True
            else:
                remaining = 2 - attempt
                if remaining > 0:
                    print(f"PIN không đúng! Còn {remaining} lần thử.")
                else:
                    print("Bạn đã nhập sai PIN 3 lần. Thẻ bị khóa!")
        
        return False
    
    def check_balance():
        """Kiểm tra số dư"""
        account = accounts[current_account]
        print(f"\n=== SỐ DƯ TÀI KHOẢN ===")
        print(f"Số dư hiện tại: {account['balance']:,} VNĐ")
    
    def withdraw_money():
        """Rút tiền"""
        account = accounts[current_account]
        
        print(f"\n=== RÚT TIỀN ===")
        print(f"Số dư hiện tại: {account['balance']:,} VNĐ")
        print()
        
        print("Chọn mệnh giá:")
        print("1. 100,000 VNĐ")
        print("2. 200,000 VNĐ")
        print("3. 500,000 VNĐ")
        print("4. 1,000,000 VNĐ")
        print("5. Nhập số tiền khác")
        
        choice = input("Lựa chọn: ")
        
        amounts = {"1": 100000, "2": 200000, "3": 500000, "4": 1000000}
        
        if choice in amounts:
            amount = amounts[choice]
        elif choice == "5":
            amount = int(input("Nhập số tiền: "))
        else:
            print("Lựa chọn không hợp lệ!")
            return
        
        # Kiểm tra số dư
        if amount > account['balance']:
            print("Số dư không đủ!")
            return
        
        # Kiểm tra mệnh giá (phải chia hết cho 50,000)
        if amount % 50000 != 0:
            print("Số tiền phải chia hết cho 50,000 VNĐ!")
            return
        
        # Thực hiện rút tiền
        account['balance'] -= amount
        account['transactions'].append({
            'type': 'withdraw',
            'amount': amount,
            'time': datetime.datetime.now(),
            'balance': account['balance']
        })
        
        print(f"\nBạn đã rút {amount:,} VNĐ")
        print(f"Số dư còn lại: {account['balance']:,} VNĐ")
        print("Cảm ơn bạn đã sử dụng dịch vụ!")
        
        # Ghi log
        time_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"\n[{time_str}] Rút tiền: -{amount:,} VNĐ")
    
    def deposit_money():
        """Gửi tiền"""
        account = accounts[current_account]
        
        print(f"\n=== GỬI TIỀN ===")
        amount = int(input("Nhập số tiền gửi: "))
        
        if amount <= 0:
            print("Số tiền phải lớn hơn 0!")
            return
        
        account['balance'] += amount
        account['transactions'].append({
            'type': 'deposit',
            'amount': amount,
            'time': datetime.datetime.now(),
            'balance': account['balance']
        })
        
        print(f"Đã gửi {amount:,} VNĐ vào tài khoản")
        print(f"Số dư mới: {account['balance']:,} VNĐ")
    
    def show_menu():
        """Hiển thị menu"""
        print(f"\nMENU CHÍNH:")
        print("1. Kiểm tra số dư")
        print("2. Rút tiền")
        print("3. Gửi tiền")
        print("4. Chuyển khoản")
        print("5. Đổi mã PIN")
        print("6. Lịch sử giao dịch")
        print("7. Thoát")
    
    # Demo ATM
    print("=== CHÀO MỪNG ĐẾN ATM TECHBANK ===")
    print("\nNhập số thẻ: 1234567890")
    print("Nhập mã PIN: ****")
    print("\nĐăng nhập thành công!")
    print("Xin chào, Nguyễn Văn A")
    
    show_menu()
    print("\nLựa chọn: 2")
    
    # Mô phỏng rút tiền
    print("\n=== RÚT TIỀN ===")
    print("Số dư hiện tại: 2,500,000 VNĐ")
    print("\nChọn mệnh giá:")
    print("1. 100,000 VNĐ")
    print("2. 200,000 VNĐ")
    print("3. 500,000 VNĐ")
    print("4. 1,000,000 VNĐ")
    print("5. Nhập số tiền khác")
    print("\nLựa chọn: 3")
    print("\nBạn đã rút 500,000 VNĐ")
    print("Số dư còn lại: 2,000,000 VNĐ")
    print("Cảm ơn bạn đã sử dụng dịch vụ!")
    
    time_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n[{time_str}] Rút tiền: -500,000 VNĐ")
    print()

def main():
    """Hàm main chạy tất cả bài tập"""
    print("GIẢI BÀI TẬP CONTROL FLOW")
    print("=" * 50)
    
    exercise_1_student_classification()
    print("-" * 50)
    
    exercise_2_warehouse_management()
    print("-" * 50)
    
    exercise_3_snake_game()
    print("-" * 50)
    
    exercise_4_sorting_algorithms()
    print("-" * 50)
    
    exercise_5_atm_simulation()

if __name__ == "__main__":
    main()
