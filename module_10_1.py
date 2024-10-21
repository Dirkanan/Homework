from time import sleep
from threading import Thread
from datetime import datetime

def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        for i in range(1, word_count + 1):
            f.write(f"Какое-то слово № {i}\n")
            sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")

time_start = datetime.now()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
time_end = datetime.now()
time_res = time_end - time_start
print(time_res)

time_start2 = datetime.now()
the_first = Thread(target=write_words, args=(10, 'example5.txt'))
the_two   = Thread(target=write_words,   args=(30, 'example6.txt'))
the_third = Thread(target=write_words, args=(200, 'example7.txt'))
the_four  = Thread(target=write_words,  args=(100, 'example8.txt'))

the_first.start()
the_two.start()
the_third.start()
the_four.start()


the_first.join()
the_two.join()
the_third.join()
the_four.join()

time_end2 = datetime.now()
time_res2 = time_end2 - time_start2
print(time_res2)
