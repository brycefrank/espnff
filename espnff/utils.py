def square_matrix(X):
    '''Squares a matrix'''
    result = [[0.0]*len(X) for x in range(len(X))]

    # iterate through rows of X
    for i in range(len(X)):

        # iterate through columns of X
        for j in range(len(X)):

            # iterate through rows of X
            for k in range(len(X)):
                result[i][j] += X[i][k] * X[k][j]

    return result


def add_matrix(X, Y):
    '''Adds two matrices'''
    result = [[0.0]*len(X) for x in range(len(X))]

    for i in range(len(X)):

        # iterate through columns
        for j in range(len(X)):
            result[i][j] = X[i][j] + Y[i][j]

    return result


def two_step_dominance(X):
    '''Returns result of two step dominance formula'''
    matrix = add_matrix(square_matrix(X), X)
    result = [sum(x) for x in matrix]
    return result


def power_points(dominance, teams, week):
    '''Returns list of power points'''
    power_points = []
    for i, team in zip(dominance, teams):
        avg_score = sum(team.scores[:week]) / week
        avg_mov = sum(team.mov[:week]) / week

        power = '{0:.2f}'.format((int(i)*0.8) + (int(avg_score)*0.15) +
                                 (int(avg_mov)*0.05))
        power_points.append(power)
    power_tup = [(i, j) for (i, j) in zip(power_points, teams)]
    return sorted(power_tup, key=lambda tup: float(tup[0]), reverse=True)
