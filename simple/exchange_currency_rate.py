import requests


class RateCurrency:
    """
    A small class for obtaining data on exchange boats

    Attributes
    ----------
    Format ->
        Full:
            {'CharCode': 'EUR',
             'ID': 'R01239',
             'Name': 'Евро',
             'Nominal': 1,
             'NumCode': '978',
             'Previous': 59.9756,
             'Value': 60.8019}
        Short:
            60.8019

    CurrencyCode ->
        'USD', 'EUR' etc.

    Methods
    -------
    get_currency_data(currency: CurrencyCode) -> str
        return data string from service
    usd()
        short for 'get_currency_data(RateCurrency.CurrencyCode.USD)' or 'get_currency_data("USD")'
    """

    class Format:
        """Response format

        Parameters
        ----------
        """
        full = "Full"
        short = "Short"

    class CurrencyCode:
        """Short currency name

        Parameters
        ----------
        """
        USD = "USD"
        EUR = "EUR"
        AZN = "AZN"

    def __init__(self, response_format: Format = Format.short):
        self.__url = "https://www.cbr-xml-daily.ru/daily_json.js"
        self.__response_format = response_format

    @property
    def response_format(self):
        return self.__response_format

    @response_format.setter
    def response_format(self, new_format: Format):
        self.__response_format = new_format

    def _exchange_rates(self):
        request_obj = requests.get(self.__url)
        return request_obj.json()["Valute"]

    def _get_full_currency_data(self, currency: CurrencyCode):
        response = self._exchange_rates()
        if currency in response:
            return response[currency]
        else:
            raise ValueError(f"No currency with name '{currency}'")

    def get_currency_with_format(self, currency: CurrencyCode) -> str:
        data = self._get_full_currency_data(currency)
        if self.__response_format == RateCurrency.Format.full:
            return data
        if self.__response_format == RateCurrency.Format.short:
            return data["Value"]

    def usd(self):
        """Return value for 'USD'"""
        return self.get_currency_with_format(RateCurrency.CurrencyCode.USD)

    # def __del__(self):
    #     # close file and connections


class NestRate(RateCurrency):
    def __init__(self):
        super(NestRate, self).__init__(response_format=RateCurrency.Format.full)

    def get_currency_id(self, currency: RateCurrency.CurrencyCode) -> str:
        return self._get_full_currency_data(currency)["ID"]


if __name__ == '__main__':
    from pprint import pprint

    r = RateCurrency()
    # print(RateCurrency.__doc__)
    # print(r.response_format)
    # pprint(r.get_currency_data("USD"))
    # r.response_format = RateCurrency.Format.full
    print(r.response_format)
    pprint(r.get_currency_with_format(RateCurrency.CurrencyCode.EUR))

    nr = NestRate()
    print(NestRate.__doc__)
    print(nr.response_format)
    pprint(nr.get_currency_with_format(RateCurrency.CurrencyCode.EUR))
    pprint(nr.get_currency_id("USD"))
