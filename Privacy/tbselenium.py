from tbselenium.tbdriver import TorBrowserDriver
TBB_PATH = "/path/to/tbb/7.0.8/tor-browser_en-US/"


def main():
    with TorBrowserDriver(TBB_PATH) as driver:
        driver.get('https://check.torproject.org')


if __name__ == '__main__':
    main()
