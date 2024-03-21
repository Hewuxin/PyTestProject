## YAML文件用途，结构，数据类型

- 是一种数据类型，可以和json灵活的进行切换，支持注释，换行，字符串

- 配置文件
- 编写测试用例

### yaml数据结构

1. Map对象dict（键: 值）
2. 数组（list），用一组横线"-"开头表示

```yaml
{"student_info":[{
				"Parents":{"father":"hsh", "mother":"cmx"},
				"age":18,
				"flavor":["running","swimming","basketball"],
				"name":"heyuyang",
				"password":"123",
				"sex":"name"},
				,]}
student_info:
- Parents:
    father: hsh
    mother: cmx
  age: 18
  flavor:
  - running
  - swimming
  - basketball
  name: heyuyang
  password: '123'
  sex: man

```

### pyyaml安装

```
pip install pyyaml
```

### YAML文件python自动读取/写入/清空

- 读取

  ```python
  import os
  import yaml
  
  def read_yaml(key):
      with open(file_path, encoding='utf-8') as f:
          value = yaml.load(stream=f,Loader=yaml.FullLoader)
          return value[key]
      	pprinit.pprinit(value)
  ```

- 写入1

  ```python
  import os
  import yaml
  
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
  def write_yaml(data):
      with open(file_path, encoding='utf-8', mode='a') as f:
          value = yaml.dump(data, stream=f,allow_unicode=True)
          return value[key]
  ```

  ```yaml
  headers:
    Authorization: bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJoeXkiLCJleHAiOjE3MTA3MzA2MDB9.M8FifvP11z4YtpswWVTWZ0ANvnMEnGz3vM1g1-w4bek
    Context-Type: application/json
  student_info:
  - Parents:
      father: hsh
      monther: cmx
    age: 18
    flavor:
    - running
    - swimming
    - basketball
    name: heyuyang
    password: '123'
    sex: man
  - Parents:
      father: csh
      monther: hmx
    age: 36
    flavor:
    - gaming
    - swimming
    - baseball
    name: hyy
    password: '456'
    sex: man
  - Parents:
      father: ash
      monther: bmx
    age: 10
    flavor:
    - singing
    - hanging out
    - watch tv
    name: lisi
    password: '123456'
    sex: woman
  ```

- 写入2

  ```python
  import yaml
  
  data = {
      "student_info": [{
          "Parents": {"father": "hsh", "mother": "cmx"},
          "age": 18,
          "flavor": ["running", "swimming", "basketball"],
          "name": "heyuyang",
          "password": "123",
          "sex": "name"
      }],
      "class": 1,
      "desc": [["a", "b", "c"], [1, 2, 3], [4, 5, 6]]
  }
  
  yaml_data = yaml.dump(data, default_flow_style=False)
  print(yaml_data)
  
  ```
  
  ```yaml
  class: 1
  desc:
  - - a
    - b
    - c
  - - 1
    - 2
    - 3
  - - 4
    - 5
    - 6
  student_info:
  - Parents:
      father: hsh
      mother: cmx
    age: 18
    flavor:
    - running
    - swimming
    - basketball
    name: heyuyang
    password: '123'
    sex: name
  ```
  
- 清空

  ```python
  import os
  import yaml
  
  def clear_yaml(key):
      with open(file_path, encoding='utf-8', mode='w') as f:
          f.truncate()
  ```

## yaml测试用例

看文档--->写请求代码(自动生成) --->改成yaml

自动生成yaml  
