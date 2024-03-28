## 1. string.Template

​	如果碰到特殊符号`${}`，它会自动去用字典的key替换`${}`同名的变量

```python
from string import Template

info = {"age":11, "name": "heyuyang"}
url = "你好我叫${name}，今年${age}岁了"
print(Template(url).substitute(info))
```

