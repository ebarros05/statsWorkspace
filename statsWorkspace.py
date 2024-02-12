the_list = []
    
def insertion_sort(alist):
    """Returns sorted list"""
    for j in range(1, len(alist)):
        key = alist[i]
        i = j-1
        while(alist[i] > key and i > 0):
            alist[i+1] = alist[i]
            i = i - 1
        alist[i+1] = key
    return alist
        
#clears the grid and then prints it
def cleardata():
    """Clears data"""
    global the_list
    the_list = []
    print(the_list)
    print("list cleared")
            
def input_data():
    """Inputs the data"""
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
    """Prints the list"""
    print("[")
    for n in the_list:
        if n == len(the_list)-1:
            print(n)
            break
        print(f"{n}, ")
    print("]")

def s_mean():
    """Prints sample mean"""
    global the_list
    tot = 0.0
    n = len(the_list)
    for x in the_list:
        tot += x
    ret = tot/float(n)
    print(f"The sample mean is: {ret} ")
    return ret


def s_median():
    """Prints sample median"""
    global the_list
    sorted_list = sorted(the_list)
    #print(sorted_list)
    n = len(sorted_list)
    if n%2 == 0:
        middle1 = sorted_list[n // 2 - 1]
        middle2 = sorted_list[n // 2]
        median = (middle1 + middle2) / 2
    else:
        # If the length is odd, the median is the middle element
        median = sorted_list[n // 2]
    print(f"The median is: ",end='')
    return median

#NOT WORKING
def trimmed_mean(trim):
    """Returns trimmed mean
    :param trim: arg1, 
    :type trim: int
    :return:trimmed mean
    """
    global the_list

    #check if list empty
    if not the_list:
        print("list empty")
        return None
    
    n = len(the_list)
    
    #check if trim is within a valid range
    if trim <= 0 or trim >= 100:
        print("Error: trim should be a percentage between 0 and 100 exclusive.")
        return None
    
    how_many_to_trim =  n * (float(trim) / 100)
    
    if how_many_to_trim < 0.0:
        trimup = int(-(-how_many_to_trim // 1))
        trimdown = int(how_many_to_trim)
        if trimdown < 0:
            print("Error: trim value results in a negative k.")
            return None
        if n <= 2 * trimup:
            print("Error: Not enough elements after trimming.")
            return None
        t_list_u = the_list[trimup:n-trimup]
        t_list_d = the_list[trimdown:n-trimdown]
        mean1 = sum(t_list_u)/float(n-2 * trimup)
        mean2 = sum(t_list_d)/float(n-2 * trimdown)
        
        ret = (mean1+mean2) / 2

    else:
        how_many_to_trim = int(how_many_to_trim)
        # Check if how_many_to_trim is less than 0
        if how_many_to_trim < 0:
            print("Error: trim value results in a negative k.")
            return None

        # Check if there are enough elements after trimming
        if n <= 2 * how_many_to_trim:
            print("Error: Not enough elements after trimming.")
            return None

        t_list = the_list[how_many_to_trim:n-how_many_to_trim]

        # find mean of trimmed list
        tot = sum(t_list)
        ret = tot / float(n - 2 * how_many_to_trim)

    print(f"A {trim}% trimmed mean is: {ret}")
    return ret

def skew():
    """Prints skew"""
    global the_list
    mean = s_mean()
    median = s_median()
    if mean > median:
        print("negative skew")
    elif median < mean:
        print("positive skew")
    else:
        print("no skew")
        

def s_sum():
    """Prints the sample sum"""
    tot = 0
    for x in the_list:
        tot += x
    return x

def s_range():
    """Prints the sample range"""
    sorted_list = sorted(the_list)
    hi = sorted_list[-1]
    lo = sorted_list[0]
    print(f"The highest value is: {hi}")
    print(f"The lowest value is: {lo}")
    print(f"Range is: {(hi-lo)}")
    return (hi-lo)

def s_variance():
    """Prints sample variance"""
    global the_list
    
    if not the_list:
        print("Error: the_list is empty.")
        return None

    n = len(the_list)

    # Calculate the mean
    mean = sum(the_list) / n

    # Calculate the sum of squared differences from the mean
    sum_squared_diff = sum((x - mean) ** 2 for x in the_list)

    # Divide by (n-1) for sample variance
    variance = sum_squared_diff / (n - 1)

    return variance
    
def s_std():
    """Prints the sample standard deviation"""
    v = s_variance()
    return v**0.5

def sum_sqr():
    """Prints the sum of squares"""
    global the_list
    sum_squares = sum(entry ** 2 for entry in the_list)
    return sum_squares

def s_stats():
    """Prints all sample stats functions. Specifically:
        s_mean()
        s_median()
        s_sum()
        s_range()
        s_variance()
        s_std()
    """
    print("Printing sample stats")
    print("-------------------------------------")
    s_mean()
    s_median()
    s_sum()        
    s_range()
    s_variance()
    s_std()
    print("-------------------------------------")
