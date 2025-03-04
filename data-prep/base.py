from op import *

# BASE FEATURE TYPES #

class BaseFeature:
    def __init__(self, op_class, group_on, feat_name):
        self.op_class = op_class(["match_id", "innings", group_on], feat_name)

    def apply(self, df):
        return self.op_class.apply(df)

class BaseSumFeature(BaseFeature):
    def __init__(self, op_class, sum_on, group_on, feat_name):
        self.op_class = op_class(sum_on, ["match_id", "innings", group_on], feat_name)

class RunFeature(BaseSumFeature):
    def __init__(self, op_class, group_on, feat_name, extras = False):
        sum_on = ["runs_off_bat", "extras"] if extras else "runs_off_bat"
        super().__init__(op_class, sum_on, group_on, feat_name)

class WicketFeature(BaseSumFeature):
    def __init__(self, op_class, group_on, feat_name):
        self.wicket_feature = ColumnMap(
            lambda c : int(pd.notna(c)),
            "player_dismissed",
            "is_wicket"
        )

        super().__init__(op_class, "is_wicket", group_on, feat_name)

    def apply(self, df):
        df = self.wicket_feature.apply(df)
        return super().apply(df)

class RunCounter(RunFeature):
    def __init__(self, group_on, feat_name, extras = False):
        super().__init__(CumulativeSum, group_on, feat_name, extras)

class BallCounter(BaseFeature):
    def __init__(self, group_on, feat_name):
        super().__init__(CumulativeCount, group_on, feat_name)

class RunTotaller(RunFeature):
    def __init__(self, group_on, feat_name, extras = False):
        super().__init__(TotalSum, group_on, feat_name, extras)

class BallTotaller(BaseFeature):
    def __init__(self, group_on, feat_name):
        super().__init__(TotalCount, group_on, feat_name)

class WicketCounter(WicketFeature):
    def __init__(self, group_on, feat_name):
        super().__init__(CumulativeSum, group_on, feat_name)
    
class WicketTotaller(WicketFeature):
    def __init__(self, group_on, feat_name):
        super().__init__(TotalSum, group_on, feat_name)