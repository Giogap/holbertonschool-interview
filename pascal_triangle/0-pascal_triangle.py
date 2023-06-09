#!/usr/bin/python3
""" pascal triangle """


def pascal_triangle(n):
    """ function pascal triangle """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1] + [triangle[i-1][j] + triangle[i-1][j+1] for j in
                     range(len(triangle[i-1])-1)] + [1]
        triangle.append(row)

    return triangle
