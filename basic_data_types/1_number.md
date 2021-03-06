### 数字(```number```)

Python数字数据类型用于存储数值。
数据类型是不允许改变的,这就意味着如果改变数字数据类型得值，将重新分配内存空间。
以下实例在变量赋值时Number对象将被创建：

```python
var1 = 1
var2 = 10
```

也可以使用del语句删除一些数字对象的引用。del语句的语法是：
```python
del var1[,var2[,var3[....,varN]]]]
```

Python 支持四种不同的数值类型：
- 布尔型(bool) 取值为true或false
- 整型(int) 通常被称为是整型或整数，是正或负整数，不带小数点。Python3整型是没有限制大小的，可以当作long类型使用，所以Python3没有Python2的long类型
- 浮点型(float) 浮点型由整数部分与小数部分组成，浮点型也可以使用科学计数法表示（2.5e2 = 2.5 x 10^2 = 250）
- 复数(complex) 复数由实数部分和虚数部分构成，可以用a + bj,或者complex(a,b)表示，复数的实部a和虚部b都是浮点型

(复数和虚数不一样，形如a＋bi的数。式中a，b 为实数，i是一个满足i^2＝－1的数，因为任何实数的平方不等于－1，所以i不是实数，而是实数以外的新的数。
在复数a＋bi中，a 称为复数的实部，b称为复数的虚部，i称为虚数单位。
当虚部等于零时，这个复数就是实数；当虚部不等于零时，这个复数称为虚数，虚数的实部如果等于零，则称为纯虚数。
由上可知，复数集包含了实数集，因而是实数集的扩张。

 复数的加法按照以下规定的法则进行：设z1=a+bi,z2=c+di是任意两个复数,
 　　则它们的和是 (a+bi)+(c+di)=(a+c)+(b+d)i.
 　　两个复数的和依然是复数,它的实部是原来两个复数实部的和,它的虚部是原来两个虚部的和.
 　　复数的加法满足交换律和结合律,
 　　即对任意复数z1,z2,z3,有：z1+z2=z2+z1; (z1+z2)+z3=z1+(z2+z3).

 复数的乘法法则
 　　规定复数的乘法按照以下的法则进行：
 　　设z1=a+bi,z2=c+di(a、b、c、d∈R)是任意两个复数,那么它们的积(a+bi)(c+di)=(ac－bd)+(bc+ad)i.
 　　其实就是把两个复数相乘,类似两个多项式相乘,展开得:ac+adi+bci+bdi^2,因为i^2=-1,所以结果是(ac－bd)+(bc+ad)i .两个复数的积仍然是一个复数.)

###### 1、布尔型
布尔型其实是整型的子类型，布尔型数据只有两个取值：True和False，分别对应整型的1和0。
每一个Python对象都天生具有布尔值（True或False），进而可用于布尔测试（如用在if、while中）。
以下对象的布尔值都是False：
- None
- False（布尔型）
- 0（整型0）
- 0.0（浮点型0）
- 0.0+0.0j（复数0）
- ''（空字符串）
- []（空列表）
- ()（空元组）
- {}（空字典）
- 用户自定义的类实例，该类定义了方法__nonzero__()或 __len__()，并且这些方法返回0或False

```python
class Number(object):
    def __bool__(self):
        return False

    def __nonzero__(self):
        # 兼容做法
        return self.__bool__()

print(bool(Number()))

# 输出结果
False
```

###### 2、Python数字类型转换
- bool(x) 将x转换为一个布尔类型。
- int(x) 将x转换为一个整数。
- float(x) 将x转换到一个浮点数。
- complex(x) 将x转换到一个复数，实数部分为x，虚数部分为 0。
- complex(x, y) 将x和y转换到一个复数，实数部分为x，虚数部分为y。x和y是数字表达式。

###### 3、数学函数（math模块下）

| 函数 | 描述 |
| :--- | :--- |
|fabs(x)|返回数字的绝对值，如math.fabs(-10) 返回10.0|
|ceil(x)|返回数字的上入整数，如math.ceil(4.1) 返回 5|
|floor(x)|返回数字的下舍整数，如math.floor(4.9)返回 4|
|max(x1, x2,...)|返回给定参数的最大值，参数可以为序列。|
|min(x1, x2,...)|返回给定参数的最小值，参数可以为序列。|
|modf(x)|返回x的小数部分与整数部分，两部分的数值符号与x相同，都以浮点型表示。|
|fmod(x, y)|返回x%y的值，以浮点型表示。|
|pow(x, y)|	返回x**y运算后的值。|
|round(x [,n])|	返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数。|
|exp(x)|返回e的x次幂(e^x),如math.exp(1) 返回2.718281828459045|
|log(x)|如math.log(math.e)返回1.0,math.log(100,10)返回2.0|
|log10(x)|返回以10为基数的x的对数，如math.log10(100)返回 2.0|
|sqrt(x)|	返回数字x的平方根，数字可以为负数，返回类型为实数，如math.sqrt(4)返回 2+0j|
|acos(x)|	返回x的反余弦弧度值。|
|asin(x)|	返回x的反正弦弧度值。|
|atan(x)|	返回x的反正切弧度值。|
|atan2(y, x)|返回给定的 X 及 Y 坐标值的反正切值。|
|cos(x)|	返回x的弧度的余弦值。|
|sin(x)|	返回的x弧度的正弦值。|
|tan(x)|返回x弧度的正切值。|
|hypot(x, y)|返回欧几里德范数 sqrt(x*x + y*y)。|
|degrees(x)|将弧度转换为角度,如degrees(math.pi/2) ， 返回90.0|
|radians(x)|将角度转换为弧度|

###### 4、数学常量（math模块下）

| 函数 | 描述 |
| :--- | :--- |
|math.pi |数学常量pi（圆周率）|
|math.e |数学常量e（自然常数）|

###### 5、随机数函数（random模块下）

| 函数 | 描述 |
| :--- | :--- |
|random.choice(seq)|从序列的元素中随机挑选一个元素|
|random.randrange ([start,] stop [,step])|	从指定范围内，按指定基数递增的集合中获取一个随机数，基数缺省值为1|
|random.random()|随机生成下一个实数，它在[0,1)范围内。|
|random.seed([x])|改变随机数生成器的种子seed。可以在调用其他随机模块函数之前调用此函数。|
|random.shuffle(lst)|将序列的所有元素随机排序|
|random.uniform(x, y)|	随机生成下一个实数，它在[x,y]范围内。|
