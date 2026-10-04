import time
import random
import itertools
import matplotlib.pyplot as plt

# --- Thuật toán TSP ---
def tsp_bruteforce(graph, n):
    vertex = []
    for i in range(1, n):
        vertex.append(i)
    
    min_path = float('inf')
    
    # Xét mọi hoán vị của các thành phố (trừ thành phố 0)
    perm_iter = itertools.permutations(vertex)
    
    for i in perm_iter:
        current_pathweight = 0
        k = 0
        for j in i:
            current_pathweight += graph[k][j]
            k = j
        current_pathweight += graph[k][0] # Quay về điểm đầu
        
        min_path = min(min_path, current_pathweight)
        
    return min_path

# --- Chạy thực nghiệm ---
def run_tsp():
    # n phải RẤT NHỎ vì O(n!) tăng cực nhanh
    input_sizes = [8, 9, 10, 11] 
    times = []

    print(f"{'Thành phố (n)':<15} | {'Time (s)':<15}")
    print("-" * 30)

    for n in input_sizes:
        # Sinh ma trận chi phí ngẫu nhiên n x n
        graph = [[random.randint(10, 100) if i != j else 0 for j in range(n)] for i in range(n)]

        start = time.time()
        tsp_bruteforce(graph, n)
        end = time.time()

        times.append(end - start)
        print(f"{n:<15} | {end - start:.6f}")

    plt.plot(input_sizes, times, marker='o', color='orange')
    plt.title('TSP Brute Force O(n!)')
    plt.xlabel('Số thành phố (n)')
    plt.ylabel('Thời gian (s)')
    plt.show()

if __name__ == "__main__":
    run_tsp()