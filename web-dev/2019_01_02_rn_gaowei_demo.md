# RN Demo 解析
> 本文主要用于解析，RN Demo的具体代码结构以及各部分的用途

## 项目目录结构如下
```
├── common       
└── pad     
    ├── 3rd 
    │   ├── react-native-device-info
    │   ├── react-native-exception-handler
    │   └── react-native-xlog
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
    │   ├── drawable-hdpi
    │   ├── drawable-mdpi
    │   ├── drawable-xhdpi
    │   ├── drawable-xxhdpi
    │   └── drawable-xxxhdpi
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
