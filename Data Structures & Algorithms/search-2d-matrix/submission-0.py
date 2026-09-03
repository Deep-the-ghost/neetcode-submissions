class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix)-1

        while left <= right:
            mid = (left + right) // 2
            if target >= matrix[mid][0] and target <= matrix[mid][-1]:
                l = 0
                r = len(matrix[mid])-1
                while l <= r:
                    m = (l+r) // 2
                    if matrix[mid][m] == target:
                        return True
                        break
                    elif matrix[mid][m] > target:
                        r = m - 1
                    else:
                        l = m + 1        
                break            
            elif matrix[mid][0] > target and matrix[mid][-1] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return False                        
