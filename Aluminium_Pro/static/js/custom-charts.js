document.querySelectorAll('*').forEach((element) => {
    element.addEventListener('touchstart', null, { passive: true });
    element.addEventListener('touchmove', null, { passive: true });
    element.addEventListener('mousewheel', null, { passive: true });
    element.addEventListener('wheel', null, { passive: true });
  });
  