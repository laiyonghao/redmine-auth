#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
import os
import argparse
from .redmineauth import check_password_conn_str

def main():
    parser = argparse.ArgumentParser(description = 'redmine-auth-jenkins.')
    parser.add_argument('--conn-str',
                        required = True,
                        help = 'SQLAlchemy connect string. for ex. mysql://root:pswd@localhost:3306/test?charset=utf8'
                        )
    args = parser.parse_args()
    
    if 'U' not in os.environ or 'P' not in os.environ:
        print 'environment variable U/P is not found.'
        sys.exit(1)
    user = os.environ['U']
    password = os.environ['P']
    result = check_password_conn_str(args.conn_str, user, password)
    if result:
        print 'succ'
        sys.exit(0)
    print 'fail'
    sys.exit(1)
