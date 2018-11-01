# OpenSolaris 2009.06 crash course

## 安装系统

下载 ISO，图形化安装，很简单。

* [http://dl.sda1.eu/other-os/opensolaris/osol-0906-x86.iso][1]

## SecureCRT 设置

安装完，就可以 ssh 上去了。

但 $clear 居然不能清屏。改改 terminal 的设置：

![](2018_11_01_opensolaris09_crash_course_image_01.png)

See Solaris Runs~

![](2018_11_01_opensolaris09_crash_course_image_02.png)

## vim & tmux 的基本配置

```
$ cat ~/.vimrc
" basic
set tabstop=2
set nobackup

$ cat ~/.tmux.conf
# hjkl pane traversal
bind h select-pan -L
bind j select-pan -D
bind k select-pan -U
bind l select-pan -R

# reload me
bind r source ~/.tmux.conf\; display "/.tmux.conf sourced!"
```

[1]:http://dl.sda1.eu/other-os/opensolaris/osol-0906-x86.iso
