import joblib
import pandas as pd
import psycopg2
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC

db_connect = psycopg2.connect(
    host="localhost", database="mydatabase", user="myuser", password="mypassword"
)
# query, db_connector를 인자로 받아 데이터를 불러오는 메서드.
# query sodyddms id column을 기준으로 최신 데이터 100개를 추출하는 쿼리문이다.
df = pd.read_sql("SELECT * FROM iris_data ORDER BY id DESC LIMIT 100", db_connect)
X = df.drop(["id", "target", "timestamp"], axis="columns")
y = df["target"]

X_train, X_valid, y_train, y_valid = train_test_split(
    X, y, train_size=0.8, random_state=2023
)

model_pipeline = Pipeline([("scaler", StandardScaler()), ("svc", SVC())])
model_pipeline.fit(X_train, y_train)

train_pred = model_pipeline.predict(X_train)
valid_pred = model_pipeline.predict(X_valid)

train_acc = accuracy_score(y_true=y_train, y_pred=train_pred)
valid_acc = accuracy_score(y_true=y_valid, y_pred=valid_pred)

print("Train Accuracy : ", train_acc)
print("Valid Accuracy : ", valid_acc)

joblib.dump(model_pipeline, "db_pipeline.joblib")

# save data
# 지속적으로 데이터가 쌓이고 있으므로 불러올 때마다 데이터가 바뀐다. 그러므로 사용한 데이터를 저장해서 validation part에서 사용한다.
df.to_csv("data.csv", index=False)
