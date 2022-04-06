
import urllib.request
from xml.dom import minidom


def currency_rates(code_currency):
    url = "http://www.cbr.ru/scripts/XML_daily.asp"
    file = urllib.request.urlopen(url)

    data = file.read()
    dom = minidom.parseString(data)
    dom.normalize()

    elements = dom.getElementsByTagName("Valute")
    dict_value = {}
    for el in elements:
        for child in el.childNodes:
            if child.nodeType == 1:
                if child.tagName == "Value":
                    if child.firstChild.nodeType == 3:
                        value = float(child.firstChild.data.replace(',', '.'))
                if child.tagName == "CharCode":
                    if child.firstChild.nodeType == 3:
                        char_code = child.firstChild.data
        dict_value[char_code] = value
    if code_currency.upper() in dict_value.keys():
        return dict_value[code_currency.upper()]
    else:
        return None


print(currency_rates("EUR"))
