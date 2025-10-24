import asyncio
from playwright.async_api import async_playwright

async def analyze_cookies(url):
    async with async_playwright() as p:
        # запускаем браузер
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()

        page = await context.new_page()
        
        # переходим на сайт
        await page.goto(url)
        
        # ждем загрузки и возможной установки cookie
        await page.wait_for_timeout(5000)
        
        # получаем все cookie
        cookies = await context.cookies()
        
        print(f" Анализ cookie для: {url}")
        
        # анализируем cookie
        first_party_cookies = []
        third_party_cookies = []
        
        for cookie in cookies:
            cookie_info = {
                'name': cookie['name'],
                'domain': cookie['domain'],
                'value_length': len(cookie['value']),
                'secure': cookie.get('secure', False),
                'http_only': cookie.get('httpOnly', False),
                'session': 'session' if cookie.get('expires', 0) == -1 else 'persistent'
            }
            
            # определяем тип куки
            if url.replace('https://', '').replace('http://', '').split('/')[0] in cookie['domain']:
                first_party_cookies.append(cookie_info)
            else:
                third_party_cookies.append(cookie_info)
        
        # результаты
        print(f" Собственные cookies ({len(first_party_cookies)}):")
        for cookie in first_party_cookies:
            print(f"   • {cookie['name']} | {cookie['domain']} | {cookie['session']}")
        
        print(f"\n Сторонние cookies ({len(third_party_cookies)}):")
        for cookie in third_party_cookies:
            print(f"   • {cookie['name']} | {cookie['domain']} | {cookie['session']}")

        print(f"\nИнсайты для рекомендательных систем:")
        print(f"   - Всего идентификаторов: {len(cookies)}")
        print(f"   - Собственные для трекинга поведения: {len(first_party_cookies)}")
        print(f"   - Сторонние для кросс-сайтового трекинга: {len(third_party_cookies)}")
        
        await browser.close()

async def monitor_cookie_changes(url):
    """
    Мониторинг изменений cookie во время сессии
    """
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()
        
        # отслеживание изменений
        cookie_changes = []
        
        def on_cookie_changed(cookie):
            cookie_changes.append({
                'action': 'changed' if any(c['name'] == cookie['name'] for c in cookie_changes) else 'added',
                'name': cookie['name'],
                'domain': cookie['domain'],
                'timestamp': asyncio.get_event_loop().time()
            })
        
        # подписываемся на изменения cookie
        context.on("cookie", on_cookie_changed)
        
        # выполняем действия на странице
        await page.goto(url)
        await page.wait_for_timeout(3000)
        
        # эмулируем пользовательские действия
        await page.click('body')  # простой клик
        await page.wait_for_timeout(2000)
        
        print(f"\n Изменения cookie во время сессии:")
        for change in cookie_changes:
            print(f"   • {change['action'].upper()}: {change['name']} ({change['domain']})")
        
        await browser.close()


websites = [
        "https://www.yandex.ru",
        "https://www.avito.ru/", 
        "https://ods.ai/competitions"
]
    
for site in websites:
    asyncio.run(analyze_cookies(site))
    print('\n')
        