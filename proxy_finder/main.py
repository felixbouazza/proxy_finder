from proxy_list_finder import FreeProxyLists

if __name__ == "__main__":
    free_proxy_lists = FreeProxyLists(url="https://www.freeproxylists.net/fr/")
    proxies = free_proxy_lists.get_proxies()