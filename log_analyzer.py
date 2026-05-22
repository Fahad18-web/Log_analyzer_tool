from collections import Counter , defaultdict
from importlib.resources import path
from urllib import response

from streamlit import status
import sys

# This script reads a log file and prints its contents to the console.
# def read_log_file(file_path):
#     with open(file_path, 'r') as f:
#         for line in f:
#             print(line.strip())

# read_log_file('server.log')            

# This script reads a log file and coverts each line into list parts.
# def read_log_file(file_path):
#     with open(file_path,'r') as f:
#         for line in f:
#             line = line.strip()
#             parts = line.split(' ')
#             print(parts)
# read_log_file('server.log')        


# This script reads a log file and extracts specific parts of each line to print formatted output.
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

# This script reads a log file and handles blank lines and lines with insufficient parts.
# def read_log_file(file_path):
#     with open(file_path,'r') as f:
#         for line in f:
#             line = line.strip()
#             # Blank line? Skip karo
#             if not line:
#                 continue
#             parts = line.split(' ')
#              # Kam parts hain? Kharab line hai tou skip karo
#             if len(parts) < 6:
#                 print(f'Khrab line skip karo: {line}')
#                 continue
#             # Normal processing
#             timestamp = parts[0]
#             ip_address = parts[1]
#             request_method = parts[2]
#             request_path = parts[3]
#             status_code = parts[4]
#             request_response = parts[5]    
#             print(f'IP Address: {ip_address} | Request Method: {request_method} | Status Code: {status_code}')
# read_log_file('server.log')            

# This script reads a log file, extracts specific parts of each line, and counts the occurrences of each status code.
# def read_log_file(file_path):
#     status_counter = Counter()
#     with open(file_path,'r') as f:
#          for line in f:
#             line = line.strip()
#             if not line:
#                 continue
#             parts = line.split(' ')
#             if len(parts) < 6:
#                 print(f'Incomplete lines skipped: {line}')
#                 continue
#             timestamp = parts[0]
#             ip_address = parts[1]
#             request_method = parts[2]
#             request_path = parts[3]
#             status_code = parts[4]
#             request_response = parts[5]    
#             # count status codes within loop
#             status_counter[status_code] += 1

#             print(f'IP Address: {ip_address} | Request Method: {request_method} | Status Code: {status_code}')
#     print("\n*** Status Code Report ***")
#     for code, count in status_counter.items():
#         print(f"Status {code}: {count} time comes")
# read_log_file('server.log')        

# This script reads a log file, extracts specific parts of each line, counts the occurrences of each status code, and identifies the top 3 slowest endpoints based on average response time.
def read_log_file(file_path):
    status_counter = Counter()
    path_times = defaultdict(list)
    with open(file_path,'r') as f:
         for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(' ')
            if len(parts) < 6:
                print(f'Incomplete lines skipped: {line}')
                continue
            timestamp = parts[0]
            ip_address = parts[1]
            request_method = parts[2]
            request_path = parts[3]
            status_code = parts[4]
            request_response = parts[5]    
            # count status codes within loop
            status_counter[status_code] += 1

            if request_response.endswith('ms'):
                ms = float(request_response.replace('ms', ''))
                path_times[request_path].append(ms)

            print(f'IP Address: {ip_address} | Request Method: {request_method} | Status Code: {status_code}')
    print("\n*** Status Code Report ***")
    for code, count in status_counter.items():
        print(f"Status {code}: {count} time comes")
    print("\n*** Top 3 Slowest Endpoints ***")
    # extract average times for each path
    path_avg = {}
    for p, times in path_times.items():
        path_avg[p] = sum(times) / len(times)

    # sort paths by average response time in descending order
    sorted_paths = sorted(path_avg.items(), key=lambda x: x[1], reverse=True)

    for p, avg in sorted_paths[:3]:
        print(f"{p} — Average: {avg:.1f}ms")    
if len(sys.argv) < 2:
       print("Usage: python log_analyzer.py <logfile>")
else:
       read_log_file(sys.argv[1])         