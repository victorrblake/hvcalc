from math import ceil
#
servers = {'DL360G9_E5-2697v3':[14,2.6],
           'DL360G9_E5-2699v3':[22,2.2]}
# https://en.wikipedia.org/wiki/List_of_Intel_Xeon_microprocessors#Xeon_E5-26xx_v3_.28dual-processor.29

# background
print ('')
print ('HV Server Replacement')
print ('=====================')
print ('')
print ('CURRENT CLUSTER')
cluster_name = input('Enter a name or description for the cluster: ')
hv_count = int(input('Enter the # of hypervisors currently in the cluster: '))
# compute
hv_sockets = int(input('How many sockets per hypervisor? '))
hv_clock = float(input('Enter the clock rate in GHz:  '))
hv_cores = int(input('How many cores per socket? '))
cluster_ghz = hv_cores * hv_sockets * hv_clock * hv_count
print('Total clock available is: ',cluster_ghz)
# memory
hv_mem = int(input('How much memory in GB is available on each hypervisor? '))
cluster_mem = hv_count * hv_mem
print('Total memory avalable is: ',cluster_mem)
# utilization
print ('')
print ('UTILIZATION')
hv_clock_util=float(input('Enter the clock utilization for the cluster in GHz:  '))
hv_mem_util=int(input('Enter the memory uiltilization for the cluster in GB: '))
#
# options
print ('')
print ('NEW SERVER OPTION A')
a_desc = input('Enter a brief description for the first option: ')
a_mem = int(input('Enter the memory in GB for the first option: '))
a_socket = int(input('Enter the number of sockets: '))
a_cores = int(input('Enter the the number of cores per socket: '))
a_clock = float(input('Enter the clock rate in GHz: '))
a_n = int(input('Enter the number of HOT spares 2 for N+2, 1 for N+1, etc. needed: '))
#
# OPTION A
#
# calculations for option a
#
a_ghz = a_cores * a_socket * a_clock
hv_a_ghz = hv_clock_util / a_ghz
hv_a_mem = hv_mem_util / a_mem
# raw calculations
print ('Calculated # of hypervisors required for CPU: ',hv_a_ghz)
print ('Calculated # of hypervisors required for memory: ',hv_a_mem)
# ceiling calculations
hv_a_ghz = ceil(hv_clock_util / a_ghz)
hv_a_mem = ceil(hv_mem_util / a_mem)
if hv_a_ghz > hv_a_mem:
    hv_a_required = hv_a_ghz
else:
    hv_a_required = hv_a_mem
hv_a_buy = hv_a_required + a_n
# option a output
print ('')
print ('NEW CLUSTER OPTIONS')
print ('')
print ('Cluster Option A: ',a_desc)
print ('Memory per hypervisor in GB: ',a_mem)
print ('Clock per hypervisor in GHz: ',a_ghz)
# required
print ('# of hypervisors required for CPU: ',hv_a_ghz)
print ('# of hypervisors required for memory: ',hv_a_mem)
print ('# of hypervisors required for CPU and memory (workload): ', hv_a_required)
# work capabilities
print ('Cluster memory available in GB: ',hv_a_required * a_mem)
print ('Cluster clock available in GHz: ',hv_a_required * a_ghz)
# N+     
print ('# of hypervisors required for N+',a_n,' is: ', hv_a_buy)
# N+ work capabilities
print ('Cluster memory with N+',a_n,'available in GB: ', hv_a_buy * a_mem)
print ('Cluster clock with N+',a_n,'available in GHz: ',hv_a_buy * a_ghz)
# use of capital
print ('Percentage of capital supporting workload: ', hv_a_required/hv_a_buy*100)
print ('Percentage of capital for reliaiblity: ', a_n/hv_a_buy*100)
print ('')
# end of option a
