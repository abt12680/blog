# 关于浏览器以及js runtime的一些问题总结

## v8引擎和js runtime什么关系

### V8引擎
V8引擎应该是我们听到最多的引擎，它使用在Chrome浏览器和Node.js中。找到一个解释：A JavaScript engine is a program responsible for translating source code into machine code and executing the translation result on a computer's central processing unit(CPU).

常见的引擎有以下：
* Chrome V8 : Google Chrome中使用的引擎。使用C++实现的。Opera,NodeJS和Couchbase都是使用的它。
* SpiderMonkey: FireFox使用
* Nitro: Safari使用
* Chakra Edge使用

### js runtime
JS Runtime就是运行着JS引擎的环境，它提供接口给开发者调用。有一些我们经常用到的API，比如setTimeout其实都是属于window的，跟V8引擎没有任何关系。因此诸如DOM，Ajax，setTimeout等方法都是由浏览器提供并实现的，这些可以称为Web APIs。

### 浏览器内核
浏览器内核主要分成两部分：渲染引擎和js引擎。渲染引擎主要是负责HTML、CSS以及其他一些东西的渲染，而JS引擎则主要负责对JavaScript的渲染。但是现在JS引擎越来越独立的，基本上所说的内核大多不包含JS引擎了。
|浏览器|内核|js引擎|
|------|------|------|
|IE -> Edge|trident->EdgeHTML|JScript(IE3.0-IE8.0)/Chakra(IE9+之后）|
|Chrome|webkit->blink|V8|
|Safari|webkit|Nitro(4-)|
|Firefox|Gecko|SpiderMonkey(1.0-3.0)/TraceMonkey(3.5-3.6)/JaegerMonkey(4.0-)|
|Opera|Presto->blink|Linear A(4.0-6.1)/Linera B(7.0-9.2)/Carakan(10.5-)|
至于移动端，大部分使用的均为webkit这一套，基本兼容webkit就OK。

## 渲染引擎和JS引擎的关系


## 
