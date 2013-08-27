# -*- coding:utf-8 -*-

import sys
import os

try:
    from hashlib import sha1
except ImportError:
    from sha import sha as sha1

import web

def _hash_password(raw_password, salt):
    if not salt:
        # low version redmine
        return sha1(raw_password).hexdigest()
    hashed_password = sha1(salt + sha1(raw_password).hexdigest()).hexdigest()
    return hashed_password

def check_password(dbconfig, user, password):
#    print >> sys.stderr, 'user:', user
    db = web.database(**dbconfig)

    vars = {
        'login' : user,
        'status' : 1, # active user
    }
    where = web.db.sqlwhere(vars)
    what = ','.join(['login', 'hashed_password', 'salt'])
    has_salt_field = True
    try:
        records = db.select('users', vars = vars, where = where, what = what)
    except Exception, e:
        if 'salt' in str(e): # not salt field in low version redmine
            what = ','.join(['login', 'hashed_password'])
            records = db.select('users', vars = vars, where = where, what = what)
            has_salt_field = False
        else:
            raise

    for record in records:
        if has_salt_field:
            salt = record['salt']
        else:
            salt = None
        password_expect = record['hashed_password']
#        print >> sys.stderr, 'password_expect:', password_expect
        hashed_password = _hash_password(password, salt)
#        print >> sys.stderr, 'hashed_password:', hashed_password
        if hashed_password == password_expect:
            return True
    return False




