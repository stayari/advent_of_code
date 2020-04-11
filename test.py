def remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list
    nbr_list =
def consec_len(nbr_list):
    '''

    :param nbr_list: list of int:s for which max len....
    :return:....
    '''

    nbr_list.sort()
    nbr_list = remove(nbr_list)
    print(nbr_list, "hejhej")
    max_len = 0
    # 1,2,3,4,5,   8,9,10
    start_nbr = 0
    end_nbr = 0
    len_counter = 0
    range_vector = []
    len_vector2 = []
    if len(nbr_list) == 0:
        return 0
    elif len(nbr_list) == 1:
        return 1
    for i in range(len(nbr_list)-1):
        if i == 0:
            start_nbr = nbr_list[i]
        ##corner case len 2
        #if start_nbr  == 0 and i != 0:
         #   start_nbr = nbr_list[i]

        if nbr_list[i+1] - nbr_list[i] == 1 :# or nbr_list[i+1] - nbr_list[i] == 1 :
            #print(nbr_list[i],  nbr_list[i+1], "is here" )
            #end_nbr = nbr_list[i+1]
            len_counter += 1
            print(len_counter, "is counter")
        else:
            #range_vector.append([start_nbr, end_nbr])
            #len_vector2.append(end_nbr + 1  - start_nbr)
            len_vector2.append(len_counter+1)
            len_counter = 0

            start_nbr = 0
        # if at last element
        if i == len(nbr_list) - 2:
            # If this happens last number is an own "set"
            if nbr_list[i+1] - nbr_list[i] >1:
                start_nbr = nbr_list[i+1]
                end_nbr = start_nbr
                range_vector.append([start_nbr, end_nbr])
                len_vector2.append(1)#(end_nbr + 1  - start_nbr)
                print("vafan")


            else:
                range_vector.append([start_nbr, end_nbr])
                #len_vector2.append(end_nbr +1  - start_nbr)
                len_vector2.append(len_counter+1)
                len_counter = 0





    print(len_vector2, range_vector)

    return max(len_vector2)

#print(consec_len([1]))
#print(consec_len([1,2,4,5,3,9,10,8, 22]))
print(consec_len([1,1,2,3]))
print(consec_len([0,1,1,2]))

#print(consec_len([0,0,-1]))