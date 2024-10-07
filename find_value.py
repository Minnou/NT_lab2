import pandas as pd 

def create_dataset_from_files(files):
    if len(files == 1):
        result_data_frame = pd.read_csv(files[0], sep=";")
    elif len(files >= 2):
        data_frames = []
        for filename in files:
            data_frames.append(pd.read_csv(filename, sep=";"))
        if len(files == 2):
            if (data_frames[0].shape[1] == 1 or data_frames[1].shape[1] == 1):
                result_data_frame = pd.concat(data_frames[0], data_frames[1], axis=1)
        else:
            result_data_frame = pd.DataFrame()
            for data_frame in data_frames:
                result_data_frame = pd.concat(result_data_frame, data_frame, axis=0)

    return result_data_frame

class DataFrameIterator:
    def __init__(self, dataframe):
        self.dataframe = dataframe
        self.row_iterator = dataframe.iterrows()
    
    def __iter__(self):
        return self

    def __next__(self):
        return next(self.row_iterator)