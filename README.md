# shus-benchmark 
benchmarks for self-hosted url shortener

This a research repository for benchmarking of very limited set of web
 technologies and frameworks. The purpose of the project is to help make
  framework choice for the shus project based on data.
  
The benchmarks were run on 16 cpu 8GB RAM virtual machine in Docker
 environment. 
 
Each server implementation is capable of loading redirect definitions from
 json file (1M urls) to memory and respond with appropriate http redirect
  or  404. 
 
Wrk was used for the testing (with params `-c64 -d5s -t8`) using lua script
 which preloads test urls selected from the known urls with exponential
  distribution.  
  
All results show number of requests per second handled by the server

![complete-chart](complete-chart.png)

python implementations

![python-chart](python-chart.png)

Data in [Google spreadsheet](https://docs.google.com/spreadsheets/d/172PCKdGEwJ7Po4p1TjBp1uGxplCJ8Z8VQS9P0jG_9uU/edit?usp=sharing) - with stdev for each measurement 
