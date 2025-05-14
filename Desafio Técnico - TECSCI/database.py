import json
from pprint import pprint
from datetime import datetime
from pydantic import BaseModel, Field
from utils import TimeSeriesValue, EntityWithPower, calc_inverters_generation

# Definindo o modelo de dados, usina como atributo
class Inversor(BaseModel):
    # chave primária: inversor_id + data_original
    inversor_id: int 
    potencia_ativa_watt: float 
    temperatura_celsius: float  
    data_original: datetime
    data_formatada: str
    
class Usina(BaseModel):
    usina_id: int 
    inversor_id: int
    data_original: datetime
    data_formatada: str
    
usinas = [] 
inversores = []   
# Caminho para o arquivo JSON
file_path = 'metrics.json'

# Abrindo e carregando o JSON
try:
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        print("JSON carregado com sucesso!")
except FileNotFoundError:
    print(f"Arquivo '{file_path}' não encontrado.")
    data = []
except json.JSONDecodeError:
    print(f"Erro ao decodificar o arquivo '{file_path}'.")
    data = []

# Ler dados do JSON e separar entre os DTO de Inversor e Usina
for s in data:
    try:
        if s["inversor_id"] <= 4:
            usina = 1
            inversor_id = s["inversor_id"]
            potencia_ativa_watt = s["potencia_ativa_watt"]
            temperatura_celsius = s["temperatura_celsius"]
            data_original = s["datetime"]["$date"] # Mantém como objeto datetime
            data_aux = datetime.fromisoformat(data_original.replace('Z', '+00:00'))
            data_formatada = data_aux.strftime('%d-%m-%Y')
            
            # adicionando ao DTO de Inversor
            inversores.append(Inversor(
            inversor_id=inversor_id, 
            potencia_ativa_watt=potencia_ativa_watt, 
            temperatura_celsius=temperatura_celsius, 
            data_original=data_original,  
            data_formatada=data_formatada
            ))
            
            # adicionando ao DTO de Usina
            usinas.append(Usina(
            usina_id=usina,
            inversor_id=inversor_id,
            data_original=data_original,
            data_formatada=data_formatada
            ))
        else:
            usina = 2
            inversor_id = s["inversor_id"]
            potencia_ativa_watt = s["potencia_ativa_watt"]
            temperatura_celsius = s["temperatura_celsius"]
            data_original = s["datetime"]["$date"] # Mantém como objeto datetime
            data_aux = datetime.fromisoformat(data_original.replace('Z', '+00:00'))
            data_formatada = data_aux.strftime('%d-%m-%Y')

            # adicionando ao DTO de Inversor
            inversores.append(Inversor(
            inversor_id=inversor_id, 
            potencia_ativa_watt=potencia_ativa_watt, 
            temperatura_celsius=temperatura_celsius, 
            data_original=data_original,  
            data_formatada=data_formatada
            ))
            
            # adicionando ao DTO de Usina
            usinas.append(Usina(
            usina_id=usina,
            inversor_id=inversor_id,
            data_original=data_original,
            data_formatada=data_formatada
            ))
        
        
    
        
        #print(f"Data original: {date}")
        
        
    except KeyError as e:
        print(f"Chave ausente no JSON: {e}")
    except ValueError as e:
        print(f"Erro ao processar os dados: {e}")

print("-----------------------INVERSORES-----------------")
pprint(inversores)

print("-----------------------USINAS-----------------")
pprint(usinas)

