from base import *

class FeatureBuilder:
    def __init__(self):
        self.features = []

    def add_feature(self, feature):
        self.features.append(feature)

        return self

    def apply(self, df):
        for feature in self.features:
            df = feature.apply(df)

        return df

# FEATURE FACTORY #

class FeatureFactory:
    @staticmethod
    def create_run_feature(group_on, feat_name, extras = False):
        return RunCounter(group_on, feat_name, extras)
    
    @staticmethod
    def create_run_total_feature(group_on, feat_name, extras = False):
        return RunTotaller(group_on, feat_name, extras)
    
    @staticmethod
    def create_balls_feature(group_on, feat_name):
        return BallCounter(group_on, feat_name)
    
    @staticmethod
    def create_balls_total_feature(group_on, feat_name):
        return BallTotaller(group_on, feat_name)
    
    @staticmethod
    def create_wickets_feature(group_on, feat_name):
        return WicketCounter(group_on, feat_name)
    
    @staticmethod
    def create_wickets_total_feature(group_on, feat_name):
        return WicketTotaller(group_on, feat_name)

# BATSMAN FEATURES #
        
def BatsmanScore(feat_name):
    return FeatureFactory.create_run_feature("striker", feat_name)

def BatsmanTotalScore(feat_name):
    return FeatureFactory.create_run_total_feature("striker", feat_name)

def BatsmanBalls(feat_name):
    return FeatureFactory.create_balls_feature("striker", feat_name)

def BatsmanTotalBalls(feat_name):
    return FeatureFactory.create_balls_total_feature("striker", feat_name)

# BOWLER FEATURES #

def BowlerConceded(feat_name):
    return FeatureFactory.create_run_feature("bowler", feat_name, extras=True)

def BowlerTotalConceded(feat_name):
    return FeatureFactory.create_run_total_feature("bowler", feat_name, extras=True)

def BowlerBalls(feat_name):
    return FeatureFactory.create_balls_feature("bowler", feat_name)

def BowlerTotalBalls(feat_name):
    return FeatureFactory.create_run_total_feature("bowler", feat_name)

def BowlerWickets(feat_name):
    return FeatureFactory.create_wickets_feature("bowler", feat_name)

def BowlerTotalWickets(feat_name):
    return FeatureFactory.create_wickets_total_feature("bowler", feat_name)

# INNINGS FEATURES #

def InningsRuns(feat_name):
    return FeatureFactory.create_run_feature("", feat_name, extras=True)

def InningsTotalRuns(feat_name):
    return FeatureFactory.create_run_total_feature("", feat_name, extras=True)

def InningsBalls(feat_name):
    return FeatureFactory.create_balls_feature("", feat_name)

def InningsTotalBalls(feat_name):
    return FeatureFactory.create_balls_total_feature("", feat_name)

def InningsWickets(feat_name):
    return FeatureFactory.create_wickets_feature("", feat_name)

def InningsTotalWickets(feat_name):
    return FeatureFactory.create_wickets_total_feature("", feat_name)