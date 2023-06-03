import os
os.environ["KAGGLE_USERNAME"] = os.environ["USERNAME"]
os.environ["KAGGLE_KEY"] = os.environ["PASSWORD"]
import kaggle

#prompt user: create new dataset or update existing
def k_upload(purpose,path,public=False,update_message=None):
    if purpose == "New":
        kaggle.api.dataset_create_new(path,public,False,False,"skip")
    elif purpose == "Update":
        kaggle.api.dataset_create_version(path,update_message,False,False,False,"skip")
    else:
        exit

dataset_paths = ["./data"]

#create new dataset
# k_upload("New",dataset_paths[0])

#update existing
k_upload("Update",dataset_paths[0],False,"Update dataset")
