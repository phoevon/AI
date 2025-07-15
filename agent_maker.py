from flask import Flask, render_template, request
import google.generativeai as genai
import json


# Configura tu API KEY de Gemini
genai.configure(api_key="xxxxxxxxxxxxxxAPI_KEYxxxxxxx")  # <-- Sustituye por tu API Key real

# <-- Constructor de agentes
class AgenteIA:                                  
    def __init__(self, nombre, rol, descripcion, agentes):
        self.nombre = nombre
        self.rol = rol
        self.descripcion = descripcion
        self.modelo = genai.GenerativeModel('models/gemini-2.0-flash')
        self.historial_mensajes = []
        self.agentes = agentes

    def actuar(self, entrada_usuario):
        otros_agentes = "\\n".join([f"{agente.nombre} es un(a) {agente.rol} y su responsabilidad es {agente.descripcion}." for agente in self.agentes if agente != self])
        memoria = leer_memoria()
        historial_conversaciones = memoria.get('conversations', [])
        historial_formateado = "\\n".join([f"Conversación entre {c['agent1']} y {c['agent2']}: {c['messages']}" for c in historial_conversaciones])
        prompt = f"""Soy {self.nombre}, un(a) {self.rol}.
Mi responsabilidad es: {self.descripcion}.
Conozco a los siguientes agentes:
{otros_agentes}
Historial de conversaciones: {historial_formateado}
Historial de mensajes: {self.historial_mensajes}
Mensaje recibido: '{entrada_usuario}'
Responde acorde a tu rol específico."""
        respuesta = self.enviar_a_gemini(prompt)
        self.historial_mensajes.append(f"Usuario: {entrada_usuario}, Agente: {respuesta}")

        # Guardar la conversación en memory.json
        memoria = leer_memoria()
        nueva_conversacion = {
            "agent1": self.nombre,
            "agent2": "Usuario",
            "messages": [
                {"sender": "Usuario", "text": entrada_usuario, "timestamp": "ahora"},
                {"sender": self.nombre, "text": respuesta, "timestamp": "ahora"}
            ]
        }
        memoria['conversations'].append(nueva_conversacion)
        with open('memory.json', 'w') as f:
            json.dump(memoria, f, indent=2)

        return respuesta
    
    
     # <-- Enviar a Gemini
    def enviar_a_gemini(self, prompt):             
        respuesta = self.modelo.generate_content(prompt)
        return respuesta.text.strip()

def leer_memoria():
    with open('memory.json', 'r') as f:
        memoria = json.load(f)
    return memoria

agentes = []
albert = AgenteIA("Albert", "Desarrollador Backend", "Encargado de la lógica del servidor, APIs y base de datos MySQL.", agentes)
carlos = AgenteIA("Carlos", "Desarrollador Frontend", "Diseña interfaces interactivas, claras y funcionales.", agentes)
ana = AgenteIA("Ana", "Diseñadora UX/UI", "Optimiza la experiencia del usuario para que sea fluida e intuitiva.", agentes)
lucas = AgenteIA("Lucas", "DBA", "Administra el diseño, seguridad y rendimiento de la base de datos MySQL.", agentes)
pedro = AgenteIA("Pedro", "Product Owner", "Define requerimientos del negocio y traduce necesidades del cliente en tareas técnicas.", agentes)

agentes = [albert, carlos, ana, lucas, pedro]

for agente in agentes:
    agente.agentes = agentes

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    respuesta = None
    nombre_agente = None
    if request.method == "POST":
        agente_idx = int(request.form["agente"])
        pregunta = request.form["pregunta"]
        agente = agentes[agente_idx]
        respuesta = agente.actuar(pregunta)
        nombre_agente = agente.nombre

    return render_template("index.html", agentes=agentes, respuesta=respuesta, nombre_agente=nombre_agente)

if __name__ == "__main__":
    app.run(debug=True)





#Cómo usar:
#Ejecuta agent_maker.py:

#bash
#python agent_maker.py
#Abre en el navegador:


#http://127.0.0.1:5000/
#Elige agente, escribe pregunta, envía y obtén la respuesta generada.
