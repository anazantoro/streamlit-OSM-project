import streamlit as st
import pydeck as pdk

class HotspotView:
    def render_filters(self, model):
        kabupaten_filter = st.sidebar.multiselect(
            'Pilih Kabupaten', model.data['Kabupaten/Kota'].unique())
        kepercayaan_filter = st.sidebar.multiselect(
            'Pilih Tingkat Titik Panas', model.data['Kepercayaan'].unique())
        return kabupaten_filter, kepercayaan_filter

    def render_table(self, data):
        st.header('Dasbor Titik Panas Wilayah Kalimantan Timur')
        st.subheader('Hasil Filter Data')
        st.write(data)

    def render_basic_map(self, data):
        st.map(data[['latitude', 'longitude']])

    def render_advanced_map(self, data):
        st.pydeck_chart(pdk.Deck(
            map_style='mapbox://styles/mapbox/light-v9',
            initial_view_state=pdk.ViewState(
                latitude=data['latitude'].mean(),
                longitude=data['longitude'].mean(),
                zoom=6, pitch=50),
            layers=[pdk.Layer(
                'HexagonLayer', data[['latitude', 'longitude']],
                get_position='[longitude, latitude]',
                radius=10000, elevation_scale=50, extruded=True)]
        ))
