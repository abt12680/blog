# NCURSES Crash Course

学了下 ncurses，总结之。

 * 教程原文，[http://www.tldp.org/HOWTO/NCURSES-Programming-HOWTO/index.html][1]
 * 代码实现，[https://github.com/kasicass/kasicass/tree/master/ncurses][2]
 * emake，[https://github.com/skywind3000/emake][3]
 * 所有练习，在 [Debian 9.5][5]、[OpenBSD 6.4][4] 下测试通过


## 1. Introduction

很久很久以前，没有漂亮的显示器，只有终端（terminal）。

SVR4(System V Release 4.0) 的程序员们，发明了在 terminal 上作画的 API --  CURSES。

GNU 出现了，因为 SVR4 要钱嘛，所以，重写一遍罗。就有了 NCURSES。

### 1.1 安装开发环境

Debian 9.5

```
# aptitude install ncurses-dev
```

OpenBSD 6.4 自带 ncurses 库，不需要安装。

### 1.2 示例代码

原文代码

 * [http://www.tldp.org/HOWTO/NCURSES-Programming-HOWTO/ncurses_programs.tar.gz][6]
 * 使用 [Makefile][7]

我的代码

 * [https://github.com/kasicass/kasicass/tree/master/ncurses][2]
 * 使用 [emake][3]

代码目录结构

```
ncurses
   |
   |----> JustForFun     -- just for fun programs
   |----> basics         -- basic programs
   |----> demo           -- output files go into this directory after make
   |          |
   |          |----> exe -- exe files of all example programs
   |----> forms          -- programs related to form library
   |----> menus          -- programs related to menus library
   |----> panels         -- programs related to panels library
   |----> perl           -- perl equivalents of the examples (contributed
   |                            by Anuradha Ratnaweera)
   |----> Makefile       -- the top level Makefile
   |----> README         -- the top level README file. contains instructions
   |----> COPYING        -- copyright notice
```

## 2. Hello World

 * initscr() / endwin()，初始化/释放
 * refresh()，刷新屏幕(stdscr)
 * printw()，类似 printf，内容输出到 stdscr

```C
#include <curses.h>

//! mode: exe
//! int: obj
//! flag: -Wall
//! link: ncurses
//! src: 01-hello.c
int main(void)
{
	initscr();                // Start curses mode
	printw("Hello World!");   // Print Hello World
	refresh();                // Print it on the real screen
	getch();                  // Wait for user input
    endwin();                 // End curses mode

	return 0;
}
```

## 3. The Gory Details

nothing~

## 4. Initialization

raw() / cbreak()

 * raw()，raw mode，任意键按下，都直接接收到
 * cbreak()，ctrl + break mode，会收到 CTRL+Z / CTRL+C

echo() / noecho()

 * echo() / noecho()，是否开启 echo

keypad()

 * keypad()，是否启用 F1, F2 ...

halfdelay()

 * halfdelay()，等待 0.X 秒后，结束输入。密码框可以用这个设定

看例子

```C
#include <curses.h>

//! mode: exe
//! int: obj
//! flag: -Wall
//! link: ncurses
//! src: 02-init.c
int main(void)
{
	int ch;

	initscr();                     // Start curses mode
	raw();                         // Line buffering disabled
	keypad(stdscr, TRUE);          // We get F1, F2 etc..
	noecho();                      // Don't echo() while we do getch

	printw("Type any character to see it in bold\n");
	ch = getch();                  // If raw() hadn't been called
                                   // we have to press enter before it
                                   // gets to the program

	if (ch == KEY_F(1))            // Without keypad enabled this will
	{                              //   not get to us either
		printw("F1 Key pressed");  // Without noecho() some ugly escape
	}                              // characters might have been printed
	else                           // on screen
	{
		printw("The press key is ");
		attron(A_BOLD);
		printw("%c", ch);
		attroff(A_BOLD);
	}

	refresh();                // Print it on the real screen
	getch();                  // Wait for user input
    endwin();                 // End curses mode

	return 0;
}
```

## 5. A Word about Windows

stdscr 是 defualt window / 全屏

输出到 stdscr：

```C
printw("Hi There !!!");
refresh();
```

输出到某个 window：

```C
wprintw(win, "Hi There !!!");
wrefresh(win);
```

```C
/* Print on stdscr at present cursor position */
printw(string);

/* Move to (y, x) then print string */
mvprintw(y, x, string);

/* Print on window win at present cursor position in the window */
wprintw(win, string);  

/* Move to (y, x) relative to window co-ordinates and then print */
mvwprintw(win, y, x, string);   
```


## 6. Output functions

* addch(), Print single character with attributes
* printw(), Print formatted output similar to printf()
* addstr(), Print strings

### 6.1 addch()

向 stdscr 输出单个字符，带属性，例如：

```
addch(ch | A_BOLD | A_UNDERLINE);
```

### mvaddch(), waddch() and mvwaddch()

```
move(row,col);
addch(ch);
```

等价于

```
mvaddch(row,col,ch);
```

waddch() / mvwaddch() 则是针对 window 的操作。

### 6.2 printw()

 * printw() / mvprintw()，对 stdscr 操作
 * wprintw() / mvwprintw()，对 window 操作
 * vwprintw()，对 window 操作，类似 vprintf

例子，显示 stdscr 的 row & col：

```C
#include <curses.h>
#include <string.h>

//! mode: exe
//! int: obj
//! flag: -Wall
//! link: ncurses
//! src: 03-printw.c
int main(void)
{
	char mesg[] = "Just a string";
	int row, col;

	initscr();
	getmaxyx(stdscr, row, col);
	mvprintw(row/2, (col-strlen(mesg))/2, "%s", mesg);
	mvprintw(row-2,0,"This screen has %d rows and %d columes\n", row, col);

	printw("Try resizeing your window(if possible) and then run this program again");
	refresh();
	getch();
	endwin();

	return 0;
}
```

getmaxyx() 中 row, col 并没有传入指针，如何获得数据的？看 curses.h 这里：

```
#define getmaxyx(win,y,x)   (y = getmaxy(win), x = getmaxx(win))
```

### 6.3 addstr()

类似 puts()

 * addstr() / mvaddstr()，对 stdscr 操作
 * waddstr() / mvwaddstr()，对 window 操作




[1]:http://www.tldp.org/HOWTO/NCURSES-Programming-HOWTO/index.html
[2]:https://github.com/kasicass/kasicass/tree/master/ncurses
[3]:https://github.com/skywind3000/emake
[4]:http://www.openbsd.org/64.html
[5]:https://www.debian.org/
[6]:http://www.tldp.org/HOWTO/NCURSES-Programming-HOWTO/ncurses_programs.tar.gz
[7]:https://www.gnu.org/software/make/manual/make.html
