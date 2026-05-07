import numpy as np
import time

# 100 Elemente

liste1 = list(range(100))
liste2 = np.arange(100)

start = time.time()
for i in liste1:
    liste1[i] = liste1[i]**2
print("Python Liste, 100 Elemente: ")
print(round((time.time()-start)*1000, 3), " ms")
print("")

start = time.time()
liste2**2
print("Numpy Liste, 100 Elemente: ")
print(round((time.time()-start)*1000, 3), " ms")
print("")

# 10.000 Elemente

liste1 = list(range(10000))
liste2 = np.arange(10000)

start = time.time()
for i in liste1:
    liste1[i] = liste1[i]**2
print("Python Liste, 10.000 Elemente: ")
print(round((time.time()-start)*1000, 3), " ms")
print("")

start = time.time()
liste2**2
print("Numpy Liste, 10.000 Elemente: ")
print(round((time.time()-start)*1000, 3), " ms")
print("")

# 1.000.000 Elemente

liste1 = list(range(1000000))
liste2 = np.arange(1000000)

start = time.time()
for i in liste1:
    liste1[i] = liste1[i]**2
print("Python Liste, 1.000.000 Elemente: ")
print(round((time.time()-start)*1000, 3), " ms")
print("")

start = time.time()
liste2**2
print("Numpy Liste, 1.000.000 Elemente: ")
print(round((time.time()-start)*1000, 3), " ms")