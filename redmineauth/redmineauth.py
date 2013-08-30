# -*- coding:utf-8 -*-

import sys
import os

try:
    from hashlib import sha1
except ImportError:
    from sha import sha as sha1

import sqlalchemy
from sqlalchemy.pool import NullPool
from sqlalchemy.sql import text

def _hash_password(raw_password, salt):
    if not salt:
        # low version redmine
        return sha1(raw_password).hexdigest()
    hashed_password = sha1(salt + sha1(raw_password).hexdigest()).hexdigest()
    return hashed_password

def check_password(dbconfig, user, password):
#    print >> sys.stderr, 'user:', user
    conn_str = "{dbn}://{user}:{pw}@{host}:{port}/{db}"
    engine = sqlalchemy.create_engine(conn_str.format(**dbconfig), poolclass = NullPool)
    conn = engine.connect()
    s = text('select login, hashed_password, salt from users where login=:u and status = 1')
    result = conn.execute(s, u = user)
    print result
    record = result.fetchone()
    print record
    print '*'*30
    result.close()
    conn.close()
    if not record:
        return False
    salt = record['salt']
    password_expect = record['hashed_password']
#    print >> sys.stderr, 'password_expect:', password_expect
    hashed_password = _hash_password(password, salt)
#    print >> sys.stderr, 'hashed_password:', hashed_password
    if hashed_password == password_expect:
        return True
    return False



