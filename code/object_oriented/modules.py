import logger

# logger_content = [n for n in dir(logger) if not n.startswith('_')]
# print(logger_content)

print(logger.__all__)
print(help(logger.Logger))
