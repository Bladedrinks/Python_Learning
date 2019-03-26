# Program to display a triangle made up of a certain shape (like *, #, etc) where the shapes on each side is different
# than the shapes in the interior.
# Below is the expected triangle example with 9 rows (side length):
#         *          Row 1: 1 * and 0 o
#        * *         Row 2: 2 * and 0 o
#       * o *        Row 3: 2 * and 1 o
#      * o o *       Row 4: 2 * and 2 o
#     * o o o *      Row 5: 2 * and 3 o
#    * o o o o *     Row 6: 2 * and 4 o
#   * o o o o o *    Row 7: 2 * and 5 o
#  * o o o o o o *   Row 8: 2 * and 6 o
# * * * * * * * * *  Row 9: 9 * and 0 o

# ====== Source Code ======
side = int(input("Enter the length of side of the equilateral triangle: "))
outer_unit = input("Enter the outer unit: ")
inner_unit = input("Enter the inner unit: ")
for x in range(1, side + 1):
    row = ""
    spaces = side - x
    row += " " * spaces
    if not(x == 1 or x == 2 or x == side):
        row += outer_unit + f" {inner_unit}" * (x - 2) + f" {outer_unit}"
    else:
        row += f"{outer_unit} " * x
    print(row)





