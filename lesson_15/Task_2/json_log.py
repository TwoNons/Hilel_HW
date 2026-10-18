import logging

def log_json(file):
    # Створення та налаштування логера
    logging.basicConfig(
        filename='json_vystavnoy.log',
        level=logging.ERROR,
        format='%(asctime)s - %(levelname)s - %(message)s'
        )
    logger = logging.getLogger("file")
    logger.error(f'Неправильний формат файлу {file}')