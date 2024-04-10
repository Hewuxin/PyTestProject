## Jenkins

可扩展的持续集成和持续部署的平台，也只是一个平台，运行的都是插件

### 持续集成

把整个软件生命周期中的所有工作实现自动化，以流水线的方式去完成软件的研发全过程。

- 开发：编写代码并且进行源码管理，编译打包提供给测试人员测试。
- 测试：部署测试环境进行功能测试，持续化集成自动化测试。
- 运维：部署线上环境。

## Jenkins环境配置

### 1. jenkins环境拉取

```
docker search jenkins
docker pull jenkins/jenkins
```

### 2. 启动jenkins容器

```bash
docker run -d -uroot -p 9095:8000 -p 50000:50000 --name jenkins_demo -v /Users/heyuyang/Study/jenkins_home:/var/jenkins_home jenkins/jenkins
    docker run -d 后台运行
    -uroot 添加root权限
    -P 9095:8000 将jenkins的8000端口映射到宿主机的9095端口
    -p 50000:50000  将jenkins的50000端口映射到宿主机的50000端口
    --name jenkins_demo 容器名称
    -v /Users/heyuyang/Study/jenkins_home:/var/jenkins_home
        /Users/heyuyang/Study/jenkins_home
        /var/jenkins_home
        将硬盘上的.../jenkins_home挂在到这个位置，方便后续更新镜像后继续使用原来的工作目录
    jenkins/jenkins image镜像源
```

### 3.查看容器日志，获取初始密码

`docker logs jenkins_demo`

初始密码存放在jenkins容器的`/var/jenkins_home/secrets/initialAdminPassword`文件中

## Jenkins使用

### 插件安装

1. allure Jenkins Plugin