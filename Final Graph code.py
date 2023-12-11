import matplotlib.pyplot as plt

# Data for 2DBC-15
matrix_sizes_15 = [5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000]
gflops_15 = [2.424727e+02, 1.020701e+03, 2.019943e+03, 2.868248e+03, 3.927684e+03, 4.895849e+03, 5.706575e+03, 6.090526e+03, 6.886449e+03, 7.604494e+03]

# Data for 2DBC-16
gflops_16 = [2.761532e+02, 9.104652e+02, 1.953001e+03, 2.597529e+03, 3.777996e+03, 4.662477e+03, 5.540978e+03, 6.430871e+03, 7.094814e+03, 7.974867e+03]

# Data for SBC-15
matrix_sizes_sbc_15 = [3000, 5004, 10008, 15012]
gflops_sbc_15 = [1.927464e+02, 4.715460e+02, 1.713397e+03, 3.563589e+03]

# Plotting GFLOPS for all versions
plt.figure(figsize=(10, 6))

plt.plot(matrix_sizes_15, gflops_15, marker='o', label='2DBC-15 GFLOPS')
plt.plot(matrix_sizes_15, gflops_16, marker='o', label='2DBC-16 GFLOPS')
plt.plot(matrix_sizes_sbc_15, gflops_sbc_15, marker='o', label='SBC-15 GFLOPS')

# Previously included data for 2DBC-20, 2DBC-21, and SBC-21
matrix_sizes_20 = [5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000]
gflops_20 = [2.879458e+02, 9.596935e+02, 1.931418e+03, 2.732061e+03, 3.592458e+03, 4.618281e+03, 5.346373e+03, 6.190008e+03, 6.937031e+03, 7.883767e+03]
gflops_21 = [3.138885e+02, 1.022484e+03, 1.987069e+03, 3.557344e+03, 4.601253e+03, 5.417734e+03, 6.097422e+03, 6.924790e+03, 8.077562e+03]
matrix_sizes_sbc = [5005, 10003, 15001]
gflops_sbc = [3.706715e+02, 1.747507e+03, 3.722165e+03]

plt.plot(matrix_sizes_20, gflops_20, marker='o', label='2DBC-20 GFLOPS')
plt.plot(matrix_sizes_20[:len(gflops_21)], gflops_21, marker='o', label='2DBC-21 GFLOPS')
plt.plot(matrix_sizes_sbc, gflops_sbc, marker='o', label='SBC-21 GFLOPS')

plt.xlabel('Matrix Size')
plt.ylabel('GFLOPS')
plt.title('Comparison of GFLOPS for Different Versions')
plt.legend()
plt.grid(True)
plt.show()
