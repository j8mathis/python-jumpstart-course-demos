import requests
import bs4
import collections

WeatherReport = collections.namedtuple('WeatherReport',('cond, temp, scale, loc'))

def main():
    print_header()
    code = input('What zipcode do you want weather for? (80301)')
    html = get_html_from_web(code)
    report = get_weather_from_html(html)
    print(f'The weather in {report.loc} is {report.temp} {report.scale} and {report.cond}')


def print_header():
    print('-----------------------------')
    print('        WEATHER APP')
    print('-----------------------------')
    print()


def get_html_from_web(zipcode):
    url = f'https://www.wunderground.com/weather-forecast/{zipcode}'
    response = requests.get(url)
    return response.text


def get_weather_from_html(html):
    soup = bs4.BeautifulSoup(html, "html.parser")
    loc = soup.find(class_='region-content-header').find('h1').get_text()
    condition = soup.find(class_='condition-icon').get_text()
    temp = soup.find(class_='wu-unit-temperature').find(class_='wu-value').get_text()
    scale = soup.find(class_='wu-unit-temperature').find(class_='wu-label').get_text()

    loc = clean_up_text(loc)
    loc = find_city_state(loc)
    condition = clean_up_text(condition)
    temp = clean_up_text(temp)
    scale = clean_up_text(scale)

    report = WeatherReport(loc=loc, cond=condition,temp=temp,scale=scale)
    return report


def find_city_state(text: str):
    parts = text.split('\n')
    return parts[0]


def clean_up_text(text: str):
    if not text:
        return text

    text = text.strip()
    return (text)


if __name__ == '__main__':
    main()
