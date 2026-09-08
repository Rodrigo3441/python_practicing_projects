# list comprehension
# [expression for item in iterable if condition]

def get_high_latencies(latencies):
    return [latency for latency in latencies if latency > 80]


latencies = [23, 87, 45, 102, 34, 156, 67, 12, 91, 48]

result = get_high_latencies(latencies)

print(result)