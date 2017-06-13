def is_square(vertices):
    if (len(vertices) != 4): return False
    else: 
    	edge = points_distance(vertices[0], vertices[1])
    	if(edge != points_distance(vertices[0], vertices[3])): return False
    	elif(edge != points_distance(vertices[1], vertices[2])): return False
    	elif((edge*2**0.5) != points_distance(vertices[0], vertices[2])): return False
    	else: return True


def get_area(vertices):
    area = 0
    for x in range(0, len(vertices)):
    	area+=(vertices[x][0]*vertices[(x+1)%len(vertices)][1]-vertices[x][1]*vertices[(x+1)%len(vertices)][0])
    area = abs(area/2)
    if(area == 0): area = int(area)
    return area


def points_distance(a, b):
    c = ((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5
    return c


def verticify(line):
    braceless = line.replace("(", "").replace(")", "")
    pairs = braceless.split(" ")
    tuples = [(x.split(",")) for x in pairs]
    numbers = [(int(x), int(y)) for x,y in tuples]
    return numbers

def process(input_path, output_path):
    file_in = open(input_path, "r")
    file_out = open(output_path, "w")
    same_square = False
    list_sizes = []
    for line in file_in:
    	x = verticify(line)
    	file_out.write(str(get_area(x)) + "\n")
    	if(is_square(x) == True):
    		if(get_area(x) == y for y in list_sizes): same_square = True
    		else: list_sizes.append(get_area(x))
    file_out.write(str(same_square))
    file_out.close()
    file_in.close()

process('input.txt', 'output.txt')
