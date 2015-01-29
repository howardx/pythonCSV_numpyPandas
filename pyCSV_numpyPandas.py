import os
#os.path.dirname(os.path.realpath(__file__)) # find out current working dir
import numpy
import pandas
import csv

def readCSV(filename):
  with open(filename, 'rb') as csvfile:
    freader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    #print freader.__class__.__name__ # get object class name
    for row in freader:
      data = ', '.join(row)
      print data
      
def readCSV2NumpyNumOnly(filename): # reading in numeric data ONLY
  data = numpy.genfromtxt(filename, delimiter=',')
  print data
    
def readCSV2Dict(filename):
  reader = csv.DictReader(open(filename))

  result = {}
  for row in reader:
    for column, value in row.iteritems():
      result.setdefault(column, []).append(value)
  print result
      
def readCSV2PandasDF(filename):
  data = pandas.read_csv(filename)
  print data
  return data
  
def convertPandasDF2Dict(df):
  diction = df.to_dict()
  print diction
  
'''
difference between numpy (nd)array and matrix
http://stackoverflow.com/questions/4151128/what-are-the-differences-between-numpy-arrays-and-matrices-which-one-should-i-u
'''
def convertPandasDF2Matrix(df): # returning a numpy (nd)array
  ndArray = df.as_matrix()
  ndArray = ndArray.T # transpose, other matrix operations also supports
  print ndArray
  
      
def main():
  readCSV("test.csv")
  readCSV2NumpyNumOnly("test.csv")
  readCSV2Dict("test.csv")
  df = readCSV2PandasDF("test.csv")
  convertPandasDF2Dict(df)
  convertPandasDF2Matrix(df)
if __name__ == "__main__":
    main()      
      
      
