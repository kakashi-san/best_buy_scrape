from modules.page_sourcer import ChromePageSourcer, RequestsPageSourcer
from modules.url_handler import generate_url_from_config
from pathlib import Path
import time
from modules.utils import read_config_yaml


config_yaml_path = Path('./modules/config.yaml')
config = read_config_yaml(config_yaml_path=config_yaml_path)

webdriver_path = Path(config['DRIVER_OPTIONS']['webdriver']['chrome_driver_path'])
requests_args = config['DRIVER_OPTIONS']['requests']['args']

if __name__ == "__main__":
    url = generate_url_from_config(
        config_yaml_path=config_yaml_path
    )
    print(url)

    requests_page_sourcer = RequestsPageSourcer(
        page_url=url,
        **requests_args
    )
    print(requests_page_sourcer.get_page_source())


    # PageSourcer = ChromePageSourcer(
    #     page_url=url,
    #     webdriver_path=webdriver_path
    # )

    # page_source = PageSourcer.get_page_source()

    # page_soup = BeautifulSoup(page_source)

    # time.sleep(30)