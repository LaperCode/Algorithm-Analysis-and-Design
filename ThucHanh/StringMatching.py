import time
import random
import string
import matplotlib.pyplot as plt

# --- Thuật toán String Matching ---
def brute_force_string_match(text, pattern):
    n = len(text)
    m = len(pattern)
    for i in range(n - m + 1):
        j = 0
        while j < m and pattern[j] == text[i + j]:
            j += 1
        if j == m:
            return i
    return -1

# --- Hàm sinh chuỗi ngẫu nhiên ---
def generate_random_string(length):
    # Chọn ký tự từ bảng chữ cái in hoa
    letters = string.ascii_uppercase
    return ''.join(random.choice(letters) for _ in range(length))

# --- Chạy thực nghiệm ---
def run_string_match():
    # Giữ cố định độ dài pattern m, tăng độ dài text n
    n_sizes = [10000, 50000, 100000, 200000, 500000]
    m = 100 # Pattern dài 100 ký tự
    times = []

    print(f"{'Size Text (n)':<15} | {'Time (s)':<15}")
    print("-" * 30)

    for n in n_sizes:
        text = generate_random_string(n)
        pattern = generate_random_string(m) # Pattern ngẫu nhiên (khó tìm thấy -> trường hợp xấu)

        start = time.time()
        brute_force_string_match(text, pattern)
        end = time.time()

        times.append(end - start)
        print(f"{n:<15} | {end - start:.6f}")

    plt.plot(n_sizes, times, marker='o', color='red')
    plt.title('String Match Brute Force')
    plt.xlabel('Độ dài văn bản (n)')
    plt.ylabel('Thời gian (s)')
    plt.show()

if __name__ == "__main__":
    run_string_match()