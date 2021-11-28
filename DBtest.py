import pymysql

# connects to database
db = pymysql.connect(host="mysql.agh.edu.pl", port=3306, user="thang", passwd="rKPwvXqUNxX4meuv", database="thang")
my_cursor = db.cursor()

try:
    my_cursor.execute("insert into students(student_id, groups)"
                      " values('%s', '%s')" % ("test_id", "test"))
    db.commit()
    print("updated database successful")
except Exception as e:
    db.rollback()
    print("Exception occurred: ", e)

db.close()
