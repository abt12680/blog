# setTimeout和window.onload解析

## 知识准备

### js执行

重要规则：
1. js主线程执行是单线程的，只有当前task执行完后，才能执行下一个。
2. 然而浏览器还有很多其他线程，包括处理Http请求的，键盘输入的各种I/O，均不占用主线程时间，在其就绪时会将其事件添加至主线程的EventQueue中，等待主线程处理。

在浏览器接受到html之后，整个js引擎主要分为两部分，大致如下图所示：
1. 执行页面内的主线程js，构造DOM树
2. 进入EventLoop，处理EventQueue中的Event事件。

这两个块根据我的理解应该基本等于$(document).ready()执行之前与之后。而onload只是第二部分EventLoop的其中一个事件。

![浏览器js执行过程](images/2019_03_04_settimeout_and_onload/js流程.jpeg "js流程.Jpg")

> ##### H5多线程
> 为了利用多核CPU的能力，HTML5提出了Web Worker标准，允许JavaScript脚本创建多个线程，但是线程完全受主线程控制，父子线程通过postMessage()相互传递消息。子线程可以执行任何代码，但不包括直接操作DOM节点，也不能使用window对象的默认方法和属性。然而可以使用大量window对象之下的东西，包括WebSockets,IndexedDB以及FireFox OS专用的Data Store API等数据存储机制。

### EventLoop

顾名思义就是用来处理事件的循环体，在各个语言，设计中均有类似组件。其代码形式一般如下：
```
      while (queue.waitForMessage()) {
        queue.processNextMessage();
      }  
```
EventQueue保存的只有已就绪的事件，比如已到达唤醒时间的setTimeOut，需要响应的Onload事件等。

> 在EventLoop中实际还存在两个队列，macrotask和microtask。本文不做详解，有兴趣自行查阅，可加深理解。

![EventLoop图解](images/2019_03_04_settimeout_and_onload/js_eventloop.jpeg "js执行.Jpg")

## setTimeOut
setTimeout(func, timeout)计时器的主要功能就是在倒计时结束时将func，加入EventQueue中，所以setTimeout(func,0)，并不意味着会立即执行。而且其等待是见取决事件队列中，在该事件之前的事件数量以及各自的执行时间。因此会产生类似下面代码的执行结果。
```
      setTimeout(() => {
        console.log("timeout 2000");
      }, 1000);
      for (var i = 0; i< 1000000000; i++) {

      }
      setTimeout(() => {
        console.log("timeout 0")
      }, 0);

      // =>
      // timeout 2000
      // timeout 0
      // 因为当timeout 0 被加入到EventQueue时，timeout 2000已提前就绪并执行了。
```

## Window.onload

### onload不会立马执行
在浏览器主线程处理机制中，onload事件会在整个页面的图片，css外链资源都被加载渲染完成后，被加入EventQueue中。因此他甚至不是在全部加载后立马执行。比如下面这种情况。

```
      window.onload = function() {
        console.log("onload");
      }
      setTimeout(() => {
        console.log("timeout 0")
      }, 0);
      // =>
      // timeout 0
      // onload
      // 很明显timeout 0更早被加入到EventQueue中
```

### JS执行影响onLoad

由于js主线程是单线程一旦有排在之前的Task时间较长，势必会影响到Onload执行

### img加载时间过长会影响onload执行

下述代码中，如果image.png加载时间过长，导致ajax返回早于onload的执行，很有可能onload就要等所有返回列表里的数据返回才能执行了。
```
    <img src="image.png"/>
    <script>
    window.onload = function() {
      console.log('onload');
    }
    $.ajax({
      url: imgList,
      success: function(arr) {
        arr.forEach(function() {
          $('body').append('<img src="' + arr.imgUrl + '">')
        })
      }
    })
    </script>
```

### window.onload 与 window.addEventListener('load',function() {})

这两个方法均用于注册onload事件的回调，但是会有略微的区别：
1. window.onload使用的是赋值语句，反复赋值，后者会将前者替代，而window.addEventListener则可以不断进行添加，执行顺序同添加顺序
2. 这两个函数可混用，执行顺序为添加顺序
3. window.onload兼容性更好，window.addEventListener不支持低版本以及部分浏览器，使用前最好添加判断

### Hybrid进度条
iOS中判断webview加载完成的webViewDidFinishLoad方法，Android中判断webview加载完成的onPageFinished方法本质触发机制都对应页面上的window.onload，一般来说会稍晚与window.onload（某些特殊情况会早于window.onload，比如页面中有iframe等情况）。
因此，更早的让onload触发，对于用户体验来说可能相对较好。之前遇到的进度条一直不消失的情况，可能不是网页加载慢，而是对应机制引起的。（据说ios11可能不依赖这个了）
