from models.ruangan import Kelas

class KelasService:
    ruangan = []

    @staticmethod
    def create_ruangan(ruangan_data):
        ruangan_obj = Kelas(**ruangan_data)
        KelasService.ruangan.append(ruangan_obj)
        return ruangan_obj

    @staticmethod
    def get_ruangan_by_name(name):
        for ruangan in KelasService.ruangan:
            if ruangan.name == name:
                return ruangan
        return None
