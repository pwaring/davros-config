#!/usr/bin/env python3

list_names = ['bletchley-park', 'currybeer-announce', 'geek-walks', 'test-list']
domain = 'lists.xk7.net'

for list_name in list_names:
    print(list_name + "@" + domain)
    print(list_name + "-admin@" + domain)
    print(list_name + "-bounces@" + domain)
    print(list_name + "-confirm@" + domain)
    print(list_name + "-join@" + domain)
    print(list_name + "-leave@" + domain)
    print(list_name + "-owner@" + domain)
    print(list_name + "-request@" + domain)
    print(list_name + "-subscribe@" + domain)
    print(list_name + "-unsubscribe@" + domain)
