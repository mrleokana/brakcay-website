document.addEventListener('DOMContentLoaded', function(){
  const tabs = document.querySelectorAll('#tabs-page .tab');
  tabs.forEach(tab => {
    tab.addEventListener('click', () => {
      tabs.forEach(t=>t.classList.remove('active'));
      tab.classList.add('active');
      document.querySelectorAll('.tab-content').forEach(c=>c.style.display='none');
      document.getElementById(tab.dataset.tab).style.display = 'grid';
    });
  });
});
