import timeit

setup_str = f"""
import numpy as np
import random
import heapq
random.seed(30)
test = random.sample(range(100000), 1000)
"""
print("this is the partition method: ")
print(min(timeit.Timer('np.partition(test,4)[4]',setup = setup_str).repeat(7,10000)))
print("this is the heapq method: ")
print(min(timeit.Timer('heapq.nsmallest(5,test)[4]',setup = setup_str).repeat(7,10000)))

