import pickle

def save(data):
    with open("best.pkl", "wb") as file:
        pickle.dump(data, file=file)