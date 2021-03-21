import os
DIR=[os.path.join("data","raw"),
     os.path.join("data","processsed"),
     "data_given",
     "notebooks",
     "saved_models",
     "src"]
for dir in DIR:
    os.makedirs(dir,exist_ok=True)
    with open(os.path.join(dir,".gitkeep"),"w") as f:
        pass

files=["params.yaml",
      "dvc.yaml",
      os.path.join("src","__init__.py")]

for file in files:
    with open(file,"w") as f:
        pass