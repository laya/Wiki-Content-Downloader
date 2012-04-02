from sys import argv
import sqlite3
import urllib

params = urllib.urlencode({'spam': 1, 'eggs': 2, 'bacon': 0})
f = urllib.urlopen("http://www.musi-cal.com/cgi-bin/query", params)
print f.read()

conn = sqlite3.connect('/tmp/example')
c = conn.cursor()


# Create table
"""c.execute('''create table stocks
(date text, trans text, symbol text,
 qty real, price real)''')"""

# Insert a row of data
c.execute("""insert into stocks
          values ('2006-01-05','BUY','RHAT',100,35.14)""")

# Save (commit) the changes
conn.commit()

c.execute("""select * from stocks""")
for row in c:
    print row

# We can also close the cursor if we are done with it
c.close()
script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

#print "Type the filename again:"
#file_again = raw_input("> ")

#txt_again = open(file_again)

#print txt_again.read()

