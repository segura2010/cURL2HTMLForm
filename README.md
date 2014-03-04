cURL2HTMLForm
=============

Transform your cURL command to a HTML Form.


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Usage:
Execute this python script in a terminal with:
$ python cURL2HTMLForm.py "curl 'http://site.dom/path -b ... (Your cURL command)'"

This will print the HTML code of your form. You can use this to generate a HTML file with the form:
$ python cURL2HTMLForm.py "curl 'http://site.dom/path -b ... (Your cURL command)'" > htmlform.html


IMPORTANT: Your "--data" option in your cURL command must be the latest option. We recommend that you use this script with
Google Chrome's "Copy as cURL" option.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Licencia Creative Commons" style="border-width:0" src="http://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">cURL2HTMLForm</span> por <a xmlns:cc="http://creativecommons.org/ns#" href="https://github.com/segura2010/cURL2HTMLForm/" property="cc:attributionName" rel="cc:attributionURL">Alberto Segura (@alberto__segura)</a> se distribuye bajo una <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Licencia Creative Commons Atribución-NoComercial-CompartirIgual 4.0 Internacional</a>.
