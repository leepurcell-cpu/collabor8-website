/* What we do selector. Switching boxes never scrolls the page: panels share one grid cell (sitewide.css), so the area keeps the tallest panel's height. */
(function(){
  var picks = Array.prototype.slice.call(document.querySelectorAll('.pick'));
  if (!picks.length) return;
  function select(btn, focus){
    picks.forEach(function(p){
      var on = p === btn;
      p.setAttribute('aria-selected', on ? 'true' : 'false');
      p.setAttribute('tabindex', on ? '0' : '-1');
      var panel = document.getElementById(p.getAttribute('aria-controls'));
      if (panel) panel.hidden = !on;
    });
    if (focus) {
      // Keyboard (arrow keys): move focus without jumping, but reveal the tab if it is off screen.
      btn.focus({preventScroll:true});
      var r = btn.getBoundingClientRect();
      if (r.top < 0 || r.bottom > window.innerHeight) btn.scrollIntoView({block:'nearest'});
    }
  }
  var h = (location.hash || '').slice(1);
  var target = h && document.getElementById('t-' + h);
  if (target && target.classList.contains('pick')) {
    select(target, false);
    // Deep link from Home (/what-we-do/#markets etc.): bring the chosen panel into view once, on load only.
    var open = document.getElementById(target.getAttribute('aria-controls'));
    if (open) open.scrollIntoView({block:'nearest'});
  }
  picks.forEach(function(p, idx){
    p.addEventListener('click', function(){ select(p, false); });
    p.addEventListener('keydown', function(e){
      var n = null;
      if (e.key === 'ArrowRight' || e.key === 'ArrowDown') n = picks[(idx+1) % picks.length];
      if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') n = picks[(idx-1+picks.length) % picks.length];
      if (n){ e.preventDefault(); select(n, true); }
    });
  });
})();
