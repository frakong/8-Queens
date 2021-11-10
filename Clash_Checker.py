# This file contains the functions that check if a certain permutation/board of 8 queen pieces at 8 different positions have any clashes.
# There are clashes on a certain permutation if two queens are on the same row, column, and/or diagonal.
# Currently, the algorithm is set up to generate queens via an array. The index = the row number of each queen piece on the board and the value = the column number. The values generated in the array will be a permutation of the numbers from 0 to array.length - 1. Therefore, by default, each queen will be on a different row and column,so only the diagonals need to be checked for clashes.

from Unit_Tester import unit_test
def diag_clash(x1, y1, x2, y2):
    """Checks if two queens, one at position (x1, y1) and one at position (x2, y2) are within the same diagonal on the board."""
    distance_y = abs(y2-y1)     # Absolute y distance
    distance_x = abs(x2-x1)     # Absolute x distance
    return (distance_y == distance_x)    # On same diagonal if distance_y = distance_x


# print("Beginning diag_clash tests: ")
# unit_test(not diag_clash(5,2,2,0))
# unit_test(diag_clash(5,2,3,0))
# unit_test(diag_clash(5,2,4,3))
# unit_test(diag_clash(5,2,4,1))

def col_clash(positions, col_num):
    """Return True if the queen at column col_num clashes with any queen
    to its left (previous columns) in the list of column placements called positions."""
    for column in range(col_num): # Search through all columns to the left of col_num.
        if diag_clash(col_num, positions[col_num], column, positions[column]):
            return True
    return False             # No column clashes


# print("Beginning column clash tests: ")
# unit_test(not col_clash([6,4,2,0,5], 4))
# unit_test(not col_clash([6,4,2,0,5,7,1,3], 7))

# unit_test(col_clash([0,1], 1))    

def check_for_clashes(queen_positions):
    """Determine whether we have any queens clashing on the diagonals of the board with positions of queens represented by queen_positions (index # represents the column, value of each index represents the row).
    We're assuming here that queen_positions is a permutation of row numbers so we're guaranteed that row and column numbers are unique, only need to check for diagonal clashes."""
    for column in range(1, len(queen_positions)):
        if col_clash(queen_positions, column):
            return True
    return False


print("Beginning check_for_clashes tests: ")
unit_test(not check_for_clashes([6,4,2,0,5,7,1,3]))
unit_test(check_for_clashes([4,6,2,0,5,7,1,3]))
unit_test(check_for_clashes([0,1,2,3]))
unit_test(not check_for_clashes([2,0,3,1]))