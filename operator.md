### 运算符(```operator```)

###### 1、算术运算符

| 运算符 | 描述 |
| :--- | :--- |
|+	|加，两个对象相加|
|-	|减，得到负数或是一个数减去另一个数|
|*	|乘，两个数相乘或是返回一个被重复若干次的字符串|
|/	|除，x 除以 y|
|%	|取模，返回除法的余数|
|**	|幂，返回x的y次幂|
|//	|取整除，返回商的整数部分|

###### 2、比较运算符

| 运算符 | 描述 |
| :--- | :--- |
|==	|等于，比较对象是否相等|
|!=	|不等于，比较两个对象是否不相等	|
|>	|大于，返回x是否大于y	|
|<	|小于，返回x是否小于y。所有比较运算符返回1表示真，返回0表示假。这分别与特殊的变量True和False等价。注意，这些变量名的大写。|
|>=	|大于等于，返回x是否大于等于y。|
|<=	|小于等于，返回x是否小于等于y。|

###### 3、赋值运算符

| 运算符 | 描述 |
| :--- | :--- |
|=	|简单的赋值运算符|
|+=	|加法赋值运算符|
|-=	|减法赋值运算符|
|*=	|乘法赋值运算符|
|/=	|除法赋值运算符|
|%=	|取模赋值运算符|
|**=|幂赋值运算符	|
|//=|取整除赋值运算符|

###### 4、位运算符

| 运算符 | 描述 |
| :--- | :--- |
|&	按位与运算符|
||	按位或运算符|
|^	按位异或运算符|
|~	按位取反运算符|
|<<	左移动运算符|
|>>	右移动运算符|

###### 5、逻辑运算符

| 运算符 | 描述 |
| :--- | :--- |
|and|布尔"与" |
|or	|布尔"或" |
|not|布尔"非" |

###### 6、成员运算符

| 运算符 | 描述 |
| :--- | :--- |
|in|如果在指定的序列中找到值返回True，否则返回False。|
|not in|如果在指定的序列中没有找到值返回True，否则返回 False。|

###### 7、身份运算符

| 运算符 | 描述 |
| :--- | :--- |
|is	|is 是判断两个标识符是不是引用自一个对象|
|is not|	is not 是判断两个标识符是不是引用自不同对象|

###### 8、运算符优先级

| 运算符 | 描述 |
| :--- | :--- |
|**	|指数 (最高优先级)|
|~ + -	|按位翻转, 一元加号和减号|
|* / % //|	乘，除，取模和取整除|
|+ -|	加法减法|
|>> <<|	右移，左移运算符|
|&	|位 'AND'|
|^ ||	位运算符|
|<= < > >=|	比较运算符|
|<> == !=|	等于运算符|
|= %= /= //= -= += *= **=|	赋值运算符|
|is is not|	身份运算符|
|in not in|	成员运算符|
|not or and	|逻辑运算符|