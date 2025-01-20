#The function accepts the three sides of a triangle as parameters and determines whether the largest angle (the angle opposite the largest side) is ‘obtuse’, i.e., greater than 90°, ‘acute’, i.e., less than 90°, or ‘right’, i.e. a 90° right-angle.
#Moeketsi Segogoba
#SGGMOE001
#19 September 2024

"""
>>> import triangle
>>> triangle.classify_by_angle(9, 7, 8)
'acute'
>>> triangle.classify_by_angle(5, 7, 10)
'obtuse'
>>> triangle.classify_by_angle(4, 3, 5)
'right'
>>> triangle.classify_by_angle(7, 8, 9)
'acute'
>>> triangle.classify_by_angle(7, 10, 5)
'obtuse'
>>> triangle.classify_by_angle(3, 5, 4)
'right'
>>> triangle.classify_by_angle(8, 9, 7)
'acute'
>>> triangle.classify_by_angle(10, 5, 7)
'obtuse'
>>> triangle.classify_by_angle(5, 4, 3)
'right'

"""
import doctest
doctest.testmode(verbose=True)