function deleteTask(button) {
    var url = button.getAttribute('data-delete-url');
    
    if (confirm('¿Estás seguro de eliminar esta tarea?')) {
        window.location.href = url;
    }
}
