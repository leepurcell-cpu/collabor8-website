(function(){
  // Mobile menu
  var b=document.querySelector('.menu-btn'),n=document.getElementById('nav');
  if(b&&n){b.addEventListener('click',function(){var o=n.classList.toggle('open');b.setAttribute('aria-expanded',o?'true':'false');});}
  // Cookie consent gate. Non-essential scripts must be added as
  // <script type="text/plain" data-consent="analytics" data-src="..."></script>
  // They only run after the visitor accepts. Decline keeps them switched off.
  var KEY='c8_consent',banner=document.getElementById('cookie');
  function load(){document.querySelectorAll('script[type="text/plain"][data-consent]').forEach(function(s){var x=document.createElement('script');if(s.dataset.src){x.src=s.dataset.src;}else{x.text=s.text;}document.head.appendChild(x);s.remove();});}
  function get(){try{return localStorage.getItem(KEY);}catch(e){return null;}}
  function set(v){try{localStorage.setItem(KEY,v);}catch(e){}}
  var c=get();
  if(c==='accepted'){load();}
  else if(c!=='declined'&&banner){banner.hidden=false;}
  document.addEventListener('click',function(e){var t=e.target.closest('[data-consent-action]');if(!t)return;var v=t.getAttribute('data-consent-action');set(v);if(v==='accepted')load();if(banner)banner.hidden=true;});
  window.c8Consent={reset:function(){try{localStorage.removeItem(KEY);}catch(e){}location.reload();}};
})();
