#!/usr/bin/env python

""" Assignment 2, Exercise 3, INF1340, Fall, 2015. DBMS

This module performs table operations on database tables
implemented as lists of lists.

"""


class MismatchedAttributesException(Exception):
    """
    Raised when attempting set operations with tables that
    don't have the same attributes.
    """
    pass


def check_schema_and_length(t1, t2):
    """
    Tests if two lists/tables are equal in size and have the same schemas

    :param: two lists of lists from intersection, difference and union functions
    :return: true if tables are equal, false if unequal
    :raises:
    """

    t1_header = t1[0]
    t2_header = t2[0]
    t1_header_length = len(t1_header)
    t2_header_length = len(t2_header)
    header_lengths_final = False
    header_names_final = False

    if t1_header_length == t2_header_length:
        header_lengths_final = True

    if t1_header == t2_header:
        header_names_final = True

    if header_names_final and header_lengths_final == True:
        result = True

    return result

def union(table1, table2):
    """
    Perform the union set operation on tables, table1 and table2.

    :param table1: a table (a List of Lists), table2: a table (a List of Lists)
    :return: the resulting table
    :raises: MismatchedAttributesException:
        if tables t1 and t2 don't have the same attributes
    """
    if not check_schema_and_length(table1, table2):
        raise Exception('MismatchedAttributesException')
    else:
        new_table=table1
        for i in range(0, len(table2)):
            if table2[i] not in table1:
                new_table.append(table2[i])
    return new_table


def intersection(table1, table2):
    """
    Perform the intersection set operation on tables, table1 and table2.

    :param table1: a table (a List of Lists), table2: a table (a List of Lists)
    :return: the resulting table
    :raises: MismatchedAttributesException:
        if tables t1 and t2 don't have the same attributes
    """
    if not check_schema_and_length(table1, table2):
        raise Exception('MismatchedAttributesException')
    else:
        new_table = []
    for i in range(0, len(table2)):
        if table2[i] in table1:
            new_table.append(table2[i])
    return new_table


def difference(table1, table2):
    """
    Perform the difference set operation on tables, table1 and table2.

    :param table1: a table (a List of Lists), table2: a table (a List of Lists)
    :return: the resulting table
    :raises: MismatchedAttributesException:
        if tables t1 and t2 don't have the same attributes
    """
    if not check_schema_and_length(table1, table2):
        raise Exception('MismatchedAttributesException')
    else:
        new_table = [table1[0]]
        for i in range(1, len(table1)):
            if table1[i] not in table2:
                new_table.append(table1[i])
    return new_table

#union(GRADUATES, MANAGERS)
#print intersection(GRADUATES, MANAGERS)
#print difference(GRADUATES, MANAGERS)
