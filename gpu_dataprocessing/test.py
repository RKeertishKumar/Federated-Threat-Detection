import numba

# Check if CUDA GPU support is available
cuda_available = numba.cuda.is_available()

# Print the result
print("CUDA GPU support available:", cuda_available)
