import sys
import pandas as pd

from src.exception import CustomException
from src.utils import load_object


class PredictPieline:
    def __init__(self):
        pass
    def predict(self,features):
        try:
            model_path='artifacts/model.pkl'
            preprocessing_obj='artifacts/proprocessor.pkl'
            model=load_object(model_path)
            preprocessor=load_object(preprocessing_obj)
            predict_arr=preprocessor.transform(features)
            return model.predict(predict_arr)
        except Exception as e:
            raise CustomException(e,sys)

class CustomData:
    def __init__(self,gender,race,parental_education_level,lunch,test_prepration_course,
                 reading_score,writing_score):
        self.gender= gender
        self.race= race
        self.parental_education_level= parental_education_level
        self.lunch= lunch
        self.test_prepration_course= test_prepration_course
        self.reading_score= reading_score
        self.writing_score= writing_score

    def get_predict_df(self):
        try:
            data={
                'gender':[self.gender],
                'race_ethnicity':[self.race],
                'parental_level_of_education':[self.parental_education_level],
                'lunch':[self.lunch],
                'test_preparation_course':[self.test_prepration_course],
                'reading_score':[self.reading_score],
                'writing_score':[self.writing_score]
            }
            return pd.DataFrame(data)
        except Exception as e:
            raise CustomException(e,sys)