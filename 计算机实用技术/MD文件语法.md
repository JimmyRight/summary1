#用markdown写下你的第一个md文档

对应编写网页所用HTML（超文本标记语言，Hyper Text Markup Language）中的markup？

---

#markdown 是什么？

同样是标记语言，但它相比HTML更加简单！一是体现在标记符的数量上，二是体现在标记符的书写上。
HTML标记符号非常多，并且需要标记内容的开始和结束位置，而markdown只有四个基本的标记符号，只要在开始位置标记即可。

---
#markdown 解决什么问题？

当我们需要让文档看起来层次分明，但又不依赖于word这样的编辑工具来书写、排版和读取时，markdown的易写易读优势就非常突出了。并且在我使用一段时间以后，发现使用markdown非常有助于帮助作者在写作时整理自己的逻辑思路和段落层次。

---
#怎样书写和读取 markdown？

同HTML一样，你可以使用任何一款纯文本编辑工具来编辑和读取包含markdown格式的文本，但只有在一些特别的工具（如有道云笔记、MarkDownPAD）或网站（如简书）下，才能呈现出渲染后的格式。

同时markdown也可以使用HTML来添加格式和排版，这意味着，你即可以使用标准的markdown语法，也可以在其中嵌入HTML标记，但也只能对应其中的一小部分。

Markdown支持嵌入html标签。

---

#markdown 的语法

##基本符号：* - + >

基本上所有的markdown标记都是基于这四个符号及其组合，需要注意的是，如果以基本符号开头的标记，注意基本符号后分割内容的空格。
Markdown使用#、+、*等符号来标记， 符号后面必须跟上 至少1个 空格才有效！

##标题
Markdown 标题支持两种形式:

1、用#标记
在 标题开头 加上1~6个#，依次代表一级标题、二级标题....六级标题

    一级标题 # 一级标题
    二级标题 ## 二级标题
    三级标题 ### 三级标题
    四级标题 #### 四级标题
    五级标题 ##### 五级标题
    六级标题 ###### 六级标题

2、用=和-标记

在 标题底下 加上任意个=代表一级标题，-代表二级标题

	一级标题
	======
	
	二级标题
	----------

##引用

引用以>来表示，引用中支持多级引用、标题、列表、代码块、分割线等常规语法。

引用的方式：> 引用内容

	> 这是一段引用    //在`>`后面有 1 个空格
	> 
	>     这是引用的代码块形式    //在`>`后面有 5 个空格
	>     
	> 代码例子：
	>   
	    protected void onCreate(Bundle savedInstanceState) {
	        super.onCreate(savedInstanceState);
	        setContentView(R.layout.activity_main);
	    }
	
	> 一级引用
	> > 二级引用
	> > > 三级引用
	
	> #### 这是一个四级标题
	> 
	> 1. 这是第一行列表项
	> 2. 这是第二行列表项

##强调

两个\*或\-代表加粗，一个*或-代表斜体，~~代表删除。

	**加粗文本** 或者 __加粗文本__
	
	*斜体文本*  或者_斜体文本_
	
	~~删除文本~~

##段落

段落以自然 回车 作为标记。

加一个空行表示换行   
在行尾添加两个空格加回车表示换行：

	这是一行后面加两个空格  换行

	

##分隔符

在一行中用三个以上的*、-、_来建立一个分隔线，行内不能有其他东西。也可以在符号间插入空格。

	***
	---
	___
	
	* * *

##列表

Markdown 支持有序列表和无序列表。

使用* - +中的任何一个符号加空格就可以创建无序列表，可以进一步使用+ -来表现层次关系。

使用数字+点+空格创建有序列表

列表可以嵌套，使用时在嵌套列表前空格，这篇文章的列表使用了嵌套列表。

	* 这是一个无序列表
	* 这是一个无序列表

	+ 这是一个父无序列表
	  - 这是一个子无序列表

有序列表则使用数字加英文句点.和·来表示

	1. 这是一个有序列表`
	2. 这是一个有序列表`

##链接
格式
	
	链接：[]()     [链接文本](链接地址)
用markdown写下你的第一个md文档 的文章链接是这样构成的

	[用markdown写下你的第一个md文档](http://www.jianshu.com/p/de9c98bba332) 

也可以直接用尖括号包含网址的方式来构成链接 http://www.jianshu.com

	<http://www.jianshu.com>

###链接又分为行内式、参考式和 自动链接：

	这是行内式链接：[ConnorLin's Blog](http://connorlin.github.io)。
	
	这是参考式链接：[ConnorLin's Blog][url]，其中url为链接标记，可置于文中任意位置。
	
		[url]: http://connorlin.github.io/ "ConnorLin's Blog"
	
		链接标记格式为：[链接标记文本]:  链接地址  链接title(可忽略)
	
	这是自动链接：直接使用`<>`括起来<http://connorlin.github.io>

   
##图片

像构造一个链接一样，只需要在前面加！

格式：

	图片：
	![]()    
	![图片名称(可忽略)](图片地址)

也可以使用html方式来指定图片大小：

<img src="http://upload-images.jianshu.io/upload_images/95646-5bfd0cecf587c766.png" width="300px" height="240px" alt="简书">

	<img src="http://upload-images.jianshu.io/upload_images/95646-5bfd0cecf587c766.png" width="300px" height="240px" alt="简书">

##代码段
  
` 符号在左上角esc键下方，请在半角状态输入  

代码分为行内代码和代码块。

行内代码使用 `代码` 标识，可嵌入文字中  
	
	print("这是一个代码段");

代码块使用4个空格或```标识

	```
    这里是代码
    ```

代码语法高亮在 ```后面加上空格和语言名称即可

    ``` 语言
    //注意语言前面有空格
    这里是代码
    ```

例如：  
这是行内代码`onCreate(Bundle savedInstanceState)`的例子。
	
这是代码块和语法高亮：
``` java
	// 注意java前面有空格  
	protected void onCreate(Bundle savedInstanceState) {  
	super.onCreate(savedInstanceState);  
	setContentView(R.layout.activity_main);
	}
```

##字体样式
	倾斜 *倾斜*
	加粗 **加粗**
	倾斜并加粗 ***倾斜并加粗***

##表格
使用- |符号把内容分割为你认为合适的表格样式就好。
使用:符号标识对齐。

    居左：:----
    居中：:----:或-----
    居右：----:

	标题1|标题2|标题3|
	|:---|:---:|---:|
	|居左测试文本|居中测试文本|居右测试文本|
	|居左测试文本1|居中测试文本2|居右测试文本3|
	|居左测试文本11|居中测试文本22|居右测试文本33|
	|居左测试文本111|居中测试文本222|居右测试文本333|


##脚注(注解)

使用[^]来定义脚注：

这是一个脚注的例子[^1]

[^1]: 这里是脚注

##流程图
流程图代码示例
	
	flow
	st=>start: Start:>https://www.zybuluo.com
	io=>inputoutput: verification
	op=>operation: Your Operation
	cond=>condition: Yes or No?
	sub=>subroutine: Your Subroutine
	e=>end
	st->io->op->cond
	cond(yes)->e
	cond(no)->sub->io

###流程图绘制框架
[flowchart.js](http://flowchart.js.org/)

##LaTeX 公式

### $ 表示行内公式：
代码：  
	
	质能守恒方程可以用一个很简洁的方程式 $E=mc^2$ 来表达。

### $$ 表示整行公式：

代码：

    $$\sum_{i=1}^n a_i=0$$
    $$f(x_1,x_x,\ldots,x_n) = x_1^2 + x_2^2 + \cdots + x_n^2 $$
    $$\sum^{j-1}_{k=0}{\widehat{\gamma}_{kj} z_k}$$

[访问 MathJax 参考更多使用方法。](https://math.meta.stackexchange.com/questions/5020/mathjax-basic-tutorial-and-quick-reference)

##内容目录

在段落中填写 [TOC] 以显示全文内容的目录结构。

##锚点

网页中，锚点其实就是页内超链接，也就是链接本文档内部的某些元素，实现当前页面中的跳转。比如我这里写下一个锚点，点击回到目录，就能跳转到目录。 在目录中点击这一节，就能跳过来。还有下一节的注脚。这些根本上都是用锚点来实现的。

注意： 
1. Markdown Extra 只支持在标题后插入锚点，其它地方无效。 
2. Leanote 编辑器右侧显示效果区域暂时不支持锚点跳转，所以点来点去发现没有跳转不必惊慌，但是你发布成笔记或博文后是支持跳转的。

语法描述： 在你准备跳转到的指定标题后插入锚点{#标记}，然后在文档的其它地方写上连接到锚点的链接。

代码：

    ## 0. 目录{#index}
    跳转到[目录](#index)

##保存

最后将markdown编写的文档存为 .md 格式，就可以用对应的工具查看效果和编辑了。



#常用弥补Markdown的Html标签

##字体

	<font face="微软雅黑" color="red" size="6">字体及字体颜色和大小</font>
	<font color="#0000ff">字体颜色</font>

##换行

	使用html标签`<br/>`<br/>换行

##文本对齐方式

	<p align="left">居左文本</p>
	<p align="center">居中文本</p>
	<p align="right">居右文本</p>

##下划线

	<u>下划线文本</u>


