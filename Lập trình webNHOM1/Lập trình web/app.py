# from crypt import methods

from flask import Flask, render_template, request, redirect, session, url_for, flash, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId, InvalidId
from waitress import serve
from flask_pymongo import PyMongo
from flask import abort
from seed_data import products_packages, products_processed_items, products_drinks, products_gifts


app = Flask(__name__)
app.secret_key = 'nhom1'
app.config["MONGO_URI"] = "mongodb://localhost:27017/your_database_name"
mongo = PyMongo(app)

# Kết nối MongoDB
try:
    client = MongoClient('mongodb://localhost:27017/')
    db = client['nhom1']
    packages_collection = db['packages']
    processed_collection = db['processed_items']
    drinks_collection = db['drinks']
    gifts_collection = db['gifts']
    menu_collection = db['menu_items']
    vegetarians_collection = db['vegetarians']
    products_packages_collection = db['products_packages']
    products_processed_items_collection = db['products_processed_items']
    products_drinks_collection = db['products_drinks']
    products_gifts_collection = db['products_gifts']
    user_collection = db['users']
except Exception as e:
    print(f"Lỗi kết nối MongoDB: {e}")
years_option=[]
days_option=[]
months_option=[]
for i in range (1900,2025):
    years_option.append(i)
for i in range (1,13):
    months_option.append(i)
for i in range (1,32):
    days_option.append(i)
@app.route('/')
def trang_chu():
    return render_template('Trangchu.html')

@app.template_filter('number_format')
def number_format(value, decimal_places=0, decimal_separator='.', thousands_separator=','):
    formatted_value = f"{value:,.{decimal_places}f}"
    return formatted_value.replace('.', decimal_separator)

@app.route('/dathang', methods=['GET', 'POST'])
def dat_hang():
    if request.method == 'POST':
        cart_items = request.form.getlist('cart_items')
        session['cart'] = cart_items
        return redirect(url_for('thanh_toan'))

    try:
        packages = list(packages_collection.find())
        processed_items = list(processed_collection.find())
        drinks = list(drinks_collection.find())
        gifts = list(gifts_collection.find())

    except Exception as e:
        flash("Lỗi khi tải dữ liệu từ cơ sở dữ liệu.", "error")
        packages, processed_items, drinks, gifts = [], [], [], []

    return render_template('DatHang.html', packages=packages, processed_items=processed_items, drinks=drinks, gifts=gifts )

@app.route('/chinhsua')
def chinh_sua():
    menu_items = list(menu_collection.find())
    return render_template('ChinhSua.html', menu_items=menu_items)

@app.route('/thucdon')
def thuc_don():
    menu_items = list(menu_collection.find())
    vegetarians = list(vegetarians_collection.find())
    return render_template('Thucdon.html', menu_items=menu_items, vegetarians=vegetarians)

@app.route('/tintuc')
def tin_tuc():
    return render_template('TinTuc.html')

@app.route('/faqs')
def faqs():
    return render_template('FAQs.html')

@app.route('/thanhtoan')
def thanh_toan():
    cart_items = session.get('cart', [])
    shipping_fee = 30000
    discount = 0

    subtotal = sum(item['price'] * item.get('quantity', 1) for item in cart_items if 'price' in item)
    return render_template('ThanhToan.html', cart_items=cart_items, shipping_fee=shipping_fee, discount=discount, subtotal=subtotal)

@app.route('/chitietpackages/<int:product_id>')
def chitiet_sp(product_id):
    # Lọc sản phẩm có id trùng với product_id
    product_p = next((p for p in products_packages if p["id"] == product_id), None)

    # Kiểm tra nếu sản phẩm không tồn tại
    if product_p is None:
        return "Sản phẩm không tồn tại", 404

    return render_template('ChiTietSp.html', products_packages=product_p)


@app.route('/diachithanhtoan')
def dia_chi_thanh_toan():
    return render_template('DiaChiThanhToan.html')

@app.route('/xacnhan')
def xac_nhan():
    return render_template('XacNhan.html')

@app.route('/xacnhanthanhtoan')
def xac_nhan_thanh_toan():
    return render_template('XacNhanThanhToan.html')

@app.route('/register', methods=['POST'])
def register():
    user_list=list(user_collection.find())
    name=request.form["fullname"]
    email=request.form["regEmail"]
    password=request.form["regPassword"]

    # name = request.json["name"]
    # email = request.json["email"]
    # password = request.json["pass"]

    print(user_collection.count_documents({"$or":[{"name":name},{"email":email}]}))
    if user_collection.count_documents({"$or":[{"name":name},{"email":email}]})!=0:
        session.pop("notif")
        flash("Tên người dùng này hoặc email đã có trong tài khoản","notif")
        print(" Người dùng này đã có trong tài khoản")

        return render_template('Trangchu.html', fullname=name,email=email,password=password)
    else:
        print(name,email,password)
        session['username']=name
        session.pop("_flashes",None)
        flash(" Đăng ký tài khoản thành công","notif")
        user_collection.insert_one({"name": name, "email": email, "password": password})
        return render_template('TaiKhoan.html', fullname=name,email=email,password=password)

@app.route('/login', methods=["POST"])
def login():
    email = request.form["loginEmail"]
    password = request.form["loginPassword"]
    user=user_collection.find_one({"$and":[{"email":email},{"password":password}]})
    if user_collection.find_one({"$and":[{"email":email},{"password":password}]}):
        session['username'] = user["name"]
        print(user,type(user))
        print("Đăng nhập thành công")
        flash("Đăng nhập thành công","notif")
    else:
        print("Đăng nhập ko thành công")
        flash("Không tìm thấy người dùng này", "notif")
    return render_template('Trangchu.html')

@app.route('/logout')
def logout():
    session.pop("username",None)
    session.pop("_flashes",None)
    return render_template('Trangchu.html')
@app.route('/update_profile',methods=['GET','PUT','POST'])

def update_profile():
    if request.method == 'POST':
        print(request.form)
        print(request.form["email"])
        # print(request.form.getlist())
    return render_template('TaiKhoan.html',years_option=years_option,days_option=days_option, months_option=months_option)

@app.route('/TaiKhoan')
def TaiKhoan():
    return render_template('TaiKhoan.html',years_option=years_option,days_option=days_option, months_option=months_option)
if __name__ == '__main__':
    app.run(debug=False)
