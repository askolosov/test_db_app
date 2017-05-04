#!/usr/bin/env python3
import bottle, os, MySQLdb
from bottle import template

app = bottle.Bottle()

page_tpl = """
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Employees</title>
  </head>
  <body>
    <p>Male employees, who were born at February 1, 
       1965 and were hired after Janary 1, 1990:</p>
    <table>
        <thead>
            <th>First Name</th><th>Last name</th>
        </thead>
        <tbody>
        % for r in rows:
            <tr><td>{{ r[0] }}</td><td>{{ r[1] }}</td></tr>      
        % end
        </tbody>
    </table>
  </body>
</html>
"""

@app.get('/')
def index():
    db = MySQLdb.connect(
        os.environ["DB_HOST"],
        os.environ["DB_USER"],
        os.environ["DB_PASS"],
        os.environ["DB_NAME"]
    )

    c = db.cursor()
    gender = 'M'
    birth_date = '1965-02-01'
    hire_date = '1990-01-01'
    
    c.execute("""
    SELECT first_name, last_name FROM employees 
    WHERE gender = %s AND birth_date = %s AND hire_date > %s 
    ORDER BY first_name, last_name""", (gender, birth_date, hire_date))

    return template(page_tpl, rows=c.fetchall())

if __name__ == "__main__":
    bottle.run(app, host=os.environ["HTTP_LISTEN_IP"], port=os.environ["HTTP_LISTEN_PORT"])
