from flask import Flask, render_template, request, redirect, session, url_for, flash
from pymongo import MongoClient
from bson.objectid import ObjectId, InvalidId
from waitress import serve

app = Flask(__name__)
app.secret_key = 'nhom1'

# Kết nối MongoDB
try:
    client = MongoClient('mongodb://localhost:27017/')
    db = client['ten_cua_database']
    packages_collection = db['packages']
    processed_collection = db['processed_items']
    drinks_collection = db['drinks']
    gifts_collection = db['gifts']
    menu_collection = db['menu_items']
    vegetarians_collection = db['vegetarians']
    product_collection = db['products']
except Exception as e:
    print(f"Lỗi kết nối MongoDB: {e}")

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

@app.route('/chitietsanpham/<product_id>')
def chitiet_sp(product_id):
    products = mongo.db.products.find_one({'_id': ObjectId(product_id)})
    return render_template('ChiTietSp.html', products=products)

@app.route('/diachithanhtoan')
def dia_chi_thanh_toan():
    return render_template('DiaChiThanhToan.html')

@app.route('/xacnhan')
def xac_nhan():
    return render_template('XacNhan.html')

@app.route('/xacnhanthanhtoan')
def xac_nhan_thanh_toan():
    return render_template('XacNhanThanhToan.html')

if __name__ == '__main__':
    app.run(debug=False)
    # serve(app, host="0.0.0.0", port=5000)