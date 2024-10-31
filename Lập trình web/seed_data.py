
from pymongo import MongoClient

# Kết nối MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['ten_cua_database']  # Đổi thành tên database của bạn
packages_collection = db['packages']
processed_collection = db['processed_items']
drinks_collection = db['drinks']
gifts_collection = db['gifts']
menu_collection = db['menu_items']

# Dữ liệu các gói ăn
packages = [
    {
        "name": "Gói fit 1",
        "price": 700000,
        "image": "images/fit1.jpg",
        "description": "Sáng - Trưa",
        "time": "1 tuần - 1 tháng"
    },
    {
        "name": "Gói fit 2",
        "price": 800000,
        "image": "images/fit2.jpg",
        "description": "Sáng - Tối",
        "time": "1 tuần - 1 tháng"
    },
    {
        "name": "Gói fit 3",
        "price": 600000,
        "image": "images/fit3.jpg",
        "description": "Trưa - Tối",
        "time": "1 tuần - 1 tháng"
    },
    {
        "name": "Gói full",
        "price": 1000000,
        "image": "images/fullfit.jpg",
        "description": "Sáng - Trưa - Tối",
        "time": "1 tuần - 1 tháng"
    },
    {
        "name": "Gói chay",
        "price": 650000,
        "image": "images/chay.jpg",
        "description": "Sáng - Trưa",
        "time": "1 tuần - 1 tháng"
    },
    {
        "name": "Gói slim",
        "price": 600000,
        "image": "images/slim.png",
        "description": "Sáng - Trưa",
        "time": "1 tuần - 1 tháng"
    },
    {
        "name": "Gói LUNCH",
        "price": 500000,
        "image": "images/lunch.png",
        "description": "Trưa",
        "time": "1 tuần - 1 tháng"
    },
    {
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
        "name": "COMBO 04 GÓI ỨC GÀ VIÊN (MỚI)",
        "price": 180000,
        "image": "images/ảnhcbs1.png",
        "description": "200 Gram/Gói",
        "category": "chế biến sẵn"
    },
    {
        "name": "05 Chai cà phê Cold Brew Lacàph",
        "price": 229000,
        "image": "images/anhcbs2.jpg",
        "description": "100 Gram/Gói",
        "category": "chế biến sẵn"
    },
    {
        "name": "08 gói Ức gà ăn liền",
        "price": 175000,
        "image": "images/anhcbs3.jpg",
        "description": "625 Gram/Gói",
        "category": "chế biến sẵn"
    },
    {
        "name": "1 chai Lacàph Cà phê ủ lạnh Cold Brew",
        "price": 35000,
        "image": "images/anhcbs4.jpg",
        "description": "1 Chai/Gói",
        "category": "chế biến sẵn"
    },
    {
        "name": "05 gói Cơm gạo lức ăn liền",
        "price": 119000,
        "image": "images/anhcbs5.jpg",
        "description": "200 Gram/Gói",
        "category": "chế biến sẵn"
    },
    {
        "name": "BOX Ức gà mềm mọng",
        "price": 459000,
        "image": "images/anhcbs6.jpg",
        "description": "1000 Gram/Hộp",
        "category": "chế biến sẵn"
    },
    {
        "name": "Box Trái Cây Thanh Mảnh",
        "price": 199000,
        "image": "images/anhcbs7.jpg",
        "description": "3200 Gram/Hộp",
        "category": "chế biến sẵn"
    },
    {
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
        "name": "FITFOOD JUICE SWEETIE",
        "price": 200000,
        "image": "images/nuoc1.jpeg",
        "description": "200,000đ",
        "category": "gói nước",
        "time": "5 Chai/Tuần"
    },
    {
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
        "name": "Hộp Blind Box",
        "price": 100000,
        "image": "images/qua1.jpg",
        "description": "100,000đ",
        "category": "quà tặng",
        "time": "100 Gram/Hộp"
    },
    {
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