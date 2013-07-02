import MapReduce
import sys

"""
Social Network
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    person_a = record[0]
    mr.emit_intermediate(person_a, 1)

def reducer(key, list_of_values):
    count = 0
    for val in list_of_values:
        count += val
    tup = key, count
    mr.emit(tup)
    
# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
