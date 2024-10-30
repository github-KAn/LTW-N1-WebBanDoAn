document.querySelector('.toggle-button').addEventListener('click', function() {
    const content = document.querySelector('.collapsible-content');
    const isHidden = content.style.display === 'none' || content.style.display === '';
    
    // Toggle display
    content.style.display = isHidden ? 'block' : 'none';
    
    // Toggle arrow direction
    this.textContent = isHidden ? '▲' : '▼';
});
    document.querySelectorAll('.quantity-control').forEach(control => {
        const quantityDisplay = control.querySelector('.quantity');
        let quantity = 0;

        control.querySelector('.increase').addEventListener('click', () => {
            quantity++;
            quantityDisplay.textContent = quantity;
        });

        control.querySelector('.decrease').addEventListener('click', () => {
            if (quantity > 0) {
                quantity--;
                quantityDisplay.textContent = quantity;
            }
        });
    });
