class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        l_row, r_row = 0, rows - 1

        while l_row <= r_row:
            mid_row = (l_row + r_row) // 2

            # target too small → go up
            if matrix[mid_row][0] > target:
                r_row = mid_row - 1

            # target too big → go down
            elif matrix[mid_row][-1] < target:
                l_row = mid_row + 1

            # ✅ target must be in this row
            else:
                # binary search THIS row only
                l_col, r_col = 0, cols - 1

                while l_col <= r_col:
                    mid_col = (l_col + r_col) // 2

                    if matrix[mid_row][mid_col] == target:
                        return True
                    elif matrix[mid_row][mid_col] < target:
                        l_col = mid_col + 1
                    else:
                        r_col = mid_col - 1

                return False  # searched correct row, not found

        return False


        