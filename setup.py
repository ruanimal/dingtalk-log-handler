from setuptools import setup, find_packages
from dingtalk_log_handler import __author__, __version__

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='dingtalk-log-handler',
    version=__version__,
    author=__author__,
    author_email='ruan.lj@foxmail.com',
    description='log handler for send message to dingtalk',
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    packages=find_packages(),
    python_requires='>=3.5',
    install_requires=[],
    project_urls={
        'Source': 'https://github.com/ruanimal/dingtalk-log-handler',
        'Tracker': 'https://github.com/ruanimal/dingtalk-log-handler/issues',
    },
)
