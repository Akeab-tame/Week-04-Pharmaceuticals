import pandas as pd
import numpy as np
from sklearn.preprocessing import OrdinalEncoder, OneHotEncoder, Normalizer
from sklearn.impute import SimpleImputer

class data_cleaner:
    def drop_duplicate(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        drop duplicate rows
        """
        data.drop_duplicates(inplace=True)

        return data
 
    def percent_missing(self, data: pd.DataFrame) -> float:
        """
        calculate the percentage of missing values from dataframe
        """
        totalCells = np.prod(data.shape)
        missingCount = data.isnull().sum()
        totalMising = missingCount.sum()

        return round(totalMising / totalCells * 100, 2)

    def get_numerical_columns(self, data: pd.DataFrame) -> list:
        """
        get numerical columns
        """
        return data.select_dtypes(include=['number']).columns.to_list()

    def get_categorical_columns(self, data: pd.DataFrame) -> list:
        """
        get categorical columns
        """
        return  data.select_dtypes(include=['object','datetime64[ns]']).columns.to_list()

    def percent_missing_column(self, data: pd.DataFrame, col:str) -> float:
        """
        calculate the percentage of missing values for the specified column
        """
        try:
            col_len = len(data[col])
        except KeyError:
            print(f"{col} not found")
        missing_count = data[col].isnull().sum()

        return round(missing_count / col_len * 100, 2)
    
    def fill_missing_values_categorical(self, data: pd.DataFrame, method: str) -> pd.DataFrame:
        """
        fill missing values with specified method
        """

        categorical_columns = data.select_dtypes(include=['object','datetime64[ns]']).columns

        if method == "ffill":

            for col in categorical_columns:
                data[col] = data[col].fillna(method='ffill')

            return data

        elif method == "bfill":

            for col in categorical_columns:
                data[col] = data[col].fillna(method='bfill')

            return data

        elif method == "mode":
            
            for col in categorical_columns:
                data[col] = data[col].fillna(data[col].mode()[0])

            return data
        else:
            print("Method unknown")
            return data

    def normalizer(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        normalize numerical columns
        """
        norm = Normalizer()
        return pd.DataFrame(norm.fit_transform(data[self.get_numerical_columns(data)]), columns=self.get_numerical_columns(data))
    
    def Nan_to_zero(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        substitute NaN values with 0 for a given columns
        """
        data[['MasVnrType', 'GarageYrBlt']] = data[['MasVnrType', 'GarageYrBlt']].fillna(0)

        return data
    
    def Nan_to_none(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        repalces NaN values with 'none'
        """
        data[['Alley', 'BsmtQual', 'BsmtCond', 'BsmtExposure', 'BsmtFinType1', 'BsmtFinType2', 'FireplaceQu', 'GarageType', 'GarageFinish', 'GarageQual', 'GarageCond', 'PoolQC', 'Fence', 'MiscFeature']] = data[['Alley', 'BsmtQual', 'BsmtCond', 'BsmtExposure', 'BsmtFinType1', 'BsmtFinType2', 'FireplaceQu', 'GarageType', 'GarageFinish', 'GarageQual', 'GarageCond', 'PoolQC', 'Fence', 'MiscFeature']].fillna('none')
