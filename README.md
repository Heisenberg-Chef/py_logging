#    logging模块

+   打印日志模块，很多程序都有记录日志的需求，并且日志中包含的信息既有正常的程序访问日志，还有可能是错误报告。
+   logging提供了标准日志输出接口，你可以通过它存储各种格式的日志。
    +   为什么不用print进行打印输出：这种方式对于简单的监本程序有用，但是如果是复杂的系统最好不要用，首先，这些print是没用的输出，大量使用有可能被遗忘在代码中，print输出的信息都到了标准输出中，这将影响我从std中查看其它数据
    +   使用logging的优势：
        +   我可以控制消息的级别，过滤掉那些并不重要的信息
        +   我可以决定输出到什么地方，以及怎么输出，有许多的重要级别可供输出：debug\info\warning\error以及critical。通过logger或者handler不同的级别，你就只输出错误信息到指定的记录文件，或者在调试时候只记录调试信息
### logging日志框架
+   loggers：可供程序直接调用的接口，app通过调用提供的api来记录日志：
    +   loggers 就是程序可以直接调用的一个日志接口，可以直接向logger写入日志信息。logger并不是直接实例化使用的，而是通过logging.getLogger(name)来获取对象，事实上logger对象是单例模式，logging是多线程安全的，也就是无论程序中哪里需要打日志获取到的logger对象都是同一个。但是不幸的是logger并不支持多进程，这个在后面的章节再解释，并给出一些解决方案。
+   Handlers：决定将日志记录分配至正确的目的地：
    +   Handlers 将logger发过来的信息进行准确地分配，送往正确的地方。举个栗子，送往控制台或者文件或者both或者其他地方(进程管道之类的)。它决定了每个日志的行为，是之后需要配置的重点区域。

每个Handler同样有一个日志级别，一个logger可以拥有多个handler也就是说logger可以根据不同的日志级别将日志传递给不同的handler。当然也可以相同的级别传递给多个handlers这就根据需求来灵活的设置了。
+   Filters：对日志信息进行过滤，提供更细粒度的日志是否输出的判断
+   Formatters：指定最终记录打印的格式布局
+   logging.basicConfig函数的参数：
    +   filename：指定日志文件名
    +   filemode:打开日志的模式
    +   format指定输出的格式
```
%(levelno)s：打印日志级别的数值
%(levelname)s：打印日志级别的名称
%(pathname)s：打印当前执行程序的路径，其实就是sys.argv[0]
%(filename)s：打印当前执行程序名
%(funcName)s：打印日志的当前函数
%(lineno)d：打印日志的当前行号
%(asctime)s：打印日志的时间
%(thread)d：打印线程ID
%(threadName)s：打印线程名称
%(process)d：打印进程ID
%(message)s：打印日志信息
```
+   +   datafmt:指定时间格式，同time.strftime()，例子代码里面我会用time.strftime("%Y%h%d",localtime(time.time()))
    +   level：设置日志级别，默认为logging.WARNNING
    +   stream：指定将日志的输出流，可以指定输出sys.stderr,sys.stdout或者文件，默认输出到sys.stderr，当stream和filenametognshi
### 级别排序:CRITICAL > ERROR > WARNING > INFO > DEBUG
