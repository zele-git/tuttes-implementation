import random
def undirected_graph(n, m):
    # check if number of edge is enough to connect the vertexes
    if m < n-1:
        return []
    else:
        matrix = [[0 for x in range(n)] for y in range(n)]
        dif = 1
        # assign value if hor and ver are not the same
        # value will be 0 for same hor and ver
        for i in range(m):
            ver = random.randint(0, n-1)
            hor = random.randint(0, n-1)
            if ver != hor:
                dif += dif
                matrix[ver][hor] = dif
                dif += 1
        # the original and reverse index need to have opposite value to Tutte's algorithm
        for i in range(n):
            for j in range(n):
                if matrix[i][j] != 0:
                    val = matrix[i][j]
                    matrix[j][i] = -1 * val
        mat = []
        for i in range(n):
            ent=[]
            for j in range(n):
                ent.append(matrix[i][j])
            mat.append(ent)

        return mat

def solve(matrix, mul):
    width = len(matrix)
    if width == 1:
        return mul * matrix[0][0]
    else:
        sign = 1
        total = 0
        for i in range(width):
            m = []
            for j in range(1, width):
                buff = []
                for k in range(width):
                    if k != i:
                        buff.append(matrix[j][k])
                m.append(buff)
            sign *= -1
            total += mul * solve(m, sign * matrix[0][i])
        return total

counter = 0
for i in range(5):
    out = undirected_graph(6,5 )
    if not out:
        print("Number of edge should be greater than number of vertex" )
        break
    else:
        print(out)
        determinant = solve(out,1)
        print(determinant)
        if determinant > 0 or determinant < 0:
            counter += 1
print("Number of perfect match =%s" % (counter))