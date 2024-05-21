import pandas as pd
import pandera as pa # type: ignore
from contracts.meu_schema import schema
from logs.log_config import log_decorator



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
   
class EtlFromExcel(DataSources):
    #@pa.check_output(schema, lazy=True)
    @log_decorator
    def get_data(self): 
        #with open(self.file_path, mode="r", encoding='windows-1252') as file:
        df = pd.read_excel(self.file_path)
        return df
    
    @log_decorator
    @pa.check_output(schema, lazy=True)
    def transform_data(self, data):
        return data.dropna()
    
    # @log_decorator
    def return_data(self, data):
        print(data.head(5))

    @log_decorator
    @pa.check_output(schema, lazy=True)
    def save_data(self):
        df_row = self.get_data()
        df_cleaned = self.transform_data(df_row)
        return df_cleaned
    
    @log_decorator
    def save_schema(self):
        df_row = self.get_data()
        df_cleaned = self.transform_data(df_row)

        keywords_schema = pa.infer_schema(df_cleaned)

        with open('contracts\meu_schema.py', 'w', encoding='utf-8') as arquivo:
            arquivo.write(keywords_schema.to_script())



if __name__ == '__main__':
    fonte = 'data\Key Words Pesquisa automática de legislação 3.xlsx'

    df_extract = EtlFromExcel(fonte)
    df_extract.execute_etl()


