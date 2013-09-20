import MySQLdb
import time
MySQLdb.paramstyle
from datetime import datetime
import fcntl
import time
import sys

def test_connect(ip_address, port1, username, password, database):
    port1 = int(port1)
    connMRS = MySQLdb.connect (host = ip_address,
        port=port1,
        user=username,
        passwd = password,
        db=database)

    mrstest = connMRS.cursor()
    mrstest.execute('select person_id from person limit 1')
    result = mrstest.fetchall()
    mrstest.close

    return result
