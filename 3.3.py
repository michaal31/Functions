
def triangle_area(a, b, c):
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area

area1 = triangle_area(3, 4, 5)
print('The area of ​​a triangle with sides 3, 4, 5 is', area1)

area2 = triangle_area(5, 12, 13)
print('The area of ​​a triangle with sides 5, 12, 13 is', area2)

area3 = triangle_area(7, 24, 25)
print('The area of ​​a triangle with sides 7, 24, 25 is', area3)
