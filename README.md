# EE-708-GNU-Radio-Project
# Step I

You have to pick a value of M, say 8.

generate a random codebook of M vectors of length N.

Each element can be taken IID complex  Gaussian N(0,P)
  
Take a 3bit data stream, and send the corresponding codeword for each data point.

The receiver adds IID noise of unit variance.

Do a maximal likelihood decoding to get the bits back in each block.

Plot the end to end bit error rate, as a function of P.

# Step II

Choose M=8 and N=20, repeat the above steps.

# Step III

Make the codebook using IID  QPSK samples, and find BER.

# Step IV

Construct a typical decoder for this scheme.
