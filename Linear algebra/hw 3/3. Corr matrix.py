#ваш код
def corr_rank(X):
    #строим матрицу корреляций
    corr = np.corrcoef(X)
    # возвращаем ранг матрицы корреляций
    return np.linalg.matrix_rank(corr)

corr_rank(X)
#5
