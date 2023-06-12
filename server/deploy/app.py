import pickle
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import io

with open('../building_model/pkl_files/simplified_model_rf.pkl', 'rb') as f:
    model = pickle.load(f)
with open('../building_model/pkl_files/encoding_mapping.pkl', 'rb') as f:
    encoding_mapping = pickle.load(f)
with open('../building_model/pkl_files/object_cols.pkl', 'rb') as f:
    object_cols = pickle.load(f)

sample_test = pd.read_csv('sample_test.csv')

from flask import Flask, request, jsonify, render_template

def cat_to_num(test):
    # HAVE TO PERFORM LABEL ENCODING MANUALLY
    cols = object_cols
    # Convert object file into numeric value from dictionary that storeed in the simplified_version.ipynb
    for col in cols:
        print("Current Column is: ", col)
        value = str(test[col].values).strip("'[]'")
        test[col] = encoding_mapping[col][value]
        # print("value: ", value)
        # print("encoded value: ", test[col])

    
    print("Converted categorical data into numeric values")
    print("\n")
    return test

def drop_col(test):
    cols = ['PoolQC', 'MiscFeature', 'Alley', 'Fence', 'FireplaceQu', 'LotFrontage',
    'GarageYrBlt', 'GarageCond', 'GarageType', 'GarageFinish', 'GarageQual',
    'BsmtFinType2', 'BsmtExposure', 'BsmtQual', 'BsmtCond', 'BsmtFinType1',
    'MasVnrArea', 'MasVnrType']
    test = test.drop(columns=cols)
    return test

def check_null(test):

    # Check for null values in each column
    null_columns = test.columns[test.isnull().any()].tolist()

    # Print the columns with null values
    if null_columns:
        print("Columns with null values:")
        for col in null_columns:
            print(test[col])
    else:
        print("No columns with null values")

def predict(x):
    predictions = model.predict(x)
    return predictions


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    # Get user input from index.html
    inputs={}
    for col in sample_test.columns:
        if col == 'Id':
            continue
        else:
            input = request.form.get(col)
            inputs.update({col:input})

    # Convert user inputs into DataFrame form
    inputs_to_csv = pd.DataFrame(inputs, index=[0])

    # CAUTION! This is for mismatch between train.columns and data description
    inputs_to_csv = inputs_to_csv.rename(columns={'BedroomAbvGr': 'Bedroom'})
    inputs_to_csv = inputs_to_csv.rename(columns={'KitchenAbvGr': 'Kitchen'})
    
    # Drop unnecessary columns
    result_drop_col = drop_col(inputs_to_csv)

    result_cat_to_num = cat_to_num(result_drop_col)
    
    # Check null values
    check_null(result_cat_to_num)

    # Save the user inputs
    result_drop_col.to_csv("user_input.csv", index=False)

    result_pred = predict(result_cat_to_num)
    print("Successfully predicted value")
    print("Result: ", result_pred)

    return render_template("result.html", result_pred=result_pred)
if __name__ == "__main__":
    app.run(debug=True)