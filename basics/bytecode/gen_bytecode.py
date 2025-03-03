
# -*- coding: utf-8 -*-

"""
@author: takeEasy9
@description: 读取 Python 文件内容生成字节码
@version: 1.0.0
@since: 2025/3/1 14:01
"""

import dis
import sys


def generate_bytecode(file_path):
    try:
        # 打开文件并读取全部内容
        with open(file_path, 'r', encoding='utf-8') as file:
            file_content = file.read()

        # 编译文件内容为代码对象
        code_obj = compile(file_content, file_path, 'exec')

        # 生成字节码
        dis.dis(code_obj)

    except FileNotFoundError:
        print(f"错误：文件 {file_path} 未找到。")
    except Exception as e:
        print(f"发生未知错误：{e}")


# 示例调用
if __name__ == "__main__":
    generate_bytecode(sys.argv[1])