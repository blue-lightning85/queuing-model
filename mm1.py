# MM1 Queue Calculator

# Enter known values if unknown hit enter. The results will be
# listed in the terminal. If not enough information provided 
# answer will not calculate.

# Initalizing all values 
from wsgiref.validate import InputWrapper


arrive_rate = None
arrive_time = None
serv_rate = None
serv_time = None
wait_time = None
total_time = None
wait_num = None
total_num = None
server_num = None

if __name__ == "__main__" :
  arrive_rate = input("[1/9] Enter lambda(averagae arrival rate of new jobs): ")
  arrive_time = input("[2/9] Enter E[tau] (average interparival time): ")
  serv_rate = input("[3/9] Enter mu (average service rate): ")
  serv_time = input("[4/9] Enter Ws (average service time): ")
  wait_time = input("[5/9] Enter Wq (average time in queue): ")
  total_time = input("[6/9] Enter W (average time in syte): ")
  wait_num = input("[7/9] Enter Lq (average number of jobs in queu): ")
  total_time = input("[8/9] Enter L (average number of jobs in system): ")
  server_num = input("[9/9] Enter c (number of identical servers): ")
  
  
  