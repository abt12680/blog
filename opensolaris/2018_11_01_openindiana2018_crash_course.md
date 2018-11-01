# OpenIndiana 2018.10 Crash Course

## 安装系统

下载 ISO，图形化安装，很简单。

* [http://dlc.openindiana.org/isos/hipster/latest/OI-hipster-text-20181023.iso][1]

## SecureCRT 设置

安装完，就可以 ssh 上去了。

但 $clear 居然不能清屏。改改 terminal 的设置：

![](2018_11_01_openindiana2018_crash_course_image_01.png)

See Solaris Runs~

![](2018_11_01_openindiana2018_crash_course_image_02.png)


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


[1]:http://dlc.openindiana.org/isos/hipster/latest/OI-hipster-text-20181023.iso
[2]:https://www.openindiana.org/packages/
