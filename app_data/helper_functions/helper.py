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


def prepare_descriptions_for_database(csv_row):
    """
    This function is necessary to prepare the raw description delivered by the csv for the database.

    :param csv_row: A list containing a row of the raw csv file.
    :return: A string representing the course description.
    """
    temp = csv_row[8:]
    temp = ",".join(temp).lstrip()
    temp = temp.lstrip('"')
    temp = temp.rstrip('"')
    temp = temp.lstrip()
    temp = temp.rstrip()
    temp = temp.replace("<p>", "")
    temp = temp.replace("</p>", "")
    temp = temp.replace("<strong>", "")
    temp = temp.replace("</strong>", "")
    temp = temp.replace("&amp;", "& ")

    for i in range(4):  # remove whitespaces - sometimes there are several of them, this is why the procedure has to be
        # repeated
        temp = temp.replace("  ", " ")

    return temp

