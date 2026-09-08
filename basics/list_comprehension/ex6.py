def get_all_hostnames(departments):
    return [
        server['hostname']
        for department in departments
            for server in department['servers']
    ]

departments = [
    {
        "name": "Engineering",
        "servers": [
            {"hostname": "eng-web-01", "latency": 34},
            {"hostname": "eng-db-01", "latency": 97},
        ]
    },
    {
        "name": "Finance",
        "servers": [
            {"hostname": "fin-db-01", "latency": 121},
            {"hostname": "fin-web-01", "latency": 45},
        ]
    },
    {
        "name": "Operations",
        "servers": [
            {"hostname": "ops-01", "latency": 88},
            {"hostname": "ops-02", "latency": 29},
        ]
    }
]

result = get_all_hostnames(departments)

for i in result:
    print(i)