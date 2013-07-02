import MapReduce
import sys
import operator

"""
Unique DNA Trims 
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    matrix = record[0]
    if matrix == 'a':
        a_row = record[1]
        a_col = record[2]
        a_value = record[3]
        for k in range(0,5):
            key = a_row,k
            value = matrix, a_col, a_value
            mr.emit_intermediate(key, value)
    elif matrix == 'b':
        b_row = record[1]
        b_col = record[2]
        b_value = record[3]
        for i in range(0,5):
            key = i, b_col
            value = matrix, b_row, b_value
            mr.emit_intermediate(key, value)
        
def reducer(key, list_of_values):
    key_list = list(key)
    row = key_list[0]
    col = key_list[1]
    matrix_a = []
    matrix_b = []
    for i in list_of_values:
        if i[0] == 'a':
            matrix_a.append(i)
        elif i[0] == 'b':
            matrix_b.append(i)
    
    sorted_a = sorted(matrix_a, key=operator.itemgetter(1))
    sorted_b = sorted(matrix_b, key=operator.itemgetter(1))
    value = 0
    count_a = 0
    count_b = 0
    for a_elem in sorted_a:
        if a_elem[1] != count_a:
            sorted_a.insert(count_a, (0,0,0))
        count_a += 1
    while len(sorted_a) < 5:
        sorted_a.insert(len(sorted_a), (0,0,0))
    for b_elem in sorted_b:
        if b_elem[1] != count_b:
            sorted_b.insert(count_b, (0,0,0))
        count_b += 1
    while len(sorted_b) < 5:
        sorted_b.insert(len(sorted_b), (0,0,0))

    for i in range(0,5):
        value += sorted_a[i][2] * sorted_b[i][2]
    if value > 0:
        result_tuple = row, col, value        
        mr.emit(result_tuple)
    

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
