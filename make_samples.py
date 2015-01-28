import numpy as np
import csv

params = ["a", "b", "c", "d", "BEER"]
nparam = len(params)
niter = 400

# use the CSV writer
f = open("mc.csv", "w")
writer = csv.writer(f)

# write the header
writer.writerow(params)

for i in range(niter):

    # Insert these lines of code inside the part where your MCMC algorithm logs
    # the samples
    proposed_param = np.random.rand(nparam)
    writer.writerow(proposed_param)
    
# when you're done, be sure to close the file
f.close()
