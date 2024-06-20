document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.alert').forEach(alert => {
        setTimeout(() => {
            bootstrap.Alert.getOrCreateInstance(alert).close()
        }, 4000);
    });
});
