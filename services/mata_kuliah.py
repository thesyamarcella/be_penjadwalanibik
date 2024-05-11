from models.mata_kuliah import MataKuliah

class MataKuliahService:
    mata_kuliah = []

    @staticmethod
    def create_mata_kuliah(mata_kuliah_data):
        mata_kuliah_obj = MataKuliah(**mata_kuliah_data)
        MataKuliahService.mata_kuliah.append(mata_kuliah_obj)
        return mata_kuliah_obj

    @staticmethod
    def get_mata_kuliah_by_name(name):
        for mata_kuliah in MataKuliahService.mata_kuliah:
            if mata_kuliah.name == name:
                return mata_kuliah
        return None
