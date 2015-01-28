import numpy as np

params = ["a", "b", "c", "d", "BEER"]
nparam = len(params)
niter = 400

f = open("mc.csv", "w")

# write the header
f.write(",".join(params) + "\n")
f.close()

for i in range(niter):

    # Insert these lines of code inside your likelihood call
    f = open("mc.csv", "a")
    proposed_param = np.random.rand(nparam)
    f.write(",".join([str(i) for i in proposed_param]) + "\n")
    f.close()

# when you're done, be sure to close the file
f.close()
