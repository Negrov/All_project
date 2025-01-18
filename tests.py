x1, y1, len_x1, len_y1 = [int(i) for i in input().split()]
x2, y2, len_x2, len_y2 = [int(i) for i in input().split()]
print('YES' if x1 <= x2 + len_x2 and x1 + len_x1 >= x2 and y1 <= y2 + len_y2 and y1 + len_y1 >= y2 else 'NO')
