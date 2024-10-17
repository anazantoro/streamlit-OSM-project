import pandas as pd

class HotspotModel:
    def __init__(self, file_path):
        self.data = pd.read_csv(file_path)
        self.data.columns = self.data.columns.str.strip()
        self.data['longitude'] = self.data['Bujur'].str.replace(' BT', '').astype(float)
        self.data['latitude'] = self.data['Lintang'].apply(self._convert_latitude)

    def _convert_latitude(self, value):
        return float(value[:-3]) * (-1 if 'LS' in value else 1)

    def get_filtered_data(self, kabupaten_filter, kepercayaan_filter):
        return self.data[
            self.data['Kabupaten/Kota'].isin(kabupaten_filter) &
            self.data['Kepercayaan'].isin(kepercayaan_filter)
        ]


