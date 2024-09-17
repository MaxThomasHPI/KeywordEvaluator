def convert_list_of_single_tuples_to_list(list_single_tuples):
    """
    This function converts a list of tuples with only one item per tuple into a list. It is needed for converting query
    results of a single column (just one item per tuple -> row) into a list.

    :param list_single_tuples: A list of tuples in which every tuples just contain a single item
    :return: A list containing the only value of each tuple ot the input list of tuples
    """
    output_list = list()

    for single_tuple in list_single_tuples:
        output_list.append(single_tuple[0])

    return output_list
