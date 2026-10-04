import time
import random
import matplotlib.pyplot as plt # Thư viện vẽ đồ thị

# 1. Cài đặt thuật toán Selection Sort (Theo Slide 11)
def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Hoán đổi
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# 2. Hàm thực nghiệm (Chạy và đo thời gian)
def run_experiment():
    # Các kích thước đầu vào (n) muốn kiểm tra
    input_sizes = [100, 500, 1000, 1500, 2000, 2500] 
    execution_times = []

    print(f"{'Kích thước (n)':<15} | {'Thời gian (giây)':<15}")
    print("-" * 35)

    for n in input_sizes:
        # Sinh mảng ngẫu nhiên từ 0 đến 10000
        data = [random.randint(0, 10000) for _ in range(n)]
        
        # Bắt đầu đo giờ
        start_time = time.time()
        
        # Gọi thuật toán
        selection_sort(data)
        
        # Kết thúc đo giờ
        end_time = time.time()
        
        # Tính khoảng thời gian chạy
        run_time = end_time - start_time
        execution_times.append(run_time)
        
        print(f"{n:<15} | {run_time:.6f}")

    # 3. Vẽ đồ thị kết quả
    plt.plot(input_sizes, execution_times, marker='o', color='b', label='Selection Sort')
    plt.xlabel('Kích thước đầu vào (n)')
    plt.ylabel('Thời gian thực thi (giây)')
    plt.title('Độ phức tạp thực nghiệm của Selection Sort')
    plt.grid(True)
    plt.legend()
    plt.show()

# Chạy chương trình
if __name__ == "__main__":
    run_experiment()