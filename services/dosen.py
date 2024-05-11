from models.dosen import Dosen

class DosenService:
    dosen = []

    @staticmethod
    def create_dosen(dosen_data):
        dosen_obj = Dosen(**dosen_data)
        DosenService.dosen.append(dosen_obj)
        return dosen_obj

    @staticmethod
    def get_dosen_by_name(name):
        for dosen in DosenService.dosen:
            if dosen.name == name:
                return dosen
        return None
