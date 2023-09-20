import time
from concurrent.futures import ThreadPoolExecutor, as_completed
# import threading

start = time.perf_counter()


def do_something(seconds=1):
    print(f'Sleeping {seconds} Second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping. {seconds}'


with ThreadPoolExecutor() as executer:
    secs = [5, 4, 3, 2, 1]
    results = [executer.submit(do_something, sec) for sec in secs]
    for f in as_completed(results):
        print(f.result())

# threads = []
# for _ in range(10):
#     t = threading.Thread(target=do_something, args=(1.5, ))
#     t.start()
#     threads.append(t)
#
# for thread in threads:
#     thread.join()


finish = time.perf_counter()
print(f'Finished in {round(finish - start, 2)} second(s).')
