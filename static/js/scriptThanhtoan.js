// Hàm mở form địa chỉ mới
function openAddressForm() {
    document.getElementById("addressForm").style.display = "block";
}

// Hàm đóng form địa chỉ
function closeAddressForm() {
    document.getElementById("addressForm").style.display = "none";
}

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
            <div class="product-info">
                <img src="${item.image}" alt="${item.name}">
                <span class="product-name">${item.name}</span>
            </div>
            <span class="product-price">${item.price.toLocaleString('vi-VN')}đ</span>
            <div class="product-quantity">${item.quantity}</div>
            <span class="product-total">${itemTotal.toLocaleString('vi-VN')}đ</span>
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
