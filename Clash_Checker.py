# This file contains the functions that check if a certain permutation/board of 8 queen pieces at 8 different positions have any clashes.
# There are clashes on a certain permutation if two queens are on the same row, column, and/or diagonal.
# Currently, the algorithm is set up to generate queens via an array. The index = the row number of each queen piece on the board and the value = the column number. Therefore, by default, each queen will be on a different row and only the columns and diagonals need to be checked for clashes.

from Unit_Tester import unit_test
def diagonal_clash(x1, y1, x2, y2):
    """Checks if two queens, one at position (x1, y1) and one at position (x2, y2) are within the same diagonal on the board."""
    distance_y = abs(y2-y1)     # Absolute y distance
    distance_x = abs(x2-x1)     # Absolute x distance
    return (distance_y == distance_x)    # On same diagonal if distance_y = distance_x


print("Beginning diagonal_clash tests: ")
unit_test(not diagonal_clash(5,2,2,0))
unit_test(diagonal_clash(5,2,3,0))
unit_test(diagonal_clash(5,2,4,3))
unit_test(diagonal_clash(5,2,4,1))