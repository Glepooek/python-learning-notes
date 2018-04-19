# Python数据库基础

###### 连接和游标
使用基础数据库系统，必须用connect()函数连接到它。connect()函数常用的参数：用户名、密码、主机名、数据库名。
connect()函数返回Connection对象，该对象支持的方法如下表所示：

| 函数 | 描述 |
| :--- | :--- |
| close() | 关闭连接。关闭连接后，连接对象和其游标均不可用 |
| commit()| 提交挂起的事务 |
| rollback() | 回滚挂起的事务 |
| cursor() | 返回连接的游标对象 |

游标对象，通过游标执行SQL查询并检查结果。游标对象支持如下方法：

| 函数 | 描述 |
| :--- | :--- |
| close() | 关闭游标 |
| execute()| 执行SQL操作，可能使用参数 |
| executemany()| 对序列中的每个参数执行SQL操作 |
| fetchone() | 把查询结果集中下一行保存为序列，或None |
| fetchmany(size) | 获取查询结果集中的多行，默认尺寸为size |
| fetchall() | 获取查询结果集中的所有行 |
| nextset() | 跳至下一可用结果集 |
| setinputsizes() | 为参数预先定义内存区域 |
| setoutputsizes() | 为获取的大数据值设定缓冲区尺寸 |


