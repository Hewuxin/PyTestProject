## 1. 查询日志

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

## 2. 查看系统版本信息

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

## 3. 查看系统状态

### 3.1 free监控系统内存

`free`

- -g 以GB为单位
- -m 以m为单位查看内存使用情况(默认kb)
- -b 以字节为单位查看内存使用情况
- -s 可以在指定时间段内不简单监控内存的使用情况

### 3.2 top 	

实时监控系统的运行状态，并且可以按照cpu、内存和执行时间进行排序

- 命令行启动参数
- -b 批次模型运行。 通常用作来将top的输出的结果传送给其他程式或储存文件
- -c 显示执行任务的命令行
- -d 设定延迟时间
- -h 帮助
- -H 显示线程。当这个设定开始时，将显示所有进程产生的线程
- -U 监控指定用户相关进程

## 4.查看当前运行在系统中的进程信息

`ps`

```bash
-e 显示所有进程，而不只是当前用户的进程。
-f 显示完整进程信息， 包括进程的父进程 ID（PPID）、进程组 ID（PGID）、会话 ID（SID）、控制终端等
-u 以用户为单位显示进程信息，包括用户名和启动时间等。
-l 显示长格式的进程信息，包括更多的列（如进程状态、CPU 占用率、内存占用等）
-p 显示指定进程 ID 的进程信息
-a 显示所有进程，包括其他用户的进程
-x 显示没有控制终端的进程
```

### 4.1 `ps aux`

显示系统中所有进程的详细信息，包括进程的所有者、CPU 和内存占用

### 4.2 `ps -ef｜grep python`

显示系统中所有正在运行的python进程

### 4.3 `ps -u he lf|grep python`

查看用户he正在运行的python程序相关进程的全部信息，如CPU和内存占用等

查找用户 "he" 正在运行的所有进程中，含有 "python" 关键字的行，并以长格式显示这些进程的详细信息

## 5.后台运行python脚本
