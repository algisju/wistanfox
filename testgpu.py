from numba import jit
import numpy as np
import time


@jit(nopython=True)
def go_fast():
	trace = 0
	for i in range(0,1000):
		for j in range(0,1000):
			for k in range(0,1000):
				trace +=1
	return trace

# DO NOT REPORT THIS... COMPILATION TIME IS INCLUDED IN THE EXECUTION TIME!
start = time.time()
go_fast()
end = time.time()
print("Elapsed (with compilation) = %s" % (end - start))

# NOW THE FUNCTION IS COMPILED, RE-TIME IT EXECUTING FROM CACHE
start = time.time()
go_fast()
end = time.time()
print("Elapsed (after compilation) = %s" % (end - start))
