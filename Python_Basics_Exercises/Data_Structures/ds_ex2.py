tensor = [[[1,2,3],[1,2,3],[1,2,3]],
        [[1,2,3],[1,2,3],[1,2,3]],
        [[1,2,3],[1,2,3],[1,2,3]]]

def flatten_tensor(tensor):
    flatten = []

    for matrix in tensor:
        for row in matrix:
            for element in row:
                flatten.append(element)

    return flatten

print(flatten_tensor(tensor))