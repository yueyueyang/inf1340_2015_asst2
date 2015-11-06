#!/usr/bin/env python

""" Assignment 2, Exercise 3, INF1340, Fall, 2015. DBMS

This module performs table operations on database tables
implemented as lists of lists.

"""
# GRADUATES = [["Number", "Surname", "Age"],
#              [7274, "Robinson", 37],
#              [7432, "O'Malley", 39],
#              [9824, "Darkes", 38]]
#
# MANAGERS = [["Number", "Surname", "Age"],
#             [1800, "Shah", 56],
#             [5607, "Shah", 39],
#             [7274, "Robinson", 37]]
#
# PROFESSORS = [["Number", "Surname", "Age", "Gender"],
#              [9087, "Yashvi", 43],
#              [2345, "Anirudh", 44],
#              [1234, "Aditi", 45]]
#
# FACULTY_ADMINISTRATION = [["Number", "Name", "Age"],
#              [7777, "Christina", 12],
#              [8888, "Courtney", 13],
#              [9090, "Lena", 14]]
#####################
# HELPER FUNCTIONS ##
#####################
GRADUATES = [["Number", "Surname", "Age"],
             [7274, "Robinson", 37],
             [7432, "O'Malley", 39],
             [9824, "Darkes", 38]]

MANAGERS = [["Number", "Surname", "Age"],
            [9297, "O'Malley", 56],
            [7432, "O'Malley", 39],
            [9824, "Darkes", 38]]

PROFESSORS = [["Number", "Surname", "Age", "Gender"],
             [7274, "Robinson", 37],
             [7432, "O'Malley", 39],
             [9824, "Darkes", 38]]

FACULTY_ADMINISTRATION = [["Number", "Name", "Age"],
             [7274, "Robinson", 37],
             [7432, "O'Malley", 39],
             [9824, "Darkes", 38]]

def remove_duplicates(l):
    """
    Removes duplicates from l, where l is a List of Lists.
    :param l: a List
    """

    d = {}
    result = []
    for row in l:
        if tuple(row) not in d:
            result.append(row)
            d[tuple(row)] = True

    return result


class MismatchedAttributesException(Exception):
    """
    Raised when attempting set operations with tables that
    don't have the same attributes.
    """
    pass


def union(table1, table2):
    """
    Perform the union set operation on tables, table1 and table2.

    :param table1: a table (a List of Lists)
    :param table2: a table (a List of Lists)
    :return: the resulting table
    :raises: MismatchedAttributesException:
        if tables t1 and t2 don't have the same attributes
    """
    if table1[0] != table2[0]:
        raise Exception('MismatchedAttributesException')
    else:
        new_list=table1
        for i in range(len(table2)):
            if table2[i] not in table1:
                new_list.append(table2[i])
    return new_list


def intersection(table1, table2):
    """
    Perform the intersection set operation on tables, table1 and table2.

    :param table1: a table (a List of Lists)
    :param table2: a table (a List of Lists)
    :return: the resulting table
    :raises: MismatchedAttributesException:
        if tables t1 and t2 don't have the same attributes
    """
    if table1[0] != table2[0]:
        raise Exception('MismatchedAttributesException')
    else:
        new_list = []
    for i in range(len(table2)):
        if table2[i] in table1:
            new_list.append(table2[i])
    return new_list


def difference(table1, table2):
    """
    Perform the difference set operation on tables, table1 and table2.

    :param table1: a table (a List of Lists)
    :param table2: a table (a List of Lists)
    :return: the resulting table
    :raises: MismatchedAttributesException:
        if tables t1 and t2 don't have the same attributes
    """
    if table1[0] != table2[0]:
        raise Exception('MismatchedAttributesException')
    else:
        new_list = []
        for i in range(len(table1)):
            if table1[i] not in table2:
                new_list.append(table1[i])
        return new_list

#union(GRADUATES, MANAGERS)
#intersection(GRADUATES, MANAGERS)
#difference(GRADUATES, MANAGERS)
