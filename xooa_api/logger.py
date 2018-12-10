import logging


class Logger:

    def get_logger(self, logging_level):
        name = 'XooaLogger'
        log_format = '%(asctime)s  %(name)8s  %(levelname)5s  %(message)s'
        logging.basicConfig(level=logging.INFO,
                            format=log_format,
                            filename='dev.log',
                            filemode='w')
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        console.setFormatter(logging.Formatter(log_format))
        logging.getLogger(name).addHandler(console)
        return logging.getLogger(name)
