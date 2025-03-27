import pickle
import os
from datetime import datetime, timedelta

CACHE_FILE = "sample_object.pkl"

class sampleObject:
    def __init__(self):
        self.name = "Tiago"
        self.date_created = datetime.now().isoformat()
        self.time_created = datetime.now().time().isoformat()

def save_to_cache(obj):
    """Salva o objeto no arquivo usando pickle."""
    with open(CACHE_FILE, "wb") as f:
        pickle.dump(obj, f)

def load_from_cache():
    """Carrega o objeto do arquivo, se existir e for válido."""
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "rb") as f:
            obj = pickle.load(f)

        # Verifica se o objeto foi criado hoje
        obj_date = datetime.fromisoformat(obj.date_created).date()
        if obj_date == datetime.now().date():
            return obj  # Retorna o objeto se for do mesmo dia

    return None  # Retorna None se não houver um cache válido

def get_cached_object():
    """Retorna o objeto do cache ou cria um novo se necessário."""
    obj = load_from_cache()
    if obj is None:
        obj = sampleObject()
        save_to_cache(obj)
    return obj

if __name__ == "__main__":
    obj = get_cached_object()
    print("Nome:", obj.name)
    print("Criado em:", obj.date_created)
    print("Hora da criação:", obj.time_created)
