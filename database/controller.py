import sqlite3
import DateTime.DateTime as dt
connection = sqlite3.connect('db.db')
cursor = connection.cursor()

#cursor.execute('''CREATE TABLE Gear \
#                (dateEntered TINYTEXT, Item TINYTEXT, NOTE TINYTEXT, Manufacturer TINYTEXT, PriceUSD FLOAT(24), WeightGrams INT(5),PackedSizeCM3 INT(8) )''')
#
# cursor.execute('''INSERT INTO Gear VALUES
#                 ('08-07-22', \
#                  'Roo Double Hammock', \
#                  'Core hammock', \
#                  'Kammok', \
#                  NULL, \
#                  NULL, \
#                  NULL )''')

#connection.commit()

res = cursor.execute('SELECT count(rowid) FROM Gear')
print(res.fetchone())

todays_date = '08-07-22'

data = [
    # Kitchen
    (todays_date, 'Salt', 'Kitchen', 'NULL', 'NULL', 'NULL', 'NULL'),
    (todays_date, 'Boiling pot lid', 'Kitchen', 'NULL','NULL','NULL','NULL'),
    (todays_date, 'Tea pot lid', 'Kitchen', 'NULL','NULL','NULL','NULL'),
    (todays_date, 'Tea pot',  'Kitchen', 'NULL','NULL','NULL','NULL'),
    (todays_date, 'Boiling pot',  'Kitchen', 'NULL','NULL','NULL','NULL'),
    (todays_date, 'Tea pot',  'Kitchen', 'NULL','NULL','NULL','NULL'),
    (todays_date, 'Mixed gas fuel',  'Kitchen', 'NULL','NULL','NULL','NULL'),
    (todays_date, 'Folding Stove',  'Kitchen', 'NULL','NULL','NULL','NULL'),
    (todays_date, 'Bowl',  'Kitchen', 'NULL','NULL','NULL','NULL'),
    (todays_date, 'Utensil', 'Kitchen', 'NULL', 'NULL', 'NULL', 'NULL'),

    # Infrastructure
    (todays_date, 'Trash bag',  'Infrastructure', 'NULL','NULL','NULL','NULL'),
    (todays_date, 'Zip-lock', 'Infrastructure', 'NULL', 'NULL', 'NULL', 'NULL'),
    (todays_date, 'Trash bag', 'Infrastructure', 'NULL', 'NULL', 'NULL', 'NULL'),
    (todays_date, 'Netted bag', 'Infrastructure', 'NULL', 'NULL', 'NULL', 'NULL'),
    (todays_date, 'Compression sacks', 'Infrastructure', 'NULL', 'NULL', 'NULL', 'NULL'),
    (todays_date, 'Tent under tarp', 'Infrastructure', 'NULL', 'NULL', 'NULL', 'NULL'),
    (todays_date, 'Water satchel', 'Infrastructure', 'NULL', 'NULL', 'NULL', 'NULL'),

    # Health
    (todays_date, 'Sunscreen', 'Health', 'NULL', 'NULL', 'NULL', 'NULL'),
    (todays_date, 'Wet wipes', 'Infrastructure', 'NULL', 'NULL', 'NULL', 'NULL'),
    (todays_date, 'Hat', 'Infrastructure', 'NULL', 'NULL', 'NULL', 'NULL'),

    # Camp
    (todays_date, 'Tent under tarp', 'Camp', 'NULL', 'NULL', 'NULL', 'NULL'),
    (todays_date, 'Under quilt', 'Camp', 'NULL', 'NULL', 'NULL', 'NULL'),
    (todays_date, 'Top quilt', 'Camp', 'NULL', 'NULL', 'NULL', 'NULL'),
    (todays_date, 'Hammock straps', 'Camp', 'NULL', 'NULL', 'NULL', 'NULL'),
    (todays_date, 'Double Hammock', 'Camp', 'NULL', 'NULL', 'NULL', 'NULL'),
    (todays_date, 'Light chair', 'Camp', 'NULL', 'NULL', 'NULL', 'NULL'),
    (todays_date, 'Table', 'Camp', 'NULL', 'NULL', 'NULL', 'NULL'),



]
