'''
Contains various utility functions for matrix manipulation.

Finn Frankis
6/20/19
'''
import numpy


'''
Generates an nxm matrix filled with all zeros with number of rows "rows" and number of columns "cols".
'''
def generateMatrix(rows, cols):
   newMat = []   
   for rowIndex in range(0, rows):
      newMat.append([0] * cols)
   return newMat

'''
Transposes a given matrix without directly modifying it by swapping the rows and the columns.
'''
def transpose(matrix):
   if len(matrix) == 0:
      return []
   
   newMat = generateMatrix(len(matrix[0]), len(matrix))
   for rowIndex in range(0, len(matrix)):
      for colIndex in range(0, len(matrix[0])):
         newMat[colIndex][rowIndex] = matrix[rowIndex][colIndex]

   return newMat

'''
Returns an list containing all the elements of a given column in a matrix.
'''
def getMatrixCol(matrix, colIndex):
   list = [] 
   for rowIndex in range(0, len(matrix)):
      list = numpy.append(list, matrix[rowIndex][colIndex])
   return list

'''
Multiplies two matrices using matrix multiplication. For matrix multiplication to be valid, an x by y matrix
must be multiplied by a y by z matrix.
'''
def matMultiply(matrix1, matrix2):
   if len(matrix1[0]) != len(matrix2):
      return False

   resultMat = generateMatrix(len(matrix1), len(matrix2[0])) # an x by y multiplied by a y by z results in an x by z
   for rowIndex in range(0, len(matrix1)):
      rowlist = matrix1[rowIndex]
      for colIndex in range(0, len(matrix2[0])):
         collist = getMatrixCol(matrix2, colIndex)
         sum = numpy.sum(numpy.multiply(rowlist, collist))
         print("%s + %s -> %s" % (rowlist, collist, sum))
         resultMat[rowIndex][colIndex] = sum
   return resultMat

'''
Determines the determinant of a given square matrix.
'''
def matDeterminant(matrix):
   if (len(matrix) != len(matrix[0])): # not square
      return False
   if (len(matrix) == 1):
      return matrix[0][0]
   
   determinant = 0.0

   for colIndex in range(0, len(matrix[0])):
      determinant += getCofactor(matrix, 0, colIndex) * matDeterminant(generateMinor(matrix, 0, colIndex))

   return determinant
   
'''
Finds a minor of a given matrix by "crossing out" or eliminating all elements from a given row and a given column.
'''
def generateMinor(matrix, row, column):
   newMat = generateMatrix(len(matrix) - 1, len(matrix[0]) - 1)
   if row >= len(matrix) or column >= len(matrix[0]):
      return False

   for rowIndex in range(0, len(matrix)):
      for colIndex in range(0, len(matrix[0])):
         storeRow = rowIndex
         storeCol = colIndex
         if rowIndex > row:
            storeRow -= 1
         if colIndex > column:
            storeCol -= 1
         
         if rowIndex != row and colIndex != column:
            newMat[storeRow][storeCol] = matrix[rowIndex][colIndex]

   return newMat

def getCofactor (matrix, row, column):
   return (-1) ** (row + column) * matrix[row][column]

'''
Converts a list of any size into a readable multiline string format.
'''
def printList(list):
   return "[" + ", ".join(str(item) for item in list) +  "]"

'''
Determines the number of characters in the longest number of the matrix.
'''
def findMaxLength(matrix):
   maxLength = 0
   for row in matrix:
      for element in row:
         maxLength = max(val for val in [maxLength, len(str(element))])

   return maxLength

'''
Converts a matrix of any size into a readable multiline string format.
'''
def getMatrixString(matrix):
   return '\n'.join([''.join([('{:%s}' % (findMaxLength(matrix) + 3)).format(item) for item in row]) 
      for row in matrix])

mat1 = [[4, 6, 7, 9, 10], [1, 90000000008., 8, 20, 40], [2, 32, 6, 53, -10], [6, 52, 3, 13, -2000000.00], [200, -10, 6.3, 53.4, -10]]
mat2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(findMaxLength(mat1))
print(matDeterminant(mat1))
