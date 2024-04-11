## selenium

- Selenium WebDriver和浏览器如何通信

  > - 对于每一条Selenium脚本，一个http请求会被创建并且发送给浏览器的驱动
  >
  > - 浏览器驱动中包含了一个HTTP Server， 用来接收这些http请求
  >
  > - HTTP Server接收到请求后根据请求来具体操控对应的浏览器
  >
  > - 浏览器执行具体的测试步骤
  >
  > - 浏览器将步骤执行结果返回给HTTP Server
  >
  > - HTTP Server又将结果返回给Selenium的脚本，如果是错误的http代码就会在控制台看到对应的报错信息。

### 环境依赖

- Python

- IDE

- Selenium

  - 安装

  - 验证

    ```bash
    pip show selenium
    ```

- 浏览器

- Webdriver

  - chrome会疯狂自动更新，需要自动安装Webdirver,**内网需要手动下载**

  - ```bash
    pip install webdriver-helper==1.*
    ```
  - 将`Web_driver.py`文件放到项目目录下
  
  - ```python
    from webdirver-helper import get_webdriver
    
    driver = get_webdriver() #获取浏览器驱动
    ```

## 八大元素

==coomand + f 查找标签==

前提：需要定位的元素或者它的属性必须唯一

面试题：如果元素定位不到，如何分析？

1. 元素没有加载完成
2. Frame中
3. 元素不可用，不可读，不可见
4. 动态属性，动态的div层

### 1. id

### 2. name

通过标签名称定位

```python
find_element(By.NAME, "su")
```

### 3. class_name 不常用

通过css class定位

```python
find_element(By.CLASS_NAME, "access-button")
assert element.text == "在线调用"
```

### 4. xpath

- 绝对路径 ： /开头是绝对路径

- 相对路径： //开头是相对路径

  1. 相对路径+索引定位

     `//form/span[1]/input`

  2. 相对路径+属性定位

     `//input[@autocomplete='off']`

  3. 相对路径+通配符定位

     `//*[@autocomplete='off']`

     `//*[@*='off]'`

     $\color{red}复制xpath经常会出错$

  4. 相对路径+部分属性值定位

     - 以string 开头 `//*[start_wtih(@autocomplete, string)]`
     - 以string结尾 `//*[substring(@autocomplete, 2)=string]`
     - 包含string  `//*[contains(@autocomplete, string)]`

  5. 相对路径+文本定位

     `//span[text()="按图片搜索"]`

### 5. css

copy selector

- 绝对路径 不用
- 通过ID和Class定位
- 通过属性定位
- 通过部分属性定位
- 查询子元素定位
- 查询兄弟节点定位

### 6. tage_name 不常用

标签名称 h1 input等等

### 7. link_text

### 8. partail_link_text

### 9. 获取元素函数封装

```python
def get_element(driver, *loc):
    driver.find_element(*loc)
    return e

def init_driver(base_url):
    driver = webdriver.Chrome()
    driver.get(base_url)
    return driver

def test_access_button():
    driver = init_driver("http://mataim.lntu.edu.cn/xray/#/")
    loc = ("xpath", "//*[@classname='access-button']")
    acces_btn = get_element(driver, *loc)
    assert access_btn.text == "在线试用"
    
```

## WebDriver属性和方法

| #    | 属性        | 属性描述   |
| :---: | :---------: | :----------: |
| 1    | driver.name | 浏览器名称 |
| 2    | driver.current_url | 当前url |
| 3    | driver.title | 当前页面标题 |
| 4    | driver.page_source | 当前页面源码 |
| 5    | driver.current_window_handle | 窗口句柄 |
| 6  | driver.window_handles | 当前窗口所有句柄 |
- 方法
| #    | 方法                      | 方法描述       |
| :----: | :-------------------------: | :--------------: |
| 1    | forward()                 | 前进           |
| 2    | refresh()                 | 刷新           |
| 3    | back()                    | 后退           |
| 4    | close()                   | 关闭当前窗口   |
| 5    | quit()                    | 退出浏览器     |
| 6    | switch_to_frame()         | 切换到frame    |
| 7    | switch_to.alert()         | 切换到alert    |
| 8    | switch_to.activae_element() | 切换到活动元素 |

## WebElement属性



使用WebDriver的find 方法定位到元素后，会返回一个WebElement对象，该对象用来描述Web页面上的一个元素。

| #    | 属性     | 属性描述   |
| :----: | :-------- | :----------: |
| 1    | id       | 标示       |
| 2    | size     | 宽高       |
| 3    | rect     | 宽高和坐标 |
| 4    | tag_name | 标签名称   |
| 5    | text     | 文本内容   |

==**方法**==

WebElement也有find_element方法,可以通过八大元素定位WebElement中的元素.

| #    | 方法                    | 方法描述   |
| :---: | :-----------------------: | :----------: |
| 1    | send_keys()             | 输入内容   |
| 2    | click()                 | 点击       |
| 3    | clear()                 | 清空内容   |
| 4    | get_attribute()         | 获得属性值 |
| 5    | is_selected()           | 是否被选中 |
| 6    | is_enabled()            | 是否可用   |
| 7    | is_displayed()          | 是否禁用   |
| 8    | value_of_css_property() | css属性值  |

```python
e.value_of_css_property("font")
e.value_of_css_property("color")

form_element = driver.find_element('xpath', '//*[@name="form"]')
span_elemnt = form_element.find_element("tag_name", "span")
```

## 操作form表单

form表单的操作流程

1. 定位表单元素
2. 输入测试值
3. 判断表单元素属性
4. 获得表单元素属性
5. 提交表单进行验证

```python
from selenium import webdriver
import os
import time


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        path = os.path.dirname(os.path.abspath(__file__))
        file_path = "file:///" + path + "./forms.html"
        self.driver.get(file_path)
     def test_login(self):
        username = self.driver.find_element('id', 'username')
        username.send_keys("1")
        pwd = self.driver.find_element('id', 'pwd')
        pwd.send_keys("1")
        self.driver.find_element("xpath", "//*[@class='access-button']").click()
        
        print(username.get_attribute("value"))
        print(pwd.get_attribute("value"))
```

## 操作checkbox和radio

### 1. checkbox

```python
def test_checkbox(driver):
    swimming = driver.find_element("name", "swimming")
    if not swimming.is_selected():
        swimming.click()
    reading = driver.find_elemnt("name", "reading")
    if not reading.is_selected():
        reading.click()
        
    time.sleep(3)
    # 反选
    reading.click()
```

### 2. radio button

```python
def test_radio_button(driver):
    radio_btn = driver.find_elements("name", "gender")
    radio_btn[1].click()
```

## 下拉框/下拉框操作

处理下拉列表，需要用到Selenium中的一个工具类***==Select==***，

```python
from selnium.webdirver.support.select import Select
```

| #    | 方法/属性                | 方法/属性描述  |
| ---- | ------------------------ | -------------- |
| 1    | select_by_value          | 根据值选择     |
| 2    | select_by_index          | 根据索引选择   |
| 3    | select_by_visivle_text   | 根据文本选择   |
| 4    | deselect_by_value        | 根据值反选     |
| 5    | deselect_by_index        | 根据索引反选   |
| 6    | deselect_by_visible_text | 根据文本反选   |
| 7    | deselect_all             | 反选所有       |
| 8    | options                  | 所有选项       |
| 9    | all_selected_options     | 所有选中选项   |
| 10   | first_selected_option    | 第一个选择选项 |

```python
from selenium.webdriver.support.select import Select

def test_select(driver):
    select_elemnt = driver.find_element("id", "prov")
    select = Select(select_element)
    select.select_by_value("sh")
    
    select.select_by_visible_text("上海")
```



1. 进入框架
2. 定位下拉框并转换为Select对象
3. 选中所有分类下拉框中的GSM手机
4. 搜索

```python
selenium.webdriver.support.select.Select
def test_form(driver):
    driver.switch_to.frame("menu-frame")
    driver.find_element(BY.LINK_TEXT, "商品列表").click()

    # 出框架
    driver.switch_to_default_content()
    # 进入到main框架
    driver.switch_to.frame("main-frame")
    # 选中所有分类下拉框中的GSM手机
    sel = Select(driver.find_element(By.NAME, "cat_id"))
    # value
    sel.select_by_value("4")
    # 
    sel.select_by.visible_text("手机配件")
    #
    sel.select_by_index("7")
    # 搜索
    driver.find_element(By.XPATH, "//input[@value= '搜索']").click()
```

上传单张图片

```python
# 出框架
driver.switch_to_default_content()
# 进入到main框架
driver.switch_to.frame("main-frame")
# 输入商品名称
driver.find_element(By.Name, "goods_name").send_keys("aaa")
# 选择商品分类
goods_class_sel = select(driver.find_element(By.Name, "cat_id"))
goods_class_sel.select_by_value("12")
# 输入价格
shop_price = driver.find_element(By.Name, "shop_price")
# 清除默认值
shop_price.clear()
# 输入新值
shop_price.send_keys("6880")
# 上传图片
driver.find_element(By.Name, "goods_img").send_kyes(r"E:/shu.png")
# 点击确定，完成上传
driver.find_element(By.XPATH, "//input[@value= ' 确定	']").click()
```

## 弹窗处理

- alert 只有确定

- confirm 有确定有取消

- prompt 有确定有取消还可以输入值

```html
<a href="javascript:alert('提示框')" id="alert">Alert</a><br>
<a href="javascript:confirm('真的要删除数据吗')" id="confirm">Confirm</a><br>
<a href="javascript:var age= promopt('请输入年龄');document.write(age)" id="prompt">Prompt</a><br>
```

| #    | 方法/属性   | 方法/属性描述                |
| :----: | :-----------: | :----------------------------: |
| 1    | accept()    | 接收                         |
| 2    | dismiss()   | 取消                         |
| 3    | text        | 获取弹窗文本                 |
| 4    | send_kyes() | 输入文本，只有prompt可以使用 |

```python
from selenium import webdriver

ale = driver.switch_to.alert
ale.dismiss() # 取消
ale.accept()  # 确定
ale.text # 获取弹窗文本
ale.sen_keys() # 输入文本，只有prompt可以使用

def test_alert(driver):
    # 点击按钮触发alert
    self.driver.find_elemnt("id", "alert").click()
    # 切换到alert
    alert = self.driver.switch_to.alert
    print(alert.text)
    alert.accept()

def test_confirm(driver):
    # 点击按钮触发confirm
    self.driver.find_elemnt("id", "confirm").click()
    # 切换到alert
    confirm = self.driver.switch_to.alert
    print(confirm.text)
    alert.accept()
    # alert.dismiss()
    
def test_confirm(driver):
    # 点击按钮触发prompt
    self.driver.find_elemnt("id", "prompt").click()
    # 切换到alert
    prompt = self.driver.switch_to.alert
    print(prompt.text)
    
    prompt.send_keys("20")
    
    alert.accept()
    # alert.dismiss()
```

## 三种等待

***==为什么需要等待==***

- 在UI自动化测试中，会遇到环境不稳定，网络慢的情况，这事如果不做任何处理，代码可能会由于没有找到元素而报错。

- 页面使用ajax异步加载机制。这时需要使用wait

### 1. `time.sleep()固定等待`

$\color{red}主要用于调试，不能在实际项目中使用$

### 2.  `implicitly_wait（隐式等待）`

   > - 设置一个最长等待时间，如果在规定时间内网页加载完成，则执行下一步，否则一直等待时间结束，然后执行下一步。
   >
   > - 这种隐式等待的缺陷： javaScript一般都放在body的最后进行加载，但此时页面上的元素已经加载完毕，却还在等待全部页面加载结束。

   - 隐式等待对整个driver周期都起作用，在最开始设置一次就可以。不要当作固定等待使用，到哪都使用隐式等待。

```python
def test_implicitly_wait(driver):
    driver.implicitly_wait(10)
    driver.find_element("id", "kw").send_keys("selenium")
```

### 3. `WebDriverWait(显式等待)`

是Selenium提供得到显示等待模块引入路径：

- `from selenium.webdriver.support.wait import WebDriverWait`

- `WebDriverWait参数`

    | #    | 参数               | 参数说明                                          |
    | :--- | :----------------- | :------------------------------------------------ |
    | 1    | driver             | 传入WebDriver实例                                 |
    | 2    | timeout            | 超时间，等待的最长时间                            |
    | 3    | poll_frequency     | 调用until或until_not中的方法的间隔时间，默认0.5秒 |
    | 4    | ignored_exceptions | 忽略的异常                                        |

- 这个模块中，一共只有两种方法until和until_not。

  | #    | 参数    | 参数说明                                                     |
  | :--- | :------ | :----------------------------------------------------------- |
  | 1    | method  | 在等待时间，每隔一段时间调用这个传入的方法，直到返回值不是False |
  | 2    | message | 如果超时，抛出TimeoutException，将message传入异常            |
- 各种等待条件

| #    | 方法                                   | 方法描述                                                | 返回值     |
| ---- | -------------------------------------- | ------------------------------------------------------- | ---------- |
| 1    | title_is                               | 判断title,是否出现                                      | 布尔       |
| 2    | title_contains                         | 判断title，是否包含某些字符                             | 布尔       |
| 3    | presence_of_element_located            | 判断某个元素是否被加到了dom树里，并不代表该元素一定可见 | WebElement |
| 4    | visibility_of_element_located          | 判断某个元素是否加到了dom树里，并且可见，宽高都大于0    | WebElement |
| 5    | visibility_of                          | 判断某个元素是否可见，如果可见就返回这个元素            | WebElement |
| 6    | presence_of_all_element_located        | 判断是否至少有1个元素存在于dom树中                      | 列表       |
| 7    | visibility_of_any_element_located      | 判断是否至少有1个元素在页面中可见                       | 列表       |
| 8    | text_to_be_present_in_element          | 判断指定的元素中是否包含了预期的字符串                  | 布尔       |
| 9    | text_to_be_present_in_elemnt_value     | 判断指定元素的属性值中是否包含了预期的字符串            | 布尔       |
| 10   | frame_to_available_and_switch_to_it    | 判断该frame是否可以switch进去                           | 布尔       |
| 11   | invisibility_of_element_located        | 判断某个元素是否存在于dom或不可见                       | 布尔       |
| 12   | element_to_be_clickable                | 判断某个元素中是否可见并且是enable的，代表可点击        | 布尔       |
| 13   | staleness_of                           | 等待某个元素从dom树中移除                               | 布尔       |
| 14   | element_to_be_selected                 | 判断某个元素是否被选中，一般用在下拉列表                | 布尔       |
| 15   | element_selection_state_to_be          | 判断某个元素的选中状态是否符合预期                      | 布尔       |
| 16   | element_localted_selection_state_to_be | 判断某个元素的选中状态是否符合预期                      | 布尔       |
| 17   | alert_is_present                       | 判断页面上是否存在alert                                 | alert      |

```python
from selenium.webdriver.support.ui import WebDriverWait
from selnium.webdirver.support import expected_conditions as EC

hover = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        '//div[@class="icon-user"]/*[name()="i"]/*[name()="svg"]'))
    )


def test_wait(driver):
    driver.find_element("id", "btn").click()
    
    wait = WebDriverWait(driver, 3)
    wait.until(
        EC.text_to_be_present_in_element(("id", "id2"),"id 2")
    )
    div = driver.find_element('id', 'id2')
    print(div.text)
```

## 鼠标和键盘事件

Selenium中鼠标和键盘事件被封装在`ActionChains`类中，正确的使用方法是:

`from selenium.common.action_chains import ActionChains`

`ActionChains(driver).click(btn).perform()`

`ActionChains`中常用的方法:

| #    | 方法                                                       | 方法描述                                   |
| ---- | ---------------------------------------------------------- | ------------------------------------------ |
| 1    | click(on_element=None)                                     | 单击鼠标左键                               |
| 2    | click_and_hold(on_element=None)                            | 点击鼠标左键，不松开                       |
| 3    | context_click(on_element=None)                             | 点击鼠标右键                               |
| 4    | double_click(on_element=None)                              | 双击鼠标左键                               |
| 5    | drag_and_drop(source, target)                              | 拖拽到某个元素然后松开                     |
| 6    | drag_and_drop_by_offset(source, xoffset, yoffset)          | 拖拽到某个坐标然后松开                     |
| 7    | key_down(value, element=None)                              | 按下键盘上的键                             |
| 8    | key_up(value, element=None)                                | 松开某个键                                 |
| 9    | move_by_offset(xoffset,  yoffset)                          | 鼠标从当前位置移动到某个坐标               |
| 10   | move_to_element(to_element)                                | 鼠标移动到某个元素                         |
| 11   | move_to_element_with_offset(to_element, xoffset,  yoffset) | 移动到距某个元素(左上角坐标)多少距离的位置 |
| 12   | perform()                                                  | 执行链中的所有动作                         |
| 13   | release(on_element=None)                                   | 在某个元素位置松开鼠标左键                 |
| 14   | send_keys(*keys_to_send)                                   | 发送某个键到当前焦点的元素                 |
| 15   | send_keys_to_element(element, *keys_to_send)               | 发送某个键到指定元素                       |

> 练习链接 https://sahitest.com/demo/
```python
from selenium.common.action_chains import ActionChains

def test_actionchains(driver):
    # 1. 找到悬停元素
    hover_elemnt = driver.find_element(By.XPATH, '//div[@class="icon-user"]/*[name()="i"]/*[name()="svg"]')

    # 2. 实例化ActionChains类，调用鼠标移动操作，并使用perform()方法执行所有的鼠标动作
    ActionChains(driver).move_to_element(hover_element).perform()

```

### keys 辅助键

`from selenium.webdriver.common.keys import Keys `

```python
from selenium.webdriver.common.keys import Keys


def test_key(driver):
    driver.get("http://www.baidu.com")
    kw = driver.find_element("id", "kw")
    kw.send_keys("selenium")
    kw.send_keys(Keys.CONTROL, 'a')
    seleep(2)
    kw.send_keys(Keys.CONTROL, 'x')
    seleep(2)
    kw.send_keys(Keys.CONTROL, 'v')
    
```

### 鼠标移动到指定元素

```python
from selenium..common.action_chains import ActionChains

def test_mouse_move(driver):
    driver.get("http://www.baidu.com")
    login_btn = driver.find_element("")
	ActionChains(driver).move_to_element(log_btn).perform()
    sleep(2)
    ActionChains(driver).move_to_element(log_btn).click()perform()
    sleep(2)
```

## 执行JavaScript脚本

### excute_script 同步执行

```python
from selenium import webdriver

def test_script(driver):
    driver.get('http://www.baiduc.com')
    driver.excute_script("alert('test')")
    time.sleep(2)
    driver.switch_to.alert.accept()

def test_script2(driver):
    js = "return document.title"
    title = driver.excute_script(js)
    print(title)
    
    js = 'var q = document.getElementById("kw"); q.style.border="2px solid red"'
    driver.excute_script(js)
    
def test_script3(driver):
    """滚动页面"""
    driver.get("https://www.baidu.com")
    driver.find_element("id", "kw").send_keys("selenium")
    driver.find_element("id", "su").click()
    time.sleep(2)
    js = 'window.scrollTo(0, document.body.scrollHeight)'
    driver.excute_script(js)
    time.sleep(2)
```

### excute_async_script 异步执行

## 屏幕截图

selenium内置的捕获屏幕并保存的方法：

| #    | 方法                            | 方法描述                                                     |
| ---- | ------------------------------- | ------------------------------------------------------------ |
| 1    | save_screenshot(filename)       | 获取当前屏幕截图并保存为指定文件，filename是指定保存的路径或图片的文件名 |
| 2    | get_screenshot_as_base64()      | 获取当前屏幕截图base65编码字符串                             |
| 3    | get_screenshot_as_fie(filename) | 获取当前的屏幕截图，使用完整的路径                           |
| 4    | get_screenshot_as_png()         | 获取当前屏幕截图的二进制文件数据                             |

```python
from selenium import webdriver

def test_save_screenshot(driver):
    driver.find_element("id", "kw").send_keys("selenium")
    driver.find_element("id", "su").click()
    driver.save_screenshot("result.png")

```



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

## 解决定位失败问题

`selenium.common.exceptions文件`

```python
selenium.common.exceptions.InvalidSelectorException
```

1. 定位表达式错误

2. 元素不存在

   1. 时态问题

      1. 是否曾经存在

      2. 是否未来存在

         1. 休眠

            > 使用编程语言提供的特性

            

         2. 等待

            >  使用Selenium提供的特性 

            主要差异：在等待过程中，**会保持和外界的联系**，如果等待的对象提前到达，那么等待就**提前结束**

            - 隐式等待, 可以写在任何地方

              ```python
              driver.implicitly_wait(30) # 最多等待30秒，可以提前结束
              ```

            - 显式等待，必须写在定位元素之前

              ```python
              from selenium.webdriver.support.ui import WebDriverWait
              
              hover = WebDriverWait(driver, 10).until(
                      EC.presence_of_element_located((By.XPATH,
                                                      '//div[@class="icon-user"]/*[name()="i"]/*[name()="svg"]'))
                  )
              ```

              1. 实例化WebDriverWait
              2. 调用unitl方法
              3. 传递等待函数
              4. 等待函数必须返回布尔值为真，表示找到元素可以提前结束

3.  元素存在无法操作

4. 