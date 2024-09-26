#Stream-emotion é uma aplicaçao que sabe suas emoções!!

![image](https://github.com/user-attachments/assets/807eba2b-a485-4060-9a64-1413d9ebeebb)



## O que foi usado?
- Python
  - streamlit
  - pandas
  - deepface
  
O script face.py é responsavel por abrir uma captura de video da webcam e fazer a detecção de Emoção e salva-las no arquivo db.json.
já o script app.py é responsavel por ler e analisar os dados do db.json e plotar os graficos no navegador usando o streamlit,esse mesmo script tem uma função para limpar o BD e reiniciar a coleta de emoções.

