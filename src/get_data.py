import pandas as pd
import yaml
import argparse

def read_param(config_path):
    with open(config_path) as f:
        config_file=yaml.safe_load(f)
    return config_file

def get_data(config_path):
    config_file=read_param(config_path)
    df=pd.read_csv(config_file["data_source"]["s3_source"],sep=",",encoding="utf-8")
    return df


if __name__=="__main__":
    arg=argparse.ArgumentParser()
    arg.add_argument("--config",default="params.yaml")
    parsed_args=arg.parse_args()
    get_data(config_path=parsed_args.config)

