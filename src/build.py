# Builds / (RU), /en/ (EN) and /vi/ (VI) from src/template.html + cars.json.  Run: python src/build.py
import io, json, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vi as VI

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
rd = lambda p: io.open(os.path.join(ROOT, p), encoding='utf-8').read()

LOGO = ('<svg viewBox="0 0 32 32" fill="none" stroke="#E8622C" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round">'
        '<path d="M4 21v-4l3-6.5A2 2 0 0 1 8.8 9.4h14.4a2 2 0 0 1 1.8 1.1L28 17v4a1 1 0 0 1-1 1h-2M7 22H5a1 1 0 0 1-1-1M4 17h24M11 22h10"/>'
        '<circle cx="9" cy="22" r="2.2"/><circle cx="23" cy="22" r="2.2"/></svg>')

S = {
 'title': ('Аренда авто в Нячанге недорого — без водителя от 700 000 ₫/сутки | VietAvto', 'Cheap Car Rental in Nha Trang — Self-Drive from 700,000 ₫/day | VietAvto'),
 'meta_desc': ('Аренда авто в Нячанге недорого и без водителя: VinFast, Toyota, Mitsubishi, Hyundai, Kia. От 700 000 ₫ в сутки, скидка на месяц, депозит от $200, доставка в отель или аэропорт Камрань. Заявка онлайн, ответ в WhatsApp и Telegram.', 'Cheap self-drive car rental in Nha Trang: VinFast, Toyota, Mitsubishi, Hyundai, Kia. From 700,000 ₫ per day, monthly discounts, deposit from $200, delivery to your hotel or Cam Ranh airport. Book online, reply on WhatsApp or Telegram.'),
 'meta_kw': ('аренда авто Нячанг, аренда машины Нячанг, прокат авто Нячанг, аренда авто Нячанг недорого, прокат машин Нячанг дешево, аренда авто Нячанг цены, аренда авто без водителя Нячанг, аренда авто посуточно Нячанг, аренда авто на месяц Нячанг, долгосрочная аренда авто Вьетнам, аренда авто аэропорт Камрань, аренда машины Камрань, аренда авто Вьетнам, прокат машин Вьетнам, аренда авто Кхань Хоа, аренда электромобиля VinFast Нячанг, аренда минивэна Нячанг, аренда 7-местного авто Нячанг, аренда авто для поездки в Далат, взять машину напрокат Нячанг', 'car rental Nha Trang, cheap car rental Nha Trang, rent a car Nha Trang, self-drive car hire Nha Trang, Nha Trang car hire prices, car rental Nha Trang without driver, Cam Ranh airport car rental, CXR airport car hire, monthly car rental Nha Trang, long-term car rental Vietnam, rent a car in Vietnam, Vietnam self-drive car rental, VinFast rental Nha Trang, electric car rental Nha Trang, 7-seater rental Nha Trang, minivan rental Nha Trang, SUV rental Nha Trang, car rental Nha Trang to Da Lat, Khanh Hoa car rental'),
 'about_p3': ('Ищете, где арендовать авто в Нячанге дешево? Самые доступные варианты — электромобиль VinFast VF3 за 700 000 ₫ в сутки и седан Kia Soluto за 900 000 ₫. При аренде на месяц и дольше действует отдельная, более выгодная ставка. Для семьи и компании подойдут 7-местные Toyota Rush, Veloz и Mitsubishi Xpander, для больших групп — Kia Carnival на 7–11 мест.', 'Looking for cheap car hire in Nha Trang? The most affordable options are the VinFast VF3 electric car at 700,000 ₫ a day and the Kia Soluto sedan at 900,000 ₫. Rentals of a month or longer get a separate, better rate. Families and groups can take a 7-seat Toyota Rush, Veloz or Mitsubishi Xpander, and larger groups the 7–11-seat Kia Carnival.'),
 'q7': ('Сколько стоит аренда авто в Нячанге?', 'How much does it cost to rent a car in Nha Trang?'),
 'a7': ('От 700 000 ₫ в сутки за VinFast VF3 до 2 100 000 ₫ за Kia Carnival. Седаны — от 900 000 ₫, 7-местные авто — от 1 000 000 ₫. Цены указаны в карточках машин выше.', 'From 700,000 ₫ a day for the VinFast VF3 to 2,100,000 ₫ for the Kia Carnival. Sedans start at 900,000 ₫ and 7-seaters at 1,000,000 ₫. Prices are shown on each car above.'),
 'q8': ('Можно арендовать машину на месяц дешевле?', 'Is a monthly rental cheaper?'),
 'a8': ('Да. При аренде на месяц и дольше цена за сутки заметно ниже посуточной — пришлите даты и машину через форму или в WhatsApp/Telegram, и мы назовём ставку.', 'Yes. For a month or longer the daily price is noticeably lower — send us your dates and the car via the form or WhatsApp/Telegram and we will quote the rate.'),
 'og_locale': ('ru_RU', 'en_US'),
 'about_h': ('Аренда авто в Нячанге', 'Car rental in Nha Trang'),
 'about_p1': ('Аренда машины в Нячанге — удобный способ увидеть побережье Кхань Хоа в своём темпе: пляжи и острова, водопады, горная дорога на Далат. VietAvto сдаёт автомобили без водителя из собственного парка — от электромобилей VinFast VF3 и VF5 до 7-местных Toyota Veloz, Mitsubishi Xpander и минивэна Kia Carnival.', 'Renting a car in Nha Trang is the easiest way to see the Khanh Hoa coast at your own pace: beaches and islands, waterfalls and the mountain road to Da Lat. VietAvto rents self-drive cars from its own fleet — from VinFast VF3 and VF5 electric cars to 7-seat Toyota Veloz, Mitsubishi Xpander and the Kia Carnival minivan.'),
 'about_p2': ('Цены на прокат авто в Нячанге — от 700 000 ₫ в сутки, депозит $200 по провинции и $400 для поездок по всему Вьетнаму. Машину передаём в отеле, по адресу в Нячанге или в аэропорту Камрань (CXR). Для аренды нужны паспорт, международное и национальное водительское удостоверение.', 'Car hire prices in Nha Trang start at 700,000 ₫ per day, with a $200 deposit within the province and $400 for trips across Vietnam. We hand over the car at your hotel, an address in Nha Trang or Cam Ranh airport (CXR). You need a passport, an International Driving Permit and your national licence.'),
 'nav_fleet': ('Автопарк', 'Fleet'), 'nav_terms': ('Условия', 'Terms'), 'nav_faq': ('Вопросы', 'FAQ'), 'nav_contact': ('Контакты', 'Contacts'),
 'nav_book': ('Забронировать', 'Book now'),
 'pill': ('Свой автопарк в Нячанге', 'Our own fleet in Nha Trang'),
 'h1': ('Аренда авто в Нячанге', 'Car rental in Nha Trang'),
 'lede': ('Реальные машины из нашего парка — от городского электромобиля VinFast до 7-местного минивэна. Без посредников, с понятным депозитом и возвратом «бак в бак».',
          'Real cars from our own fleet — from a compact VinFast EV to a 7-seat minivan. No middlemen, a clear deposit and a same-fuel-level return.'),
 'perk1': ('10+ машин<br>в наличии', '10+ cars<br>available'),
 'perk2': ('Без<br>посредников', 'No<br>middlemen'),
 'perk3': ('Ответ в WhatsApp<br>или Telegram', 'Reply on WhatsApp<br>or Telegram'),
 'f_car': ('Машина', 'Car'), 'f_car_any': ('Любая — подберите мне', 'Any — help me choose'),
 'f_from': ('Дата получения', 'Pick-up date'), 'f_to': ('Дата возврата', 'Return date'),
 'b_send': ('Оставить заявку', 'Send request'),
 'f_contact': ('Ваш WhatsApp или Telegram', 'Your WhatsApp or Telegram'),
 'f_contact_ph': ('+84 912 345 678 или @username', '+84 912 345 678 or @username'),
 'f_name': ('Ваше имя', 'Your name'), 'f_name_ph': ('Как к вам обращаться', 'What should we call you'),
 'f_place': ('Где забрать (необязательно)', 'Pick-up location (optional)'),
 'f_place_ph': ('Отель, адрес или аэропорт Камрань', 'Hotel, address or Cam Ranh airport'),
 'or_chat': ('или напишите нам:', 'or message us:'),
 'book_hint': ('«Оставить заявку» — мы сами напишем вам. WhatsApp и Telegram открывают чат с нами, текст заявки подставится сам.',
               '“Send request” — we will message you. WhatsApp and Telegram open a chat with us with your request filled in.'),
 'fleet_h': ('Автопарк', 'Our fleet'),
 'fleet_p': ('Цены — за сутки аренды без водителя. На месяц и дольше — отдельная ставка, уточняйте при бронировании.',
             'Prices are per day, self-drive. Monthly and longer rentals get a separate rate — ask when booking.'),
 'per_day': ('/ сутки', '/ day'),
 'ft1_h': ('Реальные машины', 'Real cars'), 'ft1_p': ('На фото — автомобили из нашего парка, а не картинки из интернета.', 'The photos show cars from our own fleet, not stock images.'),
 'ft2_h': ('Прозрачные условия', 'Clear terms'), 'ft2_p': ('Депозит, пробег и топливо — всё расписано ниже, без мелкого шрифта.', 'Deposit, mileage and fuel are all spelled out below — no fine print.'),
 'ft3_h': ('Передача в Нячанге', 'Hand-over in Nha Trang'), 'ft3_p': ('Договоримся об удобном месте — отель, адрес или аэропорт.', 'We agree on a convenient spot — hotel, address or airport.'),
 'ft4_h': ('Связь напрямую', 'Direct contact'), 'ft4_p': ('Пишете владельцу в WhatsApp или Telegram — без колл-центров.', 'You message the owner on WhatsApp or Telegram — no call centres.'),
 'terms_h': ('Условия аренды', 'Rental terms'),
 'road_k': ('Правила дороги', 'On the road'),
 'road_v': ('Соблюдайте ПДД<small>Паркуйтесь только там, где разрешено, не проезжайте на красный, не превышайте скорость и не садитесь за руль выпившим. Штрафы с камер приходят владельцу и удерживаются из депозита.</small>',
            'Follow the traffic rules<small>Park only where allowed, don’t run red lights, keep to the speed limit and never drink and drive. Camera fines reach the owner and are taken from the deposit.</small>'),
 'faq_h': ('Вопросы и ответы', 'Questions & answers'),
 'q1': ('Нужны ли международные права?', 'Do I need an international licence?'),
 'a1': ('Да. Для договора нужны паспорт, международное водительское удостоверение (МВУ) и ваши национальные права.',
        'Yes. For the rental agreement you need your passport, an International Driving Permit (IDP) and your national driving licence.'),
 'q2': ('Какой депозит?', 'How much is the deposit?'),
 'a2': ('$200 для поездок по провинции Кхань Хоа и $400 — по всему Вьетнаму. Депозит возвращается, если на машине нет повреждений и нет штрафов; иначе удерживается соразмерно.',
        '$200 for trips within Khanh Hoa province and $400 for all of Vietnam. It is refunded if the car has no damage and there are no fines; otherwise the matching amount is withheld.'),
 'q3': ('Можно поехать в Далат или дальше?', 'Can I drive to Da Lat or further?'),
 'a3': ('Да, с депозитом $400. Лимит — 250 км в сутки и суммируется за весь срок: за 3 суток — 750 км. Каждый км сверх лимита — 5 000 ₫.',
        'Yes, with the $400 deposit. The limit is 250 km per day, added up over the whole rental: 3 days = 750 km. Each km over the limit is 5,000 ₫.'),
 'q4': ('Где забрать машину?', 'Where do I pick up the car?'),
 'a4': ('Место передачи согласуем при бронировании: отель, адрес в Нячанге или аэропорт Камрань.',
        'We agree on the hand-over spot when you book: your hotel, an address in Nha Trang or Cam Ranh airport.'),
 'q5': ('Как забронировать?', 'How do I book?'),
 'a5': ('Выберите машину и даты в форме вверху и нажмите «Оставить заявку» — мы напишем вам сами. Или сразу напишите нам в WhatsApp или Telegram.',
        'Pick a car and dates in the form above and press “Send request” — we’ll message you. Or write to us directly on WhatsApp or Telegram.'),
 'q6': ('Во сколько забрать и вернуть машину?', 'What are the pick-up and return times?'),
 'a6': ('На 1 день — получение с 7:00, возврат до 22:00 того же дня. На 2 дня и больше — возврат до 22:00 последнего дня аренды.',
        'For 1 day — pick up from 7:00, return by 22:00 the same day. For 2 days or more — return by 22:00 on the last day.'),
 'cta_h': ('Готовы забрать машину?', 'Ready to hit the road?'),
 'cta_p': ('Напишите модель и даты — подберём авто из наличия и согласуем встречу в Нячанге.',
           'Send us the model and dates — we’ll match a car from stock and arrange a meeting in Nha Trang.'),
 'cta_book': ('Оставить заявку', 'Send a request'), 'cta_wa': ('Написать в WhatsApp', 'Message on WhatsApp'), 'cta_tg': ('Написать в Telegram', 'Message on Telegram'),
 'footer_l': ('Прокат авто без водителя · Нячанг, Вьетнам', 'Self-drive car rental · Nha Trang, Vietnam'),
 'footer_r': ('18+ · Аренда без водителя', '18+ · Self-drive only'),
 'lb_close': ('Закрыть', 'Close'), 'lb_prev': ('Предыдущее фото', 'Previous photo'), 'lb_next': ('Следующее фото', 'Next photo'),
}

JS = {
 'seats': ('мест', 'seats'), 'gb_auto': ('Автомат', 'Automatic'), 'gb_manual': ('Механика', 'Manual'),
 'fu_petrol': ('Бензин', 'Petrol'), 'fu_electric': ('Электро', 'Electric'), 'fu_diesel': ('Дизель', 'Diesel'), 'fu_hybrid': ('Гибрид', 'Hybrid'),
 'per_day': ('/ сутки', '/ day'), 'per_day_short': ('/сут', '/day'), 'book': ('Забронировать', 'Book'),
 'approx': ('примерно', 'approx.'),
 'no_photo': ('Фото скоро', 'Photo coming soon'),
 'err_from': ('Укажите дату получения.', 'Please choose a pick-up date.'),
 'err_to': ('Укажите дату возврата.', 'Please choose a return date.'),
 'err_order': ('Дата возврата должна быть позже даты получения.', 'The return date must be after the pick-up date.'),
 'err_contact': ('Укажите ваш WhatsApp (номер) или Telegram (@username), чтобы мы могли ответить.', 'Please enter your WhatsApp number or Telegram @username so we can reply.'),
 'err_send': ('Не удалось отправить заявку. Напишите нам в WhatsApp или Telegram — кнопки ниже.', 'Could not send the request. Please message us on WhatsApp or Telegram using the buttons below.'),
 'send': ('Оставить заявку', 'Send request'), 'sending': ('Отправляем…', 'Sending…'),
 'ok_prefix': ('Заявка отправлена! Мы напишем вам в ближайшее время: ', 'Request sent! We will contact you shortly at: '),
 'tg_copied': ('Если текст не подставился в Telegram — он скопирован, просто вставьте и отправьте.', 'If the text did not appear in Telegram, it is copied — just paste and send.'),
 'via_form': ('Заявка с сайта', 'Заявка с сайта'),
 'm_hello': ('Здравствуйте! Хочу арендовать авто.', 'Hello! I would like to rent a car.'),
 'm_car': ('Машина: ', 'Car: '), 'm_any': ('любая, подберите вариант', 'any, please suggest one'),
 'm_dates': ('Даты: ', 'Dates: '), 'm_price': ('По сайту: ', 'Website price: '), 'm_total': ('итого ≈ ', 'total ≈ '),
 'm_place': ('Где забрать: ', 'Pick-up: '), 'm_name': ('Имя: ', 'Name: '), 'm_contact': ('Мой контакт: ', 'My contact: '),
}

TERMS = [
 (('Пробег', 'Mileage'),
  ('250 км в сутки<small>Лимит суммируется за весь срок: 3 суток — 750 км. Каждый км сверх лимита — 5 000 ₫.</small>',
   '250 km per day<small>The limit adds up over the rental: 3 days = 750 km. Each km over the limit is 5,000 ₫.</small>')),
 (('Время получения и сдачи', 'Pick-up & return'),
  ('1 день: 7:00 — 22:00<small>На 2 дня и больше — вернуть до 22:00 последнего дня аренды.</small>',
   '1 day: 7:00 — 22:00<small>For 2 days or more — return by 22:00 on the last day.</small>')),
 (('Депозит по Кхань Хоа', 'Deposit — Khanh Hoa'),
  ('$200<small>Нячанг и окрестности. Возвращается при сдаче машины без повреждений.</small>',
   '$200<small>Nha Trang and around. Refunded when the car is returned undamaged.</small>')),
 (('Депозит по Вьетнаму', 'Deposit — all of Vietnam'),
  ('$400<small>$200 возвращаем сразу, остальные $200 — через месяц: штрафы с камер приходят с задержкой.</small>',
   '$400<small>$200 back on return, the other $200 after a month — camera fines can arrive late.</small>')),
 (('Документы', 'Documents'),
  ('Паспорт + МВУ + национальные права<small>Нужны для подписания договора аренды.</small>',
   'Passport + IDP + national licence<small>Required to sign the rental agreement.</small>')),
 (('Оплата', 'Payment'),
  ('После осмотра машины<small>Оплачиваете аренду после подписания договора и проверки кузова и салона.</small>',
   'After inspecting the car<small>You pay after signing the agreement and checking the body and interior.</small>')),
 (('Топливо', 'Fuel'),
  ('Бак в бак<small>Возвращаете с тем же уровнем, что при получении. Если топлива меньше — оплачиваете разницу.</small>',
   'Same level<small>Return it with the fuel level you received. If there is less, you pay the difference.</small>')),
 (('Мойка', 'Car wash'),
  ('350 000 ₫<small>Если машину вернули грязной — помоем за вас за эту сумму.</small>',
   '350,000 ₫<small>If the car comes back dirty, we wash it for this fee.</small>')),
 (('Повреждения и штрафы', 'Damage & fines'),
  ('Из депозита<small>При повреждениях или штрафах за нарушение ПДД депозит удерживается соразмерно.</small>',
   'From the deposit<small>For damage or traffic fines the matching amount is withheld from the deposit.</small>')),
 (('Долгая аренда', 'Long-term rental'),
  ('От месяца — своя ставка<small>Напишите даты — посчитаем выгоднее посуточной цены.</small>',
   'A month or more — special rate<small>Send us your dates and we’ll quote below the daily price.</small>')),
]

LANGS = ('ru', 'en', 'vi')
ORIGIN = 'https://vietavto.pro'
# Search-console ownership tags (Yandex Webmaster / Google Search Console); paste codes here.
VERIFY = '<meta name="yandex-verification" content="7a832af37c556278">\n'

def jsonld(lang, cars, vals):
    home = ORIGIN + HOME[lang]
    faq = [{'@type': 'Question', 'name': vals['q%d' % n],
            'acceptedAnswer': {'@type': 'Answer', 'text': vals['a%d' % n]}} for n in range(1, 9)]
    offers = [{'@type': 'Offer', 'name': c['name'], 'price': c['price'], 'priceCurrency': 'VND',
               'unitText': 'DAY'} for c in cars if not c.get('hidden') and c.get('price')]
    data = [
      {'@context': 'https://schema.org', '@type': 'AutoRental', 'name': 'VietAvto', 'url': home,
       'image': ORIGIN + '/images/luxa.jpg', 'logo': ORIGIN + '/apple-touch-icon.png',
       'description': vals['meta_desc'], 'telephone': '+79041188897',
       'address': {'@type': 'PostalAddress', 'addressLocality': 'Nha Trang', 'addressRegion': 'Khanh Hoa', 'addressCountry': 'VN'},
       'areaServed': ['Nha Trang', 'Khanh Hoa', 'Cam Ranh'],
       'openingHours': 'Mo-Su 07:00-22:00', 'priceRange': '700000-2100000 VND',
       'sameAs': ['https://t.me/workminer', 'https://wa.me/79041188897'],
       'makesOffer': offers},
      {'@context': 'https://schema.org', '@type': 'FAQPage', 'mainEntity': faq},
    ]
    return json.dumps(data, ensure_ascii=False)
HOME = {'ru': '/', 'en': '/en/', 'vi': '/vi/'}

def pick(table, key, lang, vi_table):
    if lang == 'vi':
        return vi_table[key]
    return table[key][0 if lang == 'ru' else 1]

def lang_switch(lang):
    return ''.join('<span>%s</span>' % l.upper() if l == lang else '<a href="%s" hreflang="%s">%s</a>' % (HOME[l], l, l.upper()) for l in LANGS)

def build(lang):
    i = 0 if lang == 'ru' else 1
    html = rd('src/template.html')
    cars = json.loads(rd('cars.json'))
    vals = {k: pick(S, k, lang, VI.S) for k in S}
    vals.update({
        'lang': lang,
        'origin': ORIGIN,
        'verify_tags': VERIFY if lang == 'ru' else '',
        'terms_html': '\n'.join('      <div class="term"><div class="k">%s</div><div class="v">%s</div></div>' % kv
                                 for kv in (VI.TERMS if lang == 'vi' else [(k[i], v[i]) for k, v in TERMS])),
        'home': HOME[lang],
        'fleet_static': '\n'.join(card_html(c, lang) for c in sorted(cars, key=lambda c: c.get('order', 0)) if not c.get('hidden')),
        'guides_html': ('<div class="guides">%s</div>' % guides_html(lang)) if lang in ('ru', 'en') else '',
        'logo_svg': LOGO,
        'lang_switch': lang_switch(lang),
        # </script> can't appear inside the JSON block
        'cars_json': json.dumps(cars, ensure_ascii=False).replace('</', '<\\/'),
        'js_strings': json.dumps({k: pick(JS, k, lang, VI.JS) for k in JS}, ensure_ascii=False),
    })
    vals['jsonld'] = jsonld(lang, cars, vals).replace('</', '<\\/')
    out = re.sub(r'\{\{(\w+)\}\}', lambda m: vals[m.group(1)], html)
    left = re.findall(r'\{\{\w+\}\}', out)
    assert not left, left
    path = os.path.join(ROOT, 'index.html' if lang == 'ru' else lang + '/index.html')
    os.makedirs(os.path.dirname(path), exist_ok=True)
    io.open(path, 'w', encoding='utf-8', newline='\n').write(out)
    return path

# ---------------- SEO landing pages (RU + EN) ----------------
import html as _html
import pages as P

LSTR = {
 'cars_h': ('Подходящие машины', 'Recommended cars'),
 'all_cars': ('Весь автопарк', 'All cars'),
 'faq_h': ('Вопросы и ответы', 'Questions & answers'),
 'more_h': ('Полезное', 'More guides'),
 'cta_book': ('Выбрать машину и даты', 'Choose car & dates'),
}
esc = lambda s: _html.escape(str(s), quote=True)

def landing_url(page, lang):
    return ORIGIN + ('/' if lang == 'ru' else '/en/') + page[lang]['slug'] + '/'

def guides_html(lang, exclude=None):
    if lang not in ('ru', 'en'):
        return ''
    links = ''.join('<a href="%s">%s</a>' % (landing_url(p, lang).replace(ORIGIN, ''), esc(p[lang]['link']))
                    for p in P.PAGES if p['id'] != exclude)
    links += ''.join('<a href="%s">%s</a>' % (car_url(c, lang), esc(('Аренда ' if lang == 'ru' else 'Rent ') + c['name']))
                     for c in sorted(json.loads(rd('cars.json')), key=lambda c: c.get('order', 0))
                     if not c.get('hidden') and 'car-' + c['id'] != exclude)
    return links

def fmt_price(v, lang):
    s = '{:,}'.format(int(v))
    return {'ru': s.replace(',', ' '), 'vi': s.replace(',', '.')}.get(lang, s)

def card_html(c, lang):
    L = lambda k: pick(JS, k, lang, VI.JS)
    cls = c.get('cls') if lang == 'ru' else (c.get('cls_' + lang) or c.get('cls_en') or c.get('cls'))
    desc = c.get('desc') if lang == 'ru' else (c.get('desc_' + lang) or c.get('desc_en') or c.get('desc'))
    meta = []
    if c.get('seats'):
        meta.append('<li>%s %s</li>' % (c['seats'], L('seats')))
    if c.get('gearbox') in ('auto', 'manual'):
        meta.append('<li>%s</li>' % L('gb_' + c['gearbox']))
    if c.get('fuel') in ('petrol', 'electric', 'diesel', 'hybrid'):
        meta.append('<li>%s</li>' % L('fu_' + c['fuel']))
    photos = c.get('photos') or []
    media = ('<img class="gallery-main" src="/%s" alt="%s" loading="lazy">' % (esc(photos[0]), esc(c['name']))
             if photos else '<div class="no-photo">%s</div>' % L('no_photo'))
    home = HOME[lang]
    return ('      <article class="car"><figure class="car-media">%s<span class="car-badge">%s</span></figure>'
            '<div class="car-body"><div class="car-top"><h3>%s</h3><div class="price"><b>%s ₫</b> %s</div></div>'
            '<ul class="car-meta">%s</ul><p class="spec">%s</p>'
            '<a class="car-cta" href="%s?car=%s#book">%s →</a></div></article>'
            % (media, esc(cls or ''), ('<a href="%s">%s</a>' % (car_url(c, lang), esc(c['name'])) if lang in ('ru', 'en') else esc(c['name'])), fmt_price(c.get('price', 0), lang), L('per_day'),
               ''.join(meta), esc(desc or ''), home, esc(c['id']), L('book')))

def build_landing(page, lang):
    i = 0 if lang == 'ru' else 1
    d = page[lang]
    tpl = rd('src/template.html')
    style = re.search(r'<style>.*?</style>', tpl, re.S).group(0)
    header = re.search(r'<header class="site-header">.*?</header>', tpl, re.S).group(0).replace('href="#', 'href="{{home}}#')
    footer = re.search(r'<footer>.*?</footer>', tpl, re.S).group(0)
    other = 'en' if lang == 'ru' else 'ru'
    switch = ''.join(
        '<span>%s</span>' % l.upper() if l == lang else
        '<a href="%s" hreflang="%s">%s</a>' % ((landing_url(page, l).replace(ORIGIN, '') if l in ('ru', 'en') else HOME[l]), l, l.upper())
        for l in LANGS)
    cars = {c['id']: c for c in json.loads(rd('cars.json'))}
    url = landing_url(page, lang)
    faq_ld = [{'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in d['faq']]
    crumbs = [{'@type': 'ListItem', 'position': 1, 'name': 'VietAvto', 'item': ORIGIN + HOME[lang]},
              {'@type': 'ListItem', 'position': 2, 'name': d['h1'], 'item': url}]
    ld = [{'@context': 'https://schema.org', '@type': 'FAQPage', 'mainEntity': faq_ld},
          {'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': crumbs}]
    vals = {k: S[k][i] for k in S}
    vals.update({k: v[i] for k, v in LSTR.items()})
    vals.update({
        'lang': lang, 'origin': ORIGIN, 'home': HOME[lang], 'logo_svg': LOGO, 'lang_switch': switch,
        'title': esc(d['title']), 'desc': esc(d['desc']), 'kw': esc(d['kw']), 'h1': esc(d['h1']), 'lead': esc(d['lead']),
        'url': url,
        'alternates': '\n'.join('<link rel="alternate" hreflang="%s" href="%s">' % (l, landing_url(page, l)) for l in ('ru', 'en'))
                      + '\n<link rel="alternate" hreflang="x-default" href="%s">' % landing_url(page, 'ru'),
        'cards': '\n'.join(card_html(cars[cid], lang) for cid in page['cars'] if cid in cars and not cars[cid].get('hidden')),
        'sections': '\n'.join('      <h2>%s</h2>\n%s' % (esc(h), '\n'.join('      <p>%s</p>' % esc(p) for p in ps)) for h, ps in d['sections']),
        'faq': '\n'.join('      <div class="qa"><h3>%s</h3><p>%s</p></div>' % (esc(q), esc(a)) for q, a in d['faq']),
        'guides': guides_html(lang, exclude=page['id']),
        'jsonld': json.dumps(ld, ensure_ascii=False).replace('</', '<\\/'),
        'style': style, 'header': header, 'footer': footer,
    })
    out = rd('src/landing.html')
    for _ in range(2):  # header/footer carry their own placeholders
        out = re.sub(r'\{\{(\w+)\}\}', lambda m: vals[m.group(1)], out)
    left = re.findall(r'\{\{\w+\}\}', out)
    assert not left, left
    path = os.path.join(ROOT, (page[lang]['slug'] if lang == 'ru' else 'en/' + page[lang]['slug']), 'index.html')
    os.makedirs(os.path.dirname(path), exist_ok=True)
    io.open(path, 'w', encoding='utf-8', newline='\n').write(out)
    return path

# ---------------- one page per car (RU + EN), generated from cars.json ----------------
def car_slug(c):
    return re.sub(r'[^a-z0-9]+', '-', c['name'].lower()).strip('-') or c['id']

def car_page(c, all_cars):
    name, p = c['name'], int(c.get('price') or 0)
    s = car_slug(c)
    fp = lambda v, l: fmt_price(v, l)
    def specs(lang):
        i = 0 if lang == 'ru' else 1
        out = []
        if c.get('seats'):
            out.append('%s %s' % (c['seats'], JS['seats'][i]))
        if c.get('gearbox') in ('auto', 'manual'):
            out.append(JS['gb_' + c['gearbox']][i].lower())
        if c.get('fuel') in ('petrol', 'electric', 'diesel', 'hybrid'):
            out.append(JS['fu_' + c['fuel']][i].lower())
        return ', '.join(out)
    ev = c.get('fuel') == 'electric'
    live = [x for x in all_cars if x['id'] != c['id'] and not x.get('hidden')]
    related = [x['id'] for x in sorted(live, key=lambda x: abs(int(x.get('price') or 0) - p))[:3]]
    cls_ru, cls_en = c.get('cls') or '', c.get('cls_en') or c.get('cls') or ''
    sp_ru, sp_en = specs('ru'), specs('en')
    ru = {
      'slug': 'arenda-%s-nyachang' % s,
      'link': 'Аренда ' + name,
      'title': 'Аренда %s в Нячанге — %s ₫/сутки без водителя | VietAvto' % (name, fp(p, 'ru')),
      'desc': 'Аренда %s в Нячанге без водителя: %s ₫ в сутки, депозит от $200, передача в отеле или аэропорту Камрань. Фото, характеристики, условия и онлайн-заявка.' % (name, fp(p, 'ru')),
      'kw': 'аренда %s Нячанг, прокат %s Нячанг, %s напрокат Вьетнам, аренда %s Камрань, %s цена аренды' % (name, name, name, name, name),
      'h1': 'Аренда %s в Нячанге' % name,
      'lead': c.get('desc') or '',
      'sections': [
        ('Характеристики %s' % name, ['%s — %s%s.%s' % (name, cls_ru.lower() or 'автомобиль', (': ' + sp_ru) if sp_ru else '',
                                     ' На фото — реальный автомобиль из нашего парка.' if c.get('photos') else '')]),
        ('Цена аренды %s' % name, ['%s ₫ в сутки. Например, 3 суток — %s ₫, неделя — %s ₫. На месяц и дольше — отдельная, более выгодная ставка. Лимит пробега 250 км в сутки суммируется за весь срок: за неделю — 1 750 км, каждый км сверх лимита — 5 000 ₫.'
                                   % (fp(p, 'ru'), fp(3 * p, 'ru'), fp(7 * p, 'ru'))]),
        ('Условия аренды', ['Депозит $200 для поездок по провинции Кхань Хоа или $400 — по всему Вьетнаму. Документы: паспорт, международное водительское удостоверение (МВУ) и национальные права. Оплата — после осмотра машины, возврат — с тем же уровнем топлива. На 1 день машину можно взять с 7:00 до 22:00.']),
        ('Где забрать %s' % name, ['Передадим машину в вашем отеле, по адресу в Нячанге или в аэропорту Камрань — место и время согласуем в WhatsApp или Telegram.']),
      ],
      'faq': [
        ('Сколько стоит аренда %s в Нячанге?' % name, '%s ₫ в сутки, неделя — %s ₫. На месяц — отдельная ставка.' % (fp(p, 'ru'), fp(7 * p, 'ru'))),
        ('Можно взять %s в аэропорту Камрань?' % name, 'Да, передадим машину в аэропорту к вашему прилёту.'),
        ('Можно поехать на %s в Далат?' % name, 'Да, с депозитом $400 для поездок по всему Вьетнаму.' + (' Электромобиль лучше подзарядить в дороге.' if ev else '')),
        ('Какие документы нужны для аренды?', 'Паспорт, международное водительское удостоверение (МВУ) и национальные права.'),
      ],
    }
    en = {
      'slug': 'rent-%s-nha-trang' % s,
      'link': 'Rent ' + name,
      'title': 'Rent %s in Nha Trang — %s ₫/day, Self-Drive | VietAvto' % (name, fp(p, 'en')),
      'desc': 'Rent a %s in Nha Trang, self-drive: %s ₫ a day, deposit from $200, hand-over at your hotel or Cam Ranh airport. Photos, specs, terms and online booking.' % (name, fp(p, 'en')),
      'kw': '%s rental Nha Trang, rent %s Nha Trang, %s hire Vietnam, %s Cam Ranh airport, %s rental price' % (name, name, name, name, name),
      'h1': 'Rent %s in Nha Trang' % name,
      'lead': c.get('desc_en') or c.get('desc') or '',
      'sections': [
        ('%s specs' % name, ['The %s is a %s%s.%s' % (name, cls_en.lower() or 'car', (': ' + sp_en) if sp_en else '',
                              ' The photos show the real car from our fleet.' if c.get('photos') else '')]),
        ('%s rental price' % name, ['%s ₫ per day. For example, 3 days — %s ₫, a week — %s ₫. A month or longer gets a separate, better rate. The 250 km per day limit adds up over the rental: 1,750 km for a week, each extra km is 5,000 ₫.'
                                    % (fp(p, 'en'), fp(3 * p, 'en'), fp(7 * p, 'en'))]),
        ('Rental terms', ['Deposit $200 for trips within Khanh Hoa province or $400 across Vietnam. Documents: passport, International Driving Permit (1968 Convention) and national licence. You pay after inspecting the car and return it with the same fuel level. One-day rentals run from 7:00 to 22:00.']),
        ('Where to pick up the %s' % name, ['We hand over the car at your hotel, an address in Nha Trang or Cam Ranh airport — we agree the place and time on WhatsApp or Telegram.']),
      ],
      'faq': [
        ('How much is a %s rental in Nha Trang?' % name, '%s ₫ per day, %s ₫ for a week. Monthly rentals get a separate rate.' % (fp(p, 'en'), fp(7 * p, 'en'))),
        ('Can I pick up the %s at Cam Ranh airport?' % name, 'Yes, we can meet you with the car on arrival.'),
        ('Can I drive the %s to Da Lat?' % name, 'Yes, with the $400 deposit for trips across Vietnam.' + (' Plan a charging stop for the EV.' if ev else '')),
        ('What documents do I need?', 'Your passport, an International Driving Permit (1968 Convention) and your national licence.'),
      ],
    }
    return {'id': 'car-' + c['id'], 'cars': [c['id']] + related, 'ru': ru, 'en': en}

def car_pages():
    cars = json.loads(rd('cars.json'))
    return [car_page(c, cars) for c in sorted(cars, key=lambda c: c.get('order', 0)) if not c.get('hidden')]

def car_url(c, lang):
    return {'ru': '/arenda-%s-nyachang/', 'en': '/en/rent-%s-nha-trang/'}[lang] % car_slug(c) if lang in ('ru', 'en') else ''

def sitemap():
    import datetime
    today = datetime.date.today().isoformat()
    alts = ''.join('    <xhtml:link rel="alternate" hreflang="%s" href="%s%s"/>\n' % (l, ORIGIN, HOME[l]) for l in LANGS)
    urls = ''.join('  <url>\n    <loc>%s%s</loc>\n%s    <lastmod>%s</lastmod>\n    <changefreq>weekly</changefreq>\n'
                   '    <priority>%s</priority>\n  </url>\n' % (ORIGIN, HOME[l], alts, today, '1.0' if l == 'ru' else '0.9')
                   for l in LANGS)
    for p in P.PAGES + car_pages():
        palts = ''.join('    <xhtml:link rel="alternate" hreflang="%s" href="%s"/>\n' % (l, landing_url(p, l)) for l in ('ru', 'en'))
        for l in ('ru', 'en'):
            urls += ('  <url>\n    <loc>%s</loc>\n%s    <lastmod>%s</lastmod>\n    <changefreq>monthly</changefreq>\n'
                     '    <priority>0.8</priority>\n  </url>\n' % (landing_url(p, l), palts, today))
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
           + urls + '</urlset>\n')
    io.open(os.path.join(ROOT, 'sitemap.xml'), 'w', encoding='utf-8', newline='\n').write(xml)

if __name__ == '__main__':
    for l in LANGS:
        print('built', build(l))
    for p in P.PAGES + car_pages():
        for l in ('ru', 'en'):
            print('built', build_landing(p, l))
    sitemap()
