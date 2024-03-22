## 一、allure介绍

- allure是多平台的Report框架

- 支持多语言，包括pyhton、javaScript、PHP、Ruby等
- 可以为开发/测试/管理人员提供详尽的测试报告，包括测试类别、测试步骤、日志、图片、视频等。
- 可以为管理层提高高水准的统计报告。
- 可以集成到Jenkins生成在线的趋势汇总报告

## 二、运行方式

### 安装allure、allure-pytest

```bash
brew install allure
pip install allure-pytest
```

### 收集测试数据

pytest 测试模块/测试包/测试用例 --alluredir=指定存储测试结果的路径

```bash
pytest --alluredir=./reports --clean-alluredir

--alluredir=./reports  表示产生的json数据保存在./reports目录下
--clean-alluredir      表示每次执行测试时都先清空文件夹
```

## 三、allure报告的生成

### 1. 在线报告，直接打开默认浏览器展示当前报告

生成在线的测试报告 

```bash
allure serve ./reports
```

### 2. 静态资源文件报告

（带index.html、Css、js等文件），需要将报告布置到web服务器上

将测试报告生成到指定的目录

```bash
allure generate ./results --clean -o ./reports

--clean 每次生成前都先清理./reports目录
./results 测试数据存放目录
./reports allure生成的测试报告存放目录
```

## 四、allure中装饰器

### 1.给测试报告添加用例标题

@allure.title

#### a. 直接食用@allure.title为测试用例自定义标题

#### b.@allure.title支持通过占位符的方式传递参数，可以实现测试用例标题参数化，动态生成测试用标题。

#### c.allure.dynamic.title动态更新测试用例标题

### 2.allure报告中添加用例步骤

应用场景：编写自动化测试用例时会遇到需要编写**流程性测试用例**的场景，一般流程性的测试用例的测试步骤比较多，在测试用例中添加详细的步骤会**提高测试用例的可阅读性**。

#### a.使用装饰器定义一个测试步骤，在测试用例中使用。

#### b.使用with allure.step()添加测试步骤。

### 3.allure报告中添加用例连接

应用场景：将报告与bug管理系统或测试用例管理系统集成，可以添加连接装饰器@allure.link、@allure.issue和@allure.testcase。

#### a. @allure.link(ur, name)，添加一个普通的link连接，name:起别名

#### b. @allure.testcase(url, name)，添加一个用例管理系统链接。

#### c. @allure.issue(url, name)，添加bug管理系统链接

### 4.allure报告中添加用例分类

应用场景：可以为项目、项目下的不同模块及用例分类管理。也可以运行某个类别下的用例。

报告展示：类别会展示在测试报告的Behaviors栏目下。

#### a. 

#### b.

#### c.

### 5. allure报告中添加用例描述

应用场景：Allure支持往测试报告中对测试用例添加非常详细的描述语，用来描述测试用例详情

#### a. @allure.description() 传递一个字符串参数来描述测试用例。

#### b. @allure.description_html() 传递一段HTML文本来描述测试用例。

#### c. 直接在测试用例方法中通过编写文档注释的方法来添加描述。会按照给定的格式展示，不需要添加\<br/>

### 6. allure报告中添加用例优先级

**应用场景：用例执行时，希望按照严重级别执行测试用例。**

解决：可以为每个用例添加一个等级的装饰器，用法allure.severity

Allure对严重级别的定义分为5个级别：

- Blocker级别：中断缺陷(客户端程序无响应，无法执行下一步操作)
- Critical级别：临界缺陷（功能点缺失）
- Normal级别：普通缺陷（数值计算错误）
- Minor级别：次要缺陷（界面错误与UI需求不符）
- Trivial级别：轻微缺陷（必输项无提示，或者提示不规范。）

### 7. allure报告中添加用例支持tags标签

allure报告支持的一些常见Pytest特性包括xfail、skipif、fixture等。

测试结果会展示特定的标识在用例详情页面

### 8. allure报告中添加pytest.fixture

**应用场景:fixture和finalizer是分别在测试开始之前和测试结束之后由Pytest调用的实用程序函数。Allure跟踪每个fixture的调用，并详细显示调用了哪些方法以及哪些参数，从而保持了调用的正确顺序。**

## 五、失败用例重试功能

allure可以收集用例运行期间，重试的用例的结果，以及这段时间重试的历史记录。

```
pip install pytest.rerunfailures
```

## 六、allure报告中添加附件

### 1. 添加图片

**应用场景:在做UI自动化测试时，可以将页面截图，或者出错的页面进行截图，将截图添加到测试报告中展示，辅助定位问题。**

解决方案: 使用allure.attch或者allure.attch.file() 添加图片。

```python

```

### 2. 添加日志

**应用场景:报告中添加详细的日志信息，有助于分析定位问题。**
**解决方案:使用python自带的logging模块生成日志，日志会自动添加到测试报告中。**