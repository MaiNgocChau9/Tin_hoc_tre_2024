n = 44

def tong_chu_so(x):
    sum = 0
    while x>0:
        sum += (x%10)**2
        x//=10
    return sum

def so_hanh_phuc(x):
    check = []
    for i in range(x):
        check.append(False)

    # check[i] == False có nghĩa là số i chưa từng được đc chạm đến trước đó
    # True có nghĩa là bạn đang chạy vào vòng lặp vô tận
    
    while True:
        if x == 1:
            print("So hanh phuc")
        elif x == 0:
            print("So buon ba")
        else:
            check[x] = True
            x = tong_chu_so(x)
            if check[x] == True: print("So nham chan")
so_hanh_phuc(n)