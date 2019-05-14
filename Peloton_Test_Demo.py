def find_max_diff(arr, arr_size):
    max_diff = arr[1] - arr[0]
    for i in range(0, arr_size):
        for j in range(i + 1, arr_size):
            if (arr[j] - arr[i] > max_diff):
                max_diff = arr[j] - arr[i]
    return max_diff


def get_positive_value_int():
    while True:
        try:
            value = int(raw_input("Enter Array Length: "))
            x = []
            for v in range(value):
                read_value = int(raw_input("Enter value " + str(v) + " : "))
                x.append(read_value)

        except ValueError:
            print("Sorry, Please Enter Valid Numeric Input")
            continue

        if value < 0:
            print("Sorry, your response must not be negative.")
            continue
        else:
            break
    return x, value


if __name__ == '__main__':
    # nums = [7, 2, 3, 10, 2, 4, 8, 1]
    # Asking inputs from user
    nums, array_size = get_positive_value_int()
    print "Maximum difference is", + find_max_diff(nums, array_size)