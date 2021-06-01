DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'root'
PASSWORD = '123456'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'religion'
SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8&autocommit=true".format(DIALECT, DRIVER,
                                                                       USERNAME, PASSWORD, HOST,
                                                                       PORT, DATABASE)

SQLALCHEMY_TRACK_MODIFICATIONS = False
