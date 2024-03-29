## selenium

## 鼠标悬停悬停操作

### 1. ActionChains

```python
from selenium import webdriver
from selenium.common.by import By
from selenium.common.action_chains import ActionChains
import time

# 0. 初始化driver,并打开url,最大化窗口
driver = webdriver.Chrome()
driver.get('http://mataim.lntu.edu.cn/xray/')
driver.maximize_window()
time.sleep(2)
# 1. 找到悬停元素
hover_elemnt = driver.find_element(By.XPATH, '//div[@class="icon-user"]/*[name()="i"]/*[name()="svg"]')

# 2. 实例化ActionChains类，调用鼠标移动操作，并使用perform()方法执行所有的鼠标动作
ActionChains(driver).move_to_element(hover_element).perform()

# 3. 定位悬浮下拉列表内的元素
driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div[1]/div/ul/li[2]').click()
```

#### 1. 百度首页`设置`悬停

```python
# 0. 初始化driver,并打开url,最大化窗口
driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.maximize_window()
time.sleep(2)

hover_element = driver.find_element(By.NAME, "tj_settingicon")
ActionChains(driver).move_to_element(hover_element).perform()

driver.find_element(By.LINK_TEXT, '搜索设置').click()
time.sleep(2)
```

#### 2. Xray 首页`登录`悬停

```python
from selenium import webdriver
from selenium.common.by import By
from selenium.common.action_chains import ActionChains
import time

# 0. 初始化driver,并打开url,最大化窗口
driver = webdriver.Chrome()
driver.get('http://mataim.lntu.edu.cn/xray/')
driver.maximize_window()
time.sleep(2)
# 1. 找到悬停元素
hover_elemnt = driver.find_element(By.XPATH, '//div[@class="icon-user"]/*[name()="i"]/*[name()="svg"]')

# 2. 实例化ActionChains类，调用鼠标移动操作，并使用perform()方法执行所有的鼠标动作
ActionChains(driver).move_to_element(hover_element).perform()

# 3. 定位悬浮下拉列表内的元素
driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div[1]/div/ul/li[2]').click()
```

#### 2.