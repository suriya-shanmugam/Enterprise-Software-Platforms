#!/bin/bash

# Record start time in milliseconds
start_time=$(($(date +%s%N)/1000000))

# Replace the following line with the command you want to measure
# Example: sleep 5

sudo docker run -d -p 5000:5000 autoexpense_docker:v1 python app.py 

# Record end time in milliseconds
end_time=$(($(date +%s%N)/1000000))

# Calculate time difference in milliseconds
time_diff=$((end_time - start_time))

# Output the result
echo "Time taken: ${time_diff} ms"