# Comparison of Docker and Virtual Machine for Flask Web Application

## Overview

This document compares the performance of a Flask-based Python web application running in Docker containers versus Virtual Machines (VMs). The key metrics evaluated are average startup time, memory usage, and CPU usage when Idle.

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

| Metric | Docker (Container) | VM |
| --- | --- | --- |
| **Average Startup Time** (seconds) | 1.6  | 26.225 |
| **Idle Memory Usage** (MB) | 53 | 89 |
| **Idle CPU Usage** (%) | 0.02 | 0.27 |

### Conclusion

From the results, it is evident that running a Flask-based Python web application in Docker provides significant advantages over traditional Virtual Machines in terms of:

- **Startup Time**: Faster startup with containers.
- **Memory Usage**: Lower memory footprint.
- **CPU Usage**: More efficient CPU utilization.