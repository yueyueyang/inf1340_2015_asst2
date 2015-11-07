# !/usr/bin/env python

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


def intersection(table1, table2):

    """
    Perform the intersection set operation on tables and return rows appearing in BOTH tables

    :param table1: a table (a List of Lists)
    :param table2: a table (a List of Lists)
    :return: the resulting table
    :raises: MismatchedAttributesException: if tables t1 and t2 don't have the same attributes
    """
    # counter for table1
    i = 0
    # counter for table2
    j = 0
    new_table = []

    # compares if lengths and header names of both tables are equal
    if table1[0] != table2[0]:
        raise Exception(MismatchedAttributesException)
    # counts through both tables and appends all unique rows that are in both tables
    else:
        while i < len(table1):
            while j < len(table2):
                if table1[i] == table2[j]:
                    new_table.append(table2[j])
                    j += 1
                else:
                    j += 1
            j = 0
            i += 1
    # if there is only one unique row found (headers), new_table set to empty list
    if len(new_table) == 1:
        new_table = []
    return new_table


def union(table1, table2):
    """
    Perform the union set operation on tables, and return rows appearing in EITHER tables


    :param table1: a table (a List of Lists)
    :param table2: a table (a List of Lists)
    :return: the resulting table
    :raises: MismatchedAttributesException:
        if tables t1 and t2 don't have the same attributes
    """
    new_table = []
    if table1[0] != table2[0]:
        raise Exception('MismatchedAttributesException')
    else:
        for i in range(0, len(table1)):
            new_table.append(table1[i])
        for i in range(0, len(table2)):
            if table2[i] not in table1:
                new_table.append(table2[i])
    return new_table


def difference(table1, table2):
    """
    Perform the difference set operation on tables, and return unique rows that are in table_1 but NOT in table_2

    :param table1: a table (a List of Lists)
    :param table2: a table (a List of Lists)
    :return: the resulting table
    :raises: MismatchedAttributesException:
        if tables t1 and t2 don't have the same attributes
    """
    # counter for table1
    i = 0
    # counter for table2
    new_table = []

    # compares if lengths and header names of both tables are equal
    if table1[0] != table2[0]:
        raise Exception('MismatchedAttributesException')
    else:
        # sets new_table equal to table1 headers and appends all items in table_1 not found in table_2
        new_table = [table1[0]]
        while i < len(table1):
                if table1[i] not in table2:
                    new_table.append(table1[i])
                i += 1
        # if there is only one unique row found (headers), new_table set to empty list
        if len(new_table) == 1:
            new_table = []
    return new_table


# union(GRADUATES, STUDENTS)
# intersection(GRADUATES, STUDENTS)
# difference(GRADUATES, MANAGERS)