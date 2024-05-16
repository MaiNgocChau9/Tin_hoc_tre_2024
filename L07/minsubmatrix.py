input_file = open("minsubmatrix.inp")
output_file = open("minsubmatrix.out", "w")

n, m = map(int, input_file.readline().split())

matrix = [list(map(int, input_file.readline().split())) for _ in range(n)]

ans = matrix[0][0]

def solution_1():
    for top_left in range(n):
        for top_right in range(top_left, n):
            for bottom_left in range(top_left, n):
                for bottom_right in range(top_right, n):
                    sum = 0
                    for i in range(top_left, bottom_left + 1):
                        for j in range(top_right, bottom_right + 1):
                            sum += matrix[i][j]
                    ans = min(ans, sum)

prefix_sum = [[0] * m for _ in range(n)]
def init_prefix_sum():
    for i in range(1, n):
        for j in range(1, m):
            prefix_sum[i][j] = prefix_sum[i][j] + prefix_sum[i-1][j] - prefix_sum[i - 1][j - 1] + matrix[i-1][j-1]


def get_sum(top_left, top_right, bottom_left, bottom_right):
    return prefix_sum[bottom_left][bottom_right] - prefix_sum[bottom_left][top_right-1] + prefix_sum[top_left-1][top_right-1]

def solution_2():
    ans = matrix[0][0]
    for top_left in range(n):
        for top_right in range(top_left, n):
            for bottom_left in range(top_left, n):
                for bottom_right in range(top_right, n):
                    ans = min(ans, get_sum(top_left+1, top_right+1, bottom_left+1, bottom_right+1))

#! :))

init_prefix_sum()
solution_2()

print(ans)