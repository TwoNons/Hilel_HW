import logging


#log_message = f"Login event - Username: {username}, Status: {status}"

    # Створення та налаштування логера
logging.basicConfig(
        filename='login_system.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
        )
logger = logging.getLogger("my_logger")

     # Логування події

"""#1 Завдання. Логування аргуменiв"""
def log_args_result(func):
    def wrapper(*args, **kwargs):
        logger.info(f'Аргументы функции {func.__name__}: {args}')
        result = func(*args, **kwargs)
        logger.info(f'Результат функции {func.__name__}: {result}')
        return result
    return wrapper

"""#2 Завдання. Обробка вийняткiв"""
def exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(f'Ошибка в функции {func.__name__}: {e}')
            return None
    return wrapper