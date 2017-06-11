def is_square(vertices):
    """
    Determines, whether the vertices form a square in 2-D space
    :param vertices: a list of polygon vertices ordered clockwise
    :return: True if the polygon is a square, otherwise False
    """
    pass


def get_area(vertices):
    """
    Calculates the are of the polygon formed from the vertices
    :param vertices: list of polygon vertices ordered clockwise
    :return: float, area of the polygon
    """
    area = 0
    for x in range(0, len(vertices)):
    	area+=(vertices[x][0]*vertices[(x+1)%len(vertices)][1]-vertices[x][1]*vertices[(x+1)%len(vertices)][0])
    area = abs(area/2)
    return area


def points_distance(a, b):
    """
    Calculates the distance between two points
    :param a: Tuple of coordinates in format (x,y)
    :param b: Tuple of coordinates in format (x,y)
    :return: float, distance between the points in 2-D space
    """
    c = ((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5
    return c


def verticify(line):
    """
    Converts a line from file into a list of vertices
    :param line: String with space-separated points, comma-separated coords
    :return: list of tuples of coordinates [(x0,y0), (x1,y1), ...]
    """
    braceless = line.replace("(", "").replace(")", "")
    pairs = braceless.split(" ")
    tuples = [(x.split(",")) for x in pairs]
    numbers = [(int(x), int(y)) for x,y in tuples]
    return numbers


def process(input_path, output_path):
    """
    Processes input text file, and creates an output text file
    :param input_path: string, path to input file
    :param input_path: string, path to output file
    :return: void
    """
    pass

# These functions should be enough to keep your
# code clean and remove unneeded details from
# the main body of the script.

#process('input.txt', 'output.txt')
print(get_area([(1,3), (3,3), (3,1), (1,1)]))
