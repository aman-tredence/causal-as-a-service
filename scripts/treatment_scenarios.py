class TreatmentScenario:

    def __init__(self, artifact_file_path) -> None:
        
        self.artifacts = pd.read_csv(artifact_file_path)

    def get_input(self, config):
        #Data
        self.data_path = config['data']['data_path']
        self.target = config['data']['target']
        self.data_output_path = config['data']['data_output_path']
        self.model_output_path = config['data']['model_output_path']
        
        self.fetch_models = config['fetch_models']

        #Model
        self.version = config['model']['version']

    def get_treatements(self):
        
        artifacts= pd.read_csv(f"{self.data_output_path}/artifacts_v{self.version}.csv")            
        treatments = artifacts['TreatmentVariables'].values[0]
        treatments = treatments.split(',')
        treatments = [x.strip() for x in treatments]
        
        return treatments    
    
    def read_data(self, target, treatment_vars):
        
        print('Reading data from GCS')
        
        data = pd.read_csv(f"{self.data_path}/predict_data.csv")
        data = data[treatment_vars + [target]]
        
        return data
    

    def preprocess_data(self, df, target, treatment_vars):
        ## Clean the data
        
        #Replace null string values
        df.replace('#N/A',0,inplace= True)
        df.replace('null',0,inplace= True)
        
        #Replace infinte values
        df = df.drop_duplicates()
        
        #Fill null values by 0
        df= df.fillna(0)
        
        df[self.treatment_vars] = df[self.treatment_vars].astype(float)

        return df  

    def fetch_model_version(self, target, model_output_path):
        model_versions = os.listdir(model_output_path[:-1])
        target_model_versions = pd.Series(model_versions).apply(lambda x:x if len(x.split(target)) > 1 else None)
        target_model_versions = list(target_model_versions[target_model_versions.notna()])
        return target_model_versions
    

    def fetch_model(self):

        print('loading Model...')
        self.model_name = f'{self.target}_Causal_model_v{model.version}.pkl'
        model_path = self.model_output_path + self.model_name
        model_file = open(model_path, 'rb')
        causal_model = pickle.load(model_file)
        # close the file
        model_file.close()
        return causal_model

    def get_predictions(self, causal_model):
        print('Performing Prediction')
        x_dowhy_input = self.test_df[self.treatment_vars]
        x_dowhy_input.insert(0,'intercept',1)

        y_pred_dowhy = causal_model.get_prediction(exog = x_dowhy_input.to_numpy())
        self.data[f'{self.target}_pred'] = y_pred_dowhy.predicted_mean.tolist()

        return self.data
    
    def normal_distribution(self, size, mean, std_dev, min_value, max_value):
        while True:
            u1 = np.random.rand(size)
            u2 = np.random.rand(size)
            z0 =  np.sqrt(-2 * np.log(u1)) * np.cos(2 * np.pi * u2)

            arr = mean + std_dev + z0
            arr.clip(arr, min_value, max_value)

            if np.all(arr >= min_value) and np.all(arr <= max_value):
                return arr
            

    def poisson_distribution(self, size, mean, min_value, max_value):
        while True:
            u = np.random.rand(size)

            arr = np.floor(np.log(u) / np.log(1 - 1/mean))
            arr = np.clip(arr, min_value, max_value)

            if np.all(arr >= min_value) and np.all(arr <= max_value):
                return arr
            
    def lognormal_distribution(self, size, mean, std_dev, min_value, max_value):
        while True:
            arr = np.random.lognormal(mean, std_dev, size)

            arr = np.clip(arr, min_value, max_value)

            if np.all(arr >= min_value) and np.all(arr <= max_value):
                return arr
            

    def scenario_creation(self, X):

        config = X[0]

        if self.fetch_models:
            #fetch the Trained Models
            model_version = self.fetch_model_version(self.target, self.model_output_path)
            print("model_versions: ", model_version[::-1])
    
        if self.fetch_columns:
            treatment_vars = self.get_treatements()
            return treatment_vars
        
        if self.data_path:
            self.treatment_vars = self.get_treatements()

            self.data = self.read_data( self.target, self.treatment_vars)

            



    
        
    

