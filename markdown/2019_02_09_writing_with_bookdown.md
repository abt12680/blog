# Bookdown - Writing Book with R Markdown

## 起源

在找用 markdown 写书的工具，无意中发现 bookdown。

 * [https://bookdown.org/][2]

而且作者 Yihui Xie 还是国人

 * 个人blog，[http://yihui.name][1]
 * 在 RStudio 工作，[http://www.rstudio.com][2]
 * 一看就是统计学大神，膜拜下~


## R Markdown 是啥？

简单说，就是 LaTeX 用烦了，新设计了一种纯文本结构（R Markdown），把 R + Markdown + Pandoc 揉合在了一起，然后写了一推工具，可以导出 PDF、HTML、ePub 等等格式。

 * R，统计学专用语言，[https://www.r-project.org/][6]
 * Markdown
 * Pandoc，各种格式互相转换，[http://pandoc.org/][7]


## bookdown 是啥？

看这里《[bookdown: Authoring Books and Technical Documents with R Markdown][5]》

    In short, you just prepare a few R Markdown book chapters, and
    bookdown can help you turn them into a beautiful book.


## bookdown 实战

### 安装 R

去任意 CRAN (the Comprehensive R Archive Network)镜像 下载 R 的安装包。

 * 比如，[https://cran.rstudio.com/bin/windows/base/R-3.5.2-win.exe][8]

启动 R，然后安装 bookdown package：

 * 注意，让选择 CRAN mirror 的时候，要选 shanghai。
 * =_=! guangzhou mirror 没有 bookdown package。oooh, sucks~

```
install.packages("bookdown", dependencies = TRUE)
```

ps. 后来发现，直接用 RStudio IDE 就好，上面这一段忽略。=_=!

### Quick Start

 1. 下载 demo，[https://github.com/rstudio/bookdown-demo][12]
 2. 下载 RStudio IDE，[https://www.rstudio.com/products/rstudio/download/][13]
 3. 安装 bookdown package，"install.packages("bookdown", dependencies = TRUE)"
 4. 用 RStudio IDE 打开 bookdown-demo/bookdown-demo.Rproj
 5. 打开 index.Rmd，然后 Build => Build Book

接下来，读 bookdown-demo 内容就好。

### 原理

简单说，R Markdown 就是一套复杂的 template generator 系统。和 django、jsp、asp.net 等各种 html 模板生成系统没啥本质不同。所谓的 knitr，就是 template 里面嵌套代码。

然后 RStudio IDE 提供了一整套"所见即所得"的编辑环境，配合上 R 这种统计语言，确实是技术死宅写 book & paper 的利器。

 * knitr，[https://yihui.name/knitr/][9]
 * Pandoc，[http://pandoc.org/][7]

R Markdown Cheat Sheet，下载

 * [https://www.rstudio.com/resources/cheatsheets/][11]
 * [https://github.com/rstudio/cheatsheets/raw/master/rmarkdown-2.0.pdf][10]
 * R Studio 做的 Cheat Sheet 好漂亮，Orz

![](2019_02_09_writing_with_bookdown/rmarkdown_cheat_sheet.png)


## 另类发现 - gitbook

快速创建文档的好帮手。

 * [https://www.gitbook.com/][4]


[1]:https://yihui.name/
[2]:https://bookdown.org/
[3]:http://www.rstudio.com
[4]:https://www.gitbook.com/?t=10
[5]:https://bookdown.org/yihui/bookdown/
[6]:https://www.r-project.org/
[7]:http://pandoc.org/
[8]:https://cran.rstudio.com/bin/windows/base/R-3.5.2-win.exe
[9]:https://yihui.name/knitr/
[10]:https://github.com/rstudio/cheatsheets/raw/master/rmarkdown-2.0.pdf
[11]:https://www.rstudio.com/resources/cheatsheets/
[12]:https://github.com/rstudio/bookdown-demo
[13]:https://www.rstudio.com/products/rstudio/download/
