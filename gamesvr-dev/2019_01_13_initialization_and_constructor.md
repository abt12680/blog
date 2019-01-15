&emsp;&emsp;项目中对需要持久化的状态数据的class以及class所有成员变量用到的class（递归下去的每一个class）的定义有一个要求，必须要写一个空的默认构造函数。

&emsp;&emsp;这个规定的来源是对数据恢复流程的一次修改引出的。

```
new (pDescTmp) DESCCLASSNAMENOC
```
&emsp;&emsp;修改为
```
new (pDescTmp) DESCCLASSNAMENOC()
```
&emsp;&emsp;这个修改导致没有写默认构造函数的class的数据，在resume的时候全部被清空了。当时用GDP跟踪调试跟在stack overfolw上查到的结果都显示，编译器在下面那句代码执行合成的默认构造函数时，插入了memset，将class的内容清零，而对于有user-defined的默认构造函数则不会插入memset。

&emsp;&emsp;第一次听到这个规定跟由来的时候没有太注意，最近解决其他问题的时候突然想到这个，所有的书都写着空默认构造函数跟自动合成的默认构造函数执行效果一致(it has exactly the same effect as a user-defined constructor with empty body and empty initializer list)。为何这种调用会有如此大的差别？

&emsp;&emsp;去翻了翻cppreference网站，才发现原来变量在构造过程中并不是单单调用Constructor来对class提供初始值，而是通过Initialization来提供初始值，而如果对Constructor进行调用是由Initialization的规定来进行的。

```
T()
new T ()
```
&emsp;&emsp;上面这两者是value initialization，而
```
new T
```
是default initialization。


&emsp;&emsp;按照标准value initialization会对所有类型为class/array 的成员变量递归执行value initialization，而对于基础类型执行zero initialization，然后调用默认构造函数。而default initialization会直接调用默认构造函数。

&emsp;&emsp;虽然标准里没有对palcement new执行时的initialization方式作出规定，但是gcc实现时应该是参考了new operator的规定。

