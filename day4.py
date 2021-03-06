
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
            for i in range(len(nbr_list)-1):
                # if adjecent duplicates, it is one combination
                if nbr_list[i] == nbr_list[i+1]:
                    combinations = combinations + 1
                    break
    return combinations


# Converting the int to a list of ints. e.g 1234 -> [1,2,3,4]
def convert_to_int_list(nbr):
    str_nbr = str(nbr)
    nbr_list = []
    for char in str_nbr:
        nbr_list.append(int(char))
    return nbr_list


print(pw_combinations(357253, 892942))
