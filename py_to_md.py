import os

def write_code_to_md(directory, md_file, relative_path=""):
    # 遍历目录下的所有文件和子目录，并按字符顺序排序
    entries = sorted(os.listdir(directory))
    for entry in entries:
        entry_path = os.path.join(directory, entry)

        if os.path.isdir(entry_path) and entry != "spiders":
            new_relative_path = os.path.join(relative_path, entry)
            write_code_to_md(entry_path, md_file, new_relative_path)
        elif os.path.isfile(entry_path) and entry.endswith(".py") and entry != "py_to_md.py":
            # 获取文件名（去掉后缀）
            file_title = os.path.splitext(entry)[0]

            # 写入大标题，包含相对路径
            md_file.write(f"#### {relative_path}/{file_title}\n\n")

            # 写入代码块标记
            md_file.write("```py\n")

            # 读取并写入代码
            with open(entry_path, 'r') as py_file:
                code_content = py_file.read()
                md_file.write(code_content)

            # 添加一个空行
            md_file.write("\n```\n\n")

            # 输出成功导入的文件信息
            print(f"导入文件成功: {relative_path}{entry}")

# 获取当前目录
current_directory = input("请输入目录: ")

# 创建 Markdown 文件
md_file_path = os.path.join(current_directory, 'code_myself.md')

with open(md_file_path, 'w') as md_file:
    # 调用函数
    write_code_to_md(current_directory, md_file)

print(f"Markdown 文档已创建: {md_file_path}")
