import numpy as np

arr1 = np.array([1,2,3,4])
arr2 = np.array([5,6,7,8])

ar_sum=arr1+arr2
print("Addition:", ar_sum)

ar_multi=arr1*arr2
print("Multiplication:", ar_multi)

slice_arr1=arr1[1:2]
print("Slice of array 1:", slice_arr1)

st_slice_arr1=arr1[::3]
print("Step slice of array 1:", st_slice_arr1)
