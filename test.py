import pytest
import random

n=2048

A = [[random.random() for _ in range(n)] for _ in range(n)]
B = [[random.random() for _ in range(n)] for _ in range(n)]
C = [[0 for _ in range(n)] for _ in range(n)]

@pytest.mark.benchmark(min_rounds=2)
@pytest.mark.parametrize('n', [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048])
def test_benchmark(benchmark, n):
    benchmark(matrix_multiplication, A, B, n)


def matrix_multiplication(A, B, n):
    for i in range(n):
        for j in range(n):
            sum = 0
            for k in range(n):
                sum += A[i][k] * B[k][j]

        C[i][j] = sum