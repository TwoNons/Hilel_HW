import logging

def get_logger(log_file):
    logging.basicConfig(
        filename=log_file,
        filemode='w',
        level=logging.WARNING,
        format='%(asctime)s %(levelname)s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        force=True
    )

def check_heartbeat(heartbeat, event_time):
    message = (
        f'Heartbeat delay: {heartbeat} seconds. '
        f'Event time: {event_time}'
    )

    if 31 < heartbeat < 33:
        logging.warning(message)

    elif heartbeat >= 33:
        logging.error(message)