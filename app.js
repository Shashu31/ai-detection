// script.js
document.getElementById("prescription-form").addEventListener("submit", function (e) {
    e.preventDefault();  // Prevent form submission
    
    // Get form data
    const patientName = document.getElementById("patientName").value;
    const medicationName = document.getElementById("medicationName").value;
    const dosage = document.getElementById("dosage").value;
    const quantity = document.getElementById("quantity").value;
    const prescriptionDate = document.getElementById("prescriptionDate").value;

    // Display confirmation message
    document.getElementById("confirmation").style.display = "block";
    document.getElementById("prescription-form").reset(); // Reset the form

    // You can also add further functionality to process the data here
    console.log(`Prescription for ${patientName}`);
    console.log(`Medication: ${medicationName}`);
    console.log(`Dosage: ${dosage} mg`);
    console.log(`Quantity: ${quantity} pills`);
    console.log(`Date: ${prescriptionDate}`);
});
