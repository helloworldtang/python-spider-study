import pymysql.cursors
import json

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='mirror-dev',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
try:
    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT id,tension from mirror_tension ORDER BY id desc"
        cursor.execute(sql)
        fetchall = cursor.fetchall()
        for tension in fetchall:
            id = tension["id"]
            tensionValue = tension["tension"]
            print(tensionValue)
            record = json.loads(tensionValue)
            context = record["context"]
            print(context)
            dirName = "train/data/tension/"
            dataFile = open(dirName + str(id) + ".txt", "w", encoding="utf-8")
            dataFile.write(context)
            dataFile.close()
            tags = record["tag"]
            print(tags)
            dataFile = open(dirName + str(id) + ".lab", "ab")
            for tag in tags:
                print(tag)
                dataFile.write(bytes(tag + "\n", encoding="utf-8"))
            dataFile.close()
finally:
    connection.close()
