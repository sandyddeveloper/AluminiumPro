document.addEventListener('DOMContentLoaded', function () {
    const inputs = document.querySelectorAll('input');

    inputs.forEach(input => {
        input.addEventListener('focus', function () {
            input.style.borderColor = '#3b82f6';
        });

        input.addEventListener('blur', function () {
            input.style.borderColor = 'transparent';
        });
    });
});
