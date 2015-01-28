# chain.js
Quick and easy web plots of MCMC samples

Got some long-running MCMC chains on the cluster? Would you like to periodically check up on them? Write the samples to a CSV file and use your browser to check up on the progress.

Input: 2D array in CSV file (easy to append), with parameters as headers. File has `nparam` columns and `nsamples` rows.

Output: a plot with one column and `nparam` rows, displaying parameter value as a function of MCMC iteration.

For an example of how to set up your MCMC code to use `chain.js`, see `make_samples.py`.
