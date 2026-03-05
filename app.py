import streamlit as st
import folium
import json
from streamlit_folium import st_folium
from folium.plugins import LocateControl, AntPath

# 1. CẤU HÌNH TRANG (Đáp ứng yêu cầu VI: tương thích di động)
st.set_page_config(page_title="Bản Đồ Fansipan", layout="wide")

# Đọc file GeoJSON bạn đã tinh chỉnh
with open('map_data.json', encoding='utf-8') as f:
    geojson_data = json.load(f)

# 2. SIDEBAR QUẢN LÝ (Đáp ứng yêu cầu III.1, III.5)
st.sidebar.title("Điều hướng nhanh")

# Chuyển vùng nhanh
area_choice = st.sidebar.radio("Chọn khu vực:", ["Fansipan", "Sun Plaza"])
center_coords = [22.305, 103.775] if area_choice == "Fansipan" else [22.337, 103.824]
zoom_level = 17 if area_choice == "Fansipan" else 16

# Tính năng Chỉ đường (Yêu cầu III.5)
st.sidebar.subheader("Chỉ đường nội khu")
# Lọc danh sách địa điểm theo vùng đã chọn
locations_in_area = [f['properties']['name'] for f in geojson_data['features'] 
                     if f['properties']['area'] == area_choice]

start_node = st.sidebar.selectbox("Điểm đi:", locations_in_area)
end_node = st.sidebar.selectbox("Điểm đến:", locations_in_area)

# 3. KHỞI TẠO BẢN ĐỒ
m = folium.Map(location=center_coords, zoom_start=zoom_level)

# Hiển thị các điểm từ GeoJSON (Yêu cầu III.2)
folium.GeoJson(
    geojson_data,
    name="Địa điểm Fansipan",
    tooltip=folium.GeoJsonTooltip(fields=["name"], localize=True),
    popup=folium.GeoJsonPopup(fields=["name", "category"]),
).add_to(m)

# Hiển thị vị trí người dùng GPS (Yêu cầu III.3)
LocateControl(auto_start=False, fly_to=True).add_to(m)

# 4. LOGIC CHỈ ĐƯỜNG (Routing)
if st.sidebar.button("Tìm đường đi"):
    # Tìm tọa độ của điểm đi và điểm đến
    p1 = next(f['geometry']['coordinates'] for f in geojson_data['features'] 
              if f['properties']['name'] == start_node)
    p2 = next(f['geometry']['coordinates'] for f in geojson_data['features'] 
              if f['properties']['name'] == end_node)
    
    # Vẽ đường đi (đảo ngược coordinates sang [lat, lon])
    path_coords = [[p1[1], p1[0]], [p2[1], p2[0]]]
    AntPath(locations=path_coords, color="blue", weight=5, delay=1000).add_to(m)
    st.sidebar.info(f"Đường đi: {start_node} ➔ {end_node}")

# 5. RENDER BẢN ĐỒ LÊN WEB
st_folium(m, width="100%", height=600)