
class Subject:

    def __init__(self, new_values):
        self.values = new_values
        self.setup_sensors(data=new_values)

    def get_values(self):
        return self.values

    def setup_sensors(self,data):
        self.oberschenkel = data[data['id'] == 1324189]
        self.unterschenkel = data[data['id'] == 1324188]
        self.oberarm = data[data['id'] == 1324185]
        self.unterarm = data[data['id'] == 1324180]
        self.ruecken = data[data['id'] == 1324181]

    def get_accelX(self, sensor):
        data = self.filter_sensor(sensor)
        filtered_data = data[['timestamp','accelx_ms2']]
        return filtered_data

    def get_accelY(self, sensor):
        data = self.filter_sensor(sensor)
        filtered_data = data[['timestamp','accely_ms2']]
        return filtered_data

    def get_accelZ(self, sensor):
        data = self.filter_sensor(sensor)
        filtered_data = data[['timestamp','accelz_ms2']]
        return filtered_data

    def get_gyroX(self, sensor):
        data = self.filter_sensor(sensor)
        filtered_data = data[['timestamp','gyrox_rads']]
        return filtered_data

    def get_gyroY(self, sensor):
        data = self.filter_sensor(sensor)
        filtered_data = data[['timestamp','gyroy_rads']]
        return filtered_data

    def get_gyroZ(self, sensor):
        data = self.filter_sensor(sensor)
        filtered_data = data[['timestamp','gyroz_rads']]
        return filtered_data

    def get_magnetX(self, sensor):
        data = self.filter_sensor(sensor)
        filtered_data = data[['timestamp','magnetx_ut']]
        return filtered_data

    def get_magnetY(self, sensor):
        data = self.filter_sensor(sensor)
        filtered_data = data[['timestamp','magnety_ut']]
        return filtered_data

    def get_magnetZ(self, sensor):
        data = self.filter_sensor(sensor)
        filtered_data = data[['timestamp','magnetz_ut']]
        return filtered_data

    def filter_sensor(self, sensor):
        data = None
        if(sensor == 'oberschenkel'):
            data = self.oberschenkel
        elif(sensor == 'unterschenkel'):
            data = self.unterschenkel
        elif(sensor == 'oberarm'):
            data = self.oberarm
        elif(sensor == 'unterarm'):
            data = self.unterarm
        elif(sensor == 'ruecken'):
            data = self.ruecken
        return data
