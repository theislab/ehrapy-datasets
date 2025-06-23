import pandas as pd

from database_processing.dataprocessor import DataProcessor

class DiagnosesProcessor(DataProcessor):
    
    def __init__(self, dataset, pth_dic=None, config_path=None):
        super().__init__(dataset, pth_dic=pth_dic, config_path=config_path)

        self.preprocessed_diagnoses_pth = self.diagnoses_pths[dataset]
    
        self.labels = self.load(self.labels_pths[dataset])
    