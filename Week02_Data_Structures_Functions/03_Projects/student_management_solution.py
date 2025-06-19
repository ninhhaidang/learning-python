"""
Student Management System - Solution
Hệ thống quản lý sinh viên hoàn chình
Tuần 2: Data Structures & Functions
"""

import json
import os
from datetime import datetime

class StudentManagementSystem:
    """Lớp chính quản lý hệ thống sinh viên"""
    
    def __init__(self):
        """Khởi tạo hệ thống"""
        self.students = {}
        self.subjects = ["Toán", "Văn", "Anh", "Lý", "Hóa", "Sinh"]
        self.data_file = "students_data.json"
        self.load_data()
    
    def load_data(self):
        """Tải dữ liệu từ file"""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    self.students = json.load(f)
                print("Đã tải dữ liệu từ file thành công!")
            else:
                print("File dữ liệu chưa tồn tại. Khởi tạo hệ thống mới.")
        except Exception as e:
            print(f"Lỗi khi tải dữ liệu: {e}")
            self.students = {}
    
    def save_data(self):
        """Lưu dữ liệu vào file"""
        try:
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(self.students, f, ensure_ascii=False, indent=2)
            print("Đã lưu dữ liệu thành công!")
        except Exception as e:
            print(f"Lỗi khi lưu dữ liệu: {e}")
    
    def generate_student_id(self):
        """Tự động tạo mã sinh viên"""
        if not self.students:
            return "SV001"
        
        # Tìm số lớn nhất trong các mã hiện có
        max_num = 0
        for student_id in self.students.keys():
            if student_id.startswith("SV"):
                try:
                    num = int(student_id[2:])
                    max_num = max(max_num, num)
                except ValueError:
                    continue
        
        return f"SV{max_num + 1:03d}"
    
    def add_student(self):
        """Thêm sinh viên mới"""
        print("\n=== THÊM SINH VIÊN MỚI ===")
        
        # Tạo mã sinh viên tự động
        student_id = self.generate_student_id()
        print(f"Mã sinh viên tự động: {student_id}")
        
        # Nhập thông tin cơ bản
        name = input("Họ và tên: ").strip()
        if not name:
            print("Tên không được để trống!")
            return
        
        try:
            age = int(input("Tuổi: "))
            if age < 15 or age > 30:
                print("Tuổi phải từ 15-30!")
                return
        except ValueError:
            print("Tuổi phải là số nguyên!")
            return
        
        gender = input("Giới tính (Nam/Nữ): ").strip()
        if gender not in ["Nam", "Nữ"]:
            print("Giới tính chỉ được nhập 'Nam' hoặc 'Nữ'!")
            return
        
        address = input("Địa chỉ: ").strip()
        phone = input("Số điện thoại: ").strip()
        
        # Nhập điểm các môn
        scores = {}
        print("\nNhập điểm các môn học (0-10):")
        for subject in self.subjects:
            while True:
                try:
                    score = float(input(f"Điểm {subject}: "))
                    if 0 <= score <= 10:
                        scores[subject] = score
                        break
                    else:
                        print("Điểm phải từ 0-10!")
                except ValueError:
                    print("Điểm phải là số!")
        
        # Tính điểm trung bình
        average = sum(scores.values()) / len(scores)
        
        # Phân loại học lực
        grade = self.classify_grade(average)
        
        # Lưu thông tin sinh viên
        self.students[student_id] = {
            "name": name,
            "age": age,
            "gender": gender,
            "address": address,
            "phone": phone,
            "scores": scores,
            "average": round(average, 2),
            "grade": grade,
            "created_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        print(f"\nĐã thêm sinh viên {student_id} - {name} thành công!")
        print(f"Điểm trung bình: {average:.2f} - Học lực: {grade}")
        
        self.save_data()
    
    def classify_grade(self, average):
        """Phân loại học lực theo điểm trung bình"""
        if average >= 9.0:
            return "Xuất sắc"
        elif average >= 8.0:
            return "Giỏi"
        elif average >= 6.5:
            return "Khá"
        elif average >= 5.0:
            return "Trung bình"
        else:
            return "Yếu"
    
    def display_student_info(self, student_id, student_data):
        """Hiển thị thông tin chi tiết một sinh viên"""
        print(f"\n{'='*50}")
        print(f"MÃ SINH VIÊN: {student_id}")
        print(f"Họ tên: {student_data['name']}")
        print(f"Tuổi: {student_data['age']}")
        print(f"Giới tính: {student_data['gender']}")
        print(f"Địa chỉ: {student_data['address']}")
        print(f"Điện thoại: {student_data['phone']}")
        print(f"Ngày tạo: {student_data.get('created_date', 'N/A')}")
        
        print(f"\nĐIỂM CÁC MÔN:")
        for subject, score in student_data['scores'].items():
            print(f"  {subject}: {score}")
        
        print(f"\nĐiểm trung bình: {student_data['average']}")
        print(f"Học lực: {student_data['grade']}")
        print(f"{'='*50}")
    
    def view_student(self):
        """Xem thông tin sinh viên"""
        if not self.students:
            print("Danh sách sinh viên trống!")
            return
        
        print("\n=== XEM THÔNG TIN SINH VIÊN ===")
        student_id = input("Nhập mã sinh viên (hoặc Enter để xem tất cả): ").strip().upper()
        
        if not student_id:
            # Hiển thị tất cả sinh viên
            print(f"\n{'STT':<5} {'Mã SV':<8} {'Họ tên':<25} {'Tuổi':<5} {'ĐTB':<6} {'Học lực':<12}")
            print("-" * 70)
            
            for i, (sid, data) in enumerate(self.students.items(), 1):
                print(f"{i:<5} {sid:<8} {data['name']:<25} {data['age']:<5} "
                      f"{data['average']:<6} {data['grade']:<12}")
        
        elif student_id in self.students:
            self.display_student_info(student_id, self.students[student_id])
        else:
            print("Không tìm thấy sinh viên với mã này!")
    
    def update_student(self):
        """Cập nhật thông tin sinh viên"""
        if not self.students:
            print("Danh sách sinh viên trống!")
            return
        
        print("\n=== CẬP NHẬT THÔNG TIN SINH VIÊN ===")
        student_id = input("Nhập mã sinh viên: ").strip().upper()
        
        if student_id not in self.students:
            print("Không tìm thấy sinh viên với mã này!")
            return
        
        student = self.students[student_id]
        print(f"\nThông tin hiện tại của {student['name']}:")
        self.display_student_info(student_id, student)
        
        print("\nChọn thông tin cần cập nhật:")
        print("1. Họ tên")
        print("2. Tuổi") 
        print("3. Địa chỉ")
        print("4. Điện thoại")
        print("5. Điểm các môn")
        print("6. Cập nhật tất cả")
        
        choice = input("Lựa chọn: ").strip()
        
        if choice == "1":
            new_name = input(f"Họ tên mới (hiện tại: {student['name']}): ").strip()
            if new_name:
                student['name'] = new_name
                print("Đã cập nhật họ tên!")
        
        elif choice == "2":
            try:
                new_age = int(input(f"Tuổi mới (hiện tại: {student['age']}): "))
                if 15 <= new_age <= 30:
                    student['age'] = new_age
                    print("Đã cập nhật tuổi!")
                else:
                    print("Tuổi phải từ 15-30!")
            except ValueError:
                print("Tuổi phải là số nguyên!")
        
        elif choice == "3":
            new_address = input(f"Địa chỉ mới (hiện tại: {student['address']}): ").strip()
            if new_address:
                student['address'] = new_address
                print("Đã cập nhật địa chỉ!")
        
        elif choice == "4":
            new_phone = input(f"Điện thoại mới (hiện tại: {student['phone']}): ").strip()
            if new_phone:
                student['phone'] = new_phone
                print("Đã cập nhật điện thoại!")
        
        elif choice == "5":
            print("Cập nhật điểm các môn:")
            new_scores = {}
            for subject in self.subjects:
                while True:
                    current_score = student['scores'].get(subject, 0)
                    try:
                        score_input = input(f"Điểm {subject} (hiện tại: {current_score}): ").strip()
                        if not score_input:
                            new_scores[subject] = current_score
                            break
                        
                        score = float(score_input)
                        if 0 <= score <= 10:
                            new_scores[subject] = score
                            break
                        else:
                            print("Điểm phải từ 0-10!")
                    except ValueError:
                        print("Điểm phải là số!")
            
            student['scores'] = new_scores
            student['average'] = round(sum(new_scores.values()) / len(new_scores), 2)
            student['grade'] = self.classify_grade(student['average'])
            print("Đã cập nhật điểm và tính lại học lực!")
        
        elif choice == "6":
            # Cập nhật tất cả thông tin
            print("Cập nhật tất cả thông tin:")
            # (Có thể implement logic cập nhật từng field)
            print("Chức năng đang phát triển...")
        
        else:
            print("Lựa chọn không hợp lệ!")
            return
        
        self.save_data()
        print("Cập nhật thành công!")
    
    def delete_student(self):
        """Xóa sinh viên"""
        if not self.students:
            print("Danh sách sinh viên trống!")
            return
        
        print("\n=== XÓA SINH VIÊN ===")
        student_id = input("Nhập mã sinh viên cần xóa: ").strip().upper()
        
        if student_id not in self.students:
            print("Không tìm thấy sinh viên với mã này!")
            return
        
        student = self.students[student_id]
        print(f"\nThông tin sinh viên sẽ bị xóa:")
        print(f"Mã: {student_id}")
        print(f"Tên: {student['name']}")
        print(f"Điểm TB: {student['average']}")
        
        confirm = input("\nBạn có chắc chắn muốn xóa? (yes/no): ").strip().lower()
        
        if confirm in ['yes', 'y']:
            deleted_student = self.students.pop(student_id)
            print(f"Đã xóa sinh viên {student_id} - {deleted_student['name']}")
            self.save_data()
        else:
            print("Hủy thao tác xóa!")
    
    def search_students(self):
        """Tìm kiếm sinh viên theo nhiều tiêu chí"""
        if not self.students:
            print("Danh sách sinh viên trống!")
            return
        
        print("\n=== TÌM KIẾM SINH VIÊN ===")
        print("1. Tìm theo tên")
        print("2. Tìm theo học lực")
        print("3. Tìm theo độ tuổi")
        print("4. Tìm theo điểm môn học")
        
        choice = input("Lựa chọn: ").strip()
        results = []
        
        if choice == "1":
            keyword = input("Nhập tên cần tìm: ").strip().lower()
            results = [(sid, data) for sid, data in self.students.items() 
                      if keyword in data['name'].lower()]
        
        elif choice == "2":
            print("Các loại học lực: Xuất sắc, Giỏi, Khá, Trung bình, Yếu")
            grade = input("Nhập học lực: ").strip()
            results = [(sid, data) for sid, data in self.students.items() 
                      if data['grade'] == grade]
        
        elif choice == "3":
            try:
                min_age = int(input("Tuổi từ: "))
                max_age = int(input("Tuổi đến: "))
                results = [(sid, data) for sid, data in self.students.items() 
                          if min_age <= data['age'] <= max_age]
            except ValueError:
                print("Tuổi phải là số nguyên!")
                return
        
        elif choice == "4":
            print(f"Các môn học: {', '.join(self.subjects)}")
            subject = input("Nhập tên môn: ").strip()
            if subject not in self.subjects:
                print("Môn học không hợp lệ!")
                return
            
            try:
                min_score = float(input("Điểm từ: "))
                max_score = float(input("Điểm đến: "))
                results = [(sid, data) for sid, data in self.students.items() 
                          if min_score <= data['scores'].get(subject, 0) <= max_score]
            except ValueError:
                print("Điểm phải là số!")
                return
        
        else:
            print("Lựa chọn không hợp lệ!")
            return
        
        # Hiển thị kết quả
        if results:
            print(f"\nTìm thấy {len(results)} sinh viên:")
            print(f"{'STT':<5} {'Mã SV':<8} {'Họ tên':<25} {'Tuổi':<5} {'ĐTB':<6} {'Học lực':<12}")
            print("-" * 70)
            
            for i, (sid, data) in enumerate(results, 1):
                print(f"{i:<5} {sid:<8} {data['name']:<25} {data['age']:<5} "
                      f"{data['average']:<6} {data['grade']:<12}")
        else:
            print("Không tìm thấy sinh viên nào phù hợp!")
    
    def generate_statistics(self):
        """Tạo báo cáo thống kê"""
        if not self.students:
            print("Danh sách sinh viên trống!")
            return
        
        print("\n" + "="*60)
        print("           BÁO CÁO THỐNG KÊ HỆ THỐNG")
        print("="*60)
        
        total_students = len(self.students)
        print(f"Tổng số sinh viên: {total_students}")
        
        # Thống kê giới tính
        gender_stats = {"Nam": 0, "Nữ": 0}
        for student in self.students.values():
            gender_stats[student['gender']] += 1
        
        print(f"\nThống kê giới tính:")
        for gender, count in gender_stats.items():
            percentage = (count / total_students) * 100
            print(f"  {gender}: {count} sinh viên ({percentage:.1f}%)")
        
        # Thống kê học lực
        grade_stats = {}
        for student in self.students.values():
            grade = student['grade']
            grade_stats[grade] = grade_stats.get(grade, 0) + 1
        
        print(f"\nThống kê học lực:")
        grade_order = ["Xuất sắc", "Giỏi", "Khá", "Trung bình", "Yếu"]
        for grade in grade_order:
            count = grade_stats.get(grade, 0)
            percentage = (count / total_students) * 100
            print(f"  {grade}: {count} sinh viên ({percentage:.1f}%)")
        
        # Thống kê độ tuổi
        ages = [student['age'] for student in self.students.values()]
        avg_age = sum(ages) / len(ages)
        min_age = min(ages)
        max_age = max(ages)
        
        print(f"\nThống kê độ tuổi:")
        print(f"  Tuổi trung bình: {avg_age:.1f}")
        print(f"  Tuổi nhỏ nhất: {min_age}")
        print(f"  Tuổi lớn nhất: {max_age}")
        
        # Thống kê điểm số
        all_averages = [student['average'] for student in self.students.values()]
        class_average = sum(all_averages) / len(all_averages)
        highest_avg = max(all_averages)
        lowest_avg = min(all_averages)
        
        print(f"\nThống kê điểm số:")
        print(f"  Điểm TB lớp: {class_average:.2f}")
        print(f"  Điểm TB cao nhất: {highest_avg}")
        print(f"  Điểm TB thấp nhất: {lowest_avg}")
        
        # Top 3 sinh viên giỏi nhất
        top_students = sorted(self.students.items(), 
                            key=lambda x: x[1]['average'], reverse=True)[:3]
        
        print(f"\nTop 3 sinh viên xuất sắc:")
        for i, (sid, data) in enumerate(top_students, 1):
            print(f"  {i}. {data['name']} ({sid}) - ĐTB: {data['average']}")
        
        # Thống kê theo từng môn
        print(f"\nĐiểm trung bình từng môn:")
        for subject in self.subjects:
            subject_scores = [student['scores'][subject] 
                            for student in self.students.values()]
            subject_avg = sum(subject_scores) / len(subject_scores)
            print(f"  {subject}: {subject_avg:.2f}")
        
        print("="*60)
    
    def export_data(self):
        """Xuất dữ liệu ra file"""
        if not self.students:
            print("Danh sách sinh viên trống!")
            return
        
        print("\n=== XUẤT DỮ LIỆU ===")
        print("1. Xuất file JSON")
        print("2. Xuất file CSV")
        print("3. Xuất báo cáo TXT")
        
        choice = input("Lựa chọn: ").strip()
        
        if choice == "1":
            filename = f"students_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            try:
                with open(filename, 'w', encoding='utf-8') as f:
                    json.dump(self.students, f, ensure_ascii=False, indent=2)
                print(f"Đã xuất dữ liệu ra file: {filename}")
            except Exception as e:
                print(f"Lỗi khi xuất file: {e}")
        
        elif choice == "2":
            filename = f"students_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
            try:
                with open(filename, 'w', encoding='utf-8') as f:
                    # Header
                    headers = ["Mã SV", "Họ tên", "Tuổi", "Giới tính", "Địa chỉ", "Điện thoại"]
                    headers.extend(self.subjects)
                    headers.extend(["Điểm TB", "Học lực"])
                    f.write(",".join(headers) + "\n")
                    
                    # Data
                    for sid, data in self.students.items():
                        row = [sid, data['name'], str(data['age']), data['gender'], 
                              data['address'], data['phone']]
                        row.extend([str(data['scores'][subject]) for subject in self.subjects])
                        row.extend([str(data['average']), data['grade']])
                        f.write(",".join(row) + "\n")
                
                print(f"Đã xuất dữ liệu ra file: {filename}")
            except Exception as e:
                print(f"Lỗi khi xuất file: {e}")
        
        elif choice == "3":
            filename = f"students_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            try:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write("BÁO CÁO DANH SÁCH SINH VIÊN\n")
                    f.write("="*50 + "\n")
                    f.write(f"Ngày tạo: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")
                    f.write(f"Tổng số sinh viên: {len(self.students)}\n\n")
                    
                    for sid, data in self.students.items():
                        f.write(f"Mã SV: {sid}\n")
                        f.write(f"Họ tên: {data['name']}\n")
                        f.write(f"Tuổi: {data['age']} - Giới tính: {data['gender']}\n")
                        f.write(f"Địa chỉ: {data['address']}\n")
                        f.write(f"Điện thoại: {data['phone']}\n")
                        f.write("Điểm các môn:\n")
                        for subject, score in data['scores'].items():
                            f.write(f"  {subject}: {score}\n")
                        f.write(f"Điểm TB: {data['average']} - Học lực: {data['grade']}\n")
                        f.write("-"*30 + "\n")
                
                print(f"Đã xuất báo cáo ra file: {filename}")
            except Exception as e:
                print(f"Lỗi khi xuất file: {e}")
        
        else:
            print("Lựa chọn không hợp lệ!")
    
    def display_menu(self):
        """Hiển thị menu chính"""
        print("\n" + "="*60)
        print("           HỆ THỐNG QUẢN LÝ SINH VIÊN")
        print("="*60)
        print("1. Thêm sinh viên mới")
        print("2. Xem thông tin sinh viên")
        print("3. Cập nhật thông tin")
        print("4. Xóa sinh viên")
        print("5. Tìm kiếm sinh viên")
        print("6. Thống kê báo cáo")
        print("7. Xuất dữ liệu")
        print("8. Tải lại dữ liệu")
        print("9. Về menu chính")
        print("0. Thoát chương trình")
        print("-"*60)
    
    def run(self):
        """Chạy chương trình chính"""
        print("CHÀO MỪNG ĐẾN HỆ THỐNG QUẢN LÝ SINH VIÊN!")
        print("Phiên bản 2.0 - Tuần 2: Data Structures & Functions")
        
        while True:
            self.display_menu()
            
            try:
                choice = input("Lựa chọn của bạn: ").strip()
                
                if choice == "1":
                    self.add_student()
                elif choice == "2":
                    self.view_student()
                elif choice == "3":
                    self.update_student()
                elif choice == "4":
                    self.delete_student()
                elif choice == "5":
                    self.search_students()
                elif choice == "6":
                    self.generate_statistics()
                elif choice == "7":
                    self.export_data()
                elif choice == "8":
                    self.load_data()
                elif choice == "9":
                    continue
                elif choice == "0":
                    print("\nCảm ơn bạn đã sử dụng hệ thống!")
                    print("Tạm biệt!")
                    break
                else:
                    print("Lựa chọn không hợp lệ! Vui lòng chọn từ 0-9.")
                
                # Pause để user đọc kết quả
                input("\nNhấn Enter để tiếp tục...")
                
            except KeyboardInterrupt:
                print("\n\nChương trình bị gián đoạn!")
                save_confirm = input("Bạn có muốn lưu dữ liệu trước khi thoát? (y/n): ")
                if save_confirm.lower() in ['y', 'yes']:
                    self.save_data()
                print("Tạm biệt!")
                break
            except Exception as e:
                print(f"Lỗi không mong muốn: {e}")
                print("Vui lòng thử lại!")

def main():
    """Hàm main"""
    system = StudentManagementSystem()
    system.run()

if __name__ == "__main__":
    main()
