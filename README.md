cURL2HTMLForm
=============

Transform your cURL command to a HTML Form.


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Usage:
Execute this python script in a terminal with:
$ python cURL2HTMLForm.py "curl 'http://site.dom/path -b ... (Your cURL command)'"

This will print the HTML code of your form. You can use this:
$ python cURL2HTMLForm.py "curl 'http://site.dom/path -b ... (Your cURL command)'" > htmlform.html

To generate a HTML file with the form.

IMPORTANT: Your "--data" option in your cURL command must be the latest option. We recommend that you use this script with
Google Chrome's "Copy as cURL" option.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Todas las funciones de la clase devuelven un Array! Deberas trabajar con el para mostrar los datos que necesites en tu aplicacion.

Esto es asi para no limitar el uso de la clase y que el usuario pueda trabajar con todos los datos que Tuenti nos envia a traves de su API.

phpTuenti version 0.0.3 by @alberto__segura

Licencia Creative Commons
phpTuenti API por Alberto Segura se encuentra bajo una Licencia Creative Commons Atribución-NoComercial-CompartirIgual 3.0 Unported.
