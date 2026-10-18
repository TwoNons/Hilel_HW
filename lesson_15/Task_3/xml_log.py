import logging

def log_xml(message):
    logging.basicConfig(
        filename='xml_vystavnoy.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
        )
    logger = logging.getLogger("xml_logger")
    logger.info(message)