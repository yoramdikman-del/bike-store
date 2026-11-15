// סטטיסטיקה לעמודי התוכן (מדריכים, מסלולים, מידה, איך קונים): Google Analytics 4, אותו מזהה כמו בחנות הצילום.
// סופר צפייה בעמוד, והקלקה על כל קישור לאלי אקספרס (click_buy) עם store=bike ושם העמוד שממנו נלחץ.
(function () {
  var GA_ID = 'G-KY0G2JCNBM';
  var STORE = 'bike';
  window.dataLayer = window.dataLayer || [];
  function gtag() { dataLayer.push(arguments); }
  window.gtag = window.gtag || gtag;
  var sc = document.createElement('script');
  sc.async = true;
  sc.src = 'https://www.googletagmanager.com/gtag/js?id=' + GA_ID;
  document.head.appendChild(sc);
  gtag('js', new Date());
  gtag('config', GA_ID);

  var page = (location.pathname.split('/').pop() || 'index.html').replace('.html', '');
  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('a[href]');
    if (!a) return;
    try {
      if (/aliexpress\./i.test(a.href)) {
        var card = a.closest('.pk');
        var t = card && card.querySelector('.t');
        var brand = t && t.querySelector('span');
        if (t) { t = t.cloneNode(true); if (t.querySelector('span')) t.querySelector('span').remove(); }
        gtag('event', 'click_buy', {
          store: STORE,
          item_id: a.dataset.id || '',
          item_brand: a.dataset.brand || (brand ? brand.textContent.trim() : ''),
          item_category: a.dataset.coll || '',
          item_name: a.dataset.title || (t ? t.textContent.trim().slice(0, 80) : a.textContent.trim().slice(0, 80)),
          section: 'guide:' + page,
          via: 'button'
        });
      } else if (/facebook\.com|instagram\.com|chat\.whatsapp\.com/.test(a.href)) {
        gtag('event', 'click_social', { network: a.hostname, place: 'guide:' + page });
      }
    } catch (err) {}
  });
})();
