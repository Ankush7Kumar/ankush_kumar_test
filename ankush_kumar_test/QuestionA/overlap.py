
# Here the first line is (x1, x2)
# The second line is (x3, x4) 
# We are checking if the lines overlap or not and return strings accordingly

def overlap(x1, x2, x3, x4):
    if (x2 > x3 and x4 > x1):
        return "overlap"
    else:
        return "do not overlap"
