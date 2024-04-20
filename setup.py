# setup.py文件内容
from setuptools import setup

setup(
    name='nonebot-plugin-sanyar',  # 应用名（pip安装和卸载时的名字）
    version='0.1.0',  # 当前版本
    author='afterow',  # 作者
    author_email='afterow@163.com', # 作者邮箱
    licence='MIT License',  # 许可协议
    url='https://github.com/afterow/nonebot-plugin-sanyao',   # 应用主页链接

    install_requires=['cnlunar','nonebot-adapter-onebot'],  # 依赖包
)
