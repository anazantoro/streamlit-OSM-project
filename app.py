import streamlit as st
from model import HotspotModel
from view import HotspotView

data_url = 'https://raw.githubusercontent.com/anazantoro/dataset_hotspot_kaltim_forest_2024/refs/heads/main/dataset_hotspot_wilayah_kalimantan_timur.csv'

def main():
    model = HotspotModel(data_url)
    view = HotspotView()

    kabupaten_filter, kepercayaan_filter = view.render_filters(model)
    filtered_data = model.get_filtered_data(kabupaten_filter, kepercayaan_filter)
    view.render_table(filtered_data)

    if st.button('Tampilkan Peta Reguler'):
        view.render_basic_map(filtered_data)
    if st.button('Tampilkan Peta 3 Dimensi'):
        view.render_advanced_map(filtered_data)

if __name__ == '__main__':
    main()
