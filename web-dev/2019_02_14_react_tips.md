# 关于初学React的一些tips总结

## Name your components
当你需要查找是哪个Component引起的bug时，Component拥有一个名字就会变得很重要。
```
// Avoid thoses notations
export default () => {};
export default calss extends React.Component {};
```

React支持自定义Component名称
```
export const Component = () => 
    <h1>I'm a component </h1>;
export default Component;

// Define user custom component name

Component.displayName = "My Component';
```

ESLint rules建议
```
"rules": {
    // check named import exists
    "import/named": 2,

    // Set to "on" in airbnb preset
    "import/prefer-default-export": "off"
}
```

## Prefer functional components
当你的Component只有展示数据作用时，使用functional component相比于 class component代码更加简洁，也更加高效。同时仍然能够正常使用props等参数。

```
class Watch extends React.Component {
    render() {
        return <div>{this.props.hours}:{this.props.minutes}</div>
    }
}

// Equivalent functional component
const Watch = (props) => <div>{props.hours}:{props.minutes}</div>;
```

## Replace divs with fragments
由于任何一个Component在render时必须包含一个唯一的root节点，为了符合这条规则，我们一般会在最外层加一层<div>标签。在React 16中引入了一个新特性Fragments。用这个作为更节点包裹在output中不会包含任何wrapper。

```
const Login = () => 
    <div><input name="login"/><input name="password"/><div>

const Login = () =>
    <React.Fragment><input name="login"/><input name="password"/></React.Fragment>;

const Login = () = // Short-hand syntax
    <><input name="login"/><input name="password"/></>;
```

## Be careful while setting state
在某些情况，在setState的时候可能需要使用之前的state数据，这时候不要直接读取this.state，因为setState是异步函数，在这个时间内state可能已经产生变化。

```
// Very bad pratice: do not use this.state and this.props in setState !
this.setState({ answered: !this.state.answered, answer});

// With quite big states: the tempatation becomes bigger
// Here keep the current state and add answer property
this.setState({ ...this.state, answer });
```
应该采用提供的function parameter来正确利用原来的数据,props也是一样
```
// Note the () notation around the object which makes the JS engine
// evaluate as an expression and not as the arrow function block
this.setState((prevState, props) 
    => ({ ...prevState, answer}));
```

## Binding component functions
有很多方法可以给当前component绑定事件，类似以下这样的
```
class DatePicker extends React.Component {
    handleDateSelected({target}) {
        // Do stuff
    }
    
    render() {
        return <input type="date" onChange={this.handleDateSelected}/>
    }
}
```
但是他却并不能正常工作，因为当你使用JSX时，this并没有绑定到当前的component instance上，以下有几种方式可以让上面的代码正常工作。

```
// #1: use an arrow function
<input type="date" onChange={(event) => this.handleDateSelected(event)}/>

// OR #2: bind this to the function in component constructor
constructor() {
    this.handleDateSelected = this.handleDateSelected.bind(this);
}

// OR #3: declare the function as a class field (arrow function syntax)
handleDateSelected = ({target}) => {
    // Do stuff
}
```
这里不推荐使用第一种方法，第一种方法会导致代码在每一次rerender是重新created，会影响渲染性能。
第三种方法的使用需要Babel的支持，需要利用Babel转化代码，否则代码不能正常运行。

## Adopt container pattern (even with Redux)
the container design pattern。希望你将React Component尽可能的进行分离(follow the separation of concerns principle)。

```
export class DatePicker extends React.Component {
    state = { currentDate: null };
    
    handleDateSelected = ({target}) => 
        this.setState({ currentDate: target.value });

    render = () =>
        <input type="date" onChange={this.handleDateSelected}/>
```
一个Component既处理了rendering又处理了user action，这里可以把他们拆成两个Components
```
const DatePicker = (props) => 
    <input type="date" onChange={props.handleDateSelected}/>

export class DatePickerController extends React.Component {
    // ... No changes except render function ...
    render = () => 
        <DatePicker handleDateSelected={this.handleDateSelected}/>
```

## Fix props drilling
在书写页面是总是会出现很多孙子Component需要用到主Component的一些props，但是这明显不能直接获取。有两个方法：
1. 将他们包含在一个Container里面进行管理（wrapping the dumb component in a container
2. 从父容器一层层传递props

第二种方案往往会传递不是所有子容器都需要的props下去
```
const Page = props => <UserDetails fullName="John Doe"/>

const UserDetails = props => 
    <section>
        <h1>User details</h1>
        <CustomInput value={props.fullName}/> //<= No need fullName but pass it down
    </section>

const inputStyle = {
    height: '30px',
    width: '200px',
    fontSize: '19px',
    border: 'none',
    borderBottom: '1px solid black'
};
const CustomInput = props => // v Finally use fullName value from Page component
    <input style={inputStyle} type="text" defaultVlue={props.value}/>
```
这种现象叫做props drilling，以下有一些解决方案主要利用了[Context API](https://reactjs.org/docs/context.html#before-you-use-context)中的children prop 和 render prop

```
// #1: Use children prop
const UserDetailsWithChildren = props =>
    <section>
        <h1>User details (with children)</h1>
        {props.children /* <= use children */}
    </section>;

// #2: Render prop pattern
const UserDetailsWithRenderProp = props => 
    <section>
        <h1>User details (with render prop)</h1>
        <props.renderFullName() /* <= use passed render function */}
    </section>;

const Page = () => 
    <React.Fragment>
        {/* #1: children prop */}
        <UserDetailsWithChildren>
            <CustomInput value="John Doe"/> {/* Define props.children */}
        </UserDetailsWithChildren>

        {/* #2: Render prop pattern */}
        {/* Remember: passing arrow functions is a bad pratice, make it a method of Page class instead */}
        <UserDetailsWithRenderProp renderFullName={() => <CustomInput value="John Doe"/>}/>
    </React.Fragment>;
```
这样的解决方案看起来简单的多，children看起来是更好的解决方案，因为在render method中他也能很好的运行。这样后再深的内联Component也可以解决了。

```
const Page = () =>
    <PageContent>
        <RightSection>
            <BoxContent>
                <UserDetailsWithChildren>
                    <CustomInput value="John Doe"/>
                </UserDetailsWithChildren>
            </BoxContent>
        </RightSection>
    </PageContent>
```

还有第三种解决思路，是利用experimental context API
```
const UserFullNameContext = React.createContext('userFullName');

const Page = () => 
    <UserFullNameContext.Provider value="John Doe"> {/* Fill context with value */}
        <UserDetailsWithContext/>
    </UserFullNameContext.Provider>

const UserDetailsWithContext = () => // No props to provide
    <section>
        <h1>User details (with context)</h1>
        <UserFullNameContext.Consumer> {/* Get Context value */}
            { fullName => <CustomInput value={fullName}/>
        </UserFullNameContext.Consumer>
    </section>;
```
不推荐使用这种方法，其相当于存储在了全局变量中。


## 待补充
