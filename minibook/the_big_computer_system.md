# THE BIG COMPUTER SYSTEM - A GAME CODER'S VIEW

游戏程序员眼中的计算机体系

```
+------------------------------------------------------+        +--------------+
|                Game / Game Engine(L8)                |        |              |
+------------+------------------------+----------------+        |              |
|   GUI(L4)  |      Network/DB(L5)    |   2D/3D (L6)   |        | Programming  |
+------------+------------------------+----------------+ <===>  |   Languages  |
|       系统API(L2)         |     compiler&linker(L3)  |        |     (L7)     |
+------------------------------------------------------+        |              |
|                    硬件/操作系统(L1)                  |        |              |
+------------------------------------------------------+        +--------------+
```

## Road To the Kernel (L1/L2)

 * CPU Architecture
 * Embedded System Development
 * Kernel Developer

## Compiler & Linker & Debugger (L3)

 * My C Compiler
 * clang / llvm

## Database Demystify (L5)

 * database fundamental
 * transaction
 * sqlite
 * mysql
 * mongodb

## Network and Game Server (L5/L8)

 * TCP/IP Stack
 * Handmade Game Server

## Uncharted Waters - Big Data

 * zookeeper
 * hadoop
 * spark

## Abount Client - 2D/3D Game Engine (L4/L8)

 * 2d game engine
 * 3d game engine
 * UE4
 * asset producting pipeline (model editor / particle editor / world editor)

## Language Zoo 

 * C
 * Go
 * Python


## NOTE

**2018.11.26**

最近在填自己挖的坑《[Road To the Kernel][1]》，和顾QQ吹牛说：

```
从 CPU 到 OS，
从 assembler 到 compiler，
从 filesystem 到 database，
从 TCP/IP stack 到 game server，
最后再到 zookeeper/hadoop/spark。
全部撸一遍，打通整个计算机体系的任督二脉。
```

顾QQ不屑："你丫是个理想主义者。"

就理想一次吧。:-) 索性把"个人技术体系refactoring"的战线扩大。

《The Big Computer System》，我的计算机系统 hack 之路。Just for fun~


[1]:https://github.com/kasicass/blog/blob/master/minibook/road_to_the_kernel.md
