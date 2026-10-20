'''
This simulates a disk usage monitoring tool — like a simplified df command that raises alerts.

The Input

Line 1: A threshold number T (here 80). Any filesystem at or above this percentage triggers a warning.

Line 2: How many filesystem lines follow (here 4).

Lines 3 onward: Each line has three parts:

device   use%   mountpoint
/dev/sda1  91%   /
/dev/sdb1  82%   /mnt/my disk
tmpfs      95%   /run
/dev/sdc1  20%   /data

mountpoint may contain whitespacee in between, this is valid
Skip any line where the device is tmpfs or overlay — these are virtual filesystems, not real disks. mount point may contains spaces
For everything else, check if the usage percentage ≥ threshold.
Print warnings for those that meet/exceed the threshold, sorted by highest percentage first. If two have the same percentage, sort by mount point alphabetically.
Last line: print exit 1 if there were any warnings, exit 0 if none.
'''


import sys

def disk_alert():
    '''
    approach here is to read from stdin line by line. then go through the log lines
    line.strip(None, 2) strips but only the first 2 characters, the rest get returned in the third element
    we use this because the mountpoint may contain spaces between words, splitting everything would not be accurate

    the we do rsplit to                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        

    '''
    threshold = int(sys.stdin.readline().strip())
    number_of_lines = int(sys.stdin.readline().strip())
    
    warnings = []
    for line in sys.stdin:
        device, usage, mount = line.strip().split(None, 2)
        
        if device in ("tmpfs", "overlay"):
            continue
            
        usage_percentage = int(usage.rstrip("%"))
        if usage_percentage >= threshold:
            warnings.append((usage_percentage, mount))
            
    warnings.sort(key=lambda x: (-x[0], x[1]))
    for usage_percentage, mount in warnings:
        print(f"WARN {mount} {usage_percentage}%")
    print("exit 1") if warnings else print("exit 0")
    
    