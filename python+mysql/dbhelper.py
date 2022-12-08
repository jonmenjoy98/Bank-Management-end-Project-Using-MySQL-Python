# On terminal just type------------- pip install mysql-connector-python

# import mysql.connector as connector
# con=connector.connect(host='localhost',port='3306',user='root',password='123456',database='pythontest',auth_plugin="mysql_native_password")
# if con.is_connected():
#     print("Successfuylly Connected...")
# else:
#     print("Connection failed")
class DBHelper():
    def __init__(self):
        #connect with mysql
        import mysql.connector as connector
        self.con=connector.connect(host='localhost',port='3306',user='root',password='123456',database='pythonTest',auth_plugin="mysql_native_password")
        #creating a table
        query="create table if not exists bank_user(acc_no int primary key,userName varchar(55),ifsc varchar(14),cur_bal int, withdral_bal int,remaining_bal int)"
        cur=self.con.cursor()
        cur.execute(query)
        print("created")
    #inserting data into table
    def insert_data(self,acc_no,userName,ifsc,cur_bal,withdral_bal,remaining_bal):
        query="insert into bank_user(acc_no,userName,ifsc,cur_bal,withdral_bal,remaining_bal) values('{}','{}','{}','{}','{}','{}')".format(acc_no,userName,ifsc,cur_bal,withdral_bal,remaining_bal)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("inserted")
    # fetching all the data from table what we have inserted
    def fetch_all(self):
        query="select * from bank_user"
        cur=self.con.cursor()
        cur.execute(query)
        for row in cur:
            # print(row )
            print("acc_no:-",row[0])
            print()
            print()
            print("uerName:-",row[1])
            print()
            print()
            print("ifsc:-" ,row[2])
            print()
            print()
            print("cur_bal:-", row[3])
            print()
            print()
            print("withdral_bal:-", row[4])
            print()
            print()
            print("remaining_bal:-" ,row[5])
            print()
            print()


    def fetch_spe(self,acc_no):
        query="select * from bank_user where acc_no={}".format(acc_no)
        cur=self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("acc_no:-",row[0])
            print()
            print("uerName:-",row[1])
            print()
            print("ifsc:-" ,row[2])
            print()
            print("cur_bal:-", row[3])
            print()
            print("withdral_bal:-", row[4])
            print()
            print("remaining_bal:-" ,row[5])
            print()
    #delete the data from table what we have inserted
    def delete_user(self,acc_no):
        query="delete from bank_user where acc_no={}".format(acc_no)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("deleted")

    # #update the data from table what we have inserted
    def update_user(self,acc_no,userName):
        query="update bank_user set userName='{}'where acc_no={}".format(userName,acc_no)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("updated")
#main coding 
# helper=DBHelper()
# acc_no,userName,ifsc,cur_bal,withdral_bal,remaining_bal
# helper.insert_data(1234,"johnmenjoy","SBIN00123",100000,3000,97000)
# helper.insert_data(3456,"niranjan","SBIN00765",100000,4000,96000)
# helper.insert_data(9809,"deep","SBIN00898",100000,5000,95000)
# helper.insert_data(7804,"ayan","SBIN00231",100000,1000,99000)
# helper.insert_data(7854,"gaurav","SBIN00908",100000,0000,100000)
# helper.insert_data(7874,"kaustav","SBIN00234",100000,3000,97000)
# helper.insert_data(9990,"arindam","SBIN00888",100000,2000,98000)
# helper.insert_data(1264,"banamali","SBIN00099",100000,6000,94000)
# helper.insert_data(8964,"biltu","SBIN00883",100000,7000,93000)
# helper.insert_data(1357,"mrinmoy","SBIN00190",100000,8000,92000)
# helper.insert_data(3334,"abhijit","SBIN00166",100000,9000,91000)
# helper.insert_data(3134,"asim","SBIN00996",100000,10000,90000)
# helper.insert_data(1334,"rupam","SBIN00161",100000,1000,99000)
# helper.insert_data(1114,"tanmay","SBIN00169",100000,9000,91000)
# helper.insert_data(1111,"xyz","SBIN00166",100000,9000,91000)
# helper.insert_data(2222,"abc","SBIN00166",100000,9000,91000)
# helper.delete_user(2222)
# helper.update_user(1111,"niloy")
# helper.update_user(2222,"chirantan")
# helper.fetch_all()
# helper.fetch_spe(1111)