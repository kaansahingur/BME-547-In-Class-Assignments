def point_finder(x1,y1,x2,y2,x):
    m = (y1-y2)/(x1-x2)
    b = (x1*y2 - x2*y1)/(x1-x2)
    y = m*x + b
    return y