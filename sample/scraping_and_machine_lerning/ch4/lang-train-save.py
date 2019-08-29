from sklearn import svm
from sklearn.externals import joblib
import json
import os

# 各言語の頻出データ(JSON)を読み込む
with open(os.path.dirname(__file__) + "/lang/freq.json", "r", encoding="utf-8") as fp:
    d = json.load(fp)
    data = d[0]

# データを学習する
clf = svm.SVC(gamma='scale')
clf.fit(data["freqs"], data["labels"])

# 学習データを保存する
dir_name = os.path.dirname(__file__) + "/cgi-bin/"
if not os.path.exists(dir_name): os.mkdir(dir_name)
joblib.dump(clf, dir_name + "freq.pkl")
print("ok")