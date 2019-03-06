## 小白开始学Python
> 上班没task的时候是真的无聊
---
> 参考资料：
> [廖雪峰Python教程](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000)  
> 开发环境：Python **3.6.3**

##### hello world
```python
# input() #默认返回字符串，int(param) #可进行强转
name = input('please enter your name: ')
print('hello,', name)
```

> python hello.py

##### 数据类型
- 整数 : ```//``` 地板除，除法只取整数部分  `%d`,`%x`
- 浮点数 : 科学计数法 ```1.23e9```； ```inf``` 无限大 `%f`
- 字符串 ：`%s`
    - ```r''```单引号内部 默认不转义
    ```Python
    >>> print('\\\t\\')
    \       \
    >>> print(r'\\\t\\')
    \\\t\\
    ```
    
    - ```'''...'''``` 表示多行内容，```...```为提示符
    ```
    >>> print('''line1
    ... line2
    ... line3''')
    line1
    line2
    line3
    ```

- 布尔值 ：and or not 与或非运算。```True```,```False```
- 空值 : ```None```

##### 变量
- 变量 ：动态语言无需指定类型
- 常量 ：全大写表示常量 

##### 字符串和编码
- 编码：
    - ASCII : 1个字节-1个字符 固定八位 表示英文字母
    - UNICODE : 2个字节-1个字符 固定16位 表示所有语言
    - UTF-8 : 可变长编码。节省空间，便于传输
- 字符串：默认`UNICODE`编码
    - 单个字符：`ord()`字符转换为数字,`chr()`编码转为字符
    - `byte`类型：`x = b'ABC'`,每个字符只占一个字节.
    - str -> byte 调用`str.encode(charset)`;
    - byte -> str 调用`byte.decode(charset)`
    - `len(param)` 统计字节数或字符数
    - `format()` 匹配占位符替换为相应的变量

##### list 和 tuple
- list ： 有序集合，内容无限制，类似于多元数组
    - `len`: 返回元素个数
    - `list[i]` : 索引元素取值，索引为负，则反向取值
    - `list.append(value)` : 追加值
    - `list.insert(index,value) ` : 指定位置插入，依次后移
    - `list.pop(index)` : 删除指定位置的元素，为空则为最后
- tuple : tuple一旦初始化就不能修改
    - 空tuple : `t = ()`;
    - 1个元素的tuple : `t = (1,)`;不能写成 `t = (1)`
    - **Tuple 本身不可变，但是其中的元素的指向可变。** 例子如下：
    ```python
    >>> t = ('a', 'b', ['A', 'B'])
    >>> t[2][0] = 'X'
    >>> t[2][1] = 'Y'
    >>> t
    ('a', 'b', ['X', 'Y'])
    
    # tuple本身的元素没变，但是其中 t[2]指向的是一个list，Tuple对List的指向并未发生改变，改变的其实list指向的两个元素
    ```

##### 条件判断
- `if-else` 的完整形式
```
if <条件判断1>:
    <执行1>
elif <条件判断2>:
    <执行2>
elif <条件判断3>:
    <执行3>
else:
    <执行4>
```

##### 循环
###### for-in 循环
- **for element in elements**
    - element 作为临时变量
    - elements 作为相关集合 list/tuple
```python
# range(num) return numbers which are less than num
sum = 0
for x in range(101):
    sum = sum + x
print(sum)
```
###### while 循环
- while、break、continue

##### dict 和 set
- **dict字典，同理于 Java 中的Map** 
    - 存储 `key-value`，初始化`d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}`
    - 获取`value`, 
        - 1、`d['Michael']`；
        - 2、`d.get('Thomas')`；若`key`不存在，可指定返回的默认值 `d.get('Thomas'，-1)`
    - 删除 `key` 对应 `value` 也会删除 `d.pop('Bob')`

- **set**，一组 `key` 的集合，但不存储 `value`
    - 初始化： `s = set([1, 2, 3])` 需要提供一个`list`作为输入集合
    - 添加： `s.add(key)`
    - 删除:  `s.remove(key)`
    - 集合运算： `&` 和 `|`


###### 函数
> [Python 自带相关函数](https://docs.python.org/3/library/functions.html)

- 自定义函数：`def my_func()`
```python
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

def nop():
    pass
    
    
# 添加参数检查
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
        
# 返回多个值
import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

>>> x, y = move(100, 100, 60, math.pi / 6)
>>> print(x, y)
151.96152422706632 70.0
        
from fileName import functionName
```

- 函数参数：
```Python
# 默认参数。（必选参数在前，默认参数在后，且默认参数必须指向不变的对象）
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
    
# 可变参数，调用时可以传入任意个参数, 调用时自动组装为 Tuple
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
    
# 调用时，可以在tuple和list前加 * 转换为可变参数
>>> nums = [1, 2, 3]
>>> calc(*nums)
14


# 关键字参数，调用时可以传入任意个含参数名的参数， 自动组装为一个 Dict
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

# 调用实例
>>> person('Bob', 32, city='Beijing')
name: Bob age: 32 other: {'city': 'Beijing'}
>>> person('Adam', 45, gender='M', job='Engineer')
name: Adam age: 45 other: {'gender': 'M', 'job': 'Engineer'}

# 也可以先组装Dict
>>> kw = {'city': 'Beijing', 'job': 'Engineer'}
>>> person('Jack', 24, city=kw['city'], job=kw['job'])
name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}
>>> kw = {'city': 'Beijing', 'job': 'Engineer'}
>>> person('Jack', 24, **kw)
name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}


# 参数组合。 顺序（必选参数、默认参数、可变参数和关键字参数）
def func(a, b, c=0, *args, **kw):
    print ('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
# 调用
>>> func(1, 2)
a = 1 b = 2 c = 0 args = () kw = {}
>>> func(1, 2, c=3)
a = 1 b = 2 c = 3 args = () kw = {}
>>> func(1, 2, 3, 'a', 'b')
a = 1 b = 2 c = 3 args = ('a', 'b') kw = {}
>>> func(1, 2, 3, 'a', 'b', x=99)
a = 1 b = 2 c = 3 args = ('a', 'b') kw = {'x': 99}
>>> args = (1, 2, 3, 4)
>>> kw = {'x': 99}
>>> func(*args, **kw)
a = 1 b = 2 c = 3 args = (4,) kw = {'x': 99}

# 对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的
```
- 递归函数：
```python
# 计算阶乘
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)
# 调用
>>> fact(1)
1
>>> fact(5)
120
```

###### 高级特性
- 切片: 类似于 `Java#subString()`
```python
>>> L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
>>> L[0:3]
['Michael', 'Sarah', 'Tracy']
>>> L[:3]
['Michael', 'Sarah', 'Tracy']
>>> L[-2:]
['Bob', 'Jack']
>>> L[-2:-1]
['Bob']

# 实现 trim() 函数

```



