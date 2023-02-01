from typing import Optional, List, Dict

from hathor_wallet.exception import HathorWalletError

import requests
from urllib import parse


class HathorWallet:
    '''
    The HathorWallet class provides an interface for communicating with the 
    Hathor Network's wallet API.

    Attributes:
    configs (dict): Dictionary containing configurations for the API request, 
    such as headers and data.

    Methods:
    start(): Start the Hathor wallet.
    status(): Get the current status of the Hathor wallet.
    balance(): Get the current balance of the Hathor wallet.
    stop(): Stop the Hathor wallet.
    current_address(mark_as_used: Optional[str]=None): Get the current address of the Hathor wallet. 
    Optionally mark it as used.
    all_generated_addresses(): Get a list of all generated addresses for the Hathor wallet.
    simple_send_tx(address: str, 
                    value: int, 
                    token: Optional[str]=None, 
                    change_address: Optional[str]=None
                ): Send a transaction from the Hathor wallet.
    tx_history(limit: int=None): Get the transaction history of the Hathor wallet. 
    Optionally limit the number of transactions.

    Exceptions:
    HathorWalletError: Raised when an error occurs during an API request.
    '''

    def __init__(
        self,
        **configs
        ):
        self.configs: dict = configs

    def start(self) -> Dict[str, bool]:
        try:
            url = parse.urljoin(self.configs.get('wallet_base_url'), '/start')
            response = requests.post(url=url, headers=self.configs.get('headers'), data=self.configs.get('data'))
            
            if response.status_code != 200:
                raise HathorWalletError('Erro stating wallet.')

            from time import sleep
            sleep(5)
            
            return response.json()

        except:
            raise HathorWalletError('Error in the request.')

    def status(self) -> Dict[str, dict]:
        try:
            url = parse.urljoin(self.configs.get('wallet_base_url'), '/wallet/status')
            response = requests.get(url=url, headers=self.configs.get('headers'), data=self.configs.get('data'))
            
            if response.status_code != 200:
                raise HathorWalletError('Error getting wallet status.')

            return response.json()
        except:
            raise HathorWalletError('Error in the request.')

    def balance(self) -> Dict:
        # Not implemented other UID.
        try:
            url = parse.urljoin(self.configs.get('wallet_base_url'), '/wallet/balance')
            response = requests.get(url=url, headers=self.configs.get('headers'))
            
            if response.status_code != 200:
                raise HathorWalletError('Error getting wallet balance.')

            return response.json()

        except:
            raise HathorWalletError('Error in the request.')
            
    def stop(self) -> Dict[str, bool]:
        try:
            url = parse.urljoin(self.configs.get('wallet_base_url'), '/wallet/stop')
            response = requests.post(url=url, headers=self.configs.get('headers'))
            
            if response.status_code != 200:
                raise HathorWalletError('Error stop wallet.')

            return response.json()
            
        except:
            raise HathorWalletError('Error in the request.')

    def current_address(self, mark_as_used: Optional[str] = None) -> str:
        params: Optional[Dict[str, str]] = None

        if mark_as_used:
            params = {'mark_as_used': mark_as_used}

        try:
            url = parse.urljoin(self.configs.get('wallet_base_url'), '/wallet/address')
            response = requests.get(url=url, headers=self.configs.get('headers'), params=params)
            
            if response.status_code != 200:
                raise HathorWalletError(f'Error return the current address')

            return response.json()
            
        except:
            raise HathorWalletError('Error in the request.')

    def all_generated_addres(self) -> Dict[str, List]:
        try:
            url = parse.urljoin(self.configs.get('wallet_base_url'), '/wallet/addresses')
            response = requests.get(url=url, headers=self.configs.get('headers'))
            
            if response.status_code != 200:
                raise HathorWalletError(f'Error return all generated addresses of the wallet.')

            return response.json()
            
        except:
            raise HathorWalletError('Error in the request.')

    def simple_send_tx(
        self, 
        address: str, 
        value: int, 
        token: Optional[str] = None, 
        change_address: Optional[str] = None
        ) -> Dict[bool, Dict]:

        data: Dict = {
            'address': address,
            'value': value
        }

        if token is not None:
            data['token'] = token
        if change_address is not None:
            data['change_address'] = change_address

        try:
            url = parse.urljoin(self.configs.get('wallet_base_url'), '/wallet/simple-send-tx')
            response = requests.post(url=url, headers=self.configs.get('headers'), data=data)
            
            if response.status_code != 200:
                raise HathorWalletError(f'Error sending transaction.')

            return response.json()
            
        except:
            raise HathorWalletError('Error in the request.')

    def tx_history(self, limit: int = None) -> Dict[Dict, Dict]:
        params: Dict[str, int] = None

        if limit:
            params = {'limit': limit}

        try:
            url = parse.urljoin(self.configs.get('wallet_base_url'), '/wallet/tx-history')
            response = requests.get(url=url, headers=self.configs.get('headers'), params=params)
            
            if response.status_code != 200:
                raise HathorWalletError(f'Error return transactions.')

            return response.json()
            
        except:
            raise HathorWalletError('Error in the request.')