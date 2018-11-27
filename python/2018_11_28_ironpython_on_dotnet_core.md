# IronPython on .NET Core

.NET Core 已经出到 2.1 了，好久没玩 .NET 了，试试看 IronPython 在 debian9 上性能如何。


## 软件安装

.NET Core 的安装，已经超级方便了。

 * [https://dotnet.microsoft.com/learn/dotnet/hello-world-tutorial][1]

安装 IronPython，参考 [这里][2]：

```
$ dotnet new console -o myApp
$ cd myApp

$ dotnet add package IronPython.Interpreter --version 2.7.4
```

装完后，死活找不到 ipy 在哪。=_=! 无法，还得好好研究下 NuGet。


## NuGet

 * [https://www.nuget.org/][4]
 * [https://docs.microsoft.com/zh-cn/nuget/what-is-nuget][3]

package 的制作/发布流程：

![](2018_11_28_ironpython_on_dotnet_core_image_01.png)


### 使用 package

```
$ dotnet new console -o myhello
$ cd myhello
$ dotnet add package Newtonsoft.Json
```

写个测试代码

```C#
using System;
using Newtonsoft.Json;

public class Account
{
    public string Name { get; set; }
    public string Email { get; set; }
    public DateTime DOB { get; set; }
}

namespace myhello
{
    class Program
    {   
        static void Main(string[] args)
        {   
            Account account = new Account
            {   
                Name  = "John",
                Email = "john@nuget.org",
                DOB   = new DateTime(1980, 2, 20, 0, 0, 0, DateTimeKind.Utc),
            };  

            string json = JsonConvert.SerializeObject(account, Formatting.Indented);
            Console.WriteLine(json);
        }   
    }   
}
```

运行结果

```
$ dotnet run
{
  "Name": "John",
  "Email": "john@nuget.org",
  "DOB": "1980-02-20T00:00:00Z"
}
```

# IronPython build from source

好像研究错方向了，改研究 IronPython 的[文档][5]。

```
$ wget https://github.com/PowerShell/PowerShell/releases/download/v6.1.1/powershell_6.1.1-1.debian.9_amd64.deb
# dpkg -i powershell_6.1.1-1.debian.9_amd64.deb

$ git clone --recursive https://github.com/IronLanguages/ironpython2
$ cd ironpython2
$ pwsh
> ./make.ps1
blab... blab...
```

还是各种出错。放弃。


[1]:https://dotnet.microsoft.com/learn/dotnet/hello-world-tutorial
[2]:https://www.nuget.org/packages/IronPython/
[3]:https://docs.microsoft.com/zh-cn/nuget/what-is-nuget
[4]:https://www.nuget.org/
[5]:https://github.com/IronLanguages/ironpython2/blob/master/Documentation/building.md
