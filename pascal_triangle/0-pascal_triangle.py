def pascal_triangle(n):
    """ pascal triangle """
    if n <= 0:
        return []  # Return an empty list for n <= 0
    
    triangle = [[1]]  # Start with the first row
    
    for i in range(1, n):
        # Create the next row of the triangle
        row = [1] + [triangle[i-1][j] + triangle[i-1][j+1] for j in range(len(triangle[i-1])-1)] + [1]
        triangle.append(row)  # Add the new row to the triangle
    
    return triangle
