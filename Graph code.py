import matplotlib.pyplot as plt

# Data for 2DBC-15
matrix_sizes = [5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000]
communication_15 = [0.307336, 2.41213, 7.10599, 14.4076, 24.3168, 36.8338, 51.9585, 69.6909, 90.031, 112.979]
time_15 = [1.718922e-01, 3.266219e-01, 5.570020e-01, 9.297894e-01, 1.326137e+00, 1.838384e+00, 2.504529e+00, 3.502839e+00, 4.410983e+00, 5.479381e+00]
gflops_15 = [2.424727e+02, 1.020701e+03, 2.019943e+03, 2.868248e+03, 3.927684e+03, 4.895849e+03, 5.706575e+03, 6.090526e+03, 6.886449e+03, 7.604494e+03]

# Data for 2DBC-16
communication_16 = [0.307336, 2.44007, 7.32951, 15.0129, 25.4903, 38.7616, 54.827, 73.6862, 95.3395, 119.787]
time_16 = [1.509277e-01, 3.661681e-01, 5.760943e-01, 1.026694e+00, 1.378679e+00, 1.930401e+00, 2.579379e+00, 3.317456e+00, 4.281439e+00, 5.224904e+00]
gflops_16 = [2.761532e+02, 9.104652e+02, 1.953001e+03, 2.597529e+03, 3.777996e+03, 4.662477e+03, 5.540978e+03, 6.430871e+03, 7.094814e+03, 7.974867e+03]

# Data for SBC-15
matrix_sizes_sbc = [3000, 5004, 10008, 15012]
communication_sbc = [0.201166, 0.757188, 3.07399, 6.86473]
time_sbc = [4.671684e-02, 8.860062e-02, 1.950418e-01, 3.164829e-01]
gflops_sbc = [1.927464e+02, 4.715460e+02, 1.713397e+03, 3.563589e+03]

# Plotting matrix size vs time for all versions
plt.figure(figsize=(10, 6))
plt.plot(matrix_sizes, time_15, marker='o', label='2DBC-15 Time')
plt.plot(matrix_sizes, time_16, marker='o', label='2DBC-16 Time')
plt.plot(matrix_sizes_sbc, time_sbc, marker='o', label='SBC-15 Time')
plt.xlabel('Matrix Size')
plt.ylabel('Total running time (sec)')
plt.title('Matrix Size vs Time')
plt.legend()
plt.grid(True)
plt.show()

# Plotting matrix size vs GFLOPS for all versions
plt.figure(figsize=(10, 6))
plt.plot(matrix_sizes, gflops_15, marker='o', label='2DBC-15 GFLOPS')
plt.plot(matrix_sizes, gflops_16, marker='o', label='2DBC-16 GFLOPS')
plt.plot(matrix_sizes_sbc, gflops_sbc, marker='o', label='SBC-15 GFLOPS')
plt.xlabel('Matrix Size')
plt.ylabel('GFLOPS/ node')
plt.title('Matrix Size vs GFLOPS')
plt.legend()
plt.grid(True)
plt.show()

# Plotting matrix size vs communication for all versions
plt.figure(figsize=(10, 6))
plt.plot(matrix_sizes, communication_15, marker='o', label='2DBC-15 Communication')
plt.plot(matrix_sizes, communication_16, marker='o', label='2DBC-16 Communication')
plt.plot(matrix_sizes_sbc, communication_sbc, marker='o', label='SBC-15 Communication')
plt.xlabel('Matrix Size')
plt.ylabel('Communication volume')
plt.title('Matrix Size vs Communication')
plt.legend()
plt.grid(True)
plt.show()
