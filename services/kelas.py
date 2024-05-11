from models.kelas import Kelas

class KelasService:
    kelas = []

    @staticmethod
    def create_kelas(kelas_data):
        kelas_obj = Kelas(**kelas_data)
        KelasService.kelas.append(kelas_obj)
        return kelas_obj

    @staticmethod
    def get_kelas_by_name(name):
        for kelas in KelasService.kelas:
            if kelas.name == name:
                return kelas
        return None
