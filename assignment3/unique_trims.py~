import MapReduce
import sys

"""
Asimmetric Social Network
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    sorted_list = sorted(record)
    sorted_tuple = tuple(sorted_list)
    orig_tuple = tuple(record)
    mr.emit_intermediate(sorted_tuple, orig_tuple)


def reducer(key, list_of_values):
    print list_of_values
    if len(list_of_values) == 1:
        result_tup = tuple(list_of_values[0])
        rev_tuple = tuple(reversed(result_tup))
        mr.emit(result_tup)
        mr.emit(rev_tuple)
    
# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
