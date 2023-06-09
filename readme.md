## house price prediction
### link: https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/overview/evaluation
--------
### folder descriptions: 
#### "building_model" folder: All the necessary files for the buidling model
##### 1. model built by simplified_version.ipynb
##### 2. train, test and result files are stored in the "train_test_results_datasets" folder
##### 3. label encoding dictionary is encoding_mapping.txt
##### 4. encoding_mappaing, object_cols and model are stored in the "pkl_files" folder
##### 5. graphs are stroed in "graphs" folder
--------
#### "deploy" folder : All the necessary files for the deploying model
##### 1. "app.py" : load model and allow user to input values. 
##### 2. webpages are stored in the "templates" folder
--------
### Detail description for input:
#### The description of all the columns stored in "/building_model/train_test_results" folder
#### We restricted user inputs in the following form:
#### 'MSSubClass': {'120': 0, '150': 1, '160': 2, '180': 3,'190': 4, '20': 5, '30': 6, '40': 7, '45': 8, '50': 9, '60': 10, '70': 11, '75': 12, '80': 13, '85': 14, '90': 15}
#### 'MSZoning': {'C (all)': 0, 'FV': 1, 'RH': 2, 'RL': 3, 'RM': 4}
#### 'Street': {'Grvl': 0, 'Pave': 1}
#### 'LotShape': {'IR1': 0, 'IR2': 1, 'IR3': 2, 'Reg': 3}
#### 'LandContour': {'Bnk': 0, 'HLS': 1, 'Low': 2, 'Lvl': 3}
#### 'Utilities': {'AllPub': 0, 'NoSeWa': 1}
#### 'LotConfig': {'Corner': 0, 'CulDSac': 1, 'FR2': 2, 'FR3': 3, 'Inside': 4}
#### 'LandSlope': {'Gtl': 0, 'Mod': 1, 'Sev': 2}
#### 'Neighborhood': {'Blmngtn': 0, 'Blueste': 1, 'BrDale': 2, 'BrkSide': 3, 'ClearCr': 4, 'CollgCr': 5, 'Crawfor': 6, 'Edwards': 7, 'Gilbert': 8, 'IDOTRR': 9, 'MeadowV': 10, 'Mitchel': 11, 'NAmes': 12, 'NPkVill': 13, 'NWAmes': 14, 'NoRidge': 15, 'NridgHt': 16, 'OldTown': 17, 'SWISU': 18, 'Sawyer': 19, 'SawyerW': 20, 'Somerst': 21, 'StoneBr': 22, 'Timber': 23, 'Veenker': 24}
#### 'Condition1': {'Artery': 0, 'Feedr': 1, 'Norm': 2, 'PosA': 3, 'PosN': 4, 'RRAe': 5, 'RRAn': 6, 'RRNe': 7, 'RRNn': 8}
#### 'Condition2': {'Artery': 0, 'Feedr': 1, 'Norm': 2, 'PosA': 3, 'PosN': 4, 'RRAe': 5, 'RRAn': 6, 'RRNn': 7}
#### 'BldgType': {'1Fam': 0, '2fmCon': 1, 'Duplex': 2, 'Twnhs': 3, 'TwnhsE': 4}, 'HouseStyle': {'1.5Fin': 0, '1.5Unf': 1, '1Story': 2, '2.5Fin': 3, '2.5Unf': 4, '2Story': 5, 'SFoyer': 6, 'SLvl': 7}
#### 'RoofStyle': {'Flat': 0, 'Gable': 1, 'Gambrel': 2, 'Hip': 3, 'Mansard': 4, 'Shed': 5}
#### 'RoofMatl': {'CompShg': 0, 'Membran': 1, 'Metal': 2, 'Roll': 3, 'Tar&Grv': 4, 'WdShake': 5, 'WdShngl': 6}
#### 'Exterior1st': {'AsbShng': 0, 'AsphShn': 1, 'BrkComm': 2, 'BrkFace': 3, 'CBlock': 4, 'CemntBd': 5, 'HdBoard': 6, 'ImStucc': 7, 'MetalSd': 8, 'Plywood': 9, 'Stone': 10, 'Stucco': 11, 'VinylSd': 12, 'Wd Sdng': 13, 'WdShing': 14}
#### 'Exterior2nd': {'AsbShng': 0, 'AsphShn': 1, 'Brk Cmn': 2, 'BrkFace': 3, 'CBlock': 4, 'CmentBd': 5, 'HdBoard': 6, 'ImStucc': 7, 'MetalSd': 8, 'Other': 9, 'Plywood': 10, 'Stone': 11, 'Stucco': 12, 'VinylSd': 13, 'Wd Sdng': 14, 'Wd Shng': 15}
#### 'ExterQual': {'Ex': 0, 'Fa': 1, 'Gd': 2, 'TA': 3}
#### 'ExterCond': {'Ex': 0, 'Fa': 1, 'Gd': 2, 'Po': 3, 'TA': 4},
#### 'Foundation': {'BrkTil': 0, 'CBlock': 1, 'PConc': 2, 'Slab': 3, 'Stone': 4, 'Wood': 5}
#### 'Heating': {'Floor': 0, 'GasA': 1, 'GasW': 2, 'Grav': 3, 'OthW': 4, 'Wall': 5}
#### 'HeatingQC': {'Ex': 0, 'Fa': 1, 'Gd': 2, 'Po': 3, 'TA': 4}
#### 'CentralAir': {'N': 0, 'Y': 1}
#### 'Electrical': {'FuseA': 0, 'FuseF': 1, 'FuseP': 2, 'Mix': 3, 'SBrkr': 4}
#### 'KitchenQual': {'Ex': 0, 'Fa': 1, 'Gd': 2, 'TA': 3}
#### 'Functional': {'Maj1': 0, 'Maj2': 1, 'Min1': 2, 'Min2': 3, 'Mod': 4, 'Sev': 5, 'Typ': 6}
#### 'PavedDrive': {'N': 0, 'P': 1, 'Y': 2},
#### 'MoSold': {'1': 0, '10': 1, '11': 2, '12': 3, '2': 4, '3': 5, '4': 6, '5': 7, '6': 8, '7': 9, '8': 10, '9': 11}
#### 'YrSold': {'2006': 0, '2007': 1, '2008': 2, '2009': 3, '2010': 4}
#### 'SaleType': {'COD': 0, 'CWD': 1, 'Con': 2, 'ConLD': 3, 'ConLI': 4, 'ConLw': 5, 'New': 6, 'Oth': 7, 'WD': 8}
#### 'SaleCondition': {'Abnorml': 0, 'AdjLand': 1, 'Alloca': 2, 'Family': 3,'Normal': 4, 'Partial': 5}