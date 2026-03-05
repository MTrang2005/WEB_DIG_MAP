# data.py

# DỮ LIỆU CHI TIẾT CÁC ĐỊA ĐIỂM (PHẦN III.4 TRONG TÀI LIỆU)
LOCATIONS = [
    {
        "name": "Chòi Nghỉ",
        "category": "Dừng chân",
        "lat": 22.3365, # Cần cập nhật tọa độ thực tế
        "lon": 103.8123,
        "description": "Chòi Nghỉ là điểm dừng chân lý tưởng cho du khách trên hành trình tham quan khu tâm linh. Tại đây, du khách có thể nghỉ ngơi, ngắm cảnh núi rừng Sa Pa và tận hưởng không khí trong lành, yên tĩnh.",
        "image": "assets/choi-nghi.jpg", 
        "hours": "08:00 - 16:30 (theo giờ mở cửa của khu tham quan)"
    },
    {
        "name": "Chùa thượng - Vân Phong Thiền Tự",
        "category": "Tâm linh",
        "lat": 22.3370,
        "lon": 103.8130,
        "description": "Ngôi chùa toạ lạc ở độ cao 3.091m, được thiết kế theo kiến trúc thời Trần bao gồm Tam bảo, Nhà tổ và 2 dãy hành lang. Nằm giữa không gian hùng vĩ của đỉnh Fansipan huyền thoại, sở hữu vẻ đẹp bồng lai, là chốn linh thiêng, mang đến sự an lành, bình yên cho du khách.",
        "image": "assets/chua-thuong.jpg",
        "hours": "08:00 - 16:30"
    },
    {
        "name": "Bảo Tháp",
        "category": "Tâm linh",
        "lat": 22.3375,
        "lon": 103.8135,
        "description": "Công trình tâm linh nổi bật, mang ý nghĩa lưu giữ giá trị Phật giáo. Bảo tháp cao 11 tầng, bề mặt tháp được ghép từ đá, đỉnh hình tháp hoa sen được đúc bằng đồng. Kiến trúc đặc trưng miền Bắc như tháp Phổ Minh (Nam Định), tháp Bình Sơn (Vĩnh Phúc).",
        "image": "assets/bao-thap.jpg",
        "hours": "08:00 - 16:30"
    },
    {
        "name": "Tượng Quán Thế Âm Bồ Tát",
        "category": "Tâm linh",
        "lat": 22.3380,
        "lon": 103.8140,
        "description": "Tượng được đúc bằng đồng, cao 12m, nặng 18 tấn, mắt hướng nhìn về phía Đông, tay phải cầm cành dương liễu, tay trái cầm bình cam lộ biểu trưng cho lòng từ bi và nhân ái. Ngự trên tảng đá lớn với tầm nhìn hướng xuống dân gian.",
        "image": "assets/quan-the-am.jpg",
        "hours": "08:00 - 16:30"
    },
    {
        "name": "Miếu Sơn Thần",
        "category": "Tâm linh",
        "lat": 22.3385,
        "lon": 103.8145,
        "description": "Miếu thờ thần núi với kiến trúc thời Trần. Núi tượng trưng cho chiều cao và vị trí trung tâm. Miếu nhắc nhở mọi người trân trọng thiên nhiên, bảo vệ nguồn nước khoáng ngầm và gìn giữ tài nguyên.",
        "image": "assets/mieu-son-than.jpg",
        "hours": "08:00 - 16:30"
    },
    {
        "name": "Phòng thông tin",
        "category": "Dịch vụ",
        "lat": 22.3390,
        "lon": 103.8150,
        "description": "Phòng Thông Tin hỗ trợ du khách về bản đồ, hướng dẫn tham quan, lịch trình và giải đáp thắc mắc.",
        "image": "assets/phong-thong-tin.jpg",
        "hours": "08:00 – 17:00"
    },
    {
        "name": "Chùa trình - Bảo An Thiền Tự",
        "category": "Tâm linh",
        "lat": 16.0, # Tọa độ độ cao 1604m
        "lon": 108.0,
        "description": "Nằm trên địa thế tuyệt đẹp ở độ cao 1604m trong quần thể Ga Hoàng Liên, Bảo An Thiền Tự là điểm dừng chân đầu tiên của du khách trước khi bước vào hành trình hành hương lễ Phật.",
        "image": "assets/chua-trinh.jpg",
        "hours": "08:00 - 16:30"
    }
]