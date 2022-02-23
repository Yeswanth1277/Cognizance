table = []
n = int(input("Enter number of rows : "))
print("Enter the roll number , name and marks respectively")
for i in range(0, n):
    ele = [input(), input(),input()]
    table.append(ele)
print("Enter the respective headings of the table")
print("{:<10} {:<10} {:<10} ".format(input(), input(),input()))
for i in range(3):
    print(table[1][i], end=" "*10)