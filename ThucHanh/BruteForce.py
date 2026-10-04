import itertools
import math

# Hàm tính khoảng cách giữa 2 thành phố
def dist(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Thuật toán TSP Vét cạn
def tsp_bruteforce(cities):
    n = len(cities)
    indices = range(n)
    shortest_path = None
    min_len = float('inf')
    
    # Sinh tất cả hoán vị (permutations) - Slide 24
    # Cố định thành phố đầu tiên (index 0) để giảm số hoán vị còn (n-1)!
    for perm in itertools.permutations(indices[1:]):
        current_path_indices = (0,) + perm + (0,) # Đi từ 0 -> ... -> 0
        current_len = 0
        
        for i in range(n):
            p1 = cities[current_path_indices[i]]
            p2 = cities[current_path_indices[i+1]]
            current_len += dist(p1, p2)
            
        if current_len < min_len:
            min_len = current_len
            shortest_path = current_path_indices
            
    return min_len

# Lưu ý: Chỉ test với n nhỏ (ví dụ: n = [8, 9, 10, 11])