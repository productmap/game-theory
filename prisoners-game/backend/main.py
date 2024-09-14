from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
import numpy as np

app = FastAPI()

# Матрица выплат
payoff_matrix = np.array([
    [3, 0],  # Выплаты для стратегии C
    [5, 1]   # Выплаты для стратегии D
])

# Начальные частоты стратегий
initial_frequencies = np.array([0.5, 0.5])  # 50% C и 50% D

# Количество итераций
num_iterations = 100

# Массивы для хранения частот стратегий на каждом шаге
frequencies_history = np.zeros((num_iterations, 2))
frequencies_history[0] = initial_frequencies

# Репликаторная динамика
for t in range(1, num_iterations):
    frequencies = frequencies_history[t-1]
    average_fitness = np.dot(payoff_matrix, frequencies)
    population_fitness = np.dot(frequencies, average_fitness)
    new_frequencies = frequencies * average_fitness / population_fitness
    new_frequencies /= np.sum(new_frequencies)
    frequencies_history[t] = new_frequencies

@app.get("/frequencies")
def get_frequencies():
    return {"frequencies": frequencies_history.tolist()}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Message text was: {data}")
    except WebSocketDisconnect:
        pass

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
