import numpy as np
from scipy.stats import multivariate_normal

matrix_text = """
3,4,17,-3
5,11,-1,6
0,2,-5,8"""

with open("matrix.txt", "w") as file:
    file.write(matrix_text)

matrix = np.genfromtxt("matrix.txt", delimiter=',')

matrix_sum = np.sum(matrix)
matrix_max = np.max(matrix)
matrix_min = np.min(matrix)

print("Сумма всех элементов матрицы:", matrix_sum)
print("Максимальный элемент матрицы:", matrix_max)
print("Минимальный элемент матрицы:", matrix_min)


def run_length_encoding(x):
    unique_values, counts = np.unique(x, return_counts=True)
    return unique_values, counts


x = np.array([2, 2, 2, 3, 3, 3, 5])

values, counts = run_length_encoding(x)
print(values, counts)

array = np.random.normal(size=(10, 4))

min_value = array.min()
max_value = array.max()
mean_value = array.mean()
std = array.std()

first_rows = array[:5]

print("Минимальное значение:", min_value)
print("Максимальное значение:", max_value)
print("Среднее значение:", mean_value)
print("Стандартное отклонение:", std)

x = np.array([6, 2, 0, 3, 0, 0, 5, 7, 0])

zero_indices = np.where(x == 0)[0]

valid_indices = zero_indices[zero_indices < len(x) - 1]

maxx = np.max(x[valid_indices + 1])

print("Максимальный элемент:", maxx)


def log_density(X, m, C):
    D = X.shape[1]
    det_C = np.linalg.det(C)
    inv_C = np.linalg.inv(C)
    log_density = -0.5 * (D * np.log(2 * np.pi) + np.log(det_C) + np.sum((X - m) @ inv_C * (X - m), axis=1))
    return log_density


X = np.random.randn(100, 3)
m = np.mean(X, axis=0)
C = np.cov(X, rowvar=False)
log_density_values = log_density(X, m, C)
scipy_log_density_values = multivariate_normal(m, C).logpdf(X)
print(log_density_values)
print(scipy_log_density_values)

a = np.arange(16).reshape(4,4)
a[[0, 2]] = a[[2, 0]]
print(a)

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')

species_column = iris[:, -1]

unique_values, counts = np.unique(species_column, return_counts=True)

print("Уникальные значения:", unique_values)
print("Количество каждого значения:", counts)

x = np.array([0, 1, 2, 0, 0, 4, 0, 6, 9])
nonzero = np.nonzero(x)[0]
print("Индексы ненулевых элементов:", nonzero)