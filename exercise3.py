#!/usr/bin/env python

""" Assignment 2, Exercise 3, INF1340, Fall, 2015. DBMS

This module performs table operations on database tables
implemented as lists of lists.

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


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
        newtable = []
        for i in range(len(table1)):
            newtable.append(table1[i])
        for i in range(1,len(table2)):
            newtable.append(table2[i])
        return newtable




def intersection(table1, table2):
    """
    Describe your function

    """

    if table1[0] != table2[0]:
        raise Exception('MismatchedAttributesException')
    else:
        newtable = []
        newtable.append(table1[0])
        for i in range(1,len(table1)):
            for j in range(1,len(table2)):
                if table1[i] == table2[j]:
                    newtable.append(table1[i])
        return newtable




def difference(table1, table2):
    """
    Describe your function

    """

    if table1[0] != table2[0]:
        raise Exception('MismatchedAttributesException')
    else:
        newtable = []
        newtable.append(table1[0])

        for i in range(1, len(table1)):
            flag = False
            for j in range(1, len(table2)):
                if table1[i] == table2[j]:
                    flag = True
                    break
            if flag == False:
                newtable.append(table1[i])

        return newtable



#####################
# HELPER FUNCTIONS ##
#####################
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

