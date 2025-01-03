import time
import matplotlib.pyplot as plt
from prettytable import PrettyTable
from matplotlib.ticker import FuncFormatter

#Sampel
psychologists = ["Dr. Naufal", "Dr. Zara", "Dr. Handoyo", "Dr. Handoko", "Dr. Hanggoro", "Dr. Haryanto", 
                 "Dr. Hartono", "Dr. Zaki", "Dr. Puput", "Dr. Badang", "Dr. Opunk", "Dr. Zamzam",
                 "Dr. Puni", "Dr. Azim", "Dr. Evan"]

#Fungsi Linear Search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

#Fungsi Binary Search
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

#Perkiraan waktu
def measure_time(func, arr, target):
    start_time = time.perf_counter()
    result = func(arr, target)
    end_time = time.perf_counter()
    return result, end_time - start_time

#Sorting untuk binary
sorted_psychologists = sorted(psychologists)

#Visualisasi
n_values = []
linear_times = []
binary_times = []

#Fungsi Update Grafik
def update_graph():
    plt.figure(figsize=(8, 6))
    plt.plot(n_values, linear_times, label='Linear Search', marker='o', linestyle='-')
    plt.plot(n_values, binary_times, label='Binary Search', marker='o', linestyle='-')
    plt.title('Perbandingan: Linear vs Binary Search')
    plt.xlabel('Iterasi')
    plt.ylabel('Running Time (seconds)')

    #Set 7 angka dibelakang koma (,)
    plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{x:.7f}'))
    
    plt.legend()
    plt.grid(True)
    plt.draw()
    plt.pause(0.01)
    
#Fungsi untuk menampilkan seluruh tabel
def print_execution_table():
    table = PrettyTable()
    table.field_names = ["Iterasi Pencarian", "Linear Time (s)", "Binary Time (s)"]
    min_len = min(len(n_values), len(linear_times), len(binary_times))
    for i in range(min_len):
        table.add_row([n_values[i], f"{linear_times[i]:.7f}", f"{binary_times[i]:.7f}"])
    print(table)

while True:    
    target_name = input("Masukkan nama dokter untuk dicari (ketik 'end' untuk keluar): ")

    if target_name.lower() == 'end':
        break

    index_linear, time_linear = measure_time(linear_search, psychologists, target_name)
    index_binary, time_binary = measure_time(binary_search, sorted_psychologists, target_name)

    #Apabila dokter yang dicari tidak ada
    if index_linear == -1 and index_binary == -1:
        print(f"'{target_name}' was not found in the dataset.")
        continue

    #Membuat 'table' menjadi PretttTable
    table = PrettyTable()
    table.field_names = ["Algoritma", "Running Time (seconds)"]

    #Baris Pada PrettyTable
    table.add_row(["Linear Search", f"{time_linear:.7f}"])
    table.add_row(["Binary Search", f"{time_binary:.7f}"])

    #Cetak Hasil
    print("Hasil Pencarian:")
    print(table)

    #Append
    n_values.append(len(n_values) + 1)
    linear_times.append(time_linear)
    binary_times.append(time_binary)

    #update Grafik
    update_graph()

    #Cetak Tabel Eksekusi
    print_execution_table()

plt.show()
