from distributed.utils_test import client
from flask import Flask, render_template, request, redirect, session, url_for, flash
from pymongo import MongoClient
from bson.objectid import ObjectId, InvalidId

# from seed_data import menu_items

app = Flask(__name__)
app.secret_key = 'nhom1'

client = MongoClient('mongodb://localhost:27017/')
db = client['ten_cua_database']
packages_collection = db['packages']
processed_collection = db['processed_items']
drinks_collection = db['drinks']
gifts_collection = db['gifts']
menu_collection = db['menu_items']
vegetarians_collection = db['vegetarians']


@app.route('/')
def trang_chu():
    return render_template('Trangchu.html')

@app.template_filter('number_format')
def number_format(value, decimal_places=0, decimal_separator='.', thousands_separator=','):
    """Định dạng số theo định dạng VNĐ (đ) với dấu phẩy"""
    formatted_value = f"{value:,.{decimal_places}f}"  # Chuyển đổi số sang định dạng có dấu phẩy
    return formatted_value.replace('.', decimal_separator)  # Thay đổi dấu phân cách thập phân


@app.route('/dathang', methods=['GET', 'POST'])  # Thêm 'POST' vào đây
def dat_hang():
    if request.method == 'POST':
        # Giả sử bạn gửi dữ liệu giỏ hàng qua form
        cart_items = request.form.getlist('cart_items')  # Lấy dữ liệu giỏ hàng từ form
        # Bạn cần đảm bảo cart_items là một danh sách chứa các sản phẩm với giá và số lượng
        # Chẳng hạn như [{'name': 'Product1', 'price': 10000, 'quantity': 2}, {...}]
        session['cart'] = cart_items  # Lưu vào session
        return redirect(url_for('thanh_toan'))  # Chuyển hướng đến trang thanh toán

    # Phần GET để hiển thị dữ liệu giỏ hàng
    packages = list(packages_collection.find())
    processed_items = list(processed_collection.find())
    drinks = list(db.drinks.find())
    gifts = list(db.gifts.find())
    return render_template('DatHang.html', packages=packages, processed_items=processed_items, drinks=drinks, gifts=gifts)

@app.route('/chinhsua')
def chinh_sua():
    menu_items = list(db.menu_items.find())
    return render_template('ChinhSua.html', menu_items=menu_items)


@app.route('/thucdon')
def thuc_don():
    menu_items = list(db.menu_items.find())
    vegetarians = list(db.vegetarians.find())
    return render_template('Thucdon.html', menu_items=menu_items, vegetarians=vegetarians)

@app.route('/tintuc')
def tin_tuc():
    return render_template('TinTuc.html')

@app.route('/faqs')
def faqs():
    return render_template('FAQs.html')


@app.route('/thanhtoan')
def thanh_toan():
    cart_items = session.get('cart', [])  # Lấy giỏ hàng từ session
    shipping_fee = 30000  # Ví dụ phí ship
    discount = 0  # Mã giảm giá (nếu có)

    # Tính tổng đơn hàng
    subtotal = sum(item['price'] * item['quantity'] for item in cart_items)

    return render_template('ThanhToan.html', cart_items=cart_items, shipping_fee=shipping_fee, discount=discount,
                           subtotal=subtotal)

@app.route('/chitietsanpham')
def chi_tiet_san_pham():
    return render_template('ChiTietSp.html')

@app.route('/diachithanhtoan')
def dia_chi_thanh_toan():
    return render_template('DiaChiThanhToan.html')

@app.route('/xacnhan')
def xac_nhan():
    return render_template('XacNhan.html')

if __name__ == '__main__':
    app.run(debug=True)