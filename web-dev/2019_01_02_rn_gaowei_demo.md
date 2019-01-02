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
- npm run bd 用于检测脚本是否完整

整个Demo项目运行过程主要有以下几步
1. 修改local.properties 
2. npm install
3. npm start
4. 启动ios或者android项目即可运行dev环境
5. 利用npm run ipa or npm run apk即可打包出对应环境App

有两个编译中遇到的问题，附上解决方案：
1. https://github.com/facebook/react-native/issues/19774#issuecomment-397910801
2. https://github.com/facebook/react-native/issues/19569#issuecomment-422691829

### 主要业务内容以及启动

#### index.js为程序入口
```
require('./index.real');//实际启动index.real.js
```
```

class AppContainer extends Component {
	constructor(props) {
		super(props);
		this.state = {
			isStoreLoading: true,
			store: null,
		};
		bindThis(this, 'codePushStatusDidChange', 'codePushDownloadDidProgress');//绑定代码更新进度
	}

	componentDidMount() {
		console.log('AppContainer componentDidMount');
		this._createStore();
	}

	async _createStore() {
		try {
			console.log('AppContainer _createStore');
			var state = await loadAppState();//检查app状态，版本号等
			this.setState({ store: createAppStore(state) });
			this.setState({ isStoreLoading: false });
		} catch (e) {
			console.log(e, e.stack);
		}
	}

	renderLoading() {
		return (
			<View style={{ flex: 1 }}>
				<Image
					style={{
						flex: 1,
						width: '100%',
						//height: '100%'
					}}
					source={require('./logo.png')}
				/>
				{isRemoteDebugging() && (
					<TouchableHighlight
						onPress={RNExitApp.exitApp}
						style={{
							//height: 48,
							flexDirection: 'row',
							justifyContent: 'flex-end',
							alignItems: 'center',
						}}
					>
						<Text style={{ fontSize: 13 }}></Text>
					</TouchableHighlight>
				)}
			</View>
		);
	}
	render() {
		let isLoading = this.state.isStoreLoading;//若在加载中展示加载图，否则进入app主页
		return isLoading || devTest.testStartLoading ? (
			this.renderLoading()
		) : (
			<Provider store={this.state.store}>
				<App />
			</Provider>
		);
	}

	key = '@update';
	codePushStatusDidChange(status) {//定义代码更新判断的各个状态
		switch (status) {
		case codePush.SyncStatus.CHECKING_FOR_UPDATE:
			console.log('Checking for updates.');

			break;
		case codePush.SyncStatus.DOWNLOADING_PACKAGE:
			console.log('Downloading package.');
			this.state.store.dispatch(NavigationActions.navigate({
				key: this.key,
				routeName: 'UpdateDialog',
				params: {
					deploymentKey: codePushKey.pro,
				},
			}));
			break;
		case codePush.SyncStatus.INSTALLING_UPDATE:
			console.log('Installing update.');
			break;
		case codePush.SyncStatus.UP_TO_DATE:
			console.log('Up-to-date.');
			break;
		case codePush.SyncStatus.UPDATE_INSTALLED:
			console.log('Update installed.');
			break;
		}
	}

	codePushDownloadDidProgress(progress) {
		console.log(progress.receivedBytes + ' of ' + progress.totalBytes + ' received.');
		this.state.store.dispatch(NavigationActions.setParams({ key: this.key, params: { progress } }));
	}
}

//忽略chrome调试时页面切到后台时的报警
console.ignoredYellowBox = ['Remote debugger'];
YellowBox.ignoreWarnings([
	'Warning: componentWillUpdate is deprecated',
	'Warning: componentWillMount is deprecated',
	'Warning: componentWillReceiveProps is deprecated',
	'Class RCTCxxModule',
	'Module RCTImageLoader requires',
	'Module XLogBridge requires',
	'[SECURITY] node-uuid',
	'socketDidDisconnect',
	'Sending `error` with no listeners',
	'RCTBridge required',
]);

console.log('---------loading app----------');//开始加载app，并调用代码推送检测
AppRegistry.registerComponent('pad', () =>
	codePush({
		deploymentKey: codePushKey.pro,
		checkFrequency: codePush.CheckFrequency.ON_APP_RESUME,
		installMode: codePush.InstallMode.IMMEDIATE,
		updateDialog: {
			appendReleaseDescription: true,
			descriptionPrefix: '',
			optionalIgnoreButtonLabel: '忽略',
			optionalInstallButtonLabel: '安装',
			optionalUpdateMessage: '新版本描述：',
			title: '发现更新',
		},
	})(AppContainer));

//////////////////////////////////////////

import { setJSExceptionHandler, setNativeExceptionHandler } from 'react-native-exception-handler';
import { addReport } from './app/report';

var isCatching = false;
setJSExceptionHandler((e, isFatal) => {
	let stack = e && e.stack;
	console.log('JSException', e, 'END', stack);
	addReport({ type: 'JSError', ...e, stack });
	if (isCatching) return;
	if (isFatal) {
		isCatching = true;
		Alert.alert('发生了错误', `isFatal: ${isFatal ? 'yes' : 'no'}\n${e.name}\n${e.message}\n\n`, [
			{ text: '重启', onPress: () => codePush.restartApp(false) },
			{
				text: '忽略',
				onPress: () => {
					isCatching = false;
				},
			},
		]);
	}
});

setNativeExceptionHandler(exception => {
	console.log('NativeException', exception);
	addReport({ type: 'NativeException', exception });
});
```
