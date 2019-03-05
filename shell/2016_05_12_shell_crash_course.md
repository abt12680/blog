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

```
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

# -a 显示隐藏文件（目录也是文件的一种）
$ ls -la
total 48
drwxr-xr-x  2 kasicass  kasicass   512 Mar   9 23:25 .
drwxr-xr-x  4 kasicass  kasicass   512 Mar   9 18:06 ..
-rwxr-xr-x  1 kasicass  kasicass  6709 Mar   9 23:25 a.out
-rwxr-xr-x  1 kasicass  kasicass  6710 Mar   9 18:19 hello
-rw-r--r--  1 kasicass  kasicass    60 Mar   9 18:59 hello.c
-rw-r--r--  1 kasicass  kasicass    77 Mar   9 23:40 my.c
```

**echo，我说啥，你说啥**

```
$ echo hello
hello

$ echo "Baby aaa"
Baby aaa

$ echo "Baby\"aaa"
Baby"aaa

# > 创建新文件，并写入内容
# >> 将内容写入文件尾部(append to file)
# 以及如何用 echo 输入多行内容
$ echo "#include <stdio.h>" > my.c
$ echo "int main(void) {" >> my.c
$ echo "  printf(\"Hello, Shell\");
>   return 0;
> }" >> my.c

# cat 干啥用的，看下一节
$ cat my.c
#include <stdio.h>
int main() {
  printf("Hello, Shell");
  return 0;
}

# 啊哈，帅不帅，我们写了个 C 程序
# "Hello, Shell" 后面没有 '\n'，所以提示符($) 跟在了 Shell 后面。
$ cc my.c
$ ./a.out
Hello, Shell$
```

**man，呼叫 help~**

man，取 manual 之意。通常也称 man page。

```
$ man echo
```

![](images/2016_05_12_shell_crash_crouse/manpage-01.png)

manpage 其实就是整个 Linux/BSD/Mac 系统中 shell命令、系统API、Driver 等等各种文档的大集合。如果 shell命令 和 系统API 有重名咋办。这就涉及到不同的 section 了。

```
# 用 j, k 或者 上/下箭头，上下翻滚页面内容
$ man write
```

![](images/2016_05_12_shell_crash_crouse/manpage-02.png)

```
# 去 section 2 中查找
$ man 2 write
```

![](images/2016_05_12_shell_crash_crouse/manpage-03.png)

用浏览器打开 [http://www.openbsd.org/cgi-bin/man.cgi][1]，可以看到 OpenBSD 所有 manpage 的分类(sections)。


[1]:http://www.openbsd.org/cgi-bin/man.cgi
