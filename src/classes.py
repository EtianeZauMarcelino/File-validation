
class DataSources():
    def __init__(self, file_path):
        self.file_path = file_path
    
    def get_data(self):
        raise NotImplementedError("Método get_data deve ser implementado nas classes filhas.")
    
    def transform_data(self, data):
        raise NotImplementedError("Método transform_data deve ser implementado nas classes filhas.")
    
    def load_data(self):
        raise NotImplementedError("Método load_data deve ser implementado nas classes filhas.")
    
    def return_data(self):
        raise NotImplementedError("Método return_data deve ser implementado nas classes filhas.")
    
    def save_data(self):
        raise NotImplementedError("Método save_data deve ser implementado nas classes filhas.")
    
    def execute_etl(self):
        extracted_data = self.get_data()
        transformed_data = self.transform_data(extracted_data)
        self.return_data(transformed_data)

    
 