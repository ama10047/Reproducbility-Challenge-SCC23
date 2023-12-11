import matplotlib.pyplot as plt

# Data for 2DBC-20
matrix_sizes_20 = [5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000]
communication_20 = [0.307336, 2.47732, 7.96281, 16.9873, 29.5509, 45.6534, 65.295, 88.4756, 115.195, 145.454]
time_20 = [1.447466e-01, 3.473852e-01, 5.825320e-01, 9.761372e-01, 1.449884e+00, 1.948875e+00, 2.673266e+00, 3.446544e+00, 4.378820e+00, 5.285280e+00]
gflops_20 = [2.879458e+02, 9.596935e+02, 1.931418e+03, 2.732061e+03, 3.592458e+03, 4.618281e+03, 5.346373e+03, 6.190008e+03, 6.937031e+03, 7.883767e+03]

# Data for 2DBC-21
communication_21 = [0.307336, 2.47732, 7.06525, 30.417, 47.1808, 67.6699, 91.8843, 119.824, 151.489]
time_21 = [1.327833e-01, 3.260525e-01, 5.662171e-01, 1.464195e+00, 1.956087e+00, 2.638055e+00, 3.498878e+00, 4.386561e+00, 5.158477e+00]
gflops_21 = [3.138885e+02, 1.022484e+03, 1.987069e+03, 3.557344e+03, 4.601253e+03, 5.417734e+03, 6.097422e+03, 6.924790e+03, 8.077562e+03]

# Data for SBC-21
matrix_sizes_sbc = [5005, 10003, 15001]
communication_sbc = [0.914149, 3.80179, 8.55058]
time_sbc = [1.127800e-01, 1.909482e-01, 3.023341e-01]
gflops_sbc = [3.706715e+02, 1.747507e+03, 3.722165e+03]

# Plotting matrix size vs time for all versions
plt.figure(figsize=(10, 6))
plt.plot(matrix_sizes_20, time_20, marker='o', label='2DBC-20 Time')
plt.plot(matrix_sizes_20[:len(communication_21)], time_21, marker='o', label='2DBC-21 Time')
plt.plot(matrix_sizes_sbc, time_sbc, marker='o', label='SBC-21 Time')
plt.xlabel('Matrix Size')
plt.ylabel('Time')
plt.title('Matrix Size vs Time')
plt.legend()
plt.grid(True)
plt.show()

# Plotting matrix size vs GFLOPS for all versions
plt.figure(figsize=(10, 6))
plt.plot(matrix_sizes_20, gflops_20, marker='o', label='2DBC-20 GFLOPS')
plt.plot(matrix_sizes_20[:len(communication_21)], gflops_21, marker='o', label='2DBC-21 GFLOPS')
plt.plot(matrix_sizes_sbc, gflops_sbc, marker='o', label='SBC-21 GFLOPS')
plt.xlabel('Matrix Size')
plt.ylabel('GFLOPS')
plt.title('Matrix Size vs GFLOPS')
plt.legend()
plt.grid(True)
plt.show()

# Plotting matrix size vs communication for all versions
plt.figure(figsize=(10, 6))
plt.plot(matrix_sizes_20, communication_20, marker='o', label='2DBC-20 Communication')
plt.plot(matrix_sizes_20[:len(communication_21)], communication_21, marker='o', label='2DBC-21 Communication')
plt.plot(matrix_sizes_sbc, communication_sbc, marker='o', label='SBC-21 Communication')
plt.xlabel('Matrix Size')
plt.ylabel('Communication')
plt.title('Matrix Size vs Communication')
plt.legend()
plt.grid(True)
plt.show()
