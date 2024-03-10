# Importação de pacotes
import pandas as pd
import os
import glob

# Caminho para ler os arquivos
folder_path = 'scr\\data\\raw'

# Lista todos os arquivos de excel 
excel_files = glob.glob(os.path.join(folder_path, '*.xlsx'))

print(excel_files)

if not excel_files:
    print("Nenhum arquivo compátivel encontrado")
else: 
    # dataframe inicial = tabela na memória para guardar os conteúdos dos arquivoss
    dfs = []

    for excel_file in excel_files:
        try: 
            # ler arquivo de excel
            df_temp = pd.read_excel(excel_file)

            # pega nome do arquivo
            file_name = os.path.basename(excel_file)

            #cria coluna de nome do arquivo
            df_temp['filename'] = file_name

            # criando meios de rastreamento, criando uma coluna de localização
            if 'brasil' in file_name.lower():
                df_temp['location'] = 'br'
            elif 'france' in file_name.lower():
                df_temp['location'] = 'fr'
            elif 'italia' in file_name.lower():
                df_temp['location'] = 'it'
            
            #criando a coluna de campanha
            df_temp['campaign'] = df_temp['utm_link'].str.extract(r'utm_campaign=(.*)')

            #guarda dados tratados dentro de um dataframe comum
            dfs.append(df_temp)
            
            
        except Exception as e:
            print(f"Erro ao ler o arquivo {excel_file}: {e}")
    if dfs:
        
        #concatena todas as tabelas salvas no dfs em uma única tabela
        result = pd.concat(dfs, ignore_index = True)

        #caminho de saída
        output_file = os.path.join('scr', 'data', 'ready', 'clean.xlsx')
        
        #configurando o motor de escrita
        writer = pd.ExcelWriter(output_file, engine = 'xlsxwriter')

        #leva os dados do resultado a serem escrito no motor de excel configurado
        result.to_excel(writer, index = False)

        # salva o arquivo de excel
        writer._save()
    else: 
        print("Nenhuma dado para ser salvo")