import threading
import time

def func_name(thread_num):
    print(f"Thread-{thread_num} started.")
    time.sleep(2)  # Simulating some work
    print(f"Thread-{thread_num} finished.")

def main():
    threads = []
    for i in range(10):
        th = threading.Thread(target=func_name, args=(i,))
        th.start()
        threads.append(th)

    # Wait for all threads to finish
    for th in threads:
        th.join()

    print(f"Total active threads: {threading.active_count() - 1}")  # Subtract 1 for the main thread

if __name__ == "__main__":
    main()
