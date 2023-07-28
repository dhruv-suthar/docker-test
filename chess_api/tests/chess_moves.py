import requests

data = {
    "positions": {
        "Queen": "E7",
        "Bishop": "B7",
        "Rook": "G5",
        "Knight": "C3"
    }
}

response = requests.post("http://127.0.0.1:8000/chess/knight", json=data)
print(response.json())
