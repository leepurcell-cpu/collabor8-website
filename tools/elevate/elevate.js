/* Collabor8 elevate: reveal on scroll + header state. Opacity/transform only (no layout shift). Reveal off for reduced motion. */
(function(){
  var h=document.querySelector('header.top');
  if(h){var f=function(){h.classList.toggle('scrolled',scrollY>8)};addEventListener('scroll',f,{passive:true});f();}
  if(matchMedia('(prefers-reduced-motion: reduce)').matches||!('IntersectionObserver' in window))return;
  document.documentElement.classList.add('js-reveal');
  var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target);}});},{rootMargin:'0px 0px -8% 0px',threshold:0.12});
  document.querySelectorAll('[data-reveal]').forEach(function(el){io.observe(el);});
})();
