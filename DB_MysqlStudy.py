import pymysql.cursors

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='python-local-test',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
try:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "insert into user(email,password) values(%s,%s)"
        cursor.execute(sql, ('admin@mysql.com', 'password-value'))

    # connection is not autocommit by default.So you must commit to save your changes
    connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "select id,password from user where email=%s"
        cursor.execute(sql, ("admin@mysql.com",))
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()

    # https: // github.com / PyMySQL / PyMySQL
    # $ pip  install PyMySQL
    # CREATE TABLE `user` (
    #     `id` int(11) NOT NULL AUTO_INCREMENT,
    #     `email` varchar(255) COLLATE utf8_bin NOT NULL,
    #     `password` varchar(255) COLLATE utf8_bin NOT NULL,
    #     PRIMARY KEY (`id`)
    # ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin
    # AUTO_INCREMENT=1 ;
