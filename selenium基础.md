## selenium

环境依赖

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

前提：需要定位的元素或者它的属性必须唯一

面试题：如果元素定位不到，如何分析？

1. 元素没有加载完成
2. Frame中
3. 元素不可用，不可读，不可见
4. 动态属性，动态的div层

### 1. id

### 2. name

### 3. class_name 不常用

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

==coomand + f 查找标签==

### 5. css

- 绝对路径 不用
- 通过ID和Class定位
- 通过属性定位
- 通过部分属性定位
- 查询子元素定位
- 查询兄弟节点定位

### 6. tage_name 不常用

### 7. link_text

### 8. partail_link_text

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

## 下拉框操作

1. 进入框架
2. 定位下拉框并转换为Select对象
3. 选中所有分类下拉框中的GSM手机
4. 搜索

```python
selenium.webdriver.support.select.Select


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

### alert

只有确定

### confirm

有确定有取消

### prompt

有确定有取消还可以输入值

```python
ale = driver.switch_to.alert
ale.dismiss() # 取消
ale.accept()  # 确定
ale.text # 获取弹窗文本
ale.sen_keys() # 输入文本，只有prompt可以使用
```

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