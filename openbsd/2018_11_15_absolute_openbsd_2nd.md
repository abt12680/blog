# Absolute OpenBSD 2nd

## 05 - The Boot Process

### single-user mode

进入 single-user mode
boot> boot -s

single-user mode 默认只挂载了 /

磁盘检查
```
# fsck -p
...
```

挂载所有磁盘
```
# mount -a
```

启动网络
```
# sh /etc/netstart
```

----------------------------

启动时，运行自己的脚本，修改 rc.local
xxx_cmd && echo -n ' xxx'         # 运行 xxx_cmd 并在屏幕上输出 xxx，配合 starting local daemons: xxx
sudo -u myname xxx_cmd            # 权限降级为 myname 来运行 xxx_cmd

