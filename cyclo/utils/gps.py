#De alguna forma esto debe servir para leer datos del gps, formatearlos y retornarlos como un objeto coordenada

class GPS():
    def __init__(self):
        print("New Cyclo")
        # Where read data
        port = "/dev/ttyAMA0"

    @staticmethod
    def current_location():
        # Return a coord object with all data
        return [12.12,12.12,400]
