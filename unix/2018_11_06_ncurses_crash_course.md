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

### 1.2 man page

ncurses 的 man page 在 debian 下没找到。OpenBSD 下直接：

```
$ man ncurses
...
   Routine Name Index
       The following table lists each curses routine and the name of the
       manual page on which it is described.  Routines flagged with `*' are
       ncurses-specific, not described by XPG4 or present in SVr4.

                     curses Routine Name     Manual Page Name
                     ===========================================
                     chgat                   curs_attr(3)
                     clear                   curs_clear(3)
                     clearok                 curs_outopts(3)
...
```

函数 initscr, clear 等等的 man page，需要加上 curs_ 前缀：

```
$ man curs_clear
...
DESCRIPTION
       The erase and werase routines copy blanks to every position in the
       window, clearing the screen.

       The clear and wclear routines are like erase and werase, but they also
       call clearok, so that the screen is cleared completely on the next call
       to wrefresh for that window and repainted from scratch.
...
```
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
//! src: hello_world.c
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
//! src: init_func_example.c
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
//! src: printw_example.c
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


## 7. Input functions

* getch()，等待输入 a character
* scanw() / mvscanw()，和 scanf() 类似
* wscanw() / mvwscanw()，针对 windows 的 scanw()
* vwscanw()，和 vscanf() 类似
* getstr()，等待输入 a line of string

看代码，一目了然：

```C
#include <ncurses.h>
#include <string.h>

//! mode: exe
//! int: obj
//! flag: -Wall
//! link: ncurses
//! src: scanw_example.c
int main()
{
    char mesg[]  = "Enter a string: ";
    char mesg1[] = "Enter a int: ";
    char str[80];
    int row, col;
    int v;

    initscr();

    // getstr()
    getmaxyx(stdscr, row, col);
    mvprintw(row/2, (col-strlen(mesg))/2, "%s", mesg);

    getstr(str);
    mvprintw(LINES-2, 0, "You Entered: %s", str);
    getch();

    // sacnw()
    clear();
    getmaxyx(stdscr, row, col);
    mvprintw(row/2, (col-strlen(mesg))/2, "%s", mesg1);

    scanw("%d", &v);
    mvprintw(LINES-2, 0, "You Entered: %d", v); 
    getch();

    endwin();
    return 0;
}
```


## 8. Attributes

 * attron() / attroff(), 开/关某个显示属性
 * attrset(), 设置显示属性（覆盖之前的）
 * attr_ 开头系列函数，通过 attr_t 来操作属性。

```
int attr_get(attr_t *attrs, short *pair, void *opts);
int attr_off(attr_t attrs, void *opts);
...
```

属性列表

```
    A_NORMAL        Normal display (no highlight)
    A_STANDOUT      Best highlighting mode of the terminal.
    A_UNDERLINE     Underlining
    A_REVERSE       Reverse video
    A_BLINK         Blinking
    A_DIM           Half bright
    A_BOLD          Extra bright or bold
    A_PROTECT       Protected mode
    A_INVIS         Invisible or blank mode
    A_ALTCHARSET    Alternate character set
    A_CHARTEXT      Bit-mask to extract a character
    COLOR_PAIR(n)   Color-pair number n 
```

设置方式

```C
	attron(A_REVERSE | A_BLINK);
```

### 8.1 attron() / attroff() 例子

将"/* */"之间的内容加粗。

```C
/* http://www.tldp.org/HOWTO/NCURSES-Programming-HOWTO/attrib.html */
#include <ncurses.h>
#include <stdlib.h>

//! mode: exe
//! int: obj
//! flag: -Wall, -Wno-unused-but-set-variable
//! link: ncurses
//! src: simple_attr.c
int main(int argc, char* argv[])
{
    int ch, prev, row, col;
    FILE *fp;
    int y, x;

    if (argc != 2)
    {
        printf("Usage: %s <a c file name>\n", argv[0]);
        exit(1);
    }

    fp = fopen(argv[1], "r");
    if (fp == NULL)
    {
        perror("Can't open input file");
        exit(1);
    }

    prev = EOF;
    initscr();
    getmaxyx(stdscr, row, col);

    while ((ch = fgetc(fp)) != EOF)
    {
        getyx(stdscr, y, x);          // get the current cursor position
        if (y == (row - 1))           // are we at the end of the screen
        {
            printw("<-Press Any Key->");
            getch();
            clear();
            move(0, 0);
        }

        if (prev == '/' && ch == '*') // If it is /* then only switch bold on
        {
            attron(A_BOLD);
            getyx(stdscr, y, x);
            move(y, x - 1);           // back up one space
            printw("%c%c", '/', ch);
        }
        else
        {
            printw("%c", ch);
        }

        refresh();

        if (prev == '*' && ch == '/')
        {
            attroff(A_BOLD);         // bold off
        }

        prev = ch;
    }
    endwin();
    fclose(fp);

    return 0;
}
```

SecureCRT 中，需要设置 ANSI Color off，才能看到 bold 效果。

![](2018_11_06_ncurses_crash_course_image_02.png)

看看效果。

```
$ emake simple_attr.c
$ ./simple_attr simple_attr.c
```

![](2018_11_06_ncurses_crash_course_image_01.png)

### 8.2 chgat() functions

chgat() 用于单独设置几个 characters 的属性。

第一个参数 -1，表示从当前位置到本行结束。

```C
chgat(-1, A_REVERSE, 0, NULL);
```

看看具体例子：

```C
#include <ncurses.h>

//! mode: exe
//! int: obj
//! flag: -Wall
//! link: ncurses
//! src: with_chgat.c
int main(void)
{
    initscr();
    start_color();     // start color functionality

    init_pair(1, COLOR_CYAN, COLOR_BLACK);
    printw("A Big string which i didn't care to type fully");
    mvchgat(0, 0, -1, A_BLINK, 1, NULL);
    // First two parameters specify the position at which to start
    // Third parameter number of characters to update. -1 means till
    //   end of line
    // Forth parameter is the normal attribute you wanted to give
    //   to the character
    // Fifth is the color index. It is the index given during init_pair()
    //   use 0 if you didn't want color
    // Sixth one is always NULL

    refresh();
    getch();
    endwin();

    return 0;
}
```

[1]:http://www.tldp.org/HOWTO/NCURSES-Programming-HOWTO/index.html
[2]:https://github.com/kasicass/kasicass/tree/master/ncurses
[3]:https://github.com/skywind3000/emake
[4]:http://www.openbsd.org/64.html
[5]:https://www.debian.org/
[6]:http://www.tldp.org/HOWTO/NCURSES-Programming-HOWTO/ncurses_programs.tar.gz
[7]:https://www.gnu.org/software/make/manual/make.html
