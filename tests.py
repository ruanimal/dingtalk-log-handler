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

def test_message():
    logging.error('testing')
