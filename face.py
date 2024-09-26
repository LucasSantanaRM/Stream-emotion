import cv2
import json
import os
from deepface import DeepFace
from collections import Counter

# Função para detectar emoções em uma imagem
def detect_emotion(frame):
    try:
        result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        if isinstance(result, list):
            result = result[0]
        emotion = result.get('dominant_emotion', None)
        return emotion
    except Exception as e:
        print(f"Erro na detecção de emoção: {e}")
        return None

# Função para salvar as emoções em um arquivo JSON
def save_emotion(emotion):
    if os.path.exists('db.json'):
        with open('db.json', 'r') as f:
            data = json.load(f)
    else:
        data = {"emotions": []}
    
    data["emotions"].append(emotion)
    
    with open('db.json', 'w') as f:
        json.dump(data, f)

# Iniciar a captura de vídeo da câmera
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Não foi possível abrir a câmera.")
    exit()

while True:
    ret, frame = cap.read()
    
    if not ret:
        print("Falha ao capturar frame. Encerrando...")
        break

    emotion = detect_emotion(frame)

    if emotion:
        save_emotion(emotion)  # Salva a emoção detectada
        cv2.putText(frame, f'Emocao: {emotion}', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    cv2.imshow('Detecção de Emoção', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
