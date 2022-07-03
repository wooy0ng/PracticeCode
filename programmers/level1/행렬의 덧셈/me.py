def solution(arr1, arr2):
    import numpy as np
    return (np.array(arr1)+np.array(arr2)).tolist()

arr1 = [[1,2],[2,3]]	
arr2 = [[3,4],[5,6]]	
print(solution(arr1, arr2))