# Builds / (RU) and /en/ (EN) from src/template.html + cars.json.  Run: python src/build.py
import io, json, os, re

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
 't1_k': ('Пробег', 'Mileage'), 't1_v': ('250 км в сутки<small>Планируете дальний маршрут — предупредите заранее, посчитаем доплату.</small>',
                                        '250 km per day<small>Planning a long trip? Tell us in advance and we’ll quote the extra.</small>'),
 't2_k': ('Депозит по Кхань Хоа', 'Deposit — Khanh Hoa'), 't2_v': ('$200<small>Нячанг и окрестности. Возвращается при сдаче машины.</small>',
                                                              '$200<small>Nha Trang and around. Refunded when you return the car.</small>'),
 't3_k': ('Депозит по Вьетнаму', 'Deposit — all of Vietnam'), 't3_v': ('$400<small>$200 возвращаем сразу, остальные $200 — через месяц: штрафы с камер приходят с задержкой.</small>',
                                                                      '$400<small>$200 back on return, the other $200 after a month — camera fines can arrive late.</small>'),
 't4_k': ('Топливо', 'Fuel'), 't4_v': ('Бак в бак<small>Возвращаете с тем же уровнем топлива — никаких доплат за литры.</small>',
                                       'Same level<small>Return it with the fuel level you received — no refuelling charges.</small>'),
 't5_k': ('Мойка', 'Car wash'), 't5_v': ('350 000 ₫<small>Машину нужно вернуть чистой — или помоем за вас за эту сумму.</small>',
                                         '350,000 ₫<small>Please return the car clean — or we’ll wash it for this fee.</small>'),
 't6_k': ('Долгая аренда', 'Long-term rental'), 't6_v': ('От месяца — своя ставка<small>Напишите даты — посчитаем выгоднее посуточной цены.</small>',
                                                        'A month or more — special rate<small>Send us your dates and we’ll quote below the daily price.</small>'),
 'faq_h': ('Вопросы и ответы', 'Questions & answers'),
 'q1': ('Нужны ли международные права?', 'Do I need an international licence?'),
 'a1': ('Да. Для вождения во Вьетнаме нужно международное водительское удостоверение (по Венской конвенции 1968 года) или вьетнамские права.',
        'Yes. To drive in Vietnam you need an International Driving Permit (1968 Vienna Convention) or a Vietnamese licence.'),
 'q2': ('Какой депозит?', 'How much is the deposit?'),
 'a2': ('$200 для поездок по провинции Кхань Хоа и $400 — по всему Вьетнаму. Подробности — в условиях выше.',
        '$200 for trips within Khanh Hoa province and $400 for all of Vietnam. Details are in the terms above.'),
 'q3': ('Можно поехать в Далат или дальше?', 'Can I drive to Da Lat or further?'),
 'a3': ('Да, с депозитом $400. Дневной лимит — 250 км: для длинного маршрута предупредите заранее, посчитаем доплату.',
        'Yes, with the $400 deposit. The daily limit is 250 km — for a long route tell us in advance and we’ll quote the extra.'),
 'q4': ('Где забрать машину?', 'Where do I pick up the car?'),
 'a4': ('Место передачи согласуем при бронировании: отель, адрес в Нячанге или аэропорт Камрань.',
        'We agree on the hand-over spot when you book: your hotel, an address in Nha Trang or Cam Ranh airport.'),
 'q5': ('Как забронировать?', 'How do I book?'),
 'a5': ('Выберите машину и даты в форме вверху и нажмите «Оставить заявку» — мы напишем вам сами. Или сразу напишите нам в WhatsApp или Telegram.',
        'Pick a car and dates in the form above and press “Send request” — we’ll message you. Or write to us directly on WhatsApp or Telegram.'),
 'q6': ('Есть скидка на долгую аренду?', 'Is there a long-term discount?'),
 'a6': ('Да, при аренде на месяц и дольше действует отдельная ставка — пришлите даты, и мы её назовём.',
        'Yes, rentals of a month or longer get a separate rate — send us your dates and we’ll quote it.'),
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

def build(lang):
    i = 0 if lang == 'ru' else 1
    html = rd('src/template.html')
    cars = json.loads(rd('cars.json'))
    vals = {k: v[i] for k, v in S.items()}
    vals.update({
        'lang': lang,
        'home': '/' if lang == 'ru' else '/en/',
        'logo_svg': LOGO,
        'lang_switch': '<span>RU</span><a href="/en/" hreflang="en">EN</a>' if lang == 'ru' else '<a href="/" hreflang="ru">RU</a><span>EN</span>',
        # </script> can't appear inside the JSON block
        'cars_json': json.dumps(cars, ensure_ascii=False).replace('</', '<\\/'),
        'js_strings': json.dumps({k: v[i] for k, v in JS.items()}, ensure_ascii=False),
    })
    out = re.sub(r'\{\{(\w+)\}\}', lambda m: vals[m.group(1)], html)
    left = re.findall(r'\{\{\w+\}\}', out)
    assert not left, left
    path = os.path.join(ROOT, 'index.html' if lang == 'ru' else 'en/index.html')
    os.makedirs(os.path.dirname(path), exist_ok=True)
    io.open(path, 'w', encoding='utf-8', newline='\n').write(out)
    return path

if __name__ == '__main__':
    for l in ('ru', 'en'):
        print('built', build(l))
