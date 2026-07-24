import logging


class CustomLogger:
    _loggers = {}
    _formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    @staticmethod
    def get_logger(
        file_path: str,
        name: str, 
        log_level: int, 
        log_formatter: bool):

        if not log_formatter:
            return CustomLogger.get_logger_per_line_no_formatter(
                name=name, 
                file_path=file_path,
                log_level=log_level)

        return CustomLogger.get_logger_per_line(
            name=name, 
            file_path=file_path,
            log_level=log_level)

    @staticmethod
    def get_logger_per_line(
        name: str, 
        log_level: int,
        file_path: str):
        
        if not file_path:
            file_path = f'./logs/{name}.log'
        
        logger = logging.getLogger(name)

        if logger.hasHandlers():
            logger.handlers = []

        logger.setLevel(log_level)

        handler = logging.FileHandler(file_path)
        handler.setLevel(log_level)
        handler.setFormatter(CustomLogger._formatter)
        logger.addHandler(handler)

        return logger
    
    @staticmethod
    def get_logger_per_line_no_formatter(
        name: str, 
        log_level: int,
        file_path: str):

        if not file_path:
            file_path = f'./logs/{name}.log'
        
        logger = logging.getLogger(name)

        if logger.hasHandlers():
            logger.handlers = []

        logger.setLevel(log_level)

        handler = logging.FileHandler(file_path)
        handler.setLevel(log_level)
        logger.addHandler(handler)

        return logger

    @staticmethod
    def write_log(
        name: str, 
        log_level: int, 
        log_message: str, 
        file_path: str = None,
        log_formatter: bool = True):
        
        logger = CustomLogger.get_logger(
            name=name, 
            log_level=log_level, 
            file_path=file_path,
            log_formatter=log_formatter)
        
        list_logging = {
            logging.DEBUG: logger.debug, #10
            logging.INFO: logger.info, #20
            logging.WARNING: logger.warning, #30
            logging.ERROR: logger.exception, #40
            logging.CRITICAL: logger.critical #50
        }
        
        if log_level not in list_logging:
            return False
        
        list_logging[log_level](log_message)
        CustomLogger.shutdown_log(loggers=logger)

    @staticmethod
    def shutdown_all_memory():
        for logger in CustomLogger._loggers.values():
            for handler in logger.handlers:
                handler.flush()
                handler.close()
        logging.shutdown()

    @staticmethod
    def shutdown_log(loggers):
        for handler in loggers.handlers:
            handler.close()
        logging.shutdown()

class TestLogger:
    @staticmethod
    def log(message):
        CustomLogger.write_log(
            name='test', 
            log_level=logging.INFO, 
            log_message=message)