from pyzabbix import ZabbixAPI
import time
from utils import write_data_in_csv_for_dict, check_result_history

request = ZabbixAPI('https://nop.zabbix.sys.local', user='igor.gubaydullin', password='24691356qW!@#$%')

answer = request.do_request('apiinfo.version')

groupid = 338         #номер группы роутеров Eltex HS 1.0


time_from = int(time.mktime((2023, 1, 1, 0, 0, 0, 0, 0, 0)))
time_till = int(time.mktime((2023, 2, 1, 0, 0, 0, 0, 0, 0)))



hosts = request.host.get(groupids=groupid, output=['hostid', 'name'])

counter = 0
for host in hosts:


    #Парсинг загрузки uplink
    items = request.do_request('item.get', params={
      'hostids': host['hostid'],
      'output': ['itemid', 'name'],
      'search': {'name': '(to uplink) Octets/s OUT'}
})

    data_dict = {}
    data_dict[host['name']] = {}

    print('HOST:', host['name'])

    traf_max = 0

    if items['result']:
        speed_request_history = request.history.get(history=3, itemids=items['result'][0]['itemid'], time_from=time_from, time_till=time_till)
        traf_max = round(check_result_history(speed_request_history) / 1000000, 2)


    data_dict[host['name']]['speed'] = str(traf_max)


    ap_request = request.do_request('item.get', params={
                'hostids': host['hostid'],
                'output': ['itemid', 'name'],
                'search': {'name': 'gre tunnel exhaustion'}
            })

    ap_count_const = 0

    if ap_request['result']:

        for i_result in ap_request['result']:

            ap_request_history = request.history.get(history=3, itemids=i_result['itemid'], time_from=time_from,
                                                     time_till=time_till)
            temp_counter = check_result_history(ap_request_history)

            if temp_counter > ap_count_const:
                ap_count_const = temp_counter

    data_dict[host['name']]['ap_count'] = str(ap_count_const)

    write_data_in_csv_for_dict(data_dict)

    counter += 1










