import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import numpy as np
from scipy.stats import mode
import seaborn as sns
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

class Preprocessing():
    def meanMode(self, X):
        """
        결측치 처리1 - 평균(수치형), 최빈값(범주형) 처리
        """
        # 연속형 피처 리스트 저장
        num_col = list(X._get_numeric_data().columns)

        # 범주형 피처 리스트 저장
        cat_col = list(X.columns)
        for col in num_col:
            cat_col.remove(col)

        # 연속형 데이터 전처리(평균값으로 채우기)
        for col in num_col:
            X[col].fillna(round(np.mean(X[col])), inplace=True)

        # 범주형 데이터 전처리 (최빈값으로 채우기)
        for col in cat_col:
            X[col].fillna(mode(X[col])[0][0], inplace=True)
            
        return X
    
    def delNaN(self, X):
        """
        # 결측치 처리2 - 결측행 제거
        """
        X = X.dropna(how='any', axis=0).reset_index()
        return X
    
    def labelEncode(self, X):
        """
        # 인코딩1 - 레이블인코딩
        """
        # 연속형 피처 리스트 저장
        num_col = list(X._get_numeric_data().columns)

        # 범주형 피처 리스트 저장
        cat_col = list(X.columns)
        for col in num_col:
            cat_col.remove(col)
            
        encoder = LabelEncoder()
        for cat in cat_col:
            X[cat] = encoder.fit_transform(X[cat])
        return X

    def oneHotEncode(self, X):
        """
        # 인코딩2 - 원핫인코딩
        """
        object_col = []
        for col in X.columns:
            if X[col].dtype == 'object':
                object_col.append(col)

        enc = OneHotEncoder()
        enc.fit(X.loc[:,object_col])

        onehot_X = pd.DataFrame(enc.transform(X.loc[:,object_col]).toarray(), 
                                    columns = enc.get_feature_names(object_col))
        X.drop(object_col, axis=1, inplace=True)
        X = pd.concat([X, onehot_X], axis=1)
        return X
    