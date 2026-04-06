class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        l_row = 0
        l_col = 0

        r_row = rows - 1
        r_col = cols - 1

        while l_row <= r_row and l_col <= r_col:

            mid_row = l_row + ((r_row - l_row) // 2)
            mid_col = l_col + ((r_col - l_col) // 2)

            # target too small
            if matrix[mid_row][0] > target:
                r_row = mid_row - 1
            elif matrix[mid_row][0] == target:
                return True
            # target too big
            elif matrix[mid_row][-1] < target:
                l_row = mid_row + 1

            elif matrix[mid_row][-1] == target:
                return True
            # should be in right row
            else:
                if matrix[mid_row][mid_col] == target:
                    return True
                elif matrix[mid_row][mid_col] > target:
                    r_col = mid_col - 1
                # matrix[mid_row][mid_col] < target
                else:
                    l_col = mid_col + 1
        return False


        