# The Bike Shop – אביזרי אופניים לכביש ולשטח

אתר סטטי (GitHub Pages, בכתובת myripo.com/bike-store) שמציג אביזרי אופניים מחנויות מותג רשמיות באלי אקספרס, עם קישורי שותפים (מזהה מעקב bikesite).
נבנה מאותה תבנית כמו camping-store ו-photo-store.

- `index.html` – האתר. קורא את המוצרים מ-`data/products.json`.
- `how-to-buy.html` – מדריך "איך קונים נכון באלי אקספרס" (משותף לכל החנויות).
- `data/products.json` – האוספים, סוגי הרכיבה (activities) והמוצרים. מוצר עם `status: pending` מוסתר עד שיורם מאשר.
- `scripts/search.py` + `search.yml` – חיפוש מחקר לפי `search/queries.txt`. רץ אוטומטית כשהקובץ משתנה. לא משנה את האתר.
- `scripts/make_links.py` + `make-links.yml` – יצירת קישורי שותפים (bikesite) למוצרים ממתינים.
- `scripts/refresh.py` + `refresh.yml` – בדיקה שבועית (יום ראשון) של מחיר, דירוג ומוצרים שנעלמו. נפתח כבקשת שינוי לאישור.
- `scripts/fetch_media.py` – הורדת תמונות מוצרים לפי `media/requests.txt`.
- הסוד של ה-API נשמר רק ב-Settings → Secrets → Actions בשם `ALI_APP_SECRET`.

## כללים
- חנויות מותג רשמיות בלבד (iGPSPORT, Magene, CYCPLUS, CoOSPO, RockBros, Rhinowalk, GACIRON, ZTTO, SENSAH, KAPVOE, Santic ועוד). לא חנויות כלבו.
- דירוג 94%+, 100+ מכירות. בלי תקרת מחיר.
- בטיחות: בלי כידון, מוט אוכף, גלגלים ושלדה מפחמן. קסדות רק כשהיצרן מציין EN 1078.
- מחיר "החל מ-", או גרסה מומלצת (variant) עם מחיר שנבדק ידנית. במוצרי חשמל: תקע EU.
- כותרות: שם המותג באנגלית, כל השאר בעברית, בלי מספרי דגם מיותרים.
- גילוי נאות בכל פרסום. שום דבר לא עולה בלי אישור יורם.

## סוגי רכיבה (activities)
road (כביש), mtb (שטח), gravel (גראבל ובייקפאקינג), city (עירוני וחשמליים), night (רכיבת לילה). מוצר יכול להתאים לכמה סוגים (שדה `acts`).
