def binary_search(list,target):
    if(len(list)==0):
        return False
    else:
        mid = len(list)//2
        
        if list[mid] == target:
            return True
        else:
            if(list[mid]>target):
                return binary_search(list[:mid],target)
            else:
                return binary_search(list[mid+1:],target)


val = [1,2,3,4,6]
val1 = []
Test1 = binary_search(val,1)
print("Test1 (Target = 1): ",Test1)
Test2 = binary_search(val,6)
print("Test2 (Target = 6): ",Test2)
Test3 = binary_search(val1,7)
print("Test3 (Target = 7): ",Test3)
            
            
            
# [1,2,3,4,5,6] , [1,2]
# Targat = 1
# mid = 3
# Target = 6   , [4,5,6]
