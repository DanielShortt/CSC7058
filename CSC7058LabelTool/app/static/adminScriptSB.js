async function adminTipModal() {
    var myModal = new bootstrap.Modal(document.getElementById('adminTipModal'), {})
    myModal.toggle()   
}
window.onload = adminTipModal;