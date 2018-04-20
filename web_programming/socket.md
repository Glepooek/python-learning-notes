### socket模块

套接字（socket）主要是两个程序之间的“信息通道”。程序可能分布在不同的计算机上，通过套接字相互发送信息。
套接字（socket）包括两个：服务器套接字和客户机套接字。

### socketserver模块
socketserver模块是标准库中很多服务器框架的基础，如http.server\xmlrpc.server。
socketserver包含以下几个基本的类：TCPServer针对TCP套接字流，UDPServer针对UDP套接字流。
        +------------+
        | BaseServer |
        +------------+
              |
              v
        +-----------+        +------------------+
        | TCPServer |------->| UnixStreamServer |
        +-----------+        +------------------+
              |
              v
        +-----------+        +--------------------+
        | UDPServer |------->| UnixDatagramServer |
        +-----------+        +--------------------+

### 多连接
有3种方法实现多连接目的：分叉、线程、异步I/O。

1）使用ForkingTCPServer\ThreadingTCPServer进行分叉和线程处理
2）带有select和poll的异步I/O

