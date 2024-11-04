// Cart toggle
const cart = document.getElementById('cart-summary');
const overlay = document.querySelector('.overlay');
const cartItemsContainer = document.getElementById('cart-items');
const totalPriceElement = document.getElementById('total-price');
const cartCountElement = document.getElementById('cart-count'); // Assuming there's an element to show item count
let totalPrice = 0;

// Tải giỏ hàng từ Local Storage khi trang được tải
window.onload = function() {
    const savedCart = JSON.parse(localStorage.getItem('cartItems'));
    if (savedCart) {
        cartItems = savedCart;
        totalPrice = cartItems.reduce((total, item) => total + item.price, 0);
        renderCart();
        updateCartCount();
    }
};

// Array to hold cart items
let cartItems = [];

// Event listener for each product
document.querySelectorAll('.iconproduct').forEach(productIcon => {
    productIcon.addEventListener('click', function () {
        const productElement = productIcon.closest('.item');
        const productName = productElement.getAttribute('data-name');
        const productPrice = parseInt(productElement.getAttribute('data-price'));
        const productImage = productElement.getAttribute('data-image');

        // Add item to cart
        addToCart(productName, productPrice, productImage);
    });
});

// Add item to cart
function addToCart(name, price, image) {
    cartItems.push({ name, price, image });
    totalPrice += price;
    localStorage.setItem('cartItems', JSON.stringify(cartItems)); // Lưu giỏ hàng vào Local Storage
    renderCart();
    toggleCart(true);
    updateCartCount();
}

// Render cart items
function renderCart() {
    cartItemsContainer.innerHTML = ''; // Clear the container
    cartItems.forEach((item, index) => {
        const itemElement = document.createElement('div');
        itemElement.classList.add('cart-item');
        itemElement.innerHTML = `
            <div class="cart-item-info">
                <img src="${item.image}" alt="${item.name}" width="50">
                <span>${item.name}</span>
            </div>
            <span>${item.price.toLocaleString('vi-VN')}đ</span>
            <button class="remove-btn" data-index="${index}">Xóa</button>
        `;
        cartItemsContainer.appendChild(itemElement);
    });

    // Update total price
    totalPriceElement.innerText = `${totalPrice.toLocaleString('vi-VN')}đ`;

    // Add event listeners to remove buttons
    document.querySelectorAll('.remove-btn').forEach(button => {
        button.addEventListener('click', function () {
            const index = parseInt(this.getAttribute('data-index'));
            removeFromCart(index);
        });
    });
}

// Remove item from cart
function removeFromCart(index) {
    const removedItem = cartItems.splice(index, 1)[0];
    totalPrice -= removedItem.price;
    localStorage.setItem('cartItems', JSON.stringify(cartItems)); // Cập nhật Local Storage
    renderCart();
    updateCartCount();
}

// Update the cart item count on the cart icon
function updateCartCount() {
    const itemCount = cartItems.length;
    cartCountElement.innerText = itemCount;
    cartCountElement.style.display = itemCount > 0 ? 'inline-block' : 'none';  // Hide the count if it's zero
}

// Toggle cart visibility
function toggleCart(show) {
    if (show) {
        cart.classList.add('active');
        overlay.classList.add('active');
    } else {
        cart.classList.remove('active');
        overlay.classList.remove('active');
    }
}

// Close cart on button click
document.querySelector('.close-btn').addEventListener('click', () => {
    toggleCart(false);
});

// Clicking on overlay should also close the cart
overlay.addEventListener('click', () => {
    toggleCart(false);
});

// Event listener for showing the cart when the cart icon is clicked
document.querySelector('.cart').addEventListener('click', () => {
    toggleCart(true); // Mở giỏ hàng
});

