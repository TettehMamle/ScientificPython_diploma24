import time
import ex2__2

if __name__ == "__main__":
    start_time = time.time()
    ex2__2.recaman(100000)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time} seconds")


    start_time = time.time()
    ex2__2.recaman2(100000)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time} seconds")