from setuptools import setup, find_packages
from dingtalk_log_handler import __author__, __version__


setup(
    name='dingtalk-log-handler',
    version=__version__,
    author=__author__,
    author_email='ruan.lj@foxmail.com',
    description='',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python :: 3'
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    packages=find_packages(),
    python_requires='>=3.5',
    include_package_data=True,
    install_requires=[],
    project_urls={
        'Source': 'https://github.com/ruanima/dingtalk-log-handler',
        'Tracker': 'https://github.com/ruanima/dingtalk-log-handler/issues',
    },
)
