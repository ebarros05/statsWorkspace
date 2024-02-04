the_list = []
    
def insertion_sort(alist):
    for j in range(1, len(alist)):
        key = alist[i]
        i = j-1
        while(alist[i] > key and i > 0):
            alist[i+1] = alist[i]
            i = i - 1
        alist[i+1] = key
            
        

"""def input_data():
    global the_list
    print("Enter data points (type 'x' to finish):")
    while True:
        user_input = input("Enter a data point (or 'x' to finish): ")
        if user_input.lower() == 'x':
            break
        try:
            data_point = float(user_input)
            the_list.append(data_point)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
"""
def input_data():
    global the_list
    print("Enter data points separated by tabs (type 'x' to finish):")
    while True:
        user_input = input("Enter data points (or 'x' to finish): ")
        if user_input.lower() == 'x':
            break
        try:
            data_points = [float(point) for point in user_input.split('\t')]
            the_list.extend(data_points)
        except ValueError:
            print("Invalid input. Please enter valid numbers separated by tabs.")

def print_list():
    print("[")
    for n in the_list:
        if n == len(the_list)-1:
            print(n)
            break
        print(f"{n}, ")
    print("]")

def s_mean():
    global the_list
    tot = 0.0
    n = len(the_list)
    for x in the_list:
        tot += x
    ret = tot/float(n)
    print(f"The sample mean is: {ret} ")
    return ret

def s_median():
    global the_list
    the_list.sort
    n = len(the_list)
    if n%2 ==0:
        middle1 = the_list[n // 2 - 1]
        middle2 = the_list[n // 2]
        median = (middle1 + middle2) / 2
    else:
        # If the length is odd, the median is the middle element
        median = the_list[n // 2]
    print(f"The median is: {median}")
    return median

def trimmed_mean(x):
    global the_list
    #trim = len(the_list) * x
    #get trimmed list
    n = len(the_list)
    k = int(round(n*(float(x)/100)/2))
    t_list = the_list[k+1:n-k]

    #find mean of trimmed list
    tot = 0
    n = len(t_list)

    for x in t_list:
        tot += x
    ret = tot/float(n)

    print(f"The trimmed mean for {x*100}% is: {ret} ")
    return ret


    #return mean(arr[k+1:n-k])


def skew():
    global the_list
    mean = s_mean()
    median = s_median()
    if mean > median:
        print("negative skew")
    elif median < mean:
        print("positive skew")
    else:
        print("no skew")