from datetime import datetime
from logger import get_logger, check_heartbeat

def heartbeat(log_file, result_file):
    key = 'Key TSTFEED0300|7E3E|0400'
    filter_log = []
    get_logger(result_file)
    with open(log_file, 'r', encoding='utf-8') as file:
        for line in file:
            if key in line:
                filter_log.append(line)

    for i in range(len(filter_log) - 1):
        before_line = filter_log[i]
        after_line = filter_log[i + 1]
        before_position = before_line.find('Timestamp ')
        after_position = after_line.find('Timestamp ')
        before_time = before_line[before_position + 10:before_position + 18]
        after_time = after_line[after_position + 10:after_position + 18]
        before_time = datetime.strptime(before_time, '%H:%M:%S')
        after_time = datetime.strptime(after_time, '%H:%M:%S')
        heartbeat = (before_time - after_time).total_seconds()
        event_time = before_time.strftime('%H:%M:%S')

        check_heartbeat(heartbeat, event_time)

    return result_file

if __name__ == '__main__':
    result = heartbeat('hblog.txt', 'hb_test.log')
    print('Analysis completed. Result file:', result)