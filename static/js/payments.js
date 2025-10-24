// small helper: prevent empty input blanks from collapsing layout and add simple formatting
document.addEventListener('DOMContentLoaded', function(){
  // basic card-number spacing (visual only)
  const cardInput = document.querySelector('input[name="card-number"]');
  if(cardInput){
    cardInput.addEventListener('input', function(e){
      this.value = this.value.replace(/[^\d]/g, '').replace(/(.{4})/g, '$1 ').trim();
    });
  }
});
