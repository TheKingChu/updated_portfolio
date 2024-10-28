function openModal(imageSrc) {
    console.log("Opening modal with image: ", imageSrc);
    const modal = document.getElementById("image-modal");
    const modalImage = document.getElementById("modal-image");
    modal.style.display = "block"; // Show the modal
    modalImage.src = imageSrc; // Set the image source
}

function closeModal(){
    console.log("Closing modal");
    const modal = document.getElementById("image-modal");
    modal.style.display = "none"; // Hide the modal
}