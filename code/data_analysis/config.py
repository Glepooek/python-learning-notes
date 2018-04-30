from configparser import ConfigParser

# 常量名全部大写
CONFIG_FILE = "config.txt"

config = ConfigParser()
# 读取配置文件
config.read(CONFIG_FILE, encoding='gb2312')

# 获取messages区段的内容
greeting = config.get('messages', 'greeting')
print(greeting)
