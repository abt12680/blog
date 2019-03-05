# Shell 命令偷偷教

掌握最基本的、最实用 *nix shell 命令。

## 总纲

shell 中有很多常用命令，日常维护看看 log 啥的，很实用。

shell 也可以用来写一些复杂的逻辑，但逻辑复杂后，shell 就远不如一门脚本语言（比如 python）来得方便了。

不是专业的 SA (system administrator)，不学 shell 中编程相关的那些 if ... else ... 等等。
只专注学习基本的一些命令就好。

随便找个 Linux/BSD/Mac 系统，打开 shell，开始玩吧。
（本教程例子是在 OpenBSD 5.9 中玩的）


## 基础篇

```Shell
$ <- shell 的提示符
# <- 我是注释
```

**pwd，请告诉我，当前在哪个目录？**

```
$ pwd
/home/kasicass/shell_beginner
```

**whoami，显示当前登录的 user id**

```
$ whoami
kasicass
```

**ls，看看当前目录下有啥**

```Shell
$ ls
a.out    hello    hello.c my.c

# -l 显示详细信息
$ ls -l
total 40
-rwxr-xr-x  1 kasicass  kasicass  6709 Mar   9 23:25 a.out
-rwxr-xr-x  1 kasicass  kasicass  6710 Mar   9 18:19 hello
-rw-r--r--  1 kasicass  kasicass    60 Mar   9 18:59 hello.c
-rw-r--r--  1 kasicass  kasicass    77 Mar   9 23:40 my.c
```
