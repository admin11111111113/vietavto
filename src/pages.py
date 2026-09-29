# SEO landing pages (RU + EN). Each page targets one search intent with its own text, FAQ and matching cars.
# Keys: slug, title, desc, kw, h1, lead, sections [(h2, [paragraphs])], faq [(q, a)], cars [ids], link (anchor text for internal links)

PAGES = [
 {
  'id': 'monthly',
  'cars': ['vf3', 'soluto', 'vf5', 'xpander'],
  'ru': {
   'slug': 'arenda-avto-na-mesyac',
   'link': 'Аренда авто на месяц в Нячанге',
   'title': 'Аренда авто в Нячанге на месяц — долгосрочный прокат дешевле посуточного | VietAvto',
   'desc': 'Долгосрочная аренда авто в Нячанге на месяц и дольше: отдельная выгодная ставка, машины от VinFast VF3 до 7-местного Xpander. Для зимовки, работы и жизни во Вьетнаме.',
   'kw': 'аренда авто на месяц Нячанг, долгосрочная аренда авто Нячанг, аренда машины на месяц Вьетнам, аренда авто на зимовку Нячанг, помесячная аренда авто Нячанг',
   'h1': 'Аренда авто на месяц в Нячанге',
   'lead': 'Зимуете в Нячанге или живёте здесь несколько месяцев? Долгосрочная аренда машины выходит заметно выгоднее посуточной — для месяца и дольше у нас отдельная ставка.',
   'sections': [
    ('Кому подходит долгосрочная аренда', [
     'Тем, кто приезжает на зимовку, работает удалённо или переезжает во Вьетнам. Своя машина на месяц — это поездки на пляжи и водопады в любое время, покупки без такси и выезды в Далат или Фанранг на выходных.',
    ]),
    ('Какие машины берут на месяц', [
     'Чаще всего — экономичные: электромобиль VinFast VF3 для города, седан Kia Soluto или электрокроссовер VF5. Для семьи с детьми — 7-местный Mitsubishi Xpander. Все машины из нашего парка, на фото — реальные автомобили.',
    ]),
    ('Как рассчитывается цена', [
     'Посуточные цены указаны на главной странице, а для аренды от месяца мы называем отдельную ставку — она ниже посуточной. Пришлите даты и машину через форму или в WhatsApp/Telegram, и мы ответим с точной суммой. Лимит пробега 250 км в сутки суммируется за весь срок: за 30 дней — 7 500 км.'
    ]),
   ],
   'faq': [
    ('Насколько дешевле аренда на месяц?', 'Ставка зависит от машины и сезона — пришлите даты, и мы назовём точную цену.'),
    ('Какой пробег за месяц?', '250 км в сутки суммируются за весь срок: за 30 дней — 7 500 км. Каждый км сверх лимита — 5 000 ₫.'),
    ('Можно продлить аренду?', 'Да, просто напишите нам заранее, до окончания срока.'),
   ],
  },
  'en': {
   'slug': 'monthly-car-rental-nha-trang',
   'link': 'Monthly car rental in Nha Trang',
   'title': 'Monthly Car Rental in Nha Trang — Long-Term Self-Drive, Better Than Daily Rates | VietAvto',
   'desc': 'Long-term car rental in Nha Trang for a month or more: a special monthly rate, cars from the VinFast VF3 to the 7-seat Xpander. For digital nomads, long stays and living in Vietnam.',
   'kw': 'monthly car rental Nha Trang, long-term car rental Nha Trang, rent a car for a month Vietnam, long term car hire Vietnam, digital nomad car rental Nha Trang',
   'h1': 'Monthly Car Rental in Nha Trang',
   'lead': 'Staying in Nha Trang for a few months? A long-term rental is noticeably cheaper than paying by the day — a month or longer gets its own rate.',
   'sections': [
    ('Who long-term rental is for', [
     'Digital nomads, long-stay travellers and anyone moving to Vietnam. Your own car for a month means beaches and waterfalls whenever you like, shopping without taxis and weekend trips to Da Lat or Phan Rang.',
    ]),
    ('Popular cars for a month', [
     'Most people choose economical cars: the VinFast VF3 electric car for the city, the Kia Soluto sedan or the VF5 electric crossover. Families pick the 7-seat Mitsubishi Xpander. All cars are from our own fleet and the photos show the real vehicles.',
    ]),
    ('How the price works', [
     'Daily prices are listed on the main page; for a month or longer we quote a separate, lower rate. Send us your dates and car via the form or WhatsApp/Telegram and we reply with the exact amount. The 250 km per day limit adds up over the rental: 30 days = 7,500 km.'
    ]),
   ],
   'faq': [
    ('How much cheaper is a monthly rental?', 'It depends on the car and season — send your dates and we will quote the exact price.'),
    ('What is the mileage allowance for a month?', '250 km per day added up over the rental: 30 days = 7,500 km. Each extra km is 5,000 ₫.'),
    ('Can I extend the rental?', 'Yes, just message us before the rental ends.'),
   ],
  },
 },
 {
  'id': 'cheap',
  'cars': ['vf3', 'vf5', 'soluto', 'mazda3'],
  'ru': {
   'slug': 'deshevaya-arenda-avto-nyachang',
   'link': 'Дешёвая аренда авто в Нячанге',
   'title': 'Аренда авто в Нячанге дешево — от 700 000 ₫ в сутки без посредников | VietAvto',
   'desc': 'Недорогая аренда авто в Нячанге без водителя: VinFast VF3 от 700 000 ₫, VF5 от 800 000 ₫, седаны от 900 000 ₫ в сутки. Без посредников и скрытых доплат, депозит от $200.',
   'kw': 'аренда авто Нячанг дешево, недорогая аренда машины Нячанг, прокат авто Нячанг недорого, дешевый прокат машин Вьетнам, аренда авто Нячанг эконом',
   'h1': 'Дешёвая аренда авто в Нячанге',
   'lead': 'Ищете, где взять машину в Нячанге недорого? Мы сдаём автомобили из своего парка без посредников, поэтому цена — от 700 000 ₫ в сутки, а все условия расписаны заранее.',
   'sections': [
    ('Самые доступные машины', [
     'VinFast VF3 — городской электромобиль за 700 000 ₫ в сутки: компактный, легко паркуется, запас хода около 210 км. VinFast VF5 — электрокроссовер за 800 000 ₫. Kia Soluto и Mazda3 — седаны за 900 000 ₫ в сутки.',
    ]),
    ('Почему у нас дешевле', [
     'Нет агрегатора и комиссии посредника — вы бронируете напрямую у владельца. Условия прозрачны: депозит $200 по провинции, 250 км в сутки с суммированием за весь срок, возврат «бак в бак». На месяц и дольше — отдельная, ещё более выгодная ставка.',
    ]),
    ('Как сэкономить ещё', [
     'Берите электромобиль, если ездите в основном по городу и окрестностям, — это дешевле бензина. Возвращайте машину с тем же уровнем топлива, чтобы не доплачивать за бензин.',
    ]),
   ],
   'faq': [
    ('Какая самая дешёвая машина?', 'VinFast VF3 — 700 000 ₫ в сутки.'),
    ('Есть скрытые платежи?', 'Нет. Отдельно оплачиваются только перепробег (5 000 ₫/км сверх лимита) и недостающее топливо.'),
    ('Есть скидка на долгий срок?', 'Да, на месяц и дольше действует отдельная ставка ниже посуточной.'),
   ],
  },
  'en': {
   'slug': 'cheap-car-rental-nha-trang',
   'link': 'Cheap car rental in Nha Trang',
   'title': 'Cheap Car Rental in Nha Trang — From 700,000 ₫ a Day, No Middlemen | VietAvto',
   'desc': 'Budget self-drive car rental in Nha Trang: VinFast VF3 from 700,000 ₫, VF5 from 800,000 ₫, sedans from 900,000 ₫ per day. No middlemen, no hidden fees, deposit from $200.',
   'kw': 'cheap car rental Nha Trang, budget car hire Nha Trang, affordable car rental Vietnam, cheapest car rental Nha Trang, economy car rental Nha Trang',
   'h1': 'Cheap Car Rental in Nha Trang',
   'lead': 'Looking for an affordable car in Nha Trang? We rent cars from our own fleet with no middlemen, so prices start at 700,000 ₫ a day and all terms are clear upfront.',
   'sections': [
    ('The most affordable cars', [
     'The VinFast VF3 city EV is 700,000 ₫ a day: compact, easy to park, about 210 km of range. The VinFast VF5 electric crossover is 800,000 ₫. The Kia Soluto and Mazda3 sedans are 900,000 ₫ a day.',
    ]),
    ('Why we are cheaper', [
     'No aggregator and no middleman commission — you book directly with the owner. Clear terms: $200 deposit within the province, 250 km per day added up over the rental, same-fuel-level return. A month or longer gets an even better rate.',
    ]),
    ('How to save more', [
     'Choose an electric car if you mostly drive around the city — it costs less than petrol. Return it with the same fuel level to avoid paying for petrol.',
    ]),
   ],
   'faq': [
    ('What is the cheapest car?', 'The VinFast VF3 — 700,000 ₫ per day.'),
    ('Are there hidden fees?', 'No. You only pay extra for mileage over the limit (5,000 ₫/km) and missing fuel.'),
    ('Is there a long-term discount?', 'Yes, a month or longer has a separate rate below the daily price.'),
   ],
  },
 },
 {
  'id': 'seven',
  'cars': ['rush', 'xpander', 'veloz', 'carnival'],
  'ru': {
   'slug': 'arenda-miniven-7-mest-nyachang',
   'link': 'Аренда минивэна и 7-местного авто',
   'title': 'Аренда минивэна и 7-местного авто в Нячанге — для семьи и компании | VietAvto',
   'desc': 'Аренда 7-местных авто и минивэнов в Нячанге без водителя: Toyota Rush, Veloz, Mitsubishi Xpander от 1 000 000 ₫, Kia Carnival на 7 мест. Для семьи, детей и больших компаний.',
   'kw': 'аренда минивэна Нячанг, аренда 7 местного авто Нячанг, аренда авто для семьи Нячанг, аренда Kia Carnival Нячанг, аренда Xpander Нячанг, аренда большой машины Нячанг',
   'h1': 'Аренда минивэна и 7-местного авто в Нячанге',
   'lead': 'Путешествуете семьёй или компанией? Вместо двух такси — одна просторная машина: 7-местные Toyota и Mitsubishi или просторный Kia Carnival на 7 мест.',
   'sections': [
    ('7-местные авто', [
     'Toyota Rush — компактный 7-местный внедорожник с высокой посадкой, увереннее на разбитых дорогах к водопадам. Mitsubishi Xpander и Toyota Veloz — семейные минивэны, где третий ряд вмещает взрослых, а багажник — чемоданы. Цены — от 1 000 000 ₫ в сутки.',
    ]),
    ('Kia Carnival для больших групп', [
     'Kia Carnival — большой 7-местный минивэн со сдвижными дверями и самым просторным салоном в парке. Подходит для большой семьи и поездок в Далат всей компанией. 2 100 000 ₫ в сутки.',
    ]),
    ('Детские кресла и багаж', [
     'Если нужно детское кресло или место под крупный багаж (коляска, доски для сёрфинга), напишите об этом в заявке — подберём подходящую машину.',
    ]),
   ],
   'faq': [
    ('Сколько человек помещается в Xpander?', '7 человек, третий ряд подходит и для взрослых.'),
    ('Какая машина самая просторная?', 'Kia Carnival — 7 мест, большой салон и багажник.'),
    ('Можно ехать на 7-местной машине в Далат?', 'Да, с депозитом $400 для поездок по всему Вьетнаму.'),
   ],
  },
  'en': {
   'slug': '7-seater-minivan-rental-nha-trang',
   'link': '7-seater & minivan rental',
   'title': '7-Seater & Minivan Rental in Nha Trang — Family and Group Cars | VietAvto',
   'desc': 'Self-drive 7-seater and minivan rental in Nha Trang: Toyota Rush, Veloz, Mitsubishi Xpander from 1,000,000 ₫ a day, Kia Carnival with 7 seats. For families, kids and groups.',
   'kw': '7 seater car rental Nha Trang, minivan rental Nha Trang, family car rental Nha Trang, Kia Carnival rental Nha Trang, Xpander rental Nha Trang, large car rental Vietnam',
   'h1': '7-Seater & Minivan Rental in Nha Trang',
   'lead': 'Travelling as a family or group? One roomy car instead of two taxis: 7-seat Toyotas and Mitsubishis or the roomy 7-seat Kia Carnival.',
   'sections': [
    ('7-seat cars', [
     'The Toyota Rush is a compact 7-seat SUV with high clearance, more confident on rough roads to the waterfalls. The Mitsubishi Xpander and Toyota Veloz are family minivans whose third row fits adults and whose boot takes suitcases. From 1,000,000 ₫ a day.',
    ]),
    ('Kia Carnival for big groups', [
     'The Kia Carnival is a large 7-seat minivan with sliding doors and the roomiest cabin in the fleet — ideal for a big family or a group trip to Da Lat. 2,100,000 ₫ a day.',
    ]),
    ('Child seats and luggage', [
     'If you need a child seat or room for bulky luggage (strollers, surfboards), mention it in your request and we will match the right car.',
    ]),
   ],
   'faq': [
    ('How many people fit in the Xpander?', '7 people; the third row fits adults too.'),
    ('Which car is the roomiest?', 'The Kia Carnival — 7 seats with a large cabin and boot.'),
    ('Can I take a 7-seater to Da Lat?', 'Yes, with the $400 deposit for trips across Vietnam.'),
   ],
  },
 },
 {
  'id': 'ev',
  'cars': ['vf3', 'vf5'],
  'ru': {
   'slug': 'arenda-elektromobilya-vinfast-nyachang',
   'link': 'Аренда электромобиля VinFast',
   'title': 'Аренда электромобиля VinFast VF3 и VF5 в Нячанге — от 700 000 ₫ | VietAvto',
   'desc': 'Аренда электромобилей VinFast в Нячанге: VF3 от 700 000 ₫ и VF5 от 800 000 ₫ в сутки. Запас хода 210–300 км, зарядные станции по всему городу. Без водителя, заявка онлайн.',
   'kw': 'аренда электромобиля Нячанг, аренда VinFast Нячанг, аренда VinFast VF3, аренда VinFast VF5 Нячанг, прокат электромобиля Вьетнам, электромобиль напрокат Нячанг',
   'h1': 'Аренда электромобиля VinFast в Нячанге',
   'lead': 'VinFast — вьетнамский производитель электромобилей, и Нячанг — удобный город, чтобы попробовать электромобиль: короткие расстояния и много зарядных станций VinFast.',
   'sections': [
    ('VinFast VF3 — городской электромобиль', [
     'Компактный 4-местный электромобиль длиной всего 3,2 м: паркуется там, где не пройдёт седан. Запас хода — около 210 км, этого хватает на несколько дней поездок по Нячангу и окрестностям. 700 000 ₫ в сутки — самая доступная машина в нашем парке.',
    ]),
    ('VinFast VF5 — электрокроссовер', [
     'Просторнее VF3, 5 мест, запас хода около 300 км. Электромотор даёт хорошую тягу с места — удобно и в городе, и на трассе до пляжей Зоклет или залива Камрань. 800 000 ₫ в сутки.',
    ]),
    ('Как заряжать', [
     'В Нячанге и по трассам Вьетнама работает сеть зарядных станций VinFast — на парковках торговых центров, отелей и заправок. Зарядка для наших клиентов бесплатная — вы платите только за аренду.',
    ]),
   ],
   'faq': [
    ('Хватит ли заряда до Далата?', 'VF5 с запасом хода около 300 км доедет (около 135 км), но лучше подзарядиться в дороге или в Далате. Для таких поездок удобнее бензиновый кроссовер.'),
    ('Нужны ли особые права для электромобиля?', 'Нет, те же документы: паспорт, МВУ и национальные права.'),
    ('Сколько мест в VF3?', '4 места.'),
   ],
  },
  'en': {
   'slug': 'electric-car-rental-vinfast-nha-trang',
   'link': 'VinFast electric car rental',
   'title': 'VinFast Electric Car Rental in Nha Trang — VF3 & VF5 from 700,000 ₫ | VietAvto',
   'desc': 'Rent a VinFast electric car in Nha Trang: VF3 from 700,000 ₫ and VF5 from 800,000 ₫ a day. 210–300 km of range, charging stations across the city. Self-drive, book online.',
   'kw': 'electric car rental Nha Trang, VinFast rental Nha Trang, rent VinFast VF3, VinFast VF5 rental, EV rental Vietnam, rent an electric car in Vietnam',
   'h1': 'VinFast Electric Car Rental in Nha Trang',
   'lead': 'VinFast is Vietnam’s own electric car maker, and Nha Trang is a great place to try one: short distances and plenty of VinFast charging stations.',
   'sections': [
    ('VinFast VF3 — the city EV', [
     'A compact 4-seat EV just 3.2 m long that parks where a sedan won’t fit. About 210 km of range — enough for several days around Nha Trang. At 700,000 ₫ a day it is the most affordable car in our fleet.',
    ]),
    ('VinFast VF5 — electric crossover', [
     'Roomier than the VF3, 5 seats and about 300 km of range. Instant electric torque makes it easy in town and on the road to Doc Let beach or Cam Ranh Bay. 800,000 ₫ a day.',
    ]),
    ('Charging', [
     'VinFast runs a charging network in Nha Trang and along Vietnam’s highways — at malls, hotels and petrol stations. Charging is free for our customers — you only pay for the rental.',
    ]),
   ],
   'faq': [
    ('Can I reach Da Lat on one charge?', 'The VF5 with about 300 km of range can cover the ~135 km, but it is best to top up on the way or in Da Lat. A petrol crossover is easier for such trips.'),
    ('Do I need a special licence for an EV?', 'No, the same documents: passport, IDP and national licence.'),
    ('How many seats does the VF3 have?', '4 seats.'),
   ],
  },
 },
 {
  'id': 'dalat',
  'cars': ['creta', 'xforce', 'rush', 'veloz'],
  'ru': {
   'slug': 'nyachang-dalat-na-mashine',
   'link': 'Нячанг — Далат на машине',
   'title': 'Нячанг — Далат на машине: маршрут, расстояние, аренда авто | VietAvto',
   'desc': 'Как доехать из Нячанга в Далат на арендованной машине: 135 км, 3–3,5 часа по перевалу Кхань Ле. Советы по маршруту, какую машину взять и сколько стоит аренда авто для поездки в Далат.',
   'kw': 'Нячанг Далат на машине, поездка в Далат из Нячанга, аренда авто Нячанг Далат, Нячанг Далат расстояние, перевал Кхань Ле, как доехать до Далата из Нячанга',
   'h1': 'Нячанг — Далат на машине',
   'lead': 'Далат — город в горах в 135 км от Нячанга, одна из самых красивых поездок во Вьетнаме. На своей машине вы едете в своём темпе и останавливаетесь у водопадов и смотровых площадок.',
   'sections': [
    ('Маршрут и время в пути', [
     'Основная дорога идёт через перевал Кхань Ле (трасса 27C): примерно 135 км и 3–3,5 часа езды. Первая половина — равнина, затем серпантин с подъёмом почти на 1 500 м и видами на джунгли и облака. Выезжайте утром: к вечеру в горах бывает туман.',
    ]),
    ('Какую машину взять', [
     'Для горной дороги удобнее кроссовер с высокой посадкой: Hyundai Creta или Mitsubishi Xforce. Если едете семьёй — 7-местные Toyota Rush или Veloz. Электромобилю лучше подзарядиться в дороге.',
    ]),
    ('Условия для поездки', [
     'Поездки за пределы провинции Кхань Хоа — с депозитом $400: $200 возвращаем сразу при сдаче, остальные $200 — через месяц. Лимит 250 км в сутки суммируется за весь срок: поездка туда и обратно (около 270 км) за двое суток укладывается в лимит.',
    ]),
   ],
   'faq': [
    ('Сколько километров от Нячанга до Далата?', 'Около 135 км по перевалу Кхань Ле.'),
    ('Сколько ехать?', '3–3,5 часа с учётом серпантина, с остановками — больше.'),
    ('Какой депозит для поездки в Далат?', '$400 — для поездок за пределы провинции Кхань Хоа.'),
   ],
  },
  'en': {
   'slug': 'nha-trang-to-da-lat-by-car',
   'link': 'Nha Trang to Da Lat by car',
   'title': 'Nha Trang to Da Lat by Car: Route, Distance & Self-Drive Rental | VietAvto',
   'desc': 'Driving from Nha Trang to Da Lat in a rental car: 135 km, 3–3.5 hours over the Khanh Le Pass. Route tips, which car to pick and what a rental for the Da Lat trip costs.',
   'kw': 'Nha Trang to Da Lat by car, drive Nha Trang Da Lat, Nha Trang Da Lat distance, Khanh Le Pass, car rental Nha Trang Da Lat, self drive Da Lat',
   'h1': 'Nha Trang to Da Lat by Car',
   'lead': 'Da Lat is a mountain town 135 km from Nha Trang and one of Vietnam’s most beautiful drives. In your own car you set the pace and stop at waterfalls and viewpoints.',
   'sections': [
    ('Route and driving time', [
     'The main road runs over the Khanh Le Pass (route 27C): about 135 km and 3–3.5 hours. The first half is flat, then the road climbs almost 1,500 m in switchbacks with views over jungle and clouds. Leave in the morning — fog often comes in the mountains by evening.',
    ]),
    ('Which car to choose', [
     'A crossover with good clearance is most comfortable on the mountain road: the Hyundai Creta or Mitsubishi Xforce. Families can take the 7-seat Toyota Rush or Veloz. With an EV, plan a charging stop.',
    ]),
    ('Rental terms for the trip', [
     'Trips outside Khanh Hoa province need the $400 deposit: $200 back on return, the other $200 after a month. The 250 km per day limit adds up over the rental, so a round trip (about 270 km) over two days fits within it.',
    ]),
   ],
   'faq': [
    ('How far is Da Lat from Nha Trang?', 'About 135 km via the Khanh Le Pass.'),
    ('How long is the drive?', '3–3.5 hours including the switchbacks, longer with stops.'),
    ('What deposit do I need for Da Lat?', '$400 — for trips outside Khanh Hoa province.'),
   ],
  },
 },
 {
  'id': 'licence',
  'cars': ['vf3', 'soluto', 'xpander', 'creta'],
  'ru': {
   'slug': 'prava-dlya-arendy-avto-vo-vetname',
   'link': 'Какие права нужны во Вьетнаме',
   'title': 'Какие права нужны для аренды авто во Вьетнаме в 2026 году | VietAvto',
   'desc': 'Можно ли водить во Вьетнаме по российским правам, нужно ли международное водительское удостоверение и какие документы нужны для аренды авто в Нячанге.',
   'kw': 'права во Вьетнаме, международные права Вьетнам, МВУ Вьетнам, можно ли водить во Вьетнаме по российским правам, документы для аренды авто Вьетнам, аренда авто Вьетнам права',
   'h1': 'Какие права нужны для аренды авто во Вьетнаме',
   'lead': 'Главный вопрос перед арендой машины во Вьетнаме — документы. Коротко: нужны паспорт, национальные права и международное водительское удостоверение (МВУ) образца Венской конвенции 1968 года.',
   'sections': [
    ('Международные права (МВУ)', [
     'Вьетнам признаёт международные водительские удостоверения по Венской конвенции о дорожном движении 1968 года. Россия, Беларусь, Казахстан и большинство стран Европы — участники этой конвенции, поэтому российское МВУ во Вьетнаме действует вместе с национальными правами.',
     'МВУ оформляется в России в Госавтоинспекции (через Госуслуги) до поездки. Во Вьетнаме его получить нельзя.',
    ]),
    ('Что нужно для договора аренды', [
     'Паспорт, национальное водительское удостоверение и МВУ. Оплата аренды — после подписания договора и осмотра машины, депозит — $200 или $400 в зависимости от маршрута.',
    ]),
    ('Правила на дороге', [
     'Движение правостороннее. Соблюдайте скоростной режим и сигналы светофора, паркуйтесь только в разрешённых местах и не садитесь за руль после алкоголя — во Вьетнаме к этому очень строгое отношение. Штрафы с камер приходят владельцу машины и удерживаются из депозита.',
    ]),
   ],
   'faq': [
    ('Можно ли водить во Вьетнаме только по российским правам?', 'Нет, вместе с национальными правами нужно международное водительское удостоверение (МВУ).'),
    ('Где получить МВУ?', 'В России, в Госавтоинспекции или через Госуслуги, до поездки.'),
    ('Какие документы нужны для аренды у VietAvto?', 'Паспорт, МВУ и национальные права.'),
   ],
  },
  'en': {
   'slug': 'driving-licence-vietnam-car-rental',
   'link': 'Driving licence rules in Vietnam',
   'title': 'Driving Licence for Car Rental in Vietnam: IDP Rules for Tourists (2026) | VietAvto',
   'desc': 'Can foreigners drive in Vietnam? Which International Driving Permit is valid (1968 Vienna Convention), what US and UK drivers need to know, and what documents you need to rent a car in Nha Trang.',
   'kw': 'Vietnam driving licence tourist, international driving permit Vietnam, IDP Vietnam 1968, can Americans drive in Vietnam, US driver license Vietnam, documents to rent a car in Vietnam',
   'h1': 'Driving Licence Rules for Renting a Car in Vietnam',
   'lead': 'Documents are the key question before renting a car in Vietnam. In short: you need your passport, your national licence and an International Driving Permit (IDP) issued under the 1968 Vienna Convention.',
   'sections': [
    ('Which IDP is valid in Vietnam', [
     'Vietnam recognises International Driving Permits issued under the 1968 Vienna Convention on Road Traffic. Most European countries, the UK, Russia and many others issue 1968-format IDPs, which are valid in Vietnam together with your national licence.',
     'Important for US drivers: the United States issues IDPs under the 1949 Geneva Convention, which Vietnam does not recognise. Americans usually need to convert their licence into a Vietnamese one to drive legally — check your situation before you travel.',
    ]),
    ('What you need for the rental agreement', [
     'Your passport, national driving licence and a valid IDP. You pay after signing the agreement and inspecting the car; the deposit is $200 or $400 depending on your route.',
    ]),
    ('On the road', [
     'Traffic drives on the right. Keep to speed limits and traffic lights, park only where allowed and never drink and drive — Vietnam is very strict about it. Camera fines reach the car owner and are taken from the deposit.',
    ]),
   ],
   'faq': [
    ('Can I drive in Vietnam with only my home licence?', 'No, you also need an International Driving Permit (1968 Vienna Convention format) or a Vietnamese licence.'),
    ('Is a US International Driving Permit valid in Vietnam?', 'US IDPs follow the 1949 Geneva Convention, which Vietnam does not recognise, so US drivers usually need a Vietnamese licence.'),
    ('What documents does VietAvto need?', 'Your passport, IDP and national driving licence.'),
   ],
  },
 },
 {
  'id': 'suv',
  'cars': ['creta', 'xforce', 'vf5', 'rush'],
  'ru': {
   'slug': 'arenda-krossovera-nyachang',
   'link': 'Аренда кроссовера и SUV',
   'title': 'Аренда кроссовера и SUV в Нячанге — Hyundai Creta, Xforce, Toyota Rush | VietAvto',
   'desc': 'Аренда кроссовера в Нячанге без водителя: Hyundai Creta, Mitsubishi Xforce 2024, VinFast VF5, 7-местный Toyota Rush. От 800 000 ₫ в сутки. Высокая посадка для поездок к водопадам и в Далат.',
   'kw': 'аренда кроссовера Нячанг, аренда SUV Нячанг, аренда внедорожника Нячанг, аренда Hyundai Creta Нячанг, аренда Mitsubishi Xforce, аренда Toyota Rush Нячанг',
   'h1': 'Аренда кроссовера и SUV в Нячанге',
   'lead': 'Кроссовер — самый универсальный выбор для Кхань Хоа: удобен в городе и уверенно чувствует себя на горных и разбитых дорогах к водопадам, пляжам и в Далат.',
   'sections': [
    ('Какие кроссоверы есть в парке', [
     'Hyundai Creta — компактный кроссовер с современными ассистентами и высокой посадкой. Mitsubishi Xforce 2024 года — один из самых новых автомобилей в парке. VinFast VF5 — электрокроссовер с запасом хода около 300 км. Toyota Rush — 7-местный внедорожник для семьи или компании.',
    ]),
    ('Зачем кроссовер в Нячанге', [
     'Дороги к водопадам Ба Хо и Янг Бей, на перевал Кхань Ле и к дальним пляжам бывают узкими и неровными. Высокий клиренс и посадка дают больше уверенности, а вместительный багажник — место для вещей на несколько дней поездки.',
    ]),
    ('Цены и условия', [
     'От 800 000 ₫ в сутки за VinFast VF5 до 1 150 000 ₫ за Creta и Xforce. Депозит $200 по провинции и $400 для поездок по всему Вьетнаму, лимит 250 км в сутки суммируется за весь срок.',
    ]),
   ],
   'faq': [
    ('Какой кроссовер самый новый?', 'Mitsubishi Xforce 2024 года.'),
    ('Есть ли 7-местный внедорожник?', 'Да, Toyota Rush на 7 мест.'),
    ('Подойдёт ли кроссовер для поездки в Далат?', 'Да, это лучший выбор для горной дороги через перевал Кхань Ле.'),
   ],
  },
  'en': {
   'slug': 'suv-crossover-rental-nha-trang',
   'link': 'SUV & crossover rental',
   'title': 'SUV & Crossover Rental in Nha Trang — Hyundai Creta, Xforce, Toyota Rush | VietAvto',
   'desc': 'Self-drive SUV and crossover rental in Nha Trang: Hyundai Creta, 2024 Mitsubishi Xforce, VinFast VF5, 7-seat Toyota Rush. From 800,000 ₫ a day. High clearance for waterfalls and Da Lat trips.',
   'kw': 'SUV rental Nha Trang, crossover rental Nha Trang, Hyundai Creta rental, Mitsubishi Xforce rental, Toyota Rush rental Nha Trang, 4x4 rental Vietnam',
   'h1': 'SUV & Crossover Rental in Nha Trang',
   'lead': 'A crossover is the most versatile choice in Khanh Hoa: easy in town and confident on mountain and rough roads to waterfalls, beaches and Da Lat.',
   'sections': [
    ('Crossovers in our fleet', [
     'The Hyundai Creta is a compact crossover with modern driver aids and a high seating position. The 2024 Mitsubishi Xforce is one of the newest cars in the fleet. The VinFast VF5 is an electric crossover with about 300 km of range. The Toyota Rush is a 7-seat SUV for families and groups.',
    ]),
    ('Why a crossover in Nha Trang', [
     'Roads to Ba Ho and Yang Bay waterfalls, over the Khanh Le Pass and to remote beaches can be narrow and uneven. Higher clearance and seating give more confidence, and the larger boot fits luggage for a multi-day trip.',
    ]),
    ('Prices and terms', [
     'From 800,000 ₫ a day for the VinFast VF5 to 1,150,000 ₫ for the Creta and Xforce. $200 deposit within the province and $400 for trips across Vietnam; the 250 km per day limit adds up over the rental.',
    ]),
   ],
   'faq': [
    ('Which crossover is the newest?', 'The 2024 Mitsubishi Xforce.'),
    ('Do you have a 7-seat SUV?', 'Yes, the 7-seat Toyota Rush.'),
    ('Is a crossover good for Da Lat?', 'Yes, it is the best choice for the mountain road over the Khanh Le Pass.'),
   ],
  },
 },
 {
  'id': 'sedan',
  'cars': ['soluto', 'mazda3', 'luxa'],
  'ru': {
   'slug': 'arenda-sedana-nyachang',
   'link': 'Аренда седана в Нячанге',
   'title': 'Аренда седана в Нячанге — Kia Soluto, Mazda3, VinFast Lux A2.0 | VietAvto',
   'desc': 'Аренда седана в Нячанге без водителя: экономичный Kia Soluto и Mazda3 от 900 000 ₫ в сутки, бизнес-седан VinFast Lux A2.0 за 1 200 000 ₫. Для пары, города и поездок к морю.',
   'kw': 'аренда седана Нячанг, аренда легкового авто Нячанг, аренда Kia Soluto Нячанг, аренда Mazda3 Нячанг, аренда бизнес седана Нячанг, аренда VinFast Lux A2.0',
   'h1': 'Аренда седана в Нячанге',
   'lead': 'Седан — удобный и экономичный вариант для пары или небольшой семьи: мягко едет по трассе вдоль побережья, легко паркуется у пляжей и расходует мало топлива.',
   'sections': [
    ('Седаны в нашем парке', [
     'Kia Soluto — простой и экономичный седан 1.4 л, самый доступный бензиновый автомобиль в парке. Mazda3 — компактный седан с плотной подвеской и точным рулём, в котором поездка вдоль моря превращается в удовольствие. VinFast Lux A2.0 — флагманский бизнес-седан на платформе BMW 5-й серии с двигателем 2.0 турбо.',
    ]),
    ('Кому подходит седан', [
     'Паре или семье из трёх человек, которые ездят по Нячангу, к пляжам Зоклет и Бай Дай. Для деловой встречи или особого случая — VinFast Lux A2.0.',
    ]),
    ('Цены', [
     'Kia Soluto и Mazda3 — 900 000 ₫ в сутки, VinFast Lux A2.0 — 1 200 000 ₫. На месяц и дольше — отдельная, более выгодная ставка.',
    ]),
   ],
   'faq': [
    ('Какой седан самый экономичный?', 'Kia Soluto с двигателем 1.4 л — 900 000 ₫ в сутки.'),
    ('Есть ли бизнес-седан?', 'Да, VinFast Lux A2.0 на платформе BMW 5-й серии.'),
    ('Поместятся ли чемоданы?', 'Да, два больших чемодана помещаются в багажник седана.'),
   ],
  },
  'en': {
   'slug': 'sedan-rental-nha-trang',
   'link': 'Sedan rental in Nha Trang',
   'title': 'Sedan Rental in Nha Trang — Kia Soluto, Mazda3, VinFast Lux A2.0 | VietAvto',
   'desc': 'Self-drive sedan rental in Nha Trang: economical Kia Soluto and Mazda3 from 900,000 ₫ a day, VinFast Lux A2.0 executive sedan at 1,200,000 ₫. For couples, city driving and beach trips.',
   'kw': 'sedan rental Nha Trang, car hire Nha Trang sedan, Kia Soluto rental, Mazda3 rental Nha Trang, executive car rental Nha Trang, VinFast Lux A2.0 rental',
   'h1': 'Sedan Rental in Nha Trang',
   'lead': 'A sedan is a comfortable, economical choice for a couple or small family: smooth on the coastal highway, easy to park at the beach and light on fuel.',
   'sections': [
    ('Sedans in our fleet', [
     'The Kia Soluto is a simple, economical 1.4 L sedan — the most affordable petrol car in the fleet. The Mazda3 is a compact sedan with firm suspension and precise steering that makes the coastal road a pleasure. The VinFast Lux A2.0 is a flagship executive sedan on the BMW 5 Series platform with a 2.0 turbo engine.',
    ]),
    ('Who a sedan suits', [
     'Couples or a family of three driving around Nha Trang, to Doc Let and Bai Dai beaches. For a business meeting or a special occasion — the VinFast Lux A2.0.',
    ]),
    ('Prices', [
     'Kia Soluto and Mazda3 — 900,000 ₫ a day, VinFast Lux A2.0 — 1,200,000 ₫. A month or longer gets a separate, better rate.',
    ]),
   ],
   'faq': [
    ('Which sedan is the most economical?', 'The 1.4 L Kia Soluto — 900,000 ₫ a day.'),
    ('Do you have an executive sedan?', 'Yes, the VinFast Lux A2.0 on the BMW 5 Series platform.'),
    ('Will suitcases fit?', 'Yes, two large suitcases fit in a sedan boot.'),
   ],
  },
 },
 {
  'id': 'where',
  'cars': ['vf3', 'soluto', 'xpander', 'creta'],
  'ru': {
   'slug': 'gde-snyat-avtomobil-v-nyachange',
   'link': 'Где снять автомобиль в Нячанге',
   'title': 'Где снять автомобиль в Нячанге: авто в аренду напрямую, без посредников | VietAvto',
   'desc': 'Где снять автомобиль в аренду в Нячанге: агрегаторы, прокатные конторы или владелец парка — плюсы и минусы. Авто в аренду напрямую от 700 000 ₫ в сутки.',
   'kw': 'где снять автомобиль в Нячанге, авто в аренду Нячанг, автомобиль в аренду Нячанг, снять машину Нячанг, взять машину в аренду Нячанг, где арендовать авто в Нячанге, машина напрокат Нячанг',
   'h1': 'Где снять автомобиль в Нячанге',
   'lead': 'Снять машину в Нячанге можно тремя способами: через агрегатор, в прокатной конторе или напрямую у владельца автопарка. Разберём, чем они отличаются, и как взять авто в аренду без переплат.',
   'sections': [
    ('Агрегаторы', [
     'Сайты-агрегаторы собирают предложения разных прокатов. Удобно сравнить цены, но вы платите комиссию сервиса, а машина и условия зависят от конкретного прокатчика, с которым вы общаетесь уже после оплаты.',
    ]),
    ('Прокатные конторы у пляжа', [
     'В туристических районах много небольших прокатов. Можно посмотреть машину вживую, но цены и условия часто устные, а депозит и правила возврата стоит уточнять заранее.',
    ]),
    ('Напрямую у владельца — VietAvto', [
     'Мы сдаём автомобили в аренду из собственного парка: VinFast, Toyota, Mitsubishi, Hyundai, Kia. Без посредников и комиссий, с реальными фото каждой машины и понятными условиями — депозит $200 или $400, 250 км в сутки с суммированием, возврат «бак в бак». Цена авто в аренду — от 700 000 ₫ в сутки.',
     'Заявку можно оставить на сайте или сразу написать в WhatsApp или Telegram.',
    ]),
   ],
   'faq': [
    ('Где лучше снять автомобиль в Нячанге?', 'Выгоднее всего — напрямую у владельца парка: без комиссии агрегатора и с понятными условиями заранее.'),
    ('Сколько стоит авто в аренду в Нячанге?', 'От 700 000 ₫ в сутки за VinFast VF3; седаны — от 900 000 ₫, 7-местные — от 1 000 000 ₫.'),
    ('Можно продлить аренду?', 'Да, напишите нам заранее, до окончания срока аренды.'),
   ],
  },
  'en': {
   'slug': 'where-to-rent-a-car-in-nha-trang',
   'link': 'Where to rent a car in Nha Trang',
   'title': 'Where to Rent a Car in Nha Trang: Direct Car Hire, No Middlemen | VietAvto',
   'desc': 'Where to rent a car in Nha Trang: aggregators, local rental shops or a fleet owner — pros and cons. Cars for rent directly from 700,000 ₫ a day.',
   'kw': 'where to rent a car in Nha Trang, car for rent Nha Trang, rent car Nha Trang, Nha Trang car hire, hire a car Nha Trang, rental cars Nha Trang, best car rental Nha Trang',
   'h1': 'Where to Rent a Car in Nha Trang',
   'lead': 'There are three ways to rent a car in Nha Trang: an online aggregator, a local rental shop, or directly from a fleet owner. Here is how they differ and how to hire a car without overpaying.',
   'sections': [
    ('Aggregators', [
     'Aggregator sites list offers from many rental companies. Comparing prices is easy, but you pay the platform’s commission, and the car and terms depend on a local company you only deal with after paying.',
    ]),
    ('Local rental shops', [
     'Tourist areas have plenty of small rental shops. You can see the car in person, but prices and terms are often verbal, so check the deposit and return rules upfront.',
    ]),
    ('Directly from the owner — VietAvto', [
     'We rent cars from our own fleet: VinFast, Toyota, Mitsubishi, Hyundai and Kia. No middlemen and no commission, real photos of every car and clear terms — a $200 or $400 deposit, 250 km per day added up over the rental, same-fuel-level return. Cars for rent from 700,000 ₫ a day.',
     'Send a request on the site or message us on WhatsApp or Telegram.',
    ]),
   ],
   'faq': [
    ('What is the best way to rent a car in Nha Trang?', 'Renting directly from a fleet owner is usually cheapest: no aggregator fee and clear terms upfront.'),
    ('How much does a rental car cost in Nha Trang?', 'From 700,000 ₫ a day for the VinFast VF3; sedans from 900,000 ₫, 7-seaters from 1,000,000 ₫.'),
    ('Can I extend the rental?', 'Yes, just message us before the rental ends.'),
   ],
  },
 },
 {
  'id': 'fuel',
  'cars': ['vf3', 'vf5', 'soluto', 'xpander'],
  'maps': [('gas', '!1m2!2m1!1zY8OieSB4xINuZyBOaGEgVHJhbmc', 'c%C3%A2y+x%C4%83ng+Nha+Trang'), ('ev', '!1m2!2m1!1zdHLhuqFtIHPhuqFjIFZpbkZhc3QgTmhhIFRyYW5n', 'tr%E1%BA%A1m+s%E1%BA%A1c+VinFast+Nha+Trang')],
  'ru': {
   'slug': 'zapravki-i-elektrozaryadki-nyachang',
   'link': 'Карта заправок и электрозарядок',
   'title': 'Заправки и зарядки для электромобилей в Нячанге — карта АЗС и VinFast | VietAvto',
   'desc': 'Карта всех заправок (АЗС) и зарядных станций VinFast в Нячанге. Какой бензин заливать, как заправляют во Вьетнаме и как зарядить электромобиль VF3 или VF5.',
   'kw': 'заправки Нячанг, АЗС Нячанг карта, зарядка электромобиля Нячанг, зарядные станции VinFast Нячанг, где заправиться в Нячанге, бензин во Вьетнаме',
   'h1': 'Заправки и электрозарядки в Нячанге',
   'lead': 'Карты всех АЗС и зарядных станций VinFast в Нячанге и окрестностях — чтобы быстро заправить машину или зарядить электромобиль.',
   'map_titles': {'gas': 'Заправки (АЗС) в Нячанге', 'ev': 'Зарядные станции VinFast в Нячанге'},
   'open_map': 'Открыть в Google Картах',
   'sections': [
    ('Как заправляться во Вьетнаме', [
     'На заправках во Вьетнаме обычно работает заправщик: назовите тип топлива и сумму или скажите «full» — полный бак. Самые распространённые сети — Petrolimex и PVOIL. Оплата наличными, на многих станциях — картой или по QR-коду.',
     'Для большинства бензиновых машин подходит RON95 (A95) — точный тип обычно указан на крышке бака. Не забудьте: машину возвращаете с тем же уровнем топлива, что при получении.',
    ]),
    ('Как зарядить электромобиль VinFast', [
     'У VinFast своя сеть зарядных станций — на парковках торговых центров, отелей и у заправок, в Нячанге и вдоль трасс. Зарядка бесплатная — вы платите только за аренду машины. VF3 проходит около 210 км на одной зарядке, VF5 — около 300 км.',
    ]),
   ],
   'faq': [
    ('Какой бензин заливать?', 'Обычно RON95 (A95) — точный тип указан на крышке бензобака.'),
    ('Где зарядить VinFast VF3 или VF5?', 'На зарядных станциях VinFast — они отмечены на карте выше.'),
    ('Нужно ли платить за зарядку?', 'Нет, зарядка бесплатная — вы платите только за аренду машины.'),
    ('Можно ли расплатиться картой на заправке?', 'На многих станциях — да, но лучше иметь с собой наличные донги.'),
   ],
  },
  'en': {
   'slug': 'gas-stations-ev-charging-nha-trang',
   'link': 'Gas stations & EV chargers map',
   'title': 'Gas Stations & EV Charging in Nha Trang — Map of Fuel and VinFast Chargers | VietAvto',
   'desc': 'Map of all gas stations and VinFast charging stations in Nha Trang. Which fuel to use, how refuelling works in Vietnam and how to charge a VF3 or VF5.',
   'kw': 'gas station Nha Trang, petrol station Nha Trang map, EV charging Nha Trang, VinFast charging station Nha Trang, refuel in Vietnam',
   'h1': 'Gas Stations & EV Charging in Nha Trang',
   'lead': 'Maps of every gas station and VinFast charging station in and around Nha Trang — to refuel quickly or charge your EV.',
   'map_titles': {'gas': 'Gas stations in Nha Trang', 'ev': 'VinFast charging stations in Nha Trang'},
   'open_map': 'Open in Google Maps',
   'sections': [
    ('How refuelling works in Vietnam', [
     'Most gas stations in Vietnam have an attendant: tell them the fuel type and the amount, or say “full”. The main chains are Petrolimex and PVOIL. You pay in cash, and many stations also take cards or QR payments.',
     'Most petrol cars take RON95 (A95) — the exact type is usually marked on the fuel cap. Remember to return the car with the same fuel level you received.',
    ]),
    ('How to charge a VinFast EV', [
     'VinFast runs its own charging network — at malls, hotels and petrol stations in Nha Trang and along the highways. Charging is free — you only pay for the rental. The VF3 covers about 210 km per charge, the VF5 about 300 km.',
    ]),
   ],
   'faq': [
    ('Which fuel should I use?', 'Usually RON95 (A95) — the exact type is marked on the fuel cap.'),
    ('Where can I charge a VinFast VF3 or VF5?', 'At VinFast charging stations — they are shown on the map above.'),
    ('Do I pay for charging?', 'No, charging is free — you only pay for the rental.'),
    ('Can I pay by card at gas stations?', 'At many stations yes, but it is best to carry some cash in dong.'),
   ],
  },
 },
]
