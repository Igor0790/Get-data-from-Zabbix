import csv


def write_data_in_csv_for_dict(data_dict: dict) -> None:
    with open('result.csv', 'a+', encoding='utf-8', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',
                                quotechar=' ')

        for i_router, data in data_dict.items():
            username = i_router
            speed = data['speed']
            ap_count = data['ap_count']



        text = [';', username, ';', speed, ';', ap_count]
        spamwriter.writerow(text)


def check_result_history(numbers_item: list) -> int:

    ap_count_const = 0
    ns_count = 0

    if numbers_item:

        ap_count_list = [i_count['value'] for i_count in numbers_item]
        for i_ap_count in ap_count_list:
            if int(i_ap_count) > ap_count_const:
                print(i_ap_count)
                ap_count_const = int(i_ap_count)

        # ns = [i_count['ns'] for i_count in numbers_item]
        #
        # for i_ap_count in ns:
        #     if int(i_ap_count) > ns_count:
        #         ns_count = int(i_ap_count)
        # a = round(ns_count / 1000000, 2)
        # b = 1
    return ap_count_const
