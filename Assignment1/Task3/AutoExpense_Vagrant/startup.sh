

start_time=$(($(date +%s%N)/1000000))

# Replace the following line with the command you want to measure
# Example: sleep 5

vagrant up 

# Record end time in milliseconds
end_time=$(($(date +%s%N)/1000000))

# Calculate time difference in milliseconds
time_diff=$((end_time - start_time))

# Output the result
echo "Time taken: ${time_diff} ms"