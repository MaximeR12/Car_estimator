import pandas as pd
import pickle

df = pd.read_csv('carprice_cleaned.csv')

from sklearn.model_selection import learning_curve
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder


from sklearn.linear_model import SGDRegressor, Lasso
from sklearn.ensemble import RandomForestRegressor



sgd = [SGDRegressor(), "sgd"]                        # 87.047%
lso = [Lasso(alpha=4), "lso"]                        # 87.478%
rdf = [RandomForestRegressor(800), "rdf"]            # 95.287%

model_to_use = sgd # <-------- Here to change the model you want



y = df['price']
X = df[["brand", "wheelbase", "carlength", "carwidth", "carheight",	"curbweight",	"cylindernumber",	"enginesize",	"horsepower",	"consumption",  "fueltype","drivewheel", "aspiration" ,"doornumber" , "enginelocation"]]
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, random_state=42)


###############  Variables utilisées  ###################

numeric_features = ["wheelbase",	"carlength", "carwidth",	"carheight",	"curbweight",	"cylindernumber",	"enginesize",	"horsepower",	"consumption", "doornumber"]
categorial_features = ["brand", "fueltype", "drivewheel", "aspiration"  , "enginelocation"]
#################  TRANSFORMERS   ######################
numeric_transformer = Pipeline([
    ('imputer', SimpleImputer(strategy='median')),
    ("minmax", MinMaxScaler())

])

categorical_transformer = OneHotEncoder(sparse_output=True, handle_unknown="ignore")

################  PREPROCESSING  #######################
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorial_features)
    ]
)

pipe = Pipeline([
    ('prep', preprocessor),
    ('model', model_to_use[0])
])

trained_pipe = pipe.fit(X_train,y_train)
score = trained_pipe.score(X_test,y_test)
print("Score : {:.3%}".format(score))



##################  SAVE AS PICKLE  #####################
with open(f'models/model_{model_to_use[1]}.pkl', 'wb') as file:
    pickle.dump(trained_pipe, file)

