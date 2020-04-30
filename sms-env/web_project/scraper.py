import requests
import MySQLdb
from bs4 import BeautifulSoup

#SQL connection data to connect and save
HOST = "localhost"
USERNAME = "scraping_user"
PASSWORD = ""
DATABASE = "covid_sms"

#Twitter url to scrape
url_to_scrape = "https://covid19.ncdc.gov.ng/"

# Load html plain text into a variable
plain = requests.get(url_to_scrape)

#parsing data
soup = BeautifulSoup(plain.text, "html.parser")

class_name = soup.find('div', {'class':'single-well'}).p
class_name = class_name.get_text()

#print (class_name.get_text())

#Database connection
db = MySQLdb.connect(HOST, USERNAME, PASSWORD, DATABASE)

cursor = db.cursor()

#SQL query to insert record into database
sql = "INSERT INTO updates (message)" "VALUES (%s)"
cursor.execute(sql, class_name)
db.commit()
'''
try:
    #execute sql command
    cursor.execute(sql, class_name)

    #commit change into database
    db.commit()
except:
    #rollback in case of error
    db.rollback()

#getting inserted class_id
'''