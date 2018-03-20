from argparse import ArgumentParser
from tbselenium.tbdriver import TorBrowserDriver


def print_cookies(tbb_dir, url):
    with TorBrowserDriver(tbb_dir) as driver:
        driver.load_url(url)
        print "Finished loading", url
        print "Cookies:", driver.execute_script("return document.cookie;")


def main():
    desc = "Print cookies on a given URL"
    nyt_hs_url = "https://www.nytimes3xbfgragh.onion/"  # NYT Hidden Service
    parser = ArgumentParser(description=desc)
    parser.add_argument('tbb_path')
    parser.add_argument('url', default=nyt_hs_url)
    args = parser.parse_args()
    print_cookies(args.tbb_path, args.url)


if __name__ == '__main__':
    main()
