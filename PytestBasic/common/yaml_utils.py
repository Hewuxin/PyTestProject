# -*- coding: utf-8 -*-
# @Time    : 2024/3/15 21:59
# @Author  : heyuyang 
# @Project : TestProject 
# @File    : yaml_utils.py
# @Desc    :
import yaml


def read_yaml(key):
    yaml_path = '/Users/heyuyang/Study/PyProject/TestProject/PytestBasic/extract.yaml'
    with open(yaml_path, encoding='utf-8') as f:
        yaml_data = yaml.load(stream=f, Loader=yaml.FullLoader)
        return yaml_data[key]


def read_all_yaml(yaml_path):
    with open(yaml_path, encoding='utf-8') as f:
        yaml_data = yaml.load(stream=f, Loader=yaml.FullLoader)
        return yaml_data


def write_yaml(data):
    yaml_path = '/Users/heyuyang/Study/PyProject/TestProject/PytestBasic/extract.yaml'
    try:
        with open(yaml_path, encoding='utf-8', mode='a') as f:
            yaml.dump(data, stream=f, allow_unicode=True)
    except IOError as e:
        raise f"{data} write to yaml error~ {e}!"


def clear_yaml():
    yaml_path = '/Users/heyuyang/Study/PyProject/TestProject/PytestBasic/extract.yaml'
    with open(yaml_path, encoding='utf-8', mode='w') as f:
        f.truncate()


if __name__ == '__main__':
    form_data = {'student_info': [{"name": "heyuyang", "password": "123", "age": 18, "sex": "man",
                                   "flavor": ["running", "swimming", "basketball"],
                                   "Parents": {"father": "hsh", "monther": "cmx"}, },

                                  {"name": "hyy", "password": "456", "age": 36, "sex": "man",
                                   "flavor": ["gaming", "swimming", "baseball"],
                                   "Parents": {"father": "csh", "monther": "hmx"}, },
                                  {"name": "lisi", "password": "123456", "age": 10, "sex": "woman",
                                   "flavor": ["singing", "hanging out", "watch tv"],
                                   "Parents": {"father": "ash", "monther": "bmx"}, }],
                 "headers": {
                     "Authorization": "bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJoeXkiLCJleHAiOjE3MTA3MzA2"
                                      "MDB9.M8FifvP11z4YtpswWVTWZ0ANvnMEnGz3vM1g1-w4bek",
                     "Context-Type": "application/json"},
                 }
    clear_yaml()
    write_yaml(form_data)
    print(read_yaml('student_info'))
