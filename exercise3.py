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


def intersection(table1, table2):

    """
    Perform the intersection set operation on tables, table1 and table2.

    :param table1: a table (a List of Lists)
    :param table2: a table (a List of Lists)
    :return: the resulting table
    :raises: MismatchedAttributesException:
        if tables t1 and t2 don't have the same attributes
    """
    i = 0
    j = 0
    new_table = []

    if table1[0] != table2[0]:
        raise Exception(MismatchedAttributesException)
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
    if len(new_table) == 1:
        new_table = []
    return new_table


def union(table1, table2):
    """
    Perform the union set operation on tables, table1 and table2.

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
    Perform the difference set operation on tables, table1 and table2.

    :param table1: a table (a List of Lists)
    :param table2: a table (a List of Lists)
    :return: the resulting table
    :raises: MismatchedAttributesException:
        if tables t1 and t2 don't have the same attributes
    """
    i = 0
    j = 0
    new_table = []

    if table1[0] != table2[0]:
        raise Exception('MismatchedAttributesException')
    else:
        new_table = [table1[0]]
        while i < len(table1):
                if table1[i] not in table2:
                    new_table.append(table1[i])
                i += 1
        if len(new_table) == 1:
            new_table = []
    return new_table


#print union(GRADUATES, STUDENTS)
#print intersection(GRADUATES, STUDENTS)
#print difference(GRADUATES, MANAGERS)