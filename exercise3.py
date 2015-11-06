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
        new_table = table1
        for i in range(0, len(table2)):
            if table2[i] not in table1:
                new_table.append(table2[i])
    return new_table


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
    elif table1[0] == table2[0]:
        new_table = []
        for i in range(0, len(table2)):
            if table2[i] in table1:
                new_table.append(table2[i])
        return new_table
    else:
        empty_table = []
        for i in range(0, len(table2)):
            if table2[i] not in table1:
                return empty_table


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
        new_table = [table1[0]]
        for i in range(1, len(table1)):
            if table1[i] not in table2:
                new_table.append(table1[i])
    return new_table

#union(GRADUATES, MANAGERS)
#print intersection(GRADUATES, MANAGERS)
#print difference(GRADUATES, MANAGERS)