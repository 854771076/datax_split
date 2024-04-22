from distutils.core import setup
from setuptools import find_packages

with open("README.md", "r",encoding='utf8') as f:
  long_description = f.read()

setup(name='datax_split',    # 包名
      version='0.1.0',        # 版本号
      description='test pip upload',
      long_description=long_description,
      author='fiang',
      author_email='854771076@qq.com',
      url='',
      install_requires=['pandas','pymysql'],	# 依赖包会同时被安装
      license='MIT',
      packages=find_packages())
