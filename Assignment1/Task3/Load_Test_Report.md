# Comparison of Docker and Virtual Machine for Flask Web Application Under Load

## Overview

This document compares the performance of a Flask-based Python web application running in Docker containers versus Virtual Machines (VMs) under a load of 1000 requests. The key metrics evaluated are average request throughput, average response times, Memory and CPU usage.

## Test Environment

- **Application**: Flask-based Python web application
- **Docker Version**: (e.g., Docker 27.2.1)
- **VM Platform**: (e.g., VirtualBox-Vagrant)
- **OS**: Ubuntu
- **Hardware Specs**:
    - CPU: Intel core i5-11260H * 12
    - RAM: 8 GB
    - Disk: SSD

## Metrics

Apache Benchmark: 

1000 concurrent request [ ab -n 1000 -c 1000 ]

| Metric | Docker (Container) | VM |
| --- | --- | --- |
| **Average Request Throughput** (req/s) | 2080 | 159 |
| **Average Response Time** (ms) | 0.4 | 250 |
| **Memory Usage**(MiB) | 67 | 150 |
| **CPU Usage** (%) | 59 | 11 |
| **Failed Request** | 0 | 419 |

## Conclusion

The results demonstrate that running a Flask-based Python web application in Docker provides significant advantages over traditional Virtual Machines in terms of:

- **Average Request Throughput**: Higher throughput in containers.
- **Average Response Time**: Faster response times in Docker.
- **Memory Usage**: More efficient memory usage in Docker

These advantages make Docker a preferable choice for deploying web applications, especially under heavy load scenarios.