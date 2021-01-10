import mysql.connector

#create connection
mydb=mysql.connector.connect(host='sl-aus-syd-1-portal.5.dblayer.com',
                                         database='q2c',
                                         port='22245',
                                         user='q2c',
                                         password='passw0rd')


mycursor = mydb.cursor()

#part 1 Update the values inside column term by adding extra 12 months across
q1= "UPDATE loan_data SET term = '42 months' WHERE term = '36 months' and loan_status != 'Fully Paid'"
mycursor.execute(q1)
#---------------------------

#part2
q2= "ALTER TABLE loan_data ADD COLUMN int_rates_add_2pct int"
mycursor.execute(q2)

q3="INSERT INTO loan_data int_rates_add_2pct VALUES(%s)"

# adding int_rate plus and addition of 2% point
for x in mycursor:
    mycursor.execute(q3,int_rate[x]+2)

mycursor.commit()
#---------------------------

#part 3 amend the installment value
q4="ALTER TABLE loan_data ADD COLUMN installment2 float AFTER installment "
mycursor.execute(q4)

#adding revised new installment value
q5="INSERT INTO loan_data installment2 VALUES(%s))"

for x in mycursor
    mycursor.execute(q5,installment[x]+(installment[x]*2/100))
mycursor.commit()


mycursor.close()
mydb.close()