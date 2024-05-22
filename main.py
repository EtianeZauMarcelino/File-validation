from src.etl import EtlFromExcel
from src.frontend import ExcelValidatorUI

fonte = 'data\Key Words Pesquisa automática de legislação 3.xlsx'

# Salva o schema
# df_extract = EtlFromExcel(fonte)
# df_extract.save_schema()

# Executa a class
df = EtlFromExcel(fonte)
df.save_data()



# def main():

#     ui = ExcelValidatorUI()
#     ui.display_header()

#     # model_choice = ui.select_model()
#     uploaded_file = ui.upload_file()

#     if uploaded_file is not None:
#         df2 = EtlFromExcel(uploaded_file)
#         error = df2.save_data()
#         ui.display_results(error)

# if __name__ == "__main__":
#     main()

