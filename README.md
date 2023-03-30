# Get-data-from-Zabbix
Get data from Zabbix


Скрипт, который подключается к  API Zabbix , собирает с него данные, и укладывает в csv.

main.py: 

строка 5 - указывает данные для подключения:
request = ZabbixAPI('url', user='username', password='password')

groupid = X
Вместо Х - номер группы ваших устройств в Zabbix. Чтобы ее узнать, нужно делать отдельные запросы к API.

items = request.do_request('item.get', params={
      'hostids': host['hostid'],
      'output': ['itemid', 'name'],
      'search': {'name': '(to uplink) Octets/s OUT'}
})

Здесь указываются имена счетчиков, триггеров в Zabbix. Получаем номер счетчика в API
После, по ранее полученному номеру счетчика, возвращаются данные, считаются, выводятся в csv.
Файл result.csv нужно создать заранее в корне проекта.
