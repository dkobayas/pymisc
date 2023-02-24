import numpy as np
from sklearn.base import BaseEstimator, RegressorMixin


def hello(name: str = "dai"):
    """_summary_

    Parameters
    ----------
    name : str, optional
        _description_, by default "dai"
    """
    print("hello,", name)


# BaseEstimatorとRegressorMixinを継承する
class LinearRegression(BaseEstimator, RegressorMixin):
    """_summary_

    Parameters
    ----------
    BaseEstimator : _type_
        _description_
    RegressorMixin : _type_
        _description_

    Returns
    -------
    _type_
        _description_
    """  # fit()を実装

    def fit(self, X, y):
        """_summary_

        Parameters
        ----------
        X : _type_
            _description_
        y : _type_
            _description_

        Returns
        -------
        _type_
            _description_
        """
        self.coef_ = np.linalg.solve(np.dot(X.T, X), np.dot(X.T, y))
        # fit は self を返す
        return self

    # predict()を実装
    def predict(self, X):
        """_summary_

        Parameters
        ----------
        X : _type_
            _description_

        Returns
        -------
        _type_
            _description_
        """
        return np.dot(X, self.coef_)
