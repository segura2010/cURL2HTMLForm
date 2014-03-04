'''
cURL2HTMLForm

Usage:
Execute this python script in a terminal with:
$ python cURL2HTMLForm.py "curl 'http://site.dom/path -b ... (Your cURL command)'"

This will print the HTML code of your form. You can use this to generate a HTML file with the form:
$ python cURL2HTMLForm.py "curl 'http://site.dom/path -b ... (Your cURL command)'" > htmlform.html


IMPORTANT: Your "--data" option in your cURL command must be the latest option. We recommend you use this script with
Google Chrome's "Copy as cURL" option.

Author: Alberto Segura
Twitter: @alberto__segura

'''

import sys
import re

curl = sys.argv[1]

url = re.findall("https?://[a-zA-Z0-9%.'+'&'?''=''_'-/]*\'", curl)
url = url[0]
dataCurl = curl[curl.find("--data"):]
dataArray = re.findall('[a-zA-Z0-9%."+""_"\]\[/]*=[a-zA-Z0-9%."+"/]*&?', dataCurl)

html = '<form action="' + str(url[:-1]) + '" method="POST">'

for v in dataArray:
	key = v[:v.find("=")]
	value = v[v.find("=")+1:v.find("&")]
	#print key
	#print value
	html = str(html) + '' + str(key) + ':<input type="text" name="' + str(key) + '" value="' + str(value) + '"/><br>'

html = str(html) + '<input type="submit"> </form>'

print html
