import time
import random
import math
import matplotlib.pyplot as plt

# --- Thuật toán Closest Pair ---
def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def brute_force_closest_pair(points):
    n = len(points)
    min_val = float('inf')
    for i in range(n - 1):
        for j in range(i + 1, n):
            d = dist(points[i], points[j])
            if d < min_val:
                min_val = d
    return min_val

# --- Chạy thực nghiệm ---
def run_closest_pair():
    input_sizes = [100, 500, 1000, 1500, 2000] # n^2 chạy khá chậm nên đừng để n quá lớn
    times = []

    print(f"{'Số điểm (n)':<15} | {'Time (s)':<15}")
    print("-" * 30)

    for n in input_sizes:
        # Sinh n điểm ngẫu nhiên tọa độ (x, y)
        points = [(random.randint(0, 10000), random.randint(0, 10000)) for _ in range(n)]

        start = time.time()
        brute_force_closest_pair(points)
        end = time.time()

        times.append(end - start)
        print(f"{n:<15} | {end - start:.6f}")

    plt.plot(input_sizes, times, marker='o', color='purple')
    plt.title('Closest Pair O(n^2)')
    plt.xlabel('Số lượng điểm (n)')
    plt.ylabel('Thời gian (s)')
    plt.show()

if __name__ == "__main__":
    run_closest_pair()