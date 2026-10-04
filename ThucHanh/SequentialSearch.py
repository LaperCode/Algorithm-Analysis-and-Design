import time
import random
import matplotlib.pyplot as plt

# --- Thuật toán Sequential Search ---
def sequential_search(arr, k):
    for i in range(len(arr)):
        if arr[i] == k:
            return i
    return -1

# --- Chạy thực nghiệm ---
def run_seq_search():
    input_sizes = [100000, 500000, 1000000, 2000000, 5000000] # n phải lớn mới thấy time chênh lệch
    times = []

    print(f"{'n':<15} | {'Time (s)':<15}")
    print("-" * 30)

    for n in input_sizes:
        # Sinh mảng ngẫu nhiên
        arr = [random.randint(0, 1000000) for _ in range(n)]
        k = random.randint(0, 1000000) # Số cần tìm

        start = time.time()
        sequential_search(arr, k)
        end = time.time()

        times.append(end - start)
        print(f"{n:<15} | {end - start:.6f}")

    # Vẽ đồ thị
    plt.plot(input_sizes, times, marker='o', color='green')
    plt.title('Độ phức tạp Sequential Search O(n)')
    plt.xlabel('Kích thước mảng (n)')
    plt.ylabel('Thời gian (giây)')
    plt.show()

if __name__ == "__main__":
    run_seq_search()