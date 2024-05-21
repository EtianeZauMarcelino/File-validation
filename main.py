from src.etl import EtlFromExcel

fonte = 'data\Key Words Pesquisa automática de legislação 3.xlsx'

# Salva o schema
df_extract = EtlFromExcel(fonte)
df_extract.save_schema()

# Executa a class
df = EtlFromExcel(fonte)
df.execute_etl()
