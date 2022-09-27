# 钉钉群告警Handler

通过钉钉群机器人, 发送Python日志到钉钉群

参考钉钉群机器人接口 https://open.dingtalk.com/document/robots/custom-robot-access

## 安装
pip install dingtalk-log-handler

## 打包
python setup.py sdist

## 参数
- webhook: webhook url for dingtalk open api
- keyword: allowed message keyword, default 'alarm'
- secret: secret for dingtalk open api
- hostname: hostname for identify machine, default local ip address
- timeout: http request timeout, default 1 second
- cert_verify: verify SSL certificates or not, default True

## 使用示例
```python
import logging
import logging.config

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[%(levelname)s %(asctime)s %(name)s %(funcName)s %(lineno)d %(process)d]\t%(message)s'
        },
    },
    'handlers': {
        'dingtalk':{
            'class': 'dingtalk_log_handler.DingTalkHandler',
            'webhook': 'https://oapi.dingtalk.com/robot/send?access_token=XXXXX',
            # 'secret': '',
            # 'keyword': '',
            'formatter':'verbose',
            'level': 'ERROR',
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        '': {
            'handlers': ['dingtalk', 'console'],
            'level': 'INFO',
            'propagate': False,
        },
    }
}

logging.config.dictConfig(LOGGING)
logging.error('testing')
```
