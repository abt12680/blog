# RN Demo 解析
> 本文主要用于解析，RN Demo的具体代码结构以及各部分的用途

## 项目目录结构如下
```
├── common       
└── pad     
    ├── 3rd 
    ├── __mocks__
    ├── android //android原生代码，由React Native生成，可以进行原生修改
    │   ├── app
    │   ├── gradle
    │   └── keystores
    ├── app // 应用的主要内容部分，主要由React Native规范书写完成，最终转化为原生代码进行运行 
    │   ├── _reducers
    │   ├── common
    │   └── pages
    ├── build
    ├── ios  //ios原生代码，由React Native生成，可以进行原生修改
    │   ├── build
    │   ├── mars.framework
    │   ├── pad
    │   ├── pad-tvOS
    │   ├── pad-tvOSTests
    │   ├── pad.xcodeproj
    │   └── padTests
    ├── localtest //本地测试配置文件
    └── tools //包含工具脚本，例如编译，打包，启动等
```
### ios以及android
整个项目中Pad部分为React Native项目，在React Native项目中，分别包含ios以及android部分代码，分别包含了两个平台下的ReactNative基础项目，其各自由原生代码实现，开发者不必关心其具体代码，但也可以单独设置相关项目内容达到修改目的。

### tools 工具合集

在此文件夹中，npm_cmd.js封装了React Native相关的npm命令，主要使用命令包含一下命令
- npm start 启动node服务器，允许热更新代码进行调试
- npm run ipa -- --build 一键打包ipa，配置好发布内容可以实时发布，比如利用蒲公英网站分发ios应用
- npm run apk -- --build 一键打包apk，同ipa
