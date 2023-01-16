from rasa import *
from rasa.nlu import test
test_result = test("./train_test_split/test_data.yml", "./models/20220517-192814-formal-keep.tar.gz")

intent_evaluation_report = test_result["intent_evaluation"]["report"]
print(intent_evaluation_report)