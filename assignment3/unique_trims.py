import MapReduce
import sys

"""
Unique DNA Trims 
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    nucleotides = record[1]
    key = record[0]
    trimmed = nucleotides[:-10]
    mr.emit_intermediate(trimmed,key)

def reducer(key, list_of_values):
    mr.emit(key)
    
# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
