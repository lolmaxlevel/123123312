# -*- coding: utf-8 -*-
import time
import yaml
import json


def getname(n):
    return n[0:n.index(':')].strip()


def getvalue(n):
    return n[n.index(':') + 1:].strip()


# Основное задание:
def n1():
    res = ''
    with open(r'yaml.yaml') as f:
        a = f.readlines()
    a1 = [i.replace('  ', '\t').count('\t') for i in a]

    for i in range(len(a) - 1):
        if a1[i] < a1[i + 1]:
            res += '"' + getname(a[i]) + '"' + ':{'
        elif a1[i] > a1[i + 1]:
            if a1[i + 2] == a1[i]:
                res += '"' + getname(a[i]) + '"' + ':' + '"' + getvalue(a[i]) + '"''},'
            else:
                res += '"' + getname(a[i]) + '"' + ':' + '"' + getvalue(a[i]) + '"''}'
        else:
            res += '"' + getname(a[i]) + '"' + ':' + '"' + getvalue(a[i]) + '"'','
    res += '"' + getname(a[-1]) + '"' + ':' + '"' + getvalue(a[-1]) + '"' + '}' * (a1[-1] // 2)
    res = '{' + res + '}'

    with open(r'json.json', 'w') as f:
        f.writelines(res)


# Доп. задание 1:
def n2():
    with open(r"yaml.yaml", 'r') as yaml_in, open(r'json2.json',
                                                                         'w') as json_out:
        yaml_object = yaml.safe_load(yaml_in)
        json.dump(yaml_object, json_out, ensure_ascii=False)


# Доп. задание 3:
t = time.time()
for i in range(10):
    n2()
print(time.time() - t)

t = time.time()
for i in range(10):
    n1()
print(time.time() - t)


# Доп. задание 4:
result_csv = []
headers = ['place', 'time', 'weektype', 'teacher', 'address', 'format']
with open(r'yaml.yaml') as f:
    a = f.readlines()
    a = [o.strip() for o in a[1:]]
e = headers[:]
for i in a:
    if getname(i) not in headers:
        result_csv.append(e[:])
        e.clear()
        e.append(getname(i))
    else:
        e.append(getvalue(i))
result_csv.append(e)
for i in result_csv:
    print(i)
