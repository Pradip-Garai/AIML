import numpy as np
from time import process_time

# Time taken by Python list operations
li = [i for i in range(10000)]

start_time_list = process_time()
pli = [i + 5 for i in li]
end_time_list = process_time()

print(f"Time taken by list: {end_time_list - start_time_list} seconds")

# Time taken by NumPy array operations
arr_time_comp = np.array([i for i in range(10000)])

start_time_np = process_time()
arr_time_comp += 5
end_time_np = process_time()

print(f"Time taken by NumPy array: {end_time_np - start_time_np} seconds")