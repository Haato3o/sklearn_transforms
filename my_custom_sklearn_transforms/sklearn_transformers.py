from sklearn.base import BaseEstimator, TransformerMixin
from numpy import np

# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Retornamos um novo dataframe sem as colunas indesejadas
        return data.drop(labels=self.columns, axis='columns')

# AlienPls
# Probably not useful anymore, but just in case
class uwu(BaseEstimator, TransformerMixin):

    @staticmethod
    def wannaBeTheOwOToMyUwU(a: int, b: int):
        if (not np.isnan(a) or not np.isnan(b)):
            if (np.isnan(a)):
                a = b
            elif (np.isnan(b)):
                b = a
        else:
            return [0,0]
        return [a, b]
        
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        data = X.copy()
        for i in range(len(data['NOTA_DE'])):
            NOTA_DE, NOTA_EM = uwu.wannaBeTheOwOToMyUwU(data['NOTA_DE'][i], data['NOTA_EM'][i])
            NOTA_MF, NOTA_GO = uwu.wannaBeTheOwOToMyUwU(data['NOTA_MF'][i], data['NOTA_GO'][i])
            
            data.at[i, 'NOTA_DE'] = NOTA_DE
            data.at[i, 'NOTA_EM'] = NOTA_EM
            data.at[i, 'NOTA_MF'] = NOTA_MF
            data.at[i, 'NOTA_GO'] = (NOTA_DE + NOTA_EM) / 2 if np.isnan(data['NOTA_GO'][i]) else data['NOTA_GO'][i]
            
        return data