import Functions
import Analysis

def main():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    # Funkcja pobierająca dane i analizująca dla wybranej kryptowaluty
    def analyze_crypto(crypto):
        url = Functions.construct_download_url(crypto, '2022-11-27', '2023-11-27', 'weekly') #ostatni parametr moze być weekly
        data = Functions.scrape_yahoo_finance_data(url, headers)
        print(f'Analiza danych dla {crypto}:\n{data}')
        Analysis.plot_candlestick_chart(data,crypto)
        Analysis.calculate_greed_fear_index(data)
        Analysis.train_linear_regression_model(data,crypto) 
        Analysis.changing_format(data)
        Analysis.endoftheday_data_weekly(data, crypto)
        Analysis.endoftheday_vs_beginningoftheday_data_weekly(data,crypto)
       

    # Przykładowa analiza dla Ethereum
    analyze_crypto('ETH')
    analyze_crypto('BTC')
    analyze_crypto('BNB')
    analyze_crypto('SOL')
    Analysis.profit4Crypto()


if __name__ == "__main__":
    main()
