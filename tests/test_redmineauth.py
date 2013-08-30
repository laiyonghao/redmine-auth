from redmineauth import check_password


DB_CONFIG = {
    "dbn" : "mysql",
    "host" : "127.0.0.1",
    "port" : 3306,
    "user" : "",
    "pw" : "",
    "db" : "redmine",
}

def test_check_password():
    assert check_password(DB_CONFIG, 'laiyonghao', 'ch1982&^')

