# -*- coding: UTF-8 -*-

import ldap

class Connection:
    def __init__(self, url='ldap://annuaire.math.univ-paris-diderot.fr:389', \
            base='ou=users,dc=chevaleret,dc=univ-paris-diderot,dc=fr'):
        self.base = base
        self.url = url
        self.con = ldap.initialize(self.url)
        self.con.bind_s('', '')

    def __del__(self):
        self.con.unbind()

    def search(self, kw, field='cn'):
        """
        Search someone in the LDAP directory using a keyword
        """
        qry = "%s=*%s*" % (field, kw)
        return self.con.search_s(self.base, ldap.SCOPE_SUBTREE, qry, None)
