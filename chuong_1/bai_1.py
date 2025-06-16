# Bài 1. Viết chương trình C để tính cước điện thoại bàn cho một hộ gia đình với các thông số như sau:
#             Phí thuê bao bắt buộc là 25 nghìn.
#             600 đồng cho mỗi phút gọi của 50 phút đầu tiên.
#             400 đồng cho mỗi phút gọi của 150 phút tiếp theo.
#             200 đồng cho bất kỳ phút gọi nào sau 200 phút đầu tiên.

def gia_cuoc(thoi_gian, cuoc_co_dinh):
    if thoi_gian <= 50:
        cuoc_thue_bao = cuoc_co_dinh + thoi_gian * 600
    elif thoi_gian <= 200:
        cuoc_thue_bao = cuoc_co_dinh + 50 * 600 + (thoi_gian - 50) * 400
    else:
        cuoc_thue_bao = cuoc_co_dinh + 50 * 600 + 150 * 400 + (thoi_gian - 200) * 200
    return cuoc_thue_bao

cuoc_co_dinh = 25000
thoi_gian = int(input("Nhập số phút gọi trong tháng: "))

tong_cuoc = gia_cuoc(thoi_gian, cuoc_co_dinh)
print("Giá cước của bạn tháng này là:", tong_cuoc, "đồng")
