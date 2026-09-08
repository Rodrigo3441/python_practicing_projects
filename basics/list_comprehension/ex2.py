def convert_high_latencies(latencies):
    return [latency * 1000 for latency in latencies if latency > 0.08]


latencies_seconds = [0.023, 0.087, 0.045, 0.102, 0.034, 0.156, 0.067]

result = convert_high_latencies(latencies_seconds)

print(result)