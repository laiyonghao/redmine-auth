redmine-auth manuals
============

Introduction
-------

redmine-auth is an `apache2` authentication provider implementation, `redmine` database is used for authenticate. It can be used for `subversion` authentication, etc.

Requirements
--------

* Apache 2.2+
* mod_wsgi 2.0+

Your must install a python database driver, for example, if you use `mysql` as your `redmine` database, use `MySQLdb`.

Only tested in `Ubuntu Server(x64) 12.04 LTS`, other softwares listed below:

* apache 2.2.22
* svn 1.6.7
* mysql 5.5
* python 2.7.3
* mod_wsgi 3.3
* redmine 2.2

Installation
-------

Run command

```
pip install -U redmine-auth
```

Configuration
-------

Run command

```
redmine-auth -g WSGI-FILE-PATH
```

`redmine-auth` will ask you some questions, then write the answers to `WSGI-FILE-PATH`.

Edit your apache2 site config file, such as `/etc/apache2/sites-enabled/svn.conf`, add AuthBasicProvider to it, make it looks like below:

```
<VirtualHost *:1081>

<Location />
  DAV svn
  SVNParentPath /opt/svn

  AuthName "Subversion repository"
  AuthType Basic

  # important !!!
  AuthBasicProvider wsgi
  WSGIAuthUserScript WSGI-FILE-PATH

  AuthzSVNAccessFile /opt/svn-authz

  Require valid-user

</Location>

</VirtualHost>
```

Please replace `WSGI-FILE-PATH` in config file with real path.

Then, restart apache2:

```
service apache2 restart
```

All will be OK.

Contribution
-------

We welcome contributions! If you would like to hack on redmine-auth, please follow these steps:

* Fork this repository
* Make your changes
* Submit a pull request

Please give us adequate time to review your submission. Thanks!

License
---------

* MIT license for this project.
