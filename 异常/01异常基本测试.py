'''1 BaseException所有异常的基类；-------Exception常规错误的基类'''
import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("localhost", "root", "root", "eating", charset='utf8')

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 使用execute方法执行SQL语句
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取一条数据
data = cursor.fetchone()

print
"Database version : %s " % data

# 关闭数据库连接
db.close()
try:
    fh = open("testfile", "w")
    fh.write("这是一个测试文件，用于测试异常!!")
except IOError:
    print
    "Error: 没有找到文件或读取文件失败"
else:
    print
    "内容写入文件成功"
    fh.close()
