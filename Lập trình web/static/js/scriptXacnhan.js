//// Hàm lấy dữ liệu giỏ hàng và hiển thị
//function loadCartItems() {
//    let cartItems = JSON.parse(localStorage.getItem("cartItems")) || [];
//    console.log(cartItems);
//    let cartContainer = document.getElementById("order-row-product");
//    let totalPrice = 0;
//
//    cartContainer.innerHTML = ""; // Xóa nội dung cũ
//
//    if (cartItems.length === 0) {
//        cartContainer.innerHTML = "<p>Giỏ hàng trống</p>";
//        document.getElementById("total-price").innerText = "0đ";
//        return;
//    }
//
//    // Hiển thị các sản phẩm trong giỏ hàng
//    cartItems.forEach(item => {
//        let itemTotal = item.price * item.quantity;
//        totalPrice += itemTotal;
//
//        // Tạo phần tử chứa thông tin sản phẩm
//        const itemElement = document.createElement('div');
//        itemElement.classList.add('product-order'); // Thêm class cho sản phẩm
//
//        // Thêm thông tin sản phẩm vào phần tử
//        itemElement.innerHTML = `
//            <div class="order-label">${item.name}</div>
//            <div class="order-label">${item.price.toLocaleString('vi-VN')}đ</div>
//            <div class="order-label">${item.quantity}</div>
//            <div class="order-label">${itemTotal.toLocaleString('vi-VN')}đ</div>
//        `;
//
//        // Thêm sản phẩm vào container
//        cartContainer.appendChild(itemElement);
//    });
//
//    // Hiển thị tổng giá trong mục tổng đơn hàng
//    document.getElementById("total-price").innerText = `${totalPrice.toLocaleString('vi-VN')}đ`;
//}
//
//// Gọi hàm loadCartItems khi trang được tải
//window.onload = loadCartItems;




// Hàm lấy dữ liệu giỏ hàng và hiển thị
function loadCartItems() {
    let cartItems = JSON.parse(localStorage.getItem("cartItems")) || [];
    console.log(cartItems);
    let cartContainer = document.getElementById("cart-items-container");
    let totalPrice = 0;

    cartContainer.innerHTML = ""; // Xóa nội dung cũ

    if (cartItems.length === 0) {
        cartContainer.innerHTML = "<p>Giỏ hàng trống</p>";
        document.getElementById("total-price").innerText = "0đ";
        return;
    }

    // Hiển thị các sản phẩm trong giỏ hàng
    cartItems.forEach(item => {
        let itemTotal = item.price * item.quantity;
        totalPrice += itemTotal;

        const itemElement = document.createElement('div'); // Tạo phần tử chứa thông tin sản phẩm
        cartContainer.classList.add('product-section');

        cartContainer.innerHTML += `
            <span class="order-label-product">${item.name}</span>
            <span class="order-label-price">${item.price.toLocaleString('vi-VN')}đ</span>
            <div class="order-label-quantity">${item.quantity}</div>
            <span class="order-value ">${itemTotal.toLocaleString('vi-VN')}đ</span>

        `;
        cartItemsContainer.appendChild(itemElement); // Thêm sản phẩm vào container
    });

    // Hiển thị tổng giá trong mục tổng đơn hàng
    document.getElementById("total-price").innerText = `${totalPrice.toLocaleString()}đ`;
}

// Gọi hàm khi trang tải
document.addEventListener("DOMContentLoaded", function () {
    loadCartItems();
});

function confirmOrder() {
    // Reset giỏ hàng
    localStorage.removeItem("cartItems");

    // Chuyển hướng đến trang xác nhận thanh toán
    window.location.href = "xacnhanthanhtoan";
}
