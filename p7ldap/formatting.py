# -*- coding: UTF-8 -*-

"""
This module provides some utilities to format LDAP search results.
"""

def format_user(user, full=False, indent=0):
    """
    Format an user for a text display
    """

    pre = '  ' * indent
    lines = []

    if full:
        lines.append("Display name: %s" % user['displayName'][0])
        lines.append("Given name: %s" % user['givenName'][0])
        lines.append('Surname: %s' % user['sn'])
    else:
        lines.append("Name: %s" % user['displayName'][0])

    lines.append('Email: %s' % user['mail'][0])

    return '\n'.join(map(lambda l: pre+l, lines)) + "\n"

def format_search_results(res, full=False):
    """
    Format a search result
    """

    count = len(res)
    plurial = 's' if count > 1 else ''
    eoheader = ':\n\n' if count > 0 else '.'

    header = "%d result%s found%s" % (count, plurial, eoheader)

    return header + '\n\n'.join([format_user(u, full, 1) for _,u in res])

def print_user(user, full=False):
    """
    Print an user
    """
    print format_user(user, full)

def print_search_results(res, full=False):
    print format_search_results(res, full)
