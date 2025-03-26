import pickle as pkl
import datetime

class sampleObject:
    def __init__(self):
        self.name = "Tiago"
        self.date_created = datetime.now().isoformat()
        self.time_created = datetime.now().time().isoformat()

obj_path = "sample_object.pkl"

obj = pkl.load(open(obj_path, "rb"))

print(obj.name)