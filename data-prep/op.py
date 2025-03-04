import pandas as pd

def remove_empty(arr):
    return [e for e in arr if len(e) > 0]

class BaseSum:
    def __init__(self, sum_on, group, feat_name):
        self.sum_on = sum_on
        self.group = remove_empty(group)
        self.feat_name = feat_name

    def _prepare_sum_column(self, df):
        is_sum_on_list = isinstance(self.sum_on, list)
        if is_sum_on_list:
            df['temp_sum'] = df[self.sum_on].sum(axis=1)
            return 'temp_sum', True
        return self.sum_on, False

    def _cleanup(self, df, temp_created):
        if temp_created:
            df.drop('temp_sum', axis=1, inplace=True)

class CumulativeSum(BaseSum):
    def apply(self, df):
        sum_column, temp_created = self._prepare_sum_column(df)
        df[self.feat_name] = (
            df.groupby(self.group)[sum_column]
            .cumsum()
            .shift()
            .fillna(0)
        )
        self._cleanup(df, temp_created)
        return df

class TotalSum(BaseSum):
    def apply(self, df):
        sum_column, temp_created = self._prepare_sum_column(df)
        df[self.feat_name] = (
            df.groupby(self.group)[sum_column]
            .transform("sum")
        )
        self._cleanup(df, temp_created)
        return df
    
class CumulativeCount:
    def __init__(self, group, feat_name):
        self.group = remove_empty(group)
        self.feat_name = feat_name

    def apply(self, df):
        df[self.feat_name] = (
            df.groupby(self.group)
            .cumcount()
        )

        return df
    
class TotalCount:
    def __init__(self, group, feat_name):
        self.group = remove_empty(group)
        self.feat_name = feat_name

    def apply(self, df):
        df[self.feat_name] = (
            df.groupby(self.group)
            .transform("count")
            .iloc[:, 0]
        )

        return df

class ColumnMap:
    def __init__(self, fx, fx_on, feat_name):
        self.fx = fx
        self.fx_on = fx_on
        self.feat_name = feat_name

    def apply(self, df):
        df[self.feat_name] = df[self.fx_on].apply(self.fx)

        return df