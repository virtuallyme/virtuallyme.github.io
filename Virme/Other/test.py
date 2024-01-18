from bs4 import BeautifulSoup

with open('/Users/appleid/Downloads/round_plus_webflow_ecommerce_template.webflow.io/round-plus-webflow-ecommerce-template.webflow.io/Virme/index.html', 'r') as f:
    html_string = f.read()

html_string = BeautifulSoup(html_string, 'html.parser').prettify()

with open('/Users/appleid/Downloads/round_plus_webflow_ecommerce_template.webflow.io/round-plus-webflow-ecommerce-template.webflow.io/Virme/index.html', 'w') as f:
    f.write(html_string)