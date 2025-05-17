#Trịnh Kiển Đạt_2280600653
#Phần này chỉ là ghi chú cho hiểu nên em có lập biến trùng tên nên chạy sẽ lỗi.



#Khai báo biến cho kiểu chuổi kiểu số nguyên và kiểu boolean
n = 15
name = "dat"
is_valid = True

#------------------------------------------------------------------------------
# if là từ khoá của ngôn ngữ không thể khai báo biến
# if = 5

#---------------------------------------------------------------------------------
# Các toán tử
a = 7
b = 5
# toán tử cộng a + b và gán cho result
result = a + b #result 12
# toán tử trừ a - b và gán cho result
result = a - b #result 2
# toán tử nhân a * b và gán cho result
result = a * b  #result 35
# toán tử chia a / b và gán cho result
result = a / b #result 1,4
# toán tử chia lấy dư a % b và gán cho result
result = a % b #result 2
# toán tử chia lấy phần nguyên a // b và gán cho result
result = a // b #result 1
# toán tử luỹ thừa a ** b và gán cho result
result = a ** b #result 16807 (7^5)

#---------------------------------------------------------------------------------------
#Toán tử logic
x = 4
y = 3
# phép toán and
result = (x>2) and (y<4) # kết quả True (True vs True = True còn False vs True = False)
# phép toán or 
result = (x>2) or (y>4) # kết quả True (Chỉ cần có True thì kết quả chung là True)
# phép toán not 
result = not (x==4) # kết quả False (phủ định điều kiện khi sử dụng not True => False và ngược lại)
# phép so sánh
result = (x==4) # kết quả True (so sánh biến = điều kiện thì True và ngược lại)
# phép so sánh không bằng
result = (x!=4) # kết quả False (so sánh biến != điều kiện thì False và ngược lại)
#Phép so sánh (<)(>) vs (<=)(>=)
x = 5
# giống phép toán lớp 2 thoi (so sánh biến x có đúng với giá trị hay không nếu đúng thì trả về True và gán cho result và ngược lại khi sai)
result = (x>3) #True
result = (x<3) #False
result = (x>=3) #True
result = (x<=3) # False

#---------------------------------------------------------------------------------------
#Nhập Xuất dữ liệu
name = input("Nhập tên của bạn: ") #dùng cho người dùng nhập 
print("Xin chào ${name}") # in ra chữ xin chào cùng với name người dùng nhập 
age = 25
print("Tuổi của tôi là : ${age}") # xuất ra câu lệnh kèm với giá trị biến age 
print("Python", "là", "ngôn", "ngữ", "lập trình", sep=" ") # kí tự phân cách Kết quả : Python là ngôn ngữ lập trình
print("Xin chào", end= " ")
print("các bank !")
# kết quả: Xin chào các bạn (ghép chuỗi)
#----------------------------------------------------------------------
#Các cấu trúc điều kiện
# câu lệnh if vs elif vs else (so sánh biến với điều kiện thoả mản thì in ra câu lệnh không thì chạy tới điều kiện tiếp theo)
x = 10
if x > 5:
    print("x lớn hơn 5")
elif x == 5:
    print("x bằng 5")
else:
    print("x nhỏ hơn 5")
# vòng lặp for cho cho chuỗi
fruits = ["táo", "chuối", "cherry"]
for fruit in fruits:
    print(fruit)
#vòng lặp while (cho bất đầu từ 0 và chạy xét điều kiện rồi cộng thêm 1 chạy đến không thoả điều kiện nữa thì dừng)
count = 0
while count < 5:
    print(count)
    count +=1
#Câu điều kiện nhảy 
#in ra giá trị 5 đầu tiên từ 1 - 100 "break"
for i in range (1, 101):
    if i % 5 == 0:
        print("Số chia hết cho 5 đầu tiên là:", i)
        break #nếu thoả điều kiện thì in ra kết quả và thoát khởi chương trình 
#in ra số chẳn từ 1 -10 và bỏ qua các số lẽ(in ra số thoả điều kiện còn không thoả thì bỏ qua)
for i in range (1, 11):
    if i % 2 != 0:
        continue
    print(i)
#Kiểm tra nếu không thoả thì tuyên bố rỗng "passs"'
x =5 
if x > 10:
    print("x lớn hơn 10")
else:
    pass

#----------------------------------------------------
#Chuỗi
#Khai báo chuỗi
string_single_quotes = 'Hay ho'
string_double_quotes = "Hay ho"
string_triple_quotes = ''' Hay ho '''
# truy xuất chuỗi theo vị trí của chuổi bất đầu chuỗi từ 0 -> ...
my_string = "Hello, nha world"
print(my_string[0])#Kết quả 'H'
print(my_string[11])#Kết quả 'w'
print(my_string[11:])#Kết quả 'world' lấy từ vị trí 11 đến hết
print(my_string[:4])#Kết quả 'Hello' lấy từ đầu đến vị trí thứ 4
print(my_string[7:9])#Kết quả 'nha' lấy từ vị trí 7 đến 9
#ghép chuỗi
string_1 = "Kiển"
string_2 = "Đạt"
concatennated_string = string_1 + " " + string_2 #Kết quả là: Kiển Đạt (ghép hai chuổi lại và gán cho concatennated_string)
# Tính độ dài của chuỗi bằng hàm "len()"
my_string = "Đạt đẹp trâu"
lenght = len(my_string) # kết quả bằng 11

#Hàm sử lý chuỗi
#loại bỏ khoản trắng đầu và cuối chuổi
my_string= "   Đạt nha    "
print(my_string.strip()) #kết quả 'Đat nha'
#Tách các chuỗi thành thành danh sách các từ hoặc phần tử
my_string = "Đạt nhu nhược"
print(my_string.split(","))#Kết quả ['Đạt', 'nhu', 'nhược'] 
#Thay thế phần tử bằng phần tử mới
my_string = "Đạt nhu nhược"
print(my_string.replace("Đạt", "Trang")) #  Kết quả "Trang nhu nhược"
#---------------------------------------------------------------------------
#Hàm (Function) cách khai báo hàm 
def my_string_function(par1, par2):
    result = par1 + par2
    return result
#cách gọi hàm
result = my_string_function(10,20) # giá trị 10, 20 cho biến par1 vs par2 = 30
print(result) # in ra kết quả trên màn hình

#Hàm tính tổng
def calculate_sum(a, b):
    result = a+b
    return result
sum_result = calculate_sum(10,20) # hàm và lưu kết quả về biến
print("Tổng hai số là ", sum_result) # hàm in ra kết quả

#hàm không trả về giá trị chỉ in ra thông báo
def greet(name):
    print("Xin chào, ", name)
greet("Đạt") # gọi hàm

#-------------------------------------------------------------
#Mảng(Array)
#nhập thêm thư viện array
from array import array
int_array = array('i', [1, 2, 3, 4, 5]) # khai báo mảng số nguyên
float_array = array('j', [1.5, 2.46, 3.1, 4.7]) #khai báo mảng số thực
print(int_array[0]) # truy câo mảng đầu tiên của array Kết quả: '1'
print(float_array[3]) # truy cập phần tử thứ 4 của array Kết quả: '4.7'
#Cập nhật giá trị phần tử 
int_array[2] = 10 # phần tử tại vị trí thứ hai trong mảng array kết quả: [1, 2, 10, 4, 5]
