# Bài 2. Viết chương trình tính tiền điện gồm các khoảng sau:
#             – Tiền thuê bao điện kế: 1000đ/tháng
#             – Định mức sử dụng điện cho mỗi hộ là: 50 KW với giá 230đ/KW
#             – Nếu phần vượt định mức <= 50KW thì tính giá 480đ/KW
#             – Nếu 50KW < phần vượt định mức < 100KW thì tính giá 700đ/KW
#             – Nếu phần vượt định mức >= 100KW thì tính giá 900đ/KW
#             Chỉ số mới và cũ được nhập vào từ bàn phím
#             – In ra màn hình chỉ số cũ, chỉ số mới, tiền trả định mức, tiền trả vượt định mức, tổng tiền phải trả.

chi_so_cu = int(input("Hãy nhập chỉ số điện tháng trước: "))
chi_so_moi = int(input("Hãy nhập chỉ số điện tháng này: "))
dien_ke = 1000
so_dien = chi_so_moi - chi_so_cu

# Khởi tạo biến
tien_tra_dinh_muc = 0
tien_tra_vuot_dinh_muc = 0

if so_dien <= 50:
        tien_tra_dinh_muc = 230 * so_dien
elif so_dien <= 100:
        tien_tra_dinh_muc = 230 * 50
        tien_tra_vuot_dinh_muc = (so_dien  - 50) * 480
elif so_dien <= 150:
        tien_tra_dinh_muc = 230 * 50
        tien_tra_vuot_dinh_muc = 50 * 480 + (so_dien - 100) * 700
else:
    tien_tra_dinh_muc = 230 * 50
    tien_tra_vuot_dinh_muc = 50 * 480 + 50 * 700 + (so_dien - 150) * 900

tong_tien_phai_tra = dien_ke + tien_tra_dinh_muc + tien_tra_vuot_dinh_muc

print("Chỉ số điện tháng trước là: ", chi_so_cu)
print("Chỉ số điện tháng này là: ", chi_so_moi)
print("Tiền trả định mức là: ", tien_tra_dinh_muc)
print("Tiền trả vượt định mức là: ", tien_tra_vuot_dinh_muc)
print("Tổng tiền phải trả là: ", tong_tien_phai_tra)