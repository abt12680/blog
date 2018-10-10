# 小肥鱼上的 Distribution Sets

Distribution Sets 就是操作系统的组件，我们可以有选择性地安装这些组件，以构建我们所需要的系统。OpenBSD的 set 不多，就那么几个，下面是这些 set 的含义：

### bsd

This small distribution set contains the kernel. The kernel is important. The installer will complain if you don't have it and issue all sorts of dire warnings. Worse, your new system will not boot without it.

### baseXX.tgz

This contains OpenBSD's core programs, all the things that make OpenBSD UNIXish. All the programs in /bin, /sbin, /usr/bin, and /usr/sbin, the system libraries, and the miscellaneous programs you expect to find on a UNIX system are in this distribution set. Without this distribution set, your OpenBSD system will not work at all.

### etcXX.tgz

You might guess that this distribution set contains the /etc/ directory, but it also contains assorted other files and directories that are required by the system, such as /var/log, as well as root's home directory. You must install this distribution set if you want your OpenBSD system to actually run.

### manXX.tgz

If you need the manual pages for the programs in the base and the etc set, install this distribution set. The manual pages for other sets are installed with the distribution set.

### compXX.tgz

This distribution contains C, C++, and Fortran compilers, tools, and the associated toolchain for each. It also includes the manual pages and documentation for the compilers. You will want this set if you plan to develop or compile software on this system. You need this set to use the ports collection. While this distribution set isn't large, you might choose to not install in on a secure machine such as a firewall. (Intruders are generally delighted to find a properly configured compiler on a firewall; such tools make a hacker's life much easier.)

### gameXX.tgz

This distribution set contains a variety of simple games and documentation for them, based on games originally distributed in the BSD 4.4-Lite software collection. Some of these, such as fortune(1), are considered UNIX classics, and old farts won't be happy unless they're installed. Others, such as rogue(6), have more advanced versions available as a port or a package. You don't really need this, unless you want to see what us old farts called "computer games" back in the day.

### miscXX.tgz

This contains dictionary files and typesettable documentation. If this system is intended as a desktop, you probably want these. If it's a server, you probably don't need them.

### xbaseXX.tgz, xfontXX.tgz, ...

X window stuffs

我个人使用，基本上就不安装 game 和 X windows 组建了，想用图形界面，用 Windows 或 Debian/Fedora 之类吧，BSD 还是用来做服务器比较爽。