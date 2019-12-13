import statistics
datasets=[2,5,8,4,9]
x=statistics.mean(datasets)
print("Mean is:",x)

datasets1=[-7,5,8,9,12,3,4]
print("Median of data-set is: % s" % (statistics.median(datasets1)))

datasets2=[5,9,6,2,4,3,5,5,8,7,5]
print("Calculated Mode is: %s" %(statistics.mode(datasets2)))

datasets3=[7,8,5,2,4]
print("Standard deviation of sample is: %s" %(statistics.stdev(datasets3)))

set1=[2,5,6,4,9]
print("Low median of data-set is: %s" %(statistics.median_low(set1)))

set2=[9,6,7,5,1,4]
print("High median of data-set is: %s" %(statistics.median_high(set2)))