import insertUtil as ut
import MySQLdb


#Tạo kết nối với RDS Aurora MySQL và thêm dữ liệu vào
conn = MySQLdb.connect(host='atabase-aurora.cluster-c7ufnweqkd7n.us-east-1.rds.amazonaws.com', user='main', passwd='lab-password', db='covid19_aurora', port=3306)
print('Open DB successfully')
ut.insert(conn)
ut.select(conn)
conn.close()
print('Successfully')

