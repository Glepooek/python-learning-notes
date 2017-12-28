import pymysql

from log.logger import Logger


class PyMQLHelper:
    """
    PyMySQL帮助类
    """

    __logger = Logger()
    """日志对象"""
    __connection = None
    """数据库连接对象"""

    def __init__(self, db_address, db_username, db_password, db_name):
        try:
            self.__connection = pymysql.connect(db_address,
                                                db_username,
                                                db_password,
                                                db_name)
        except Exception as e:
            self.__logger.debug(e)

    def create_table(self, sql):
        """
        创建数据表
        关键词 with 语句可以保证诸如文件之类的对象在使用完之后一定会正确的执行其清理方法

        :param sql 创建数据表的SQL语句
        :type sql str

        """
        if self.__connection is None:
            return

        try:
            with self.__connection.cursor() as cursor:
                cursor.execute(sql)
        except Exception as e:
            self.__logger.debug(e)
        finally:
            self.__connection.close()

    def execute_operation(self, sql):
        """
        插入、删除、更新数据

        :param sql 插入、删除、更新SQL语句
        :type sql str

        :return true 操作成功；false 操作失败

        """
        if self.__connection is None:
            return False

        try:
            with self.__connection.cursor() as cursor:
                cursor.execute(sql)
                count = cursor.rowcount
                self.__connection.commit()
                if count == 1:
                    return True
                else:
                    return False
        except Exception as e:
            self.__connection.rollback()
            self.__logger.debug(e)
        finally:
            self.__connection.close()

    def get_all(self, sql):
        """
        获取符合条件的全部数据

        :param sql 查询SQL语句
        :type sql str

        """
        if self.__connection is None:
            return None

        try:
            with self.__connection.cursor() as cursor:
                cursor.execute(sql)
                # 获取所有记录列表
                results = cursor.fetchall()
                return results
        except Exception as e:
            self.__logger.debug(e)
        finally:
            self.__connection.close()

    def get_one(self, sql):
        """
        获取符合条件的一条数据

        :param sql 查询SQL语句
        :type sql str

        """
        if self.__connection is None:
            return None

        try:
            with self.__connection.cursor() as cursor:
                cursor.execute(sql)
                # 获取一条记录
                result = cursor.fetchone()
                return result
        except Exception as e:
            self.__logger.debug(e)
        finally:
            self.__connection.close()
