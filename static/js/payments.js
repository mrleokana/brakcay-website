/document.addEventListener('DOMContentLoaded', function() {
  const paymentSelect = document.getElementById('payment-method');
  const fields = {
    visa: document.getElementById('visa-fields'),
    mpesa: document.getElementById('mpesa-fields'),
    ecocash: document.getElementById('ecocash-fields'),
    crypto: document.getElementById('crypto-fields')
  };

  function toggleFields() {
    // Hide all fields
    Object.values(fields).forEach(f => f.style.display = 'none');

    // Show the selected one
    const selected = paymentSelect.value || 'visa';
    if (fields[selected]) fields[selected].style.display = 'block';
  }

  // Initialize Visa as default
  if (!paymentSelect.value) paymentSelect.value = 'visa';
  toggleFields();

  paymentSelect.addEventListener('change', toggleFields);
});
