import argparse
import pandas as pd
from get_data import read_param
from sklearn.model_selection import train_test_split

def split_data(config_path):
    config_file=read_param(config_path)
    train_data_path=config_file["split_data"]["train_data"]
    print(train_data_path)
    test_data_path=config_file["split_data"]["test_data"]
    test_size=config_file["split_data"]["test_size"]
    random_state = config_file["base"]["random_state"]
    df=pd.read_csv(config_file["load_data"]["raw_data"])

    train,test=train_test_split(df,test_size=test_size,random_state=random_state)

    train.to_csv(train_data_path,index=False,sep=",",encoding="utf-8")
    test.to_csv(test_data_path, index=False,sep=",",encoding="utf-8")



if __name__ == "__main__":
    arg = argparse.ArgumentParser()
    arg.add_argument("--config", default="params.yaml")
    parsed_args = arg.parse_args()
    split_data(config_path=parsed_args.config)