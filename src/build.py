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
 'title': ('Аренда авто в Нячанге — VietAvto', 'Car rental in Nha Trang — VietAvto'),
 'meta_desc': ('Прокат автомобилей без водителя в Нячанге: VinFast, Toyota, Mitsubishi, Mazda и другие. Цены за сутки, понятный депозит, заявка онлайн.',
               'Self-drive car rental in Nha Trang: VinFast, Toyota, Mitsubishi, Mazda and more. Daily prices, a clear deposit, book online.'),
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
        'terms_html': '\n'.join('      <div class="term"><div class="k">%s</div><div class="v">%s</div></div>' % kv
                                 for kv in (VI.TERMS if lang == 'vi' else [(k[i], v[i]) for k, v in TERMS])),
        'home': HOME[lang],
        'logo_svg': LOGO,
        'lang_switch': lang_switch(lang),
        # </script> can't appear inside the JSON block
        'cars_json': json.dumps(cars, ensure_ascii=False).replace('</', '<\\/'),
        'js_strings': json.dumps({k: pick(JS, k, lang, VI.JS) for k in JS}, ensure_ascii=False),
    })
    out = re.sub(r'\{\{(\w+)\}\}', lambda m: vals[m.group(1)], html)
    left = re.findall(r'\{\{\w+\}\}', out)
    assert not left, left
    path = os.path.join(ROOT, 'index.html' if lang == 'ru' else lang + '/index.html')
    os.makedirs(os.path.dirname(path), exist_ok=True)
    io.open(path, 'w', encoding='utf-8', newline='\n').write(out)
    return path

if __name__ == '__main__':
    for l in LANGS:
        print('built', build(l))
