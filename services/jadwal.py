from models.jadwal import Jadwal

class JadwalService:
    jadwal = []

    @staticmethod
    def create_jadwal(jadwal_data):
        jadwal_obj = Jadwal(**jadwal_data)
        JadwalService.jadwal.append(jadwal_obj)
        return jadwal_obj

    @staticmethod
    def get_jadwal_by_name(name):
        for jadwal in JadwalService.jadwal:
            if jadwal.name == name:
                return jadwal
        return None
