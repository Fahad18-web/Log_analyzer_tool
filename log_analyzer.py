from collections import Counter , defaultdict
import sys
# *************** Problem 1: Basic Log File Reader ****************

# def read_log_file(file_path):
#     with open(file_path, 'r') as f:
#         for line in f:
#             print(line.strip())

# read_log_file('server.log')            

# *************** Problem 2: Log File Parsing *****************


# def read_log_file(file_path):
#     with open(file_path,'r') as f:
#         for line in f:
#             line = line.strip()
#             parts = line.split(' ')
#             print(parts)
# read_log_file('server.log')        

# *************** Problem 3: Log File Analysis ****************
# def read_log_file(file_path):
#     with open(file_path,'r') as f:
#         for line in f:
#             line = line.strip()
#             parts = line.split(' ')
#             timestamp = parts[0]
#             ip_address = parts[1]
#             request_method = parts[2]
#             request_path = parts[3]
#             status_code = parts[4]
#             response = parts[5]
#             print(f'IP Address: {ip_address} | Request Method: {request_method} | Status Code: {status_code}')

# read_log_file('server.log')            


# *************** Problem 4: Handling Blank Lines ****************
# def read_log_file(file_path):
#     with open(file_path,'r') as f:
#         for line in f:
#             line = line.strip()
#             if not line:
#                 continue
#             parts = line.split(' ')
#             if len(parts) < 6:
#                 print(f'Incomplete line skipped: {line}')
#                 continue
#             timestamp = parts[0]
#             ip_address = parts[1]
#             request_method = parts[2]
#             request_path = parts[3]
#             status_code = parts[4]
#             request_response = parts[5]    
#             print(f'IP Address: {ip_address} | Request Method: {request_method} | Status Code: {status_code}')
# read_log_file('server.log')            


# *************** Problem 5: Status Code Counting ****************

# def read_log_file(file_path):
#     status_counter = Counter()
#     with open(file_path,'r') as f:
#          for line in f:
#             line = line.strip()
#             if not line:
#                 continue
#             parts = line.split(' ')
#             if len(parts) < 6:
#                 print(f'Incomplete line skipped: {line}')
#                 continue
#             timestamp = parts[0]
#             ip_address = parts[1]
#             request_method = parts[2]
#             request_path = parts[3]
#             status_code = parts[4]
#             request_response = parts[5]    
#             status_counter[status_code] += 1

#             print(f'IP Address: {ip_address} | Request Method: {request_method} | Status Code: {status_code}')
#     print("\n*** Status Code Report ***")
#     for code, count in status_counter.items():
#         print(f"Status {code}: {count} time comes")
# read_log_file('server.log')        


# *************** Problem 6: Slowest Endpoints ****************

# def read_log_file(file_path):
#     status_counter = Counter()
#     path_times = defaultdict(list)
#     with open(file_path,'r') as f:
#          for line in f:
#             line = line.strip()
#             if not line:
#                 continue
#             parts = line.split(' ')
#             if len(parts) < 6:
#                 print(f'Incomplete line skipped: {line}')
#                 continue
#             timestamp = parts[0]
#             ip_address = parts[1]
#             request_method = parts[2]
#             request_path = parts[3]
#             status_code = parts[4]
#             request_response = parts[5]    
#             # count status codes within loop
#             status_counter[status_code] += 1

#             if request_response.endswith('ms'):
#                 ms = float(request_response.replace('ms', ''))
#                 path_times[request_path].append(ms)

#             print(f'IP Address: {ip_address} | Request Method: {request_method} | Status Code: {status_code}')
#     print("\n*** Status Code Report ***")
#     for code, count in status_counter.items():
#         print(f"Status {code}: {count} time comes")
#     print("\n Top 3 Slowest Endpoints ")
#     path_avg = {}
#     for p, times in path_times.items():
#         path_avg[p] = sum(times) / len(times)

#     sorted_paths = sorted(path_avg.items(), key=lambda x: x[1], reverse=True)

#     for p, avg in sorted_paths[:3]:
#         print(f"{p} — Average: {avg:.1f}ms")    
# if len(sys.argv) < 2:
#        print("Usage: python log_analyzer.py <logfile>")
# else:
#        read_log_file(sys.argv[1])         