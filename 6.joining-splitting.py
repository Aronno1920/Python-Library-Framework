import numpy  as np

ar1 = np.array([1,2,3])
ar2 = np.array([4,5,6])

# hstack used for join multiple array
array_hstack = np.hstack((ar1,ar2))
print("Horizontally stacked array \n", array_hstack)
print('-----------------------------------')

large_arr = np.array([
    [1,2,3,4,5,6,7,8,9],
    [9,8,7,6,5,4,3,2,1]
])
print("Orginal array before split\n",large_arr)

# hsplite used for split a array
array_hsplit = np.hsplit(large_arr, 3)
for spl_arr in array_hsplit:
    print("Split array of orginal array\n",spl_arr)

