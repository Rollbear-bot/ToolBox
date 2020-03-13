# 笔记
## Java

### Module 模块系统

### OpenJDK

+ Offical repo: <https://hg.openjdk.java.net/jdk/jdk>
  + dir "bowser" shows the source code.![1583972066906](assets/1583972066906.png)
    





## C++

+ 错误：error: passing ‘const List<char>’ as ‘this’ argument discards qualifiers [-fpermissive]
               flag->data = operand.find(index)->data;
    原因：函数中出现了const参数调用了非const属性的函数的情况，编译器有理由认为该const参数被非法修改；解决办法：检查const参数是否调用了必要的、且没有const标记的函数

### 函数返回引用

+ 函数返回引用的问题出错与否，取决于返回的是本地变量的空间（函数结束后被销毁）还是**父域的变量空间**

           >**由于临时变量的作用域短暂（在C++标准中，临时变量或对象的生命周期在一个完整的语句表达式结束后便宣告结束，也就是在语句float &b=fn1(5.0);之后） ，所以b面临无效的危险，很有可能以后的值是个无法确定的值。**
           >
           > **如果真的希望用函数的返回值来初始化一个引用，应当先创建一个变量，将函数的返回值赋给这个变量，然后再用该变量来初始化引用：**

### “使用了已删除的函数”
error: use of deleted functionc++中如果不显示的提供构造函数, 编译器会给一个默认的构造函数, 但在钻石结构的继承关系中, 默认构造函数显然
是有问题的, 因此构造函数不会提供默认版本. 因此会触发该错误.

一般来说, 该错误大致都是编译器认为默认构造函数有问题时, 不提供默认构造函数造成的.

当然, 如果自己显示的使用delete关键字, 也会报该错误

+ 解决
  解决方法就是显示的提供一个合适的构造函数即可.

### C异常基类std::exception
![exceptions_in_cpp](其他笔记.assets/exceptions_in_cpp.png)

| 异常                   | 描述                                                         |
| :--------------------- | :----------------------------------------------------------- |
| **std::exception**     | 该异常是所有标准 C++ 异常的父类。                            |
| std::bad_alloc         | 该异常可以通过 **new** 抛出。                                |
| std::bad_cast          | 该异常可以通过 **dynamic_cast** 抛出。                       |
| std::bad_exception     | 这在处理 C++ 程序中无法预期的异常时非常有用。                |
| std::bad_typeid        | 该异常可以通过 **typeid** 抛出。                             |
| **std::logic_error**   | 理论上可以通过读取代码来检测到的异常。                       |
| std::domain_error      | 当使用了一个无效的数学域时，会抛出该异常。                   |
| std::invalid_argument  | 当使用了无效的参数时，会抛出该异常。                         |
| std::length_error      | 当创建了太长的 std::string 时，会抛出该异常。                |
| std::out_of_range      | 该异常可以通过方法抛出，例如 std::vector 和 std::bitset<>::operator[]()。 |
| **std::runtime_error** | 理论上不可以通过读取代码来检测到的异常。                     |
| std::overflow_error    | 当发生数学上溢时，会抛出该异常。                             |
| std::range_error       | 当尝试存储超出范围的值时，会抛出该异常。                     |
| std::underflow_error   | 当发生数学下溢时，会抛出该异常。                             |

### Segmentation Fault错误

+ 指针越界和SIGSEGV是最常出现的情况，经常看到有帖子把两者混淆，而这两者的关系也确实微妙。在此，我们把指针运算（加减）引起的越界、野指针、空指针都归为指针越界。SIGSEGV在很多时候是由于指针越界引起的，但并不是所有的指针越界都会引发SIGSEGV。**一个越界的指针，如果不引用它，是不会引起SIGSEGV的。而即使引用了一个越界的指针，也不一定引起SIGSEGV。**

1. 错误的访问类型引起

2. 访问了不属于进程地址空间的内存，或往收到系统保护的内存地址写数据

3. 访问了不存在的内存，如引用一个空指针指向的单元

4. 内存越界，数组越界，变量类型不一致

5. 试图把一个整数按字符串的方式输出

   ```c++
   int main(){
   	int b = 10;
   	printf("%s\n", b);
   	return 0;
   }
   ```

   > 在打印字符串的时候，实际上是打印某个地址开始的所有字符，但是当你想把整数当字符串打印的时候，这个整数被当成了一个地址，然后printf从这个地址开始去打印字符，直到某个位置上的值为\0。所以，如果这个整数代表的地址不存在或者不可访问，自然也是访问了不该访问的内存——segmentation fault。

6. 栈溢出







## 编译器

+ MinGW，即Minimalist GNU for Windows，GCC的端口集合
+ GCC，一套编译器套件，其中G++是C++的编译器



## 杂项

### 最短路径（在通信中是一种常见的路由应用）
（dijkstra算法与课本不同的另一种C++实现方式）创建两个表，OPEN, CLOSE。

OPEN表保存所有已生成而未考察的节点，CLOSED表中记录已访问过的节点。

1． 访问路网中距离起始点最近且没有被检查过的点，把这个点放入OPEN组中等待检查。

2． 从OPEN表中找出距起始点最近的点，找出这个点的所有子节点，把这个点放到CLOSE表中。

3． 遍历考察这个点的子节点。求出这些子节点距起始点的距离值，放子节点到OPEN表中。

4． 重复第2和第3步,直到OPEN表为空，或找到目标点。

```c++
#include<iostream>
#include<vector>
using namespace std;
void dijkstra(const int &beg,//出发点
              const vector<vector<int> > &adjmap,//邻接矩阵，通过传引用避免拷贝
              vector<int> &dist,//出发点到各点的最短路径长度
              vector<int> &path)//路径上到达该点的前一个点
//负边被认作不联通
//福利：这个函数没有用任何全局量，可以直接复制！
{
    const int &NODE=adjmap.size();//用邻接矩阵的大小传递顶点个数，减少参数传递
    dist.assign(NODE,-1);//初始化距离为未知
    path.assign(NODE,-1);//初始化路径为未知
    vector<bool> flag(NODE,0);//标志数组，判断是否处理过
    dist[beg]=0;//出发点到自身路径长度为0
    while(1)
    {
        int v=-1;//初始化为未知
        for(int i=0; i!=NODE; ++i)
            if(!flag[i]&&dist[i]>=0)//寻找未被处理过且
                if(v<0||dist[i]<dist[v])//距离最小的点
                    v=i;
        if(v<0)return;//所有联通的点都被处理过
        flag[v]=1;//标记
        for(int i=0; i!=NODE; ++i)
            if(adjmap[v][i]>=0)//有联通路径且
                if(dist[i]<0||dist[v]+adjmap[v][i]<dist[i])//不满足三角不等式
                {
                    dist[i]=dist[v]+adjmap[v][i];//更新
                    path[i]=v;//记录路径
                }
    }
}
int main()
{
    int n_num,e_num,beg;//含义见下
    cout<<"输入点数、边数、出发点：";
    cin>>n_num>>e_num>>beg;
    vector<vector<int> > adjmap(n_num,vector<int>(n_num,-1));//默认初始化邻接矩阵
    for(int i=0,p,q; i!=e_num; ++i)
    {
        cout<<"输入第"<<i+1<<"条边的起点、终点、长度（负值代表不联通）：";
        cin>>p>>q;
        cin>>adjmap[p][q];
    }
    vector<int> dist,path;//用于接收最短路径长度及路径各点
    dijkstra(beg,adjmap,dist,path);
    for(int i=0; i!=n_num; ++i)
    {
        cout<<beg<<"到"<<i<<"的最短距离为"<<dist[i]<<"，反向打印路径：";
        for(int w=i; path[w]>=0; w=path[w])
            cout<<w<<"<-";
        cout<<beg<<'\n';
    }
}
```

### 递归转化为非递归的方法：

1. 要么用队列，要么用栈
2. 在递归函数的形参列表中的变量就是非递归的迭代中需要修改的变量

### 里氏替换原则

里氏替换原则(Liskov Substitution Principle LSP)面向对象设计的基本原则之一。 里氏替换原则中说，任何基类可以出现的地方，子类一定可以出现。 LSP是继承复用的基石，只有当衍生类可以替换掉基类，软件单位的功能不受到影响时，基类才能真正被复用，而衍生类也能够在基类的基础上增加新的行为。

### Base64编码

+ 一种将**二进制数据**转换为**文本数据**的编码方法
+ Base64编码的主要的作用不在于安全性，而在于让内容能在网络间无错的传输。(常用语编码特殊字符，编码小型二进制文件等)
+ b64编码完了还是二进制数据，不是字符串
  UTF-8解码完才是字符串
  在传输时为了向下兼容（设备或者协议）常常把图像、音频、视频用b64编码

### 进程与线程

+ 面试题：进程和线程的区别和联系？
  进程 - 操作系统分配内存的基本单位 - 一个进程可以包含一个或多个线程
  线程 - 操作系统分配CPU的基本单位
  并发编程（concurrent programming）

1. 提升执行性能 - 让程序中没有因果关系的部分可以并发的执行
2. 改善用户体验 - 让耗时间的操作不会造成程序的假死

+ 进程和线程的关系：
  （1）一个线程只能属于一个进程，而一个进程可以有多个线程，但至少有一个线程。
  （2）资源分配给进程，同一进程的所有线程**共享该进程的所有资源**。
  （3）处理机分给线程，即真正在处理机上运行的是线程。
  （4）线程在执行过程中，需要协作同步。不同进程的线程间要利用消息通信的办法实现同步。

+ 说明：**多线程和多进程的比较**。
  以下情况需要使用**多线程**：

1. 程序需要维护许多共享的状态（尤其是可变状态），Python中的列表、字典、集合都是线程安全的，所以使用线程而不是进程维护共享状态的代价相对较小。

2. 程序会花费大量时间在I/O操作上，没有太多并行计算的需求且不需占用太多的内存。

   以下情况需要使用**多进程**：

3. 程序执行计算密集型任务（如：字节码操作、数据处理、科学计算）。

4. 程序的输入可以并行的分成块，并且可以将运算结果合并。

5. 程序在内存使用方面没有任何限制且不强依赖于I/O操作（如：读写文件、套接字等）。

+ 一个进程死掉就等于所有的线程死掉，所以多进程的程序要比多线程的程序健壮，但在进程切换时，耗费资源较大，效率要差一些

### 并发与并行

+ 并发：多个进程/线程通过**时间片**分配的方式在同一个处理机上执行，微观上是串行
+ 并行：进程/线程**真正意义上的同时执行**，例如在多核处理器不同核心上运行的程序
+ 若机器上搭载多核处理器，进程少时（任务 < 核心数量）可以实现并行；进程多时则是并发

### SQLite

+ 它是一种轻量的（几十兆），开源的嵌入式数据库（管理系统）
+ 它的数据库就是一个文件（后缀.db）
+ 在python3中**内置SQLite3**，无需配置，开箱即用




## Python

### 协程

单线程+异步IO

### turtle模块的使用

+ 海龟角度体系（设置朝向、左转向、右转向等）
+ 绝对坐标（画布上的位置，画布中心的坐标即是原点，海龟初始化时位于中心的原点，且朝向右边；绝对坐标中正右方是0度，可以用seth函数指定海龟的绝对坐标朝向）
+ 海龟坐标（海龟向前移动、向后移动等）
+ RGB色彩体系，turtle库默认使用RGB小数值表示色彩（0~1范围）
+ 画笔控制（penup()，pendown()，pensize()，pencolor()）
  pendown函数只是放下画笔，并不绘制任何内容
+ circle函数画圆时，半径取正数表示圆心在海龟的左边，半径取负数表示圆心在海龟的右边

### 基础语法

+ import 库名 as 自定义名称
  可以给调用的外部库关联一个更短的、更适合自己的名字
  
+ 注意“^”运算符不是计算幂次，而是按位异或运算符；计算幂次的运算符是“**”

+ 函数装饰器：限定函数的某种属性，例如setter，getter，静态函数，类函数等等

+ with关键字释放资源：在离开上下文环境时释放变量
  ```with open('hello.txt', 'r', encoding='utf-8') as f:```
  
+ 字符串前加'r'字母，表示该字符串是raw string，其中的'\\'没有转义作用

+ \__str__魔法：常用于打印对象信息

  ```python
  def __str__(self):
      """魔法方法：类似Java中的toString
      在直接print该类对象的时候会触发
      该魔法只能返回字符串，否则会报错"""
      return "(%s, %s)" % (self.x, self.y)
  ```

+ 匿名函数lambda的用法：
  ```comp=lambda x, y: x < y```
  “:”的左边为参数列表，右边为返回值
  内部的结果形同comp(x, y): return x < y
  lambda可以放在函数的参数表中

  ```python
  def select_sort(origin_items, comp=lambda x, y: x < y):
      """简单选择排序"""
  ```

+ 生成式（推导式）语法，常用于字典、集合、列表等
  指定条件来挑选元素组成新字典

  ```python
  prices = {
      'AAPL': 1991.88,
      'IBM': 48.44,
      'FB': 208
  }
  # 遍历prices字典，挑出那些value>100的键值对置入新字典
  prices2 = {key: value for key, value in prices.items()
             if value > 100}
  ```

+ 字符串模板format
  在py3.6后，可以在字符串前加'f'实现变量的填充
  ```float(input(f'请输入{name}的{course}成绩:'))```
  
+ yield关键字
  包含yield语句的函数被视为一个生成器，产生一个可迭代对象

  > 带有 yield 的函数不再是一个普通函数，Python 解释器会将其视为一个 generator，调用 fab(5) 不会执行 fab 函数，而是返回一个 iterable 对象！在 for 循环执行时，每次循环都会执行 fab 函数内部的代码，执行到 yield b 时，fab 函数就返回一个迭代值，下次迭代时，代码从 yield b 的下一条语句继续执行，而函数的本地变量看起来和上次中断执行前是完全一样的

  使用yield生成一个斐波那契数列：

  ```python
  def fab(max): 
      n, a, b = 0, 0, 1 
      while n < max: 
          yield b      # 使用 yield
          # print b 
          a, b = b, a + b 
          n = n + 1
   
  for n in fab(5): 
      print n
  ```


+ 其实python中的函数也是对象，他们都具有一个“可调用”的属性（callable），类的实例可以通过定义\__called__魔法使得类/实例变得可调用，可以像函数那样在后面加括号直接执行

+ with关键字：紧跟with后面的语句会被求值，返回对象的\_\_enter()方法被调用，这个方法的返回值将被赋值给as关键字后面的变量，当with后面的代码块全部被执行完之后，将调用前面返回对象的\_\_exit()方法。

   with语句最关键的地方在于被求值对象必须有\_\_enter()\_\_和\_\_exit()__这两个方法，那我们就可以通过自己实现这两方法来自定义with语句处理异常。
   
+ **Python中的name与object的关系**

   + 与C++有很大不同，Python中的标识符并不会对应一个内存地址，而是绑定到一个python object*（2，'hello'，False这些都是object，而且是“不可变”object）*
   + 由于name不对应内存地址，所以同一个标识符可以绑定不同类型的object（用赋值号）
   + 



### Python数据结构

+ python堆（heapq）
  利用匿名函数limbda指定排序的依据，利用堆排序找出前n大/小的元素

  ```python
  list2 = [
      {'name': 'IBM', 'shares': 100, 'price': 91.1},
      {'name': 'AAPL', 'shares': 50, 'price': 543.22},
      {'name': 'FB', 'shares': 200, 'price': 21.09}
  ]  # list2是一个3个字典组成的列表
  ```

  ```python
  # 匿名函数lambda指定比较的依据
  # 根据比较依据取出前n大/小的元素
  print(heapq.nlargest(2, list2, key=lambda x: x['price']))
  print(heapq.nsmallest(2, list2, key=lambda x: x['shares']))
  ```
  
+ python中**二叉树**的实现

  1. list of lists，表的表，形如arr[1,[2],[3]]，*这里2和3是1的子节点*
  2. 链接形式，构造类，在类成员中指向子节点
  3. 二叉堆，使用python内置的堆类型构造



### Python3内置函数

+ filter（筛选器）：根据选定的函数（该函数必须返回布尔值）筛选可迭代对象，filter返回一个迭代器

  ```python
  # 使用筛选函数is_odd筛选序列lt，然后返回新序列
  new_list = filter(is_odd, lt)
  ```

+ map（映射器）：序列结果指定的函数映射之后生成新的序列，map返回迭代器；序列可以指定多个，对应映射函数的多个参数

  ```python
  lt = [1, 2, 3, 4, 5]
  lt2 = [6, 7, 8, 9]
  # 列表可以为多个，尾部多余的元素会被舍弃（以短序列为准）
  # 对相同位置的元素相加
  new_list = map(lambda a, b: a + b, lt, lt2)
  ```

+ 自定义装饰器（需要引入wraps包）

  装饰器类似一个将目标函数“包起来”的父函数，可以定义在目标函数执行前和后执行的语句

  ```python
  # 自定义装饰器
  from functools import wraps
  from time import time
  def record_time(func):
      """自定义一个记录函数运行时间的装饰器"""
      @wraps(func)
      def wrapper(*args, **kwargs):
          start = time()  # 记录开始时间
          result = func(*args, **kwargs)  # 记录被装饰的函数的返回值
          print(f"in {time()-start}s")  # 计算func运行用时并输出
          return result  # 返回函数的返回值
      return wrapper
  ```
  
+ str.join((s1, s2, s3, ...))
  用于字符串的处理，用str将元组中的字符串连接起来，函数返回一个字符串
  ```str = "-"; seq = ("a", "b", "c"); # 字符串序列 print str.join( seq );```

  \>>\>a-b-c



### 面向对象进阶

+ Mixin（混入）模式：通过多继承的方式实现

  >通过实现最小的`Dictionary Interface`，还有继承`DictMixin`实现Mixin模式，我们就轻松获得了完整的原生字典的行为：下表语法，`get`, `has_keys`, `iteritems`, `itervalues`甚至还有[iterable protocol implementation](https://www.jianshu.com/p/d3fb22de98ee)等一系列的方法和实现。

+ 什么是\*args和\**kwargs？

  + 可以让你传递可变数量的位置参数；函数会获取所有输入的参数，将他们打包成一个可迭代的简单对象，命名为args，当然这个名字是可以修改的

  + "\*"是解包运算符，解包(unpacking)操作符*获得的可迭代对象不是一个list，而是一个元组(tuple)

  + **kwargs工作原理和\*args有点类似，但不是接收位置参数，而是接收关键字(keyword)参数(也叫被命名的参数)。以下为例：

    ```python
    # concatenate.py
    def concatenate(**kwargs):
        result = ""
        # Iterating over the Python kwargs dictionary
        for arg in kwargs.values():
            result += arg
        return result
     
    print(concatenate(a="Real", b="Python", c="Is", d="Great", e="!"))
    ```

    执行上面的脚本，concatenate()会通过python的kwargs字典进行迭代并将找到的所有值连接起来：

    ```
    $ python concatenate.py
    RealPythonIsGreat!
    ```

+ 元（meta）类
  当希望一些类具有某个共同特征，使用元类
  它类似某种类模板

  + 使用元类的类在定义时加上
    ```__metaclass__ = Singleton``` 或

    ```class President(metaclass=SingletonMeta):```

    这里Singleton是元类的类名



### Django框架

+ 不在settings.py 中 **ALLOWED_HOSTS** 中的ip没法访问django的debug功能
  *提示：Invalid HTTP_HOST header*
+ setting中的模组变量DEBUG(boolean)决定是否打开debug模式，debug模式下，django会返回出错的traceback等各种信息到浏览器
+ **web服务器**和**web框架**之间的区别

  1. web服务器解析（从客户端过来的）报文，组织（发送到客户端的）响应报文，维持服务器和客户端之间的连接
  2. web框架进行**路由分发**（根据url找到相应的*处理函数*）；完成*处理函数*中进行的业务
  3. web服务器接收到（来自客户端）请求之后，将请求和参数传给web框架，**由框架负责生成内容**，并将生成的内容传给web服务器，web服务器传回客户端
     <img src="其他笔记.assets/web服务器和web框架.png" alt="web服务器和web框架" style="zoom: 80%;" />

+ Django默认使用Python内置的SQLite作为数据库，更改数据库可以修改settings文件



#### 视图(view)

+ 视图是**“一类具有相同功能和模板的网页的集合”**，比如一个博客中的首页、以年为单位的归档页、评论处理器等

+ 在Django中，页面和内容是**通过视图来输送**的；每个视图实际上是一个python方法；Django根据URL的匹配来**选择**视图

+ 视图和urlconf，根URLconf和自定义URLconf的引用关系

+ path(route, view, kwargs, name)的使用方法

  + route：

    1. 一个**匹配**URL的准则（类似正则表达式），从urlpatterns的第一下开始往下顺序匹配
    2. 它**不会**处理GET/POST的参数和域名，例如*https://www.example.com/app?page=3*，他只会匹配“app/”

  + view：

    > 当 Django **找到**了一个匹配的准则，就会调用这个特定的**视图函数**，并传入一个 [`HttpRequest`](https://docs.djangoproject.com/zh-hans/3.0/ref/request-response/#django.http.HttpRequest) 对象作为第一个参数，被“捕获”的参数以关键字参数的形式传入。

+ 数据库迁移
  + **迁移**是非常强大的功能，它能让你在开发过程中**持续的改变数据库结构而不需要重新删除和创建表 - 它专注于使数据库平滑升级而不会丢失数据**。我们会在后面的教程中更加深入的学习这部分内容，现在，你只需要记住，改变模型需要这三步：
    - 编辑 `models.py` 文件，改变模型。
    - 运行 [`python manage.py makemigrations`](https://docs.djangoproject.com/zh-hans/3.0/ref/django-admin/#django-admin-makemigrations) 为模型的改变生成迁移文件。
    - 运行 [`python manage.py migrate`](https://docs.djangoproject.com/zh-hans/3.0/ref/django-admin/#django-admin-migrate) 来应用数据库迁移。
  
+ 配置模板（templates）

  + 在app目录下，建立templates目录，Django会自动寻路来加载模板（默认在settings已经配置好了）
  
  + **render()函数**：因为*“载入模板、填充上下文、再返回生成的HttpResponse对象”*是很常用的功能，所以快捷函数render将他们集中起来；直接一步载入、填充、返回HttpResponse对象
    
    ```python
    return render(request, 'polls/index.html', context)
    ```
    
  + 去除模板中的硬编码URL
    使用我们在urls.py中为url定义的name，利用{% url %}的标签
  
  + *为URL名称添加命名空间*
  
    + 使用app_name = ...
    + 可以防止和其他app的视图重名带来错误
    + 改完了urls.py，别忘了改模板



+ **get_object_or_404()函数**：

  + 可以理解为object.get()函数的升级版
+ 如果找不到对应的对象，会直接在该函数**内部**raise Http404，而不是主动捕获ObjectDoesNotExist的异常再抛出404
  + 简化了设计，同时有利于**模型和视图的解耦**
  + object.filter也有对应函数get_list_or_404()



+ **request.POST['choice']** 的形式可以获取POST部分中某字段的值（类字典），request.POST 的值永远是字符串；request.GET 同理

+ HttpResponse和HttpResponseRedirect的区别：
  重定向只接受一个参数：用户将要被重定向的URL

  

#### 通用视图

+ 使用**通用视图**来解决视图中的代码冗余问题

  + 他们是继承generic的类，具有ListView, DetailView两种类型

  + 改良URLconf
  + 改良视图



#### 模型(Models)

  定义模型即**数据库结构设计**和附加的其他元数据
  在{appName}/models.py中定义模型

+ 修改模型之后，要进行激活和数据库迁移，执行*makemigrations*和*migrate*两条指令

+ timezone设置



#### manage.py命令行常用指令

1. shell 

   + 进入python交互式执行模式

   + >我们使用这个命令而不是简单的使用 "Python" 是因为 `manage.py` 会设置 `DJANGO_SETTINGS_MODULE` 环境变量，这个变量会让 Django 根据 `mysite/settings.py` 文件来设置 Python 包的导入路径。

   + **shell <** 执行脚本

   + Django提供了大量的数据库检索api

     + filter()：根据对象的id检索，根据对象字段的文本匹配\__startwith等
   
       ```shell
       >>> Question.objects.filter(id=1)
       <QuerySet [<Question: What's up?>]>
       >>> Question.objects.filter(question_text__startswith='What')
    <QuerySet [<Question: What's up?>]>
       ```
   
     + objects.get()
     
       ```shell
       >>> Question.objects.get(pub_date__year=current_year)
       <Question: What's up?>
       ```
     
       但是这个语句不能直接检索id，可以通过get(pk=1)的形式检索id
       get**只能返回一个对象**，否则报错，filter可以返回列表



#### 后台管理界面

+ 创建超级用户 createsuperuser

+ 在管理界面添加app中的内容：修改{app}/admin.py，在其中注册要添加的对象，这样就可以在管理界面**图形化操作**对象了
  <img src="其他笔记.assets/管理界面.png" alt="管理界面" style="zoom:67%;" />
  
+ 在admin文件中注册过的对象可以显示在后台，例如上图的Question对象；非常有意思的是，Django对字段的每种数据类型提供了不同的**图形化修改方案**，例如上方的Date字段是*Datetime*这种数据类型的，后台会识别出这种类型，在右边提供一个图形化的小日历来选择日期，其他数据类型也类似。实现机理是一些预设（Django内置）的javascript代码

+ **自定义的后台表单**

  + 在admin文件中创建一个模型后台类（继承admin.ModelAdmin），然后将这个类作为第二个参数传给regester()，可以在模型后台类中**改变数据的展示方式**

  + 模型的字段很多时，可以使用fieldsets来分类存放

    ```python
    class QuestionAdmin(admin.ModelAdmin):
        fieldsets = [
            (None,               {'fields': ['question_text']}),
            ('Date information', {'fields': ['pub_date']}),
        ]
    ```

  + 添加关联的对象（外部键）
    修改模型后台类的inlines属性来关联外部对象

    ```python
    # TabularInLine, StackedInline等多种不同展示方式
    class ChoiceInline(admin.StackedInline):
        model = Choice
        extra = 3
    
    
    class QuestionAdmin(admin.ModelAdmin):
        fieldsets = [
            (None,               {'fields': ['question_text']}),
            ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
        ]
        inlines = [ChoiceInline]
    ```

    这样在创建Question对象时可以同时添加它关联的Choice

  + **自定义的列表界面**：修改<u>模型后台类</u>的list_display属性，添加要展示的字段

    ```python
    list_display = ('question_text', 'pub_date')
    ```

    效果：

    <img src="其他笔记.assets/image-20200310150304703.png" alt="image-20200310150304703" style="zoom:80%;" />

    若要对列表的首行更改，可以在模型models.py中设置

    ```python
    # 更改在后台列表页的展示标题
        was_published_recently.short_description = 'Published recently?'
        # 用彩色小图标而不是字符显示True/False
        was_published_recently.boolean = True
    
        was_published_recently.admin_order_field = 'pub_date'
    ```

  + 对象排序和筛选
    在模型后台类中修改list_filter属性，将它指向排序的依据字段

    ```python
    list_filter = ['pub_date']
    ```

  + 在列表顶部添加一个搜索框：修改search_fields属性

    ```python
    search_fields = ['question_text']
    ```

    



#### 自动化测试

+ 按照惯例，写在app目录下的**tests.py文件**里，这样测试模块可以自动找到它

+ 创建test.TestCase的子类，在成员方法中编写测试语句，用**self.assertIs()**断言来帮助debug

+ 测试方法（成员方法）**应该以"test_"开头**

+ > - 对于每个模型和视图都建立单独的 `TestClass`
  > - 每个测试方法只测试一个功能
  > - 给每个测试方法起个能描述其功能的名字

+ 在控制台输入**"py manage.py test {app's name}"**来自动化执行这个app内的所有测试

+ 内置的测试模块会自动在测试时创建数据库，并在测试完毕后删除，因此不会影响已有的数据

+ 对于**视图**的测试

  + 使用Django内置的视图测试工具Client
  + 使用Django提供的TestCase类时，不需要自己再创建Client实例（内置了）



#### 静态文件

+ 样式表（css）：放在app目录下的static文件夹中；加载入html模板即可实装



#### 自定义<u>工程的</u>模板

+ 位于项目目录下的templates目录；在settings文件中的TEMPLATES的DIR属性添加路径，让Django能够找到这个模板目录
+ 属于特定应用的模板文件最好放在应用所属的模板目录（例如 `polls/templates`），而不是工程的模板目录（`templates`）。以便创建可复用的应用。
+ 若要更改内置后台的样式，可以Django包中内置的模板到项目目录/templates，作出修改



### 其他

+ 使用PIL模块在图片上添加文字
  分别使用了PIL库中的Image, ImageDraw, ImageFont模块，可以实现对文本的字体、大小、位置、颜色等的设置，并且支持中文；**支持指定自定义字体**
+ 使用tkinter模块的 filedialog 来（通过用户点选的方式）获取文件路径





## Docker

