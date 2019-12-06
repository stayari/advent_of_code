
def pw_combinations(lower, upper):
    combinations = 0
    # Turning into list of ints
    for nbr in range(lower, upper + 1):
        nbr_list = convert_to_int_list(nbr)
        # Making a sorted copy which is to be compared to
        sorted_list = nbr_list.copy()
        sorted_list.sort()
        # Check if the number order is increasing (e.g. sorted)
        if nbr_list == sorted_list:
            nbr_dict = dict()
            for num in nbr_list:
                # Combination only if there is adjecent of two
                if num not in nbr_dict:
                    nbr_dict[num] = 1
                else:
                    nbr_dict[num] += 1
            if 2 in nbr_dict.values():
                combinations = combinations + 1
    return combinations


# Converting the int to a list of ints. e.g 1234 -> [1,2,3,4]
def convert_to_int_list(nbr):
    str_nbr = str(nbr)
    nbr_list = []
    for char in str_nbr:
        nbr_list.append(int(char))
    return nbr_list


print(pw_combinations(357253, 892942))
