function openAddressForm() {
    const form = document.getElementById("addressForm");
    form.style.display = "flex";
    setTimeout(() => form.classList.add("active"), 10); // Đảm bảo hiệu ứng transition
}

function closeAddressForm() {
    const form = document.getElementById("addressForm");
    form.classList.remove("active");
    setTimeout(() => form.style.display = "none", 300); // Đợi hiệu ứng trước khi ẩn
}
