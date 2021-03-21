import os
import argparse
from get_data import get_data,read_param

def load_data(config_path):
    config_file=read_param(config_path)
    df=get_data(config_path)
    new_cols=[col.replace(" ","_") for col in df.columns]
    raw_path=config_file["load_data"]["raw_data"]

    df.to_csv(raw_path,sep=",",index=False,header=new_cols)
    print(new_cols)
#

if __name__=="__main__":
    arg=argparse.ArgumentParser()
    arg.add_argument("--config",default="params.yaml")
    parsed_arg=arg.parse_args()
    load_data(parsed_arg.config)