# Debian 9.5 Crash Course

## 安装系统

下载 netinst.iso，一路安装即可。

* [http://mirrors.163.com/debian-cd/9.5.0/amd64/iso-cd/][1]

源选择163，速度有保障。

* [http://mirrors.163.com/debian/][2]

在安装 package 那一步，只选择 SSH Server，其它的 package 都不选。

## 软件安装（使用aptitude）

package source，包的源，比如：[http://mirrors.163.com/debian/][2]

```
# cat /etc/apt/sources.list
deb http://mirrors.163.com/debian/ stretch main contrib non-free
deb-src http://mirrors.163.com/debian/ stretch main contrib non-free
```

```
apt-get, 是 APT 的第一版 command-line 工具
apt，是 APT 的第二版 command-line 工具
aptitude，是 graphical interface （也支持 command-line，我一般用这个）

aptitude update，从源上，拉取最新的package信息
aptitude full-update，更新所有安装的package到最新版本

aptitude search <keyword>，根据 keyword 寻找 package

aptitude install <package>，安装package
aptitude remove <package>，删除patcker
aptitude show <package>，显示packaged的详细信息

aptitude clean，删除本地下载的所有 .deb 文件
```

## 常用软件

```
# apt-get install aptitude
# aptitude install make gcc g++
# aptitude install net-tools sysstat locate ntpdate tmux
```

* aptitude
* net-tools, ifconfig、netstat
* sysstat, sar、iostat、mpstat
* locate, locate、updatedb
* ntpdate, ntpdate pool.ntp.org
* tmux, terminal multiplexer

## 启用 mongodb

```
# aptitude install mongodb
```

安装完后，mongodb 就启动了。常用的管理命令：

```
# systemctl start mongodb
# systemctl stop mongodb
# systemctl restart mongodb
```

[systemd][3] 是一套管理各种 service process 的管理器。配置文件放在 /etc 下面。

用 locate 寻找 systemd 配置文件。

```
# updatedb
# locate mongodb.service
/etc/systemd/system/multi-user.target.wants/mongodb.service
```

mongodb 配置文件

* /etc/mongodb.conf

启动 mongo 会看到

```
** WARNING: soft rlimits too low. rlimits set to 31861 processes, 65535 files.
Number of processes should be at least 32767.5 : 0.5 times number of files.
```

虽然开发环境无所谓，但看着烦躁，还是解决下。解决方法看 [这里][4]，修改 mongodb.service，增加如下内容：

```
[Service]
LimitFSIZE=infinity
LimitCPU=infinity
LimitAS=infinity
LimitMEMLOCK=infinity
LimitNOFILE=64000
LimitNPROC=64000
```

重启服务，搞定。

```
# systemctl daemon-reload
# systemctl restart mongodb
```

## 启用 mysql

```
# aptitude install mysql-server
```

mysql配置文件

* /etc/mysql/my.cnf

默认dbpath

* /var/lib/mysql

debian9开始，mysql使用系统的认证。让某个 user 可以通过 mysql client 访问 mysql-server，需要：
```
# su
# mysql

> USE mysql;
> CREATE USER 'YOUR_SYSTEM_USER'@'localhost' IDENTIFIED VIA unix_socket;
> exit;
```

* 参考，[https://wiki.debian.org/MySql][5]
* 重置密码，[https://www.vultr.com/docs/reset-mysql-root-password-on-debian-ubuntu][6]

## vim & tmux 的基本配置

```
$ cat ~/.vimrc
" basic
syn on
set tabstop=2
set nobackup
set background=dark
colorscheme desert
set number

$ cat ~/.tmux.conf
# hjkl pane traversal
bind h select-pan -L
bind j select-pan -D
bind k select-pan -U
bind l select-pan -R

# reload me
bind r source ~/.tmux.conf\; display "/.tmux.conf sourced!"
```

[1]:http://mirrors.163.com/debian-cd/9.5.0/amd64/iso-cd/
[2]:http://mirrors.163.com/debian/
[3]:http://www.freedesktop.org/wiki/Software/systemd/
[4]:https://docs.mongodb.com/manual/reference/ulimit/#linux-distributions-using-systemd
[5]:https://wiki.debian.org/MySql
[6]:https://www.vultr.com/docs/reset-mysql-root-password-on-debian-ubuntu
