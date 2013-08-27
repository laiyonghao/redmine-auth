# -*- coding:utf-8 -*-

import argparse

wsgi_template = '''import redmineauth

DB_CONFIG = {{
    "dbn" : "{dbn}",
    "host" : "{host}",
    "port" : {port},
    "user" : "{user}",
    "pw" : "{pw}",
    "db" : "{db}",
}}

def check_password(environ, user, password):
    return redmineauth.check_password(DB_CONFIG, user, password)
'''

def main():
    parser = argparse.ArgumentParser(description = 'redmine-auth helper.')
    parser.add_argument('-g',
                        '--generate-config',
                        dest = 'config_file',
                        type = argparse.FileType('w'),
                        required = True,
                        help = 'Specify the wsgi script file storage path, if the file already exists, it will be overwritten.'
                        )
    args = parser.parse_args()

    settings = {}
    t = raw_input('Database name[mysql]:')
    settings['dbn'] = t if t.strip() else 'mysql'
    t = raw_input('Database Host [127.0.0.1]:')
    settings['host'] = t if t.strip() else '127.0.0.1'
    t = raw_input('Database Port [3306]:')
    settings['port'] = t if t.strip() else '3306'
    t = raw_input('Database User [root]:')
    settings['user'] = t if t.strip() else 'root'
    t = raw_input('Database Password:')
    settings['pw'] = t.strip()
    t = raw_input('Redmine Database Name [redmine]:')
    settings['db'] = t if t.strip() else 'redmine'

    args.config_file.write(wsgi_template.format(**settings))

