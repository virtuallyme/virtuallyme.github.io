from bs4 import BeautifulSoup

with open('/Users/appleid/Desktop/Projects/Virme/pages/waitlist.html', 'r') as f:
    html_string = f.read()

html_string = BeautifulSoup(html_string, 'html.parser').prettify()

with open('/Users/appleid/Desktop/Projects/Virme/pages/waitlist.html', 'w') as f:
    f.write(html_string)