def create_latency_alerts(servers):
    return [
        {
           'server_id': server['id'],
           'hostname': server['hostname'],
           'latency': server['latency']
        }
        for server in servers
        if server['latency'] > 80
    ]

servers = [
    {"id": 101, "hostname": "web-01", "latency": 34},
    {"id": 102, "hostname": "db-01", "latency": 112},
    {"id": 103, "hostname": "cache-01", "latency": 67},
    {"id": 104, "hostname": "web-02", "latency": 95},
    {"id": 105, "hostname": "backup-01", "latency": 143},
]

result = create_latency_alerts(servers)

for i in result:
    print(i)