def classify_cpu_usage(servers):
    return [
        {
            'hostname': server['hostname'],
            'cpu_status': 'high' if server['cpu_usage'] > 80 else 'normal'
        }
        for server in servers
    ]

servers = [
    {"hostname": "web-01", "cpu_usage": 34},
    {"hostname": "db-01", "cpu_usage": 92},
    {"hostname": "cache-01", "cpu_usage": 67},
    {"hostname": "web-02", "cpu_usage": 81},
    {"hostname": "backup-01", "cpu_usage": 45},
]

result = classify_cpu_usage(servers)

for i in result:
    print(i)