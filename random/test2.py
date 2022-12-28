# import numpy as np


# arr1=np.array([[2,2,2],[2,2,2],[2,2,2]])
# arr2=np.array([[2,2,2],[2,2,2],[2,2,2]])

# # print(arr1[:,1])#to select column
# # print(arr1[1])#to select row

# def mulMatrix(arr1,arr2):
    
#     mullist=[]
#     order=3

#     for i in range(order):
#         for j in range(order):
#             mullist.append(arr1[i]*arr2[:,j])

#     mularr=np.array(mullist)
#     # print(mularr)

#     summedlist=[]

#     for i in mularr:
#         sum=0
#         for j in i:
#             sum+=j
#         summedlist.append(sum)

#     summedarr=np.array(summedlist).reshape(order,order)
#     return summedarr
    


