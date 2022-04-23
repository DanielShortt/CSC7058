async function tipModal() {
    var myModal = new bootstrap.Modal(document.getElementById('tipModal'), {})
    myModal.toggle()   
}
window.onload = tipModal;