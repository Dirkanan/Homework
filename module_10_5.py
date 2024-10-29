import time
from multiprocessing import Pool


def read_info(filename):
    all_data = []

    with open(filename, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line.strip())



def linear_processing(file_list):
    start_time = time.time()

    for filename in file_list:
        read_info(filename)

    end_time = time.time()
    print(f"Время затраченное потоком: {end_time - start_time:.2f} seconds")


def multiprocessing_processing(file_list):
    start_time = time.time()

    with Pool() as pool:
        pool.map(read_info, file_list)

    end_time = time.time()
    print(f"Время затраченное мультипроцессором: {end_time - start_time:.2f} seconds")


if __name__ == '__main__':

    file_list = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']

    print("Начало линейного процесса...")
    linear_processing(file_list)

    print("Начало мультипроцессорного процесса...")
    multiprocessing_processing(file_list)
