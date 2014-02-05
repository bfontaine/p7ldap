# p7ldap

**p7ldap** is a very lightweight layer on top of [`python-ldap`][pldap] to
search on Paris Diderot University’s LDAP server.

[pldap]: http://www.python-ldap.org/

This is only a proof of concept for now.

## Install

Requirements:
* Python 2.7

The library can’t be installed for now, you can clone the repo and play with it
if you want.

```sh
git clone https://github.com/IP7/p7ldap.git
cd p7ldap
pip install -r requirements.txt
```

## Usage

Simple search:

```python
from p7ldap import connection,formatting

con = connection.Connection()
formatting.print_search_results(con.search('yun'))
```

This should print something like (I changed the email address):

```
1 result found:

  Name: Jean-Baptiste Yunes
  Email: bar@foo.univ-paris-diderot.fr
```
