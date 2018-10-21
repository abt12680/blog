# 安装 Debian 9.5

下载 small cd

* [http://mirrors.163.com/debian-cd/9.5.0/amd64/iso-cd/][1]

启动后，graphic install，一路Next，就装好了。

```
# apt-get install aptitude net-tools sysstat locate make ntpdate
```

* aptitude
* net-tools, ifconfig、netstat
* sysstat, sar、iostat、mpstat
* locate, locate、updatedb
* ntpdate, ntpdate pool.ntp.org

[1]:http://mirrors.163.com/debian-cd/9.5.0/amd64/iso-cd/