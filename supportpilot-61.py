# === Stage 61: Add performance timing for core list and search operations ===
# Project: SupportPilot
import time

def benchmark_support_pilot():
    """Run core list and search operations with timing."""
    start_time = time.perf_counter()
    
    # Simulate listing all requests
    request_list = [
        {"id": i, "title": f"Request {i}", "owner": f"user{i % 5}", 
         "status": ["open", "in_progress", "resolved"][i % 3]}
        for i in range(100)
    ]
    
    list_time = time.perf_counter() - start_time
    
    # Simulate searching requests by status
    target_status = "open"
    search_start = time.perf_counter()
    
    filtered_requests = [r for r in request_list if r["status"] == target_status]
    
    search_end = time.perf_counter() - search_start
    
    print(f"List operation took: {list_time * 1000:.2f}ms")
    print(f"Search operation took: {search_end * 1000:.2f}ms")
    print(f"Found {len(filtered_requests)} open requests out of {len(request_list)} total.")

benchmark_support_pilot()
