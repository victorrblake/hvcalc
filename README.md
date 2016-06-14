# hvcalc
Calculate # of servers required for a hv cluster

input: current hv cluster information, utilization (GHz and memory utilized), and parameters for new hypervisor (memory, socket count, cores/socket, clock rate), desired redundancy (N+0, N+1, N+2)
action: calculate the number of hv required
export: text with number of hypervisors required

Currently allows the naming and entry of one server configuration on each run. 

Future:
- expand to 2-3 options to compare
- pre-loaded libraries with intel configurations (typical Xeon)
- API load intel configs ?
- Grab HV utilization stats from vrops or vcenter API for vmware
- save configurations to libraries
- save configurations/libraries to files
- django integration and run this from a web page
