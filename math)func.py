# Task 1
# Write your get_y() function here
def get_y(m, b, x):
    y = m * x + b
    return y


# Uncomment each print() statement to check your work. Each of the following should print True
# print(get_y(1, 0, 7) == 7)
# print(get_y(5, 10, 3) == 25)


# Tasks 2 and 3
# Write your calculate_error() function here
def calculate_error(m, b, point: list):
    x_point = point[0]
    y_point = point[1]
    calc_y = get_y(m, b, x_point)
    diff = abs(calc_y - y_point)
    # print(f'Y is {calc_y}, diff is {diff}')
    return diff


# Task 4
# Uncomment each print() statement and check the output against the expected result

# this is a line that looks like y = x, so (3, 3) should lie on it. thus, error should be 0:
# print(calculate_error(1, 0, (3, 3)))
#
# the point (3, 4) should be 1 unit away from the line y = x:
# print(calculate_error(1, 0, (3, 4)))
#
# the point (3, 3) should be 1 unit away from the line y = x - 1:
# print(calculate_error(1, -1, (3, 3)))
#
# the point (3, 3) should be 5 units away from the line y = -x + 1:
# print(calculate_error(-1, 1, (3, 3)))


# Task 5
# Write your calculate_all_error() function here
def calculate_all_error(m, b, datapoints: list):
    diff = 0
    for point in datapoints:
        diff += calculate_error(m, b, point)
    return diff


# Task 6
# Uncomment each print() statement and check the output against the expected result
# datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]

# every point in this dataset lies upon y=x, so the total error should be zero:
# print(calculate_all_error(1, 0, datapoints))

# every point in this dataset is 1 unit away from y = x + 1, so the total error should be 4:
# print(calculate_all_error(1, 1, datapoints))

# every point in this dataset is 1 unit away from y = x - 1, so the total error should be 4:
# print(calculate_all_error(1, -1, datapoints))

# the points in this dataset are 1, 5, 9, and 3 units away from y = -x + 1, respectively, so total error should be
# 1 + 5 + 9 + 3 = 18
# print(calculate_all_error(-1, 1, datapoints))


# Tasks 8 and 9
possible_ms = [x / 10 for x in range(-100, 101)]
possible_bs = [x / 10 for x in range(-200, 201)]

# Task 10
datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]


# Tasks 11 and 12

def smallest_error(ms, bs, datapoints):
    smallest_error = float('inf')
    best_m = 0
    best_b = 0
    for m in ms:
        for b in bs:
            error = calculate_all_error(m, b, datapoints)
            if error < smallest_error :
                smallest_error = error
                best_b = b
                best_m = m
    print(f'err is {smallest_error}, m is {best_m}, b  is {best_b}')
    return smallest_error

print(smallest_error(possible_ms, possible_bs, datapoints))
# print(calculate_all_error(0.3, 1.7, datapoints))

# Task 13









