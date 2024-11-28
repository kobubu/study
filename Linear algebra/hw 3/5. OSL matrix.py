#ваш код
def fit_model(X, y):
  return (inverse_matrix(X.T@X)@X.T@y).to_numpy()

print(fit_model(X, y))
