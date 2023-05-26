#task36

def print_operation_table(f, num_rows, num_columns):
    res = [[f(i, j) for i in range(1, num_columns + 1)] for j in range(1, num_rows + 1)]
         #[[operation(i, j) for i in range(1, num_columns + 1)] for j in range(1, num_raws + 1)]
    for i in res:
        print(i)

print_operation_table(lambda x, y: x * y, 6, 6)