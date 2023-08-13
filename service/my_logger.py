import os
import logging

def setup_logger(log_file):
    # 确定日志文件的绝对路径
    log_file_path = os.path.abspath(log_file)

    # 获取日志文件所在的目录路径
    log_dir = os.path.dirname(log_file_path)

    # 创建日志文件所在的目录（如果不存在）
    os.makedirs(log_dir, exist_ok=True)

    # 创建并配置日志记录器
    logging.basicConfig(filename=log_file_path, level=logging.ERROR)

    # 创建日志格式
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # 创建文件处理器并设置日志格式
    file_handler = logging.FileHandler(log_file_path)
    file_handler.setFormatter(formatter)

    # 创建日志记录器并添加文件处理器
    logger = logging.getLogger()
    logger.addHandler(file_handler)

    return logger

def log_error(logger, error_message):
    logger.error(error_message)