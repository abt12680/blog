# GCC编译.a和.so

`
// print_hello.c
#include <stdio.h>

void print_hello()
{
        printf("hello\n");
}
`

`
// print_bye.c
#include <stdio.h>

void print_bye()
{
        printf("bye\n");
}
`

---------- Makefile ----------
all:
        gcc -o print_hello.o -Wall -fPIC -c print_hello.c
        gcc -o print_bye.o -Wall -fPIC -c print_bye.c
        gcc -o libprint.so -shared print_hello.o print_bye.o
        ar cru libprint.a print_hello.o print_bye.o
--------------------------------
