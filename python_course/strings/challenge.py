logs = [
    "INFO | 2026-11-01 10:30:15 | AUTH | User logged in",
    "ERROR | 2026-11-01 10:31:42 | DATABASE | Connection timeout",
    "WARNING | 2026-11-01 10:32:10 | AUTH | Failed login attempt",
    "INFO | 2026-11-01 10:33:05 | API | Request processed in 250ms",
    "ERROR | 2026-11-01 10:34:20 | API | Request failed with status 500",
    "INFO | 2026-11-01 10:35:00 | DATABASE | Query executed in 120ms",
    "WARNING | 2026-11-01 10:36:15 | DATABASE | High query execution time",
    "INFO | 2026-11-01 10:37:30 | AUTH | User logged out"
]

def normalization(logs):
    normalized_logs = []
    for log in logs:
        parts = [part.strip() for part in log.split('|')]
        if len(parts) == 4:
            level, timestamp, source, message = parts
            normalized_log = {
                'level': level,
                'timestamp': timestamp,
                'source': source,
                'message': message
            }
            normalized_logs.append(normalized_log)

    return normalized_logs

def statistics(logs):
    stats = {
        'INFO': 0,
        'ERROR': 0,
        'WARNING': 0
    }
    for log in logs:
        level = log['level']
        if level in stats:
            stats[level] += 1
    return stats


def get_logs_by_level(logs, level):
    filtered_logs = []
    for log in logs:
        if log['level'].upper() == level.upper():
            filtered_logs.append(log)
    return filtered_logs


def numerical_analysis(logs):
    operations = []
    for log in logs:
        time = ''.join(filter(str.isdigit, log['message']))
        if f'{time}ms' in log['message']:
            operations.append(int(time))

    return {
        'total_operations': len(operations),
        'average_time': sum(operations) / len(operations) if operations else 0,
        'max_time': max(operations) if operations else 0,
        'min_time': min(operations) if operations else 0
    }

    


nm_logs = normalization(logs)
# print(statistics(nm_logs))
# print(get_logs_by_level(nm_logs, 'ERROR'))
print(numerical_analysis(nm_logs))