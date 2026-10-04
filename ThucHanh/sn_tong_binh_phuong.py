# Bài toán tính tổng S=12+22+…+n2
def sn_tong_binh_phuong(n):
    s=0
    for i in range(1,n+1):
        s+=i**2
    return s

# Giải thuật sắp xếp chọn trực tiếp (Selection Sort)
def selection_sort(a,n):
    for i in range(n-1):
        min = i
        j = i+1
        for j in range(n):
            if a[i] < a[min]:
                min = i
        swap(a[i], a[j])

# Giải thuật tìm kiếm tuần tự (Sequential Search)
def sequential_search(n,k):
    i = 0
    while i<n and a[i]!=k:
        i+=1
    if i<n:
        return i
    else:
        return -1
    
# Bài toán so trùng mẫu của chuỗi ký tự (String Matching)
def string_match(T[n], P[m]):
    for i in range(n-m):
        j=0
        while j<m and P[j] == T[i+j]:
            j+=1
        if j==m:
            return i
    return -1

# Bài toán tìm cặp điểm gần nhất (Closest-Pair)
def Closet_pair(n, x):
    d = max
    i=1
    for i in range(n):
        j=i+1
        for j in range(n+1):
            d= min(d, abs(x[i]-x[j]))
    return d

# Bài toán người đi du lịch (Traveling Salesman)
def traveling_salesman(dist_matrix):
    n = len(dist_matrix)
    if n <= 1:
        return [0], 0

    # 1. Khởi tạo khoảng cách nhỏ nhất d = vô cùng, và đường đi tốt nhất pi = rỗng
    d = float("inf")
    pi = []

    # Thành phố bắt đầu cố định là 0 (tương ứng với t1 trong mã giả)
    start_city = 0

    # Danh sách các thành phố còn lại cần tìm hoán vị: [1, 2, ..., n-1]
    remaining_cities = list(range(1, n))

    # 2, 3. Lặp qua tất cả (n-1)! hoán vị của các thành phố còn lại
    for p in itertools.permutations(remaining_cities):
        # 4. Tính tổng khoảng cách của chu trình hiện tại
        # Bắt đầu từ 0 -> thành phố đầu tiên trong hoán vị
        current_dist = dist_matrix[start_city][p[0]]

        # Cộng khoảng cách giữa các thành phố trong hoán vị
        for i in range(len(p) - 1):
            current_dist += dist_matrix[p[i]][p[i + 1]]

        # Quay trở lại thành phố bắt đầu 0
        current_dist += dist_matrix[p[-1]][start_city]

        # 5. Nếu tìm thấy đường đi ngắn hơn d hiện tại
        if current_dist < d:
            d = current_dist  # 6. Cập nhật lại d nhỏ nhất
            pi = [start_city] + list(p) + [start_city]  # 7. Lưu lại đường đi pi

    # 8. Trả về đường đi tốt nhất và tổng khoảng cách của nó
    return pi, d