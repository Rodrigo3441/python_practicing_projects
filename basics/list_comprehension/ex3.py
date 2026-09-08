def get_slow_online_devices(devices):
    return [
            device['hostname']
            for device in devices 
            if device['latency'] > 80 and device['status'] == 'online'
        ]
    pass

devices = [
    {"hostname": "router-01", "latency": 23, "status": "online"},
    {"hostname": "switch-01", "latency": 91, "status": "online"},
    {"hostname": "server-01", "latency": 120, "status": "offline"},
    {"hostname": "server-02", "latency": 87, "status": "online"},
    {"hostname": "ap-01", "latency": 42, "status": "online"},
    {"hostname": "switch-02", "latency": 105, "status": "online"},
]

result = get_slow_online_devices(devices)
print(result)