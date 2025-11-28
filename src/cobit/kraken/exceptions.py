class KrakenAPIError(Exception):
    def __init__(self, errors, *args):
        super().__init__(*args)
        self.errors = errors

    def __str__(self):
        return f'Kraken API error(s): {self.errors}'
