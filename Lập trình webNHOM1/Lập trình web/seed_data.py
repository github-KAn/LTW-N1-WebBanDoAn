from flask import Flask, render_template, request, redirect, session, url_for, flash
from numpy.ma.core import product
from pymongo import MongoClient
from bson.objectid import ObjectId, InvalidId
from flask_pymongo import PyMongo



app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/your_database_name"
mongo = PyMongo(app)

# Kết nối MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['nhom1']  # Đổi thành tên database của bạn
packages_collection = db['packages']
processed_collection = db['processed_items']
drinks_collection = db['drinks']
gifts_collection = db['gifts']
menu_collection = db['menu_items']
products_packages_collection = db['products_packages']
products_processed_items_collection = db['products_processed_items']
products_drinks_collection = db['products_drinks']
products_gifts_collection = db['products_gifts']


# Dữ liệu các gói ăn
packages = [
    {
        "id": 1,
        "name": "Gói fit 1",
        "price": 700000,
        "image": "images/fit1.jpg",
        "description": "Sáng - Trưa",
        "time": "1 tuần - 1 tháng"
    },
    {
    "id": 2,
        "name": "Gói fit 2",
        "price": 800000,
        "image": "images/fit2.jpg",
        "description": "Sáng - Tối",
        "time": "1 tuần - 1 tháng"
    },
    {
    "id": 3,
        "name": "Gói fit 3",
        "price": 600000,
        "image": "images/fit3.jpg",
        "description": "Trưa - Tối",
        "time": "1 tuần - 1 tháng"
    },
    {
    "id": 4,
        "name": "Gói full",
        "price": 1000000,
        "image": "images/fullfit.jpg",
        "description": "Sáng - Trưa - Tối",
        "time": "1 tuần - 1 tháng"
    },
    {
    "id": 5,
        "name": "Gói chay",
        "price": 650000,
        "image": "images/chay.jpg",
        "description": "Sáng - Trưa",
        "time": "1 tuần - 1 tháng"
    },
    {
    "id": 6,
        "name": "Gói slim",
        "price": 600000,
        "image": "images/slim.png",
        "description": "Sáng - Trưa",
        "time": "1 tuần - 1 tháng"
    },
    {
    "id": 7,
        "name": "Gói LUNCH",
        "price": 500000,
        "image": "images/lunch.png",
        "description": "Trưa",
        "time": "1 tuần - 1 tháng"
    },
    {
    "id": 8,
        "name": "Gói MEAT",
        "price": 750000,
        "image": "images/meat.jpg",
        "description": "Sáng - Trưa",
        "time": "1 tuần - 1 tháng"
    }
]

# Xóa dữ liệu cũ và thêm dữ liệu mới
packages_collection.delete_many({})
packages_collection.insert_many(packages) #Sử dụng biến đã định nghĩa
print("Dữ liệu cho mục 'GÓI ĂN' đã được thêm vào cơ sở dữ liệu.")

# Thêm dữ liệu cho các sản phẩm thuộc mục "CHẾ BIẾN SẴN"
processed_items = [
    {
    "id": 1,
        "name": "COMBO 04 GÓI ỨC GÀ VIÊN (MỚI)",
        "price": 180000,
        "image": "images/ảnhcbs1.png",
        "description": "200 Gram/Gói",
        "category": "chế biến sẵn"
    },
    {
    "id": 2,
        "name": "05 Chai cà phê Cold Brew Lacàph",
        "price": 229000,
        "image": "images/anhcbs2.jpg",
        "description": "100 Gram/Gói",
        "category": "chế biến sẵn"
    },
    {
    "id": 3,
        "name": "08 gói Ức gà ăn liền",
        "price": 175000,
        "image": "images/anhcbs3.jpg",
        "description": "625 Gram/Gói",
        "category": "chế biến sẵn"
    },
    {
    "id": 4,
        "name": "1 chai Lacàph Cà phê ủ lạnh Cold Brew",
        "price": 35000,
        "image": "images/anhcbs4.jpg",
        "description": "1 Chai/Gói",
        "category": "chế biến sẵn"
    },
    {
    "id": 5,
        "name": "05 gói Cơm gạo lức ăn liền",
        "price": 119000,
        "image": "images/anhcbs5.jpg",
        "description": "200 Gram/Gói",
        "category": "chế biến sẵn"
    },
    {
    "id": 6,
        "name": "BOX Ức gà mềm mọng",
        "price": 459000,
        "image": "images/anhcbs6.jpg",
        "description": "1000 Gram/Hộp",
        "category": "chế biến sẵn"
    },
    {
    "id": 7,
        "name": "Box Trái Cây Thanh Mảnh",
        "price": 199000,
        "image": "images/anhcbs7.jpg",
        "description": "3200 Gram/Hộp",
        "category": "chế biến sẵn"
    },
    {
    "id": 8,
        "name": "Gói fit 3",
        "price": 600000,
        "image": "images/fit3.jpg",
        "description": "Trưa - Tối",
        "category": "chế biến sẵn"
    }
]

# Xóa dữ liệu cũ và Thêm dữ liệu mới
db['processed_items'].delete_many({})
db['processed_items'].insert_many(processed_items) #Sử dụng cú pháp từ điển
print("Dữ liệu cho mục 'CHẾ BIẾN SẴN' đã được thêm vào cơ sở dữ liệu.")


# Dữ liệu cho phần "GÓI NƯỚC"
drinks = [
    {
    "id": 1,
        "name": "FITFOOD JUICE SWEETIE",
        "price": 200000,
        "image": "images/nuoc1.jpeg",
        "description": "200,000đ",
        "category": "gói nước",
        "time": "5 Chai/Tuần"
    },
    {
    "id": 2,
        "name": "FITFOOD JUICE GREENIE",
        "price": 200000,
        "image": "images/nuoc2.jpeg",
        "description": "200,000đ",
        "category": "gói nước",
        "time": "5 Chai/Tuần"
    }
]

# Xóa dữ liệu cũ và thêm dữ liệu mới cho gói nước
db.drinks.delete_many({})
db.drinks.insert_many(drinks) #Sử dụng thuộc tính
print("Dữ liệu cho mục 'GÓI NƯỚC' đã được thêm vào cơ sở dữ liệu.")


# Dữ liệu cho phần "QUÀ TẶNG"
gifts = [
    {
    "id": 1,
        "name": "Hộp Blind Box",
        "price": 100000,
        "image": "images/qua1.jpg",
        "description": "100,000đ",
        "category": "quà tặng",
        "time": "100 Gram/Hộp"
    },
    {
    "id": 2,
        "name": "SET QUÀ FITFOOD",
        "price": 319000,
        "image": "images/qua2.jpg",
        "description": "319,000đ",
        "category": "quà tặng",
        "time": "1 Chai/Hộp"
    }
]


# Xóa dữ liệu cũ và thêm dữ liệu mới cho quà tặng
db.gifts.delete_many({})
db.gifts.insert_many(gifts)
print("Dữ liệu cho mục 'QUÀ TẶNG' đã được thêm vào cơ sở dữ liệu.")

menu_items = [
    {
        "day": "T2",
        "date": "14.10",
        "menu_items_list": [
            {
                "name": "SALAD GÀ CAJUN BALSAMIC",
                "description": "Cajun Chicken Salad W Balsamic Sauce",
                "calories": 350,
                "nutrition": "29, 10, 35"
            },
            {
                "name": "**BÒ TỨ XUYÊN + BÚN GẤC** (NEW)",
                "description": "Sichuan Beef with Noodles** (NEW)",
                "calories": 550 ,
                "nutrition": "41, 28, 35"
            },
            {
                "name": "MÌ Ý TÔM SỐT CÀ",
                "description": "Shrimp Pasta in Tomato Sauce",
                "calories": 460 ,
                "nutrition": "35, 20, 34"
            }
        ]
    },
    {
        "day": "T3",
        "date": "15.10",
        "menu_items_list": [
            {
                "name": "SALAD GÀ CAJUN BALSAMIC",
                "description": "Cajun Chicken Salad W Balsamic Sauce",
                "calories": 350,
                "nutrition": "29, 10, 35"
            },
            {
                "name": "**BÒ TỨ XUYÊN + BÚN GẤC** (NEW)",
                "description": "Sichuan Beef with Noodles** (NEW)",
                "calories": 550,
                "nutrition": "41, 28, 35"
            },
            {
                "name": "MÌ Ý TÔM SỐT CÀ",
                "description": "Shrimp Pasta in Tomato Sauce",
                "calories": 460,
                "nutrition": "35, 20, 34"
            }
        ]
    },
{
        "day": "T4",
        "date": "16.10",
        "menu_items_list": [
            {
                "name": "SALAD GÀ CAJUN BALSAMIC",
                "description": "Cajun Chicken Salad W Balsamic Sauce",
                "calories": 350,
                "nutrition": "29, 10, 35"
            },
            {
                "name": "**BÒ TỨ XUYÊN + BÚN GẤC** (NEW)",
                "description": "Sichuan Beef with Noodles** (NEW)",
                "calories": 550 ,
                "nutrition": "41, 28, 35"
            },
            {
                "name": "MÌ Ý TÔM SỐT CÀ",
                "description": "Shrimp Pasta in Tomato Sauce",
                "calories": 460 ,
                "nutrition": "35, 20, 34"
            }
        ]
    },
{
        "day": "T5",
        "date": "17.10",
        "menu_items_list": [
            {
                "name": "SALAD GÀ CAJUN BALSAMIC",
                "description": "Cajun Chicken Salad W Balsamic Sauce",
                "calories": 350,
                "nutrition": "29, 10, 35"
            },
            {
                "name": "**BÒ TỨ XUYÊN + BÚN GẤC** (NEW)",
                "description": "Sichuan Beef with Noodles** (NEW)",
                "calories": 550 ,
                "nutrition": "41, 28, 35"
            },
            {
                "name": "MÌ Ý TÔM SỐT CÀ",
                "description": "Shrimp Pasta in Tomato Sauce",
                "calories": 460 ,
                "nutrition": "35, 20, 34"
            }
        ]
    },
{
        "day": "T6",
        "date": "18.10",
        "menu_items_list": [
            {
                "name": "SALAD GÀ CAJUN BALSAMIC",
                "description": "Cajun Chicken Salad W Balsamic Sauce",
                "calories": 350,
                "nutrition": "29, 10, 35"
            },
            {
                "name": "**BÒ TỨ XUYÊN + BÚN GẤC** (NEW)",
                "description": "Sichuan Beef with Noodles** (NEW)",
                "calories": 550 ,
                "nutrition": "41, 28, 35"
            },
            {
                "name": "MÌ Ý TÔM SỐT CÀ",
                "description": "Shrimp Pasta in Tomato Sauce",
                "calories": 460 ,
                "nutrition": "35, 20, 34"
            }
        ]
    },
{
        "day": "T7",
        "date": "19.10",
        "menu_items_list": [
            {
                "name": "SALAD GÀ CAJUN BALSAMIC",
                "description": "Cajun Chicken Salad W Balsamic Sauce",
                "calories": 350,
                "nutrition": "29, 10, 35"
            },
            {
                "name": "**BÒ TỨ XUYÊN + BÚN GẤC** (NEW)",
                "description": "Sichuan Beef with Noodles** (NEW)",
                "calories": 550 ,
                "nutrition": "41, 28, 35"
            },
            {
                "name": "MÌ Ý TÔM SỐT CÀ",
                "description": "Shrimp Pasta in Tomato Sauce",
                "calories": 460 ,
                "nutrition": "35, 20, 34"
            }
        ]
    },
{
        "day": "CN",
        "date": "20.10",
        "menu_items_list": [
            {
                "name": "SALAD GÀ CAJUN BALSAMIC",
                "description": "Cajun Chicken Salad W Balsamic Sauce",
                "calories": 350,
                "nutrition": "29, 10, 35"
            },
            {
                "name": "**BÒ TỨ XUYÊN + BÚN GẤC** (NEW)",
                "description": "Sichuan Beef with Noodles** (NEW)",
                "calories": 550 ,
                "nutrition": "41, 28, 35"
            },
            {
                "name": "MÌ Ý TÔM SỐT CÀ",
                "description": "Shrimp Pasta in Tomato Sauce",
                "calories": 460 ,
                "nutrition": "35, 20, 34"
            }
        ]
    }
]
db.menu_items.delete_many({})
db.menu_items.insert_many(menu_items)
print("Dữ liệu cho mục 'THỰC ĐƠN' đã được thêm vào cơ sở dữ liệu.")

vegetarians = [
    {
        "day": "T2",
        "date": "14.10",
        "vegetarians_items": [
            {
                "name": "XÍU MẠI CHAY",
                "description": "Vegetarian Meatball"
            },
            {
                "name": "**Gà chay sốt cam** (NEW)",
                "description": "**Vegetarian Chicken With Orange Sauce** (NEW)"
            }
        ]
    },
    {
        "day": "T3",
        "date": "15.10",
        "vegetarians_items": [
            {
                "name": "BÁNH BÔNG CẢI SỐT HUMMUS",
                "description": "Broccoli Pie served with Hummus Sauce"
            },
            {
                "name": "**Miến Gochujang chay** (NEW)",
                "description": "**Vegetarian Gochujang Vermicelli** (NEW)"
            }
        ]
    },
    {
        "day": "T4",
        "date": "16.10",
        "vegetarians_items": [
            {
                "name": "**Cà ri gà lát chay** (NEW)",
                "description": "**Vegetarian Chicken Curry** (NEW)"
            },
            {
                "name": "Bún thịt nướng chay",
                "description": "Vegetarian Grilled Pork and Brown Rice Vermicelli"
            }
        ]
    },
    {
        "day": "T5",
        "date": "17.10",
        "vegetarians_items": [
            {
                "name": "CÀ TÍM DỒN RAU CỦ + Gạo lức nâu",
                "description": "Stuffed Eggplant Served With Brown Rice"
            },
            {
                "name": "TEMPEH CHIÊN GIÒN + SỐT MÈ RANG",
                "description": "Crunchy Tempeh With Sesame Sauce"
            }
        ]
    },
    {
        "day": "T6",
        "date": "18.10",
        "vegetarians_items": [
            {
                "name": "CẢI THẢO CUỘN GÀ CHAY",
                "description": "Vegetable Chicken Roll + Corn Vermicelli"
            },
            {
                "name": "**Cơm gà teriyaki chay** (NEW)",
                "description": "**Vegetarian Teriyaki Chicken** (NEW)"
            }
        ]
    },
    {
        "day": "T7",
        "date": "19.10",
        "vegetarians_items": [
            {
                "name": "XÍU MẠI CHAY",
                "description": "Vegetarian Meatball"
            },
            {
                "name": "**Gà chay sốt cam** (NEW)",
                "description": "**Vegetarian Chicken With Orange Sauce** (NEW)"
            }
        ]
    },
    {
        "day": "CN",
        "date": "20.10",
        "vegetarians_items": [
            {
                "name": "BÁNH BÔNG CẢI SỐT HUMMUS",
                "description": "Broccoli Pie served with Hummus Sauce"
            },
            {
                "name": "**Miến Gochujang chay** (NEW)",
                "description": "**Vegetarian Gochujang Vermicelli** (NEW)"
            }
        ]
    }
]
db.vegetarians.delete_many({})
db.vegetarians.insert_many(vegetarians)
print("Dữ liệu cho mục 'THỰC ĐƠN CHAY' đã được thêm vào cơ sở dữ liệu.")


products_packages = [
    {
        "id": 1,
        "name": "Gói fit 1",
        "description": "Gói fit 1 gồm 2 bữa TRƯA - TỐI (Hạn chế tinh bột, GẤP ĐÔI rau)",
        "details": [
            "Sử dụng thực đơn 2 bữa TRƯA - TỐI tại trang fitfood.vn/menu.",
            "Giao 02 phần ăn tận nơi mỗi ngày, từ thứ 2 đến thứ 6.",
            "Calories dao động từ 300 - 400 Kcal / phần ăn.",
            "Lưu ý gói SLIM này HẠN CHẾ tinh bột, ít đường, gấp đôi lượng rau củ và giảm lượng đạm."
        ],
        "suitable_for": "* Thích hợp cho các bạn siết cân, thích ăn nhiều rau, giảm cân nhanh, và tiết kiệm thời gian.",
        "options": [
            {"plan": "Gói Tuần - 5 ngày", "selected": True},
            {"plan": "Gói Tháng (4 tuần)", "selected": False}
        ],
        "price": 700000,
        "image": "images/fit1.jpg"  # Đường dẫn hình ảnh sản phẩm
    },
    {
        "id": 2,
        "name": "Gói fit 2",
        "description": "Gói fit 2 với 1 bữa TRƯA năng lượng cao",
        "details": [
            "Thực đơn gồm 1 bữa trưa bổ dưỡng, phù hợp cho người bận rộn.",
            "Giao mỗi ngày từ thứ 2 đến thứ 6.",
            "Calories từ 500 - 600 Kcal mỗi phần ăn.",
            "Bổ sung đầy đủ protein và rau củ cho năng lượng bền vững."
        ],
        "suitable_for": "* Phù hợp cho người cần bữa ăn tiện lợi, giàu năng lượng.",
        "options": [
            {"plan": "Gói Tuần - 5 ngày", "selected": True},
            {"plan": "Gói Tháng (4 tuần)", "selected": False}
        ],
        "price": 800000,
        "image": "images/fit2.jpg"
    },
{
        "id": 3,
        "name": "Gói fit 3",
        "description": "Gói fit 3 gồm 2 bữa TRƯA - TỐI (Hạn chế tinh bột, GẤP ĐÔI rau)",
        "details": [
            "Sử dụng thực đơn 2 bữa TRƯA - TỐI tại trang fitfood.vn/menu.",
            "Giao 02 phần ăn tận nơi mỗi ngày, từ thứ 2 đến thứ 6.",
            "Calories dao động từ 300 - 400 Kcal / phần ăn.",
            "Lưu ý gói SLIM này HẠN CHẾ tinh bột, ít đường, gấp đôi lượng rau củ và giảm lượng đạm."
        ],
        "suitable_for": "* Thích hợp cho các bạn siết cân, thích ăn nhiều rau, giảm cân nhanh, và tiết kiệm thời gian.",
        "options": [
            {"plan": "Gói Tuần - 5 ngày", "selected": True},
            {"plan": "Gói Tháng (4 tuần)", "selected": False}
        ],
        "price": 600000,
        "image": "images/fit3.jpg"  # Đường dẫn hình ảnh sản phẩm
    },
{
        "id": 4,
        "name": "Gói full",
        "description": "Gói full gồm 2 bữa TRƯA - TỐI (Hạn chế tinh bột, GẤP ĐÔI rau)",
        "details": [
            "Sử dụng thực đơn 2 bữa TRƯA - TỐI tại trang fitfood.vn/menu.",
            "Giao 02 phần ăn tận nơi mỗi ngày, từ thứ 2 đến thứ 6.",
            "Calories dao động từ 300 - 400 Kcal / phần ăn.",
            "Lưu ý gói SLIM này HẠN CHẾ tinh bột, ít đường, gấp đôi lượng rau củ và giảm lượng đạm."
        ],
        "suitable_for": "* Thích hợp cho các bạn siết cân, thích ăn nhiều rau, giảm cân nhanh, và tiết kiệm thời gian.",
        "options": [
            {"plan": "Gói Tuần - 5 ngày", "selected": True},
            {"plan": "Gói Tháng (4 tuần)", "selected": False}
        ],
        "price": 1000000,
        "image": "images/fullfit.jpg"  # Đường dẫn hình ảnh sản phẩm
    },
{
        "id": 5,
        "name": "Gói chay",
        "description": "Gói chay gồm 2 bữa TRƯA - TỐI (Hạn chế tinh bột, GẤP ĐÔI rau)",
        "details": [
            "Sử dụng thực đơn 2 bữa TRƯA - TỐI tại trang fitfood.vn/menu.",
            "Giao 02 phần ăn tận nơi mỗi ngày, từ thứ 2 đến thứ 6.",
            "Calories dao động từ 300 - 400 Kcal / phần ăn.",
            "Lưu ý gói SLIM này HẠN CHẾ tinh bột, ít đường, gấp đôi lượng rau củ và giảm lượng đạm."
        ],
        "suitable_for": "* Thích hợp cho các bạn siết cân, thích ăn nhiều rau, giảm cân nhanh, và tiết kiệm thời gian.",
        "options": [
            {"plan": "Gói Tuần - 5 ngày", "selected": True},
            {"plan": "Gói Tháng (4 tuần)", "selected": False}
        ],
        "price": 650000,
        "image": "images/chay.jpg"  # Đường dẫn hình ảnh sản phẩm
    },
{
        "id": 6,
        "name": "Gói SLIM",
        "description": "Gói SLIM gồm 2 bữa TRƯA - TỐI (Hạn chế tinh bột, GẤP ĐÔI rau)",
        "details": [
            "Sử dụng thực đơn 2 bữa TRƯA - TỐI tại trang fitfood.vn/menu.",
            "Giao 02 phần ăn tận nơi mỗi ngày, từ thứ 2 đến thứ 6.",
            "Calories dao động từ 300 - 400 Kcal / phần ăn.",
            "Lưu ý gói SLIM này HẠN CHẾ tinh bột, ít đường, gấp đôi lượng rau củ và giảm lượng đạm."
        ],
        "suitable_for": "* Thích hợp cho các bạn siết cân, thích ăn nhiều rau, giảm cân nhanh, và tiết kiệm thời gian.",
        "options": [
            {"plan": "Gói Tuần - 5 ngày", "selected": True},
            {"plan": "Gói Tháng (4 tuần)", "selected": False}
        ],
        "price": 600000,
        "image": "images/slim.png"  # Đường dẫn hình ảnh sản phẩm
    },
{
        "id": 7,
        "name": "Gói LUNCH",
        "description": "Gói LUNCH gồm 2 bữa TRƯA - TỐI (Hạn chế tinh bột, GẤP ĐÔI rau)",
        "details": [
            "Sử dụng thực đơn 2 bữa TRƯA - TỐI tại trang fitfood.vn/menu.",
            "Giao 02 phần ăn tận nơi mỗi ngày, từ thứ 2 đến thứ 6.",
            "Calories dao động từ 300 - 400 Kcal / phần ăn.",
            "Lưu ý gói SLIM này HẠN CHẾ tinh bột, ít đường, gấp đôi lượng rau củ và giảm lượng đạm."
        ],
        "suitable_for": "* Thích hợp cho các bạn siết cân, thích ăn nhiều rau, giảm cân nhanh, và tiết kiệm thời gian.",
        "options": [
            {"plan": "Gói Tuần - 5 ngày", "selected": True},
            {"plan": "Gói Tháng (4 tuần)", "selected": False}
        ],
        "price": 500000,
        "image": "images/lunch.png"  # Đường dẫn hình ảnh sản phẩm
    },
{
        "id": 8,
        "name": "Gói MEAT",
        "description": "Gói MEAT gồm 2 bữa TRƯA - TỐI (Hạn chế tinh bột, GẤP ĐÔI rau)",
        "details": [
            "Sử dụng thực đơn 2 bữa TRƯA - TỐI tại trang fitfood.vn/menu.",
            "Giao 02 phần ăn tận nơi mỗi ngày, từ thứ 2 đến thứ 6.",
            "Calories dao động từ 300 - 400 Kcal / phần ăn.",
            "Lưu ý gói SLIM này HẠN CHẾ tinh bột, ít đường, gấp đôi lượng rau củ và giảm lượng đạm."
        ],
        "suitable_for": "* Thích hợp cho các bạn siết cân, thích ăn nhiều rau, giảm cân nhanh, và tiết kiệm thời gian.",
        "options": [
            {"plan": "Gói Tuần - 5 ngày", "selected": True},
            {"plan": "Gói Tháng (4 tuần)", "selected": False}
        ],
        "price": 750000,
        "image": "images/meat.jng"  # Đường dẫn hình ảnh sản phẩm
    },
]
db.products_packages.delete_many({})
db.products_packages.insert_many(products_packages)
print("Dữ liệu cho mục 'CHI TIẾT SẢN PHẨM GÓI ĂN' đã được thêm vào cơ sở dữ liệu.")




products_processed_items = [
    {
        "id": 1,
        "name": "Gói SLIM",
        "description": "Gói SLIM gồm 2 bữa TRƯA - TỐI (Hạn chế tinh bột, GẤP ĐÔI rau)",
        "details": [
            "Sử dụng thực đơn 2 bữa TRƯA - TỐI tại trang fitfood.vn/menu.",
            "Giao 02 phần ăn tận nơi mỗi ngày, từ thứ 2 đến thứ 6.",
            "Calories dao động từ 300 - 400 Kcal / phần ăn.",
            "Lưu ý gói SLIM này HẠN CHẾ tinh bột, ít đường, gấp đôi lượng rau củ và giảm lượng đạm."
        ],
        "suitable_for": "* Thích hợp cho các bạn siết cân, thích ăn nhiều rau, giảm cân nhanh, và tiết kiệm thời gian.",
        "options": [
            {"plan": "Gói Tuần - 5 ngày", "selected": True},
            {"plan": "Gói Tháng (4 tuần)", "selected": False}
        ],
        "price": 600000,
        "image": "images/slim.png"  # Đường dẫn hình ảnh sản phẩm
    },
    {
        "id": 2,
        "name": "Gói LUNCH",
        "description": "Gói SLIM gồm 2 bữa TRƯA - TỐI (Hạn chế tinh bột, GẤP ĐÔI rau)",
        "details": [
            "Sử dụng thực đơn 2 bữa TRƯA - TỐI tại trang fitfood.vn/menu.",
            "Giao 02 phần ăn tận nơi mỗi ngày, từ thứ 2 đến thứ 6.",
            "Calories dao động từ 300 - 400 Kcal / phần ăn.",
            "Lưu ý gói SLIM này HẠN CHẾ tinh bột, ít đường, gấp đôi lượng rau củ và giảm lượng đạm."
        ],
        "suitable_for": "* Thích hợp cho các bạn siết cân, thích ăn nhiều rau, giảm cân nhanh, và tiết kiệm thời gian.",
        "options": [
            {"plan": "Gói Tuần - 5 ngày", "selected": True},
            {"plan": "Gói Tháng (4 tuần)", "selected": False}
        ],
        "price": 600000,
        "image": "images/slim.png"  # Đường dẫn hình ảnh sản phẩm
    },
{
        "id": 3,
        "name": "Gói LUNCH",
        "description": "Gói SLIM gồm 2 bữa TRƯA - TỐI (Hạn chế tinh bột, GẤP ĐÔI rau)",
        "details": [
            "Sử dụng thực đơn 2 bữa TRƯA - TỐI tại trang fitfood.vn/menu.",
            "Giao 02 phần ăn tận nơi mỗi ngày, từ thứ 2 đến thứ 6.",
            "Calories dao động từ 300 - 400 Kcal / phần ăn.",
            "Lưu ý gói SLIM này HẠN CHẾ tinh bột, ít đường, gấp đôi lượng rau củ và giảm lượng đạm."
        ],
        "suitable_for": "* Thích hợp cho các bạn siết cân, thích ăn nhiều rau, giảm cân nhanh, và tiết kiệm thời gian.",
        "options": [
            {"plan": "Gói Tuần - 5 ngày", "selected": True},
            {"plan": "Gói Tháng (4 tuần)", "selected": False}
        ],
        "price": 600000,
        "image": "images/slim.png"  # Đường dẫn hình ảnh sản phẩm
    },
{
        "id": 4,
        "name": "Gói LUNCH",
        "description": "Gói SLIM gồm 2 bữa TRƯA - TỐI (Hạn chế tinh bột, GẤP ĐÔI rau)",
        "details": [
            "Sử dụng thực đơn 2 bữa TRƯA - TỐI tại trang fitfood.vn/menu.",
            "Giao 02 phần ăn tận nơi mỗi ngày, từ thứ 2 đến thứ 6.",
            "Calories dao động từ 300 - 400 Kcal / phần ăn.",
            "Lưu ý gói SLIM này HẠN CHẾ tinh bột, ít đường, gấp đôi lượng rau củ và giảm lượng đạm."
        ],
        "suitable_for": "* Thích hợp cho các bạn siết cân, thích ăn nhiều rau, giảm cân nhanh, và tiết kiệm thời gian.",
        "options": [
            {"plan": "Gói Tuần - 5 ngày", "selected": True},
            {"plan": "Gói Tháng (4 tuần)", "selected": False}
        ],
        "price": 600000,
        "image": "images/slim.png"  # Đường dẫn hình ảnh sản phẩm
    },
{
        "id": 5,
        "name": "Gói LUNCH",
        "description": "Gói SLIM gồm 2 bữa TRƯA - TỐI (Hạn chế tinh bột, GẤP ĐÔI rau)",
        "details": [
            "Sử dụng thực đơn 2 bữa TRƯA - TỐI tại trang fitfood.vn/menu.",
            "Giao 02 phần ăn tận nơi mỗi ngày, từ thứ 2 đến thứ 6.",
            "Calories dao động từ 300 - 400 Kcal / phần ăn.",
            "Lưu ý gói SLIM này HẠN CHẾ tinh bột, ít đường, gấp đôi lượng rau củ và giảm lượng đạm."
        ],
        "suitable_for": "* Thích hợp cho các bạn siết cân, thích ăn nhiều rau, giảm cân nhanh, và tiết kiệm thời gian.",
        "options": [
            {"plan": "Gói Tuần - 5 ngày", "selected": True},
            {"plan": "Gói Tháng (4 tuần)", "selected": False}
        ],
        "price": 600000,
        "image": "images/slim.png"  # Đường dẫn hình ảnh sản phẩm
    },
{
        "id": 6,
        "name": "Gói LUNCH",
        "description": "Gói SLIM gồm 2 bữa TRƯA - TỐI (Hạn chế tinh bột, GẤP ĐÔI rau)",
        "details": [
            "Sử dụng thực đơn 2 bữa TRƯA - TỐI tại trang fitfood.vn/menu.",
            "Giao 02 phần ăn tận nơi mỗi ngày, từ thứ 2 đến thứ 6.",
            "Calories dao động từ 300 - 400 Kcal / phần ăn.",
            "Lưu ý gói SLIM này HẠN CHẾ tinh bột, ít đường, gấp đôi lượng rau củ và giảm lượng đạm."
        ],
        "suitable_for": "* Thích hợp cho các bạn siết cân, thích ăn nhiều rau, giảm cân nhanh, và tiết kiệm thời gian.",
        "options": [
            {"plan": "Gói Tuần - 5 ngày", "selected": True},
            {"plan": "Gói Tháng (4 tuần)", "selected": False}
        ],
        "price": 600000,
        "image": "images/slim.png"  # Đường dẫn hình ảnh sản phẩm
    },
{
        "id": 7,
        "name": "Gói LUNCH",
        "description": "Gói SLIM gồm 2 bữa TRƯA - TỐI (Hạn chế tinh bột, GẤP ĐÔI rau)",
        "details": [
            "Sử dụng thực đơn 2 bữa TRƯA - TỐI tại trang fitfood.vn/menu.",
            "Giao 02 phần ăn tận nơi mỗi ngày, từ thứ 2 đến thứ 6.",
            "Calories dao động từ 300 - 400 Kcal / phần ăn.",
            "Lưu ý gói SLIM này HẠN CHẾ tinh bột, ít đường, gấp đôi lượng rau củ và giảm lượng đạm."
        ],
        "suitable_for": "* Thích hợp cho các bạn siết cân, thích ăn nhiều rau, giảm cân nhanh, và tiết kiệm thời gian.",
        "options": [
            {"plan": "Gói Tuần - 5 ngày", "selected": True},
            {"plan": "Gói Tháng (4 tuần)", "selected": False}
        ],
        "price": 600000,
        "image": "images/slim.png"  # Đường dẫn hình ảnh sản phẩm
    },
{
        "id": 8,
        "name": "Gói LUNCH",
        "description": "Gói SLIM gồm 2 bữa TRƯA - TỐI (Hạn chế tinh bột, GẤP ĐÔI rau)",
        "details": [
            "Sử dụng thực đơn 2 bữa TRƯA - TỐI tại trang fitfood.vn/menu.",
            "Giao 02 phần ăn tận nơi mỗi ngày, từ thứ 2 đến thứ 6.",
            "Calories dao động từ 300 - 400 Kcal / phần ăn.",
            "Lưu ý gói SLIM này HẠN CHẾ tinh bột, ít đường, gấp đôi lượng rau củ và giảm lượng đạm."
        ],
        "suitable_for": "* Thích hợp cho các bạn siết cân, thích ăn nhiều rau, giảm cân nhanh, và tiết kiệm thời gian.",
        "options": [
            {"plan": "Gói Tuần - 5 ngày", "selected": True},
            {"plan": "Gói Tháng (4 tuần)", "selected": False}
        ],
        "price": 600000,
        "image": "images/slim.png"  # Đường dẫn hình ảnh sản phẩm
    },
]
db.products_processed_items.delete_many({})
db.products_processed_items.insert_many(products_processed_items)
print("Dữ liệu cho mục 'CHI TIẾT SẢN PHẨM CHẾ BIẾN SẴN' đã được thêm vào cơ sở dữ liệu.")

products_drinks = [
{
        "id": 1,
        "name": "Gói SLIM",
        "description": "Gói SLIM gồm 2 bữa TRƯA - TỐI (Hạn chế tinh bột, GẤP ĐÔI rau)",
        "details": [
            "Sử dụng thực đơn 2 bữa TRƯA - TỐI tại trang fitfood.vn/menu.",
            "Giao 02 phần ăn tận nơi mỗi ngày, từ thứ 2 đến thứ 6.",
            "Calories dao động từ 300 - 400 Kcal / phần ăn.",
            "Lưu ý gói SLIM này HẠN CHẾ tinh bột, ít đường, gấp đôi lượng rau củ và giảm lượng đạm."
        ],
        "suitable_for": "* Thích hợp cho các bạn siết cân, thích ăn nhiều rau, giảm cân nhanh, và tiết kiệm thời gian.",
        "options": [
            {"plan": "Gói Tuần - 5 ngày", "selected": True},
            {"plan": "Gói Tháng (4 tuần)", "selected": False}
        ],
        "price": 600000,
        "image": "images/slim.png"  # Đường dẫn hình ảnh sản phẩm
    },
    {
        "id": 2,
        "name": "Gói LUNCH",
        "description": "Gói SLIM gồm 2 bữa TRƯA - TỐI (Hạn chế tinh bột, GẤP ĐÔI rau)",
        "details": [
            "Sử dụng thực đơn 2 bữa TRƯA - TỐI tại trang fitfood.vn/menu.",
            "Giao 02 phần ăn tận nơi mỗi ngày, từ thứ 2 đến thứ 6.",
            "Calories dao động từ 300 - 400 Kcal / phần ăn.",
            "Lưu ý gói SLIM này HẠN CHẾ tinh bột, ít đường, gấp đôi lượng rau củ và giảm lượng đạm."
        ],
        "suitable_for": "* Thích hợp cho các bạn siết cân, thích ăn nhiều rau, giảm cân nhanh, và tiết kiệm thời gian.",
        "options": [
            {"plan": "Gói Tuần - 5 ngày", "selected": True},
            {"plan": "Gói Tháng (4 tuần)", "selected": False}
        ],
        "price": 600000,
        "image": "images/slim.png"  # Đường dẫn hình ảnh sản phẩm
    },
]
db.products_drinks.delete_many({})
db.products_drinks.insert_many(products_drinks)
print("Dữ liệu cho mục 'CHI TIẾT SẢN PHẨM GÓI NƯỚC' đã được thêm vào cơ sở dữ liệu.")


products_gifts = [
{
        "id": 1,
        "name": "Gói SLIM",
        "description": "Gói SLIM gồm 2 bữa TRƯA - TỐI (Hạn chế tinh bột, GẤP ĐÔI rau)",
        "details": [
            "Sử dụng thực đơn 2 bữa TRƯA - TỐI tại trang fitfood.vn/menu.",
            "Giao 02 phần ăn tận nơi mỗi ngày, từ thứ 2 đến thứ 6.",
            "Calories dao động từ 300 - 400 Kcal / phần ăn.",
            "Lưu ý gói SLIM này HẠN CHẾ tinh bột, ít đường, gấp đôi lượng rau củ và giảm lượng đạm."
        ],
        "suitable_for": "* Thích hợp cho các bạn siết cân, thích ăn nhiều rau, giảm cân nhanh, và tiết kiệm thời gian.",
        "options": [
            {"plan": "Gói Tuần - 5 ngày", "selected": True},
            {"plan": "Gói Tháng (4 tuần)", "selected": False}
        ],
        "price": 600000,
        "image": "images/slim.png"  # Đường dẫn hình ảnh sản phẩm
    },
    {
        "id": 2,
        "name": "Gói LUNCH",
        "description": "Gói SLIM gồm 2 bữa TRƯA - TỐI (Hạn chế tinh bột, GẤP ĐÔI rau)",
        "details": [
            "Sử dụng thực đơn 2 bữa TRƯA - TỐI tại trang fitfood.vn/menu.",
            "Giao 02 phần ăn tận nơi mỗi ngày, từ thứ 2 đến thứ 6.",
            "Calories dao động từ 300 - 400 Kcal / phần ăn.",
            "Lưu ý gói SLIM này HẠN CHẾ tinh bột, ít đường, gấp đôi lượng rau củ và giảm lượng đạm."
        ],
        "suitable_for": "* Thích hợp cho các bạn siết cân, thích ăn nhiều rau, giảm cân nhanh, và tiết kiệm thời gian.",
        "options": [
            {"plan": "Gói Tuần - 5 ngày", "selected": True},
            {"plan": "Gói Tháng (4 tuần)", "selected": False}
        ],
        "price": 600000,
        "image": "images/slim.png"  # Đường dẫn hình ảnh sản phẩm
    },
]
db.products_gifts.delete_many({})
db.products_gifts.insert_many(products_gifts)
print("Dữ liệu cho mục 'CHI TIẾT SẢN PHẨM QUÀ TẶNG' đã được thêm vào cơ sở dữ liệu.")