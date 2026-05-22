import random
import sys

# Possible values
IPs      = ['192.168.1.42', '10.0.0.7', '172.16.0.5']
Methods  = ['GET', 'POST', 'PUT', 'DELETE']
Paths   = ['/api/users', '/api/login', '/api/products', '/api/orders']
Statuses = ['200', '200', '200', '401', '404', '500']

def generate_logs(output_file, total_lines):
    with open(output_file, 'w') as f:
        for i in range(total_lines):
            
            roll = random.random()
            
            # there is 5% chance of a blank line
            if roll < 0.05:
                f.write('\n')
                continue
            
            # there is 5% chance of a incomplete line
            if roll < 0.10:
                f.write('%%partial write%%\n')
                continue
            
            # Normal line
            ip     = random.choice(IPs)
            method = random.choice(Methods)
            path   = random.choice(Paths)
            status = random.choice(Statuses)
            ms     = random.randint(10, 2000)
            
            line = f"2024-03-15T14:23:01Z {ip} {method} {path} {status} {ms}ms\n"
            f.write(line)
    
    print(f"Log file ready: {output_file} ({total_lines} lines)")
generate_logs('server.log', 1000)