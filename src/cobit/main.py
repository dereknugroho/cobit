from cobit.kraken.kraken_services import server_time, order_book, recent_trades, recent_spreads

if __name__ == '__main__':
    # server_time = server_time()
    # print(f'---------------')
    # print(f'| Server Time |')
    # print(f'---------------')
    # print(f'{server_time}')

    # order_book = order_book()
    # print(f'--------------')
    # print(f'| Order Book |')
    # print(f'--------------')
    # print(f'{order_book}')

    # recent_spreads = recent_spreads()
    # print(f'------------------')
    # print(f'| Recent Spreads |')
    # print(f'------------------')
    # print(f'{recent_spreads}')

    recent_trades = recent_trades()
    print(f'-----------------')
    print(f'| Recent Trades |')
    print(f'-----------------')
    print(f'{recent_trades}')