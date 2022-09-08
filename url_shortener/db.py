import mysql.connector
import string
import secrets

credentials={
        'user':"root",
        'password':"root",
        'host':"localhost",
        'database':"node0"

}
def initializedb(long_url,values):

        db = mysql.connector.connect(**credentials)

        #connecting to db

        if db.is_connected():
            print("connected to database")
            cursor = db.cursor()

            sql_stat="insert into url (Longurl,Shorturl)values(%s,%s)"

            cursor.execute(sql_stat,values)
            db.commit()
            print("inserted values into database")


def generate_random():
    res = ''.join(secrets.choice(string.ascii_uppercase + string.digits)
              for i in range(4))

    return res



def generate_url(key,value):


    key=list(key.values())
    long_url=key[0]
    if if_url_exist(long_url):
        result = {"message":"url exist","long_url": long_url, "short_url": if_url_exist(long_url)}
        return result
    else:
        localhost_url = "http://localhost:5000/"
        short_url = localhost_url + value
        insert_values = (long_url, short_url)
        initializedb(long_url, insert_values)
        result = {"long_url": long_url, "short_url": short_url}
        return result




def if_url_exist(long_url):

    sql_stat_for_existing_url="select * from url where longurl like '%"+long_url+"%'"
    db = mysql.connector.connect(**credentials)
    cursor = db.cursor()
    cursor.execute(sql_stat_for_existing_url)
    result=cursor.fetchall()

    if(result):
        print("url exist ")
        short_url=result[0][2]
        return short_url

def checking_for_url(short_url_code):
    short_url= "http://localhost:5000/"+short_url_code
    sql_stat_for_finding_url = "select * from url where shorturl like '%" + short_url + "%'"
    db = mysql.connector.connect(**credentials)
    cursor = db.cursor()
    cursor.execute(sql_stat_for_finding_url)
    result = cursor.fetchall()

    if (result):
        print("url exist ")
        long_url = result[0][1]
        return long_url
    else:
        return "sorry something went wrong"







