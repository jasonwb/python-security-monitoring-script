#!/usr/bin/env python3

import os
import datetime

LOG_FILE = "/var/log/security_monitor.log"

def log_network_connections():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    connections = os.popen("netstat -tunp").read()
    
    with open(LOG_FILE, "a") as log:
        log.write(f"\n[{timestamp}] Active Network Connections:\n")
        log.write(connections)

if __name__ == "__main__":
    log_network_connections()
