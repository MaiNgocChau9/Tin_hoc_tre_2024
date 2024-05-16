def submatrix_count(matrix, K):
    count = 0
    # Create prefix sum matrix
    prefix_sum = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            prefix_sum[i][j] = (
                prefix_sum[i][j - 1]
                + prefix_sum[i - 1][j]
                - prefix_sum[i - 1][j - 1]
                + matrix[i - 1][j - 1]
            )
    # Iterate over all pairs of columns
    for left_col in range(1, m + 1):
        for right_col in range(left_col, m + 1):
            # Calculate prefix sum for each row
            row_sum = [
                prefix_sum[i][right_col]
                - prefix_sum[i][left_col - 1]
                - prefix_sum[i - 1][right_col]
                + prefix_sum[i - 1][left_col - 1]
                for i in range(1, n + 1)
            ]
    # Count subarrays with sum equal to K
    cumulative_sum = 0
    sum_freq = {}
    sum_freq[0] = 1
    # Initialize with 0 to handle subarrays starting from the first row
    for row_sum_val in row_sum:
        cumulative_sum += row_sum_val
        if cumulative_sum - K in sum_freq:
            count += sum_freq[cumulative_sum - K]
        sum_freq[cumulative_sum] = sum_freq.get(cumulative_sum, 0) + 1
    return count

input_file = open("submatrixk.inp")
output_file = open("submatrixk.out", "w")
# Read input
n, m, k = map(int, input_file.readline().split())
matrix = [list(map(int, input_file.readline().split())) for _ in range(n)]
# Calculate result
result = submatrix_count(matrix, k)
output_file.write(str(result) + "\n")
input_file.close()
output_file.close()