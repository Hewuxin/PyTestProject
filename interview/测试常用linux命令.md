### 1. 查询日志

#### 1.1 显示末尾内容

```bash
tail -n 10 test.log 查看test.log最后10内容
tail -n +10 test.log 查案test.og第10行开始的所有内容
tail -f test.log 动态查看test.log
tail -f test.log｜grep "mom" 动态查看test.log中包含'mom'的内容
```

#### 1.2 显示前几行内容

```bash
head -n 10 test.log 查看test.log前10行内容
```

#### 1.3 查找关键字所在行号和内容

```bash
cat -n test.log |head -n 9|tail -n +2 查看test.log 2到9行内容

cat -n test.log|grep "mom" 查找test.log 文件 'mom'关键字所在行号和内容

cat -n test.log|grep "mom"|more 查找test.log 文件 多条'mom'关键字所在行号和内容，使用空格翻页查看

cat -n test.log|grep "mom"|less 允许用户通过按键(空格，模式匹配，G末尾，g开头)查看

cat -n test.log|grep "mom" > res.log 查找test.log 文件 'mom'关键字所在行号和内容，并输出到res.log文件

cat -n test.log|grep -v "mom" 查找test.log文件，不包含'mom'关键字所在行号和内容

cat -n test.log|grep -Ev "mom|batch" 查找test.log文件，不包含'mom'和'batch'关键字所在行号和内容

grep -rl 'mom' 查看当前路径下的所有文件中是否包含'mom' 输出文件相对路径/文件名
grep -r 'mom'  查看当前路径下的所有文件中具体哪一个文件中的哪一行是否包含'mom' 输出
```

#### 1.4 关联1.3 查找关键字所在的前几行或后几行

​	依据1.3查找到的行号 如102

```bash
cat -n params.txt |tail -n +92|head -n 20 查看从92开始的前20行内容
其中 tail -n +92 查看92行及以后的内容
    head -n	20  查看前20行
```

#### 1.5 按日期查找日志

```bash
sed -n '/^2024-03-13/p' test.log 查找test.log中以`2024-03-13`开头的行
sed -n '/2024-03-13/p' test.log 查找test.log中包含`2024-03-13`的行
sed -n '/2024-03-10/,/2024-03-13/p' test.log 查找指定日期范围的日志行
```

### 2. 查看版本信息

#### 1.使用`lsb_release`命令查看ubuntu版本信息

```bash
lsb_release -a
```

这将显示你的Ubuntu发行版的详细信息，包括发行版代号、发行版号、发行版名称等。

#### 2. 使用cat命令查看/etc/issue文件

```
cat /etc/issue
```

#### 3. 使用cat命令查看/etc/os-release文件 **$\color{red}通用$**

```
cat /etc/os-release
```

这将显示包含操作系统信息的文本文件的内容，其中包括了发行版的名称、版本号等





