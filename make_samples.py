import numpy as np

params = ["a", "b", "c", "d"]
nparam = len(params)
niter = 400

f = open("mc.csv", "w")

# write the header
f.write(",".join(params) + "\n")
f.close()

for i in range(niter):

    # Insert these three lines of code inside your likelihood call
    f = open("mc.csv", "a")
    f.write(",".join([str(i) for i in np.random.rand(nparam)]) + "\n")
    f.close()

f.close()
