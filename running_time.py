current_time=6+52/60
distance1=1
pace1=8+15/60
distance2=3
pace2=7+12/60
distance3=1
pace3=8+15/60
running_time_in_minutes=distance1/pace1+distance2/pace2+distance3/pace3
running_time = running_time_in_minutes / 60
arrival_time = current_time + running_time
print ((arrival_time//1)+":"+((arrival_time-arrival_time//1)*60))