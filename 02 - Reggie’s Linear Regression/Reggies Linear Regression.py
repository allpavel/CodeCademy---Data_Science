def get_y(m, b, x):
    y = m * x + b
    return y


def calculate_error(m, b, point):
    x_point = point[0]
    y_point = point[1]
    y = get_y(m, b, x_point)
    difference = y - y_point
    return abs(difference)


def calculate_all_error(m, b, points):
    total_error = 0
    for point in points:
        total_error += calculate_error(m, b, point)
    return total_error


datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]
possible_ms = [i*0.1 for i in range(-100, 110)]
possible_bs = [i*0.1 for i in range(-200, 210)]

smallest_error = float("inf")
best_m = 0
best_b = 0
for each_m in possible_ms:
    for each_b in possible_bs:
        new_var = calculate_all_error(each_m, each_b, datapoints)
        if new_var < smallest_error:
            best_m = each_m
            best_b = each_b
            smallest_error = new_var

print(smallest_error)
print(best_m)
print(best_b)

print(get_y(0.3, 1.7, 6))
