from logging import getLogger, info, debug, exception

from CredentialManagement import CredentialManagement

from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetAssetsRequest
from alpaca.trading.enums import AssetClass


getLogger()


class AccountEnumeration:





  def __init__(self, keyfile, database, paperage=False):
    """
    Unlock market api credentials using a ```keyfile``` and a ```database```; where ```keyfile``` is
    a filepath to an ssh private key, and ```database``` is a filepath to a sqlite3.db file formatted
    with a __*credentials*__ table with username, alpaca_key, and alpaca_secret colums.

    It's assumed these columns are populated with an 'admin' user and valid alpaca credentials.
    """


    # Unlock the Alpaca.Markets API key and secret.
    debug("Unlocking alpaca credentials from:\n{database}")
    debug("Using encryption key:\n{keyfile}")
    try:
      credentials = CredentialManagement.MultiKeyAPICredentials(
        platform="alpaca", credabase=database, keyfile=keyfile
      )

      # Pull the credentials from the dictionary.
      key = credentials['key']; secret = credentials['secret']
      debug(f"Alpaca key and secret successfully retrieved.")

    except Exception as error:
      exception(f"There was a problem unlocking alpaca credentials:\n{error}")
      return error
    

    # Initialize the trade client with key and secret.
    debug("Initializing Alpaca trading client.")
    try:
      self.client = TradingClient(key, secret, paper=paperage)
      debug("Trade client set up successfully.")

    except Exception as error:
      exception(f"There was a problem setting up the trade client:\n{error}")
      return error





  def GetAccount(self, cmdline=True):
    """
    Collects and displays the 'bank account' functionality of the trade client.
    If cmdline is set to False then a dictionary containing all collected endpoints
    from a get_account request.

    Some important endpoints of note are:
        - "cash": Balance in USD.
        - "equity": Total worth in USD.
    """
  
    # Request account data from the trade client.
    debug("Gathering account data.")
    try:
      account = self.client.get_account()
      debug("Account data retrieved.")

    except Exception as error:
      exception(f"There was a problem gathering account data:\n{error}")
      return error
  

    # Enumerate account data in a hard-coded dictionary.
    debug("Constructing account data as hard-coded dictionary.")
    try:
      account_data = {
        "account blocked": account.account_blocked,
        "account number": account.account_number,
        "accrued fees": account.accrued_fees,
        "buying power": account.buying_power,
        "cash": account.cash,
        "created at": account.created_at,
        "crypto status": account.crypto_status,
        "currency": account.currency,
        "daytrade count": account.daytrade_count,
        "daytrading buying power": account.daytrading_buying_power,
        "equity": account.equity,
        "id": account.id,
        "initial margin": account.initial_margin,
        "last equity": account.last_equity,
        "last maintenance margin": account.last_maintenance_margin,
        "long market value": account.long_market_value,
        "maintenance margin": account.maintenance_margin,
        "multiplier": account.multiplier,
        "non-marginable buying power": account.non_marginable_buying_power,
        "pattern day trader": account.pattern_day_trader,
        "pending transfer in": account.pending_transfer_in,
        "pending transfer out": account.pending_transfer_out,
        "portfolio value": account.portfolio_value,
        "regt buying power": account.regt_buying_power,
        "short market value": account.short_market_value,
        "shorting enabled": account.shorting_enabled,
        "sma": account.sma,
        "status": account.status,
        "trade suspended by user": account.trade_suspended_by_user,
        "trading blocked": account.trading_blocked,
        "transfers blocked": account.transfers_blocked
      }; debug("Data construct enumerated.")

    except Exception as error:
      exception(f"There was a problem constructing account data:\n{error}")
      return error
 

    ''' RETURN VALUES '''
    # Format return string with constructed endpoints.
    debug("Curating return on constructed endpoints.")
    try:
      if cmdline is True:
        debug("Output is set to interactive mode.")
        debug("Writing return string:\n")
        return_string = ( f"Account Details:"
                          f"\n\n  Account Number: {account_data['account number']}"
                          f"\n  Account Fees: {account_data['accrued fees']}"
                          f"\n  Currency: {account_data['currency']}"
                          f"\n  Buying Power: ${account_data['buying power']}"
                          f"\n  Cash: ${account_data['cash']}"
                          f"\n  Equity: ${account_data['equity']}"
                          f"\n  Portfolio Value: ${account_data['portfolio value']}" )
        debug(f"{return_string}\n\n")

        return return_string

      else:
        debug("Output is set to scripting mode.")
        debug(f"Returning data construct:\n{account_data}\n\n")
        return account_data
  



  
  # Gather positional data.
  def GetAllPositions(self, cmdline=True):
    """
    Collect a readout of all of our currently held positions.
    Can either be used in an interactive setting or a programmatic setting.
  
    For interactivity, a string 'message' is constructed enumerating the most
    relevant-at-a-glance endpoints in a human readable format to be distributed
    by a telegram bot.
  
    For programmatic usage, the entire result is returned to the caller.
    """
  
  
    # Make the API call requesting positions.
    debug("Collecting positional data.")
    try:
      positions = self.client.get_all_positions()
      debug("Successfully collected positional data.")

    except Exception as error:
      exception(f"There was a problem collecting positional data:\n{error}")
      return error
  

    # Establish data structure for collections.
    debug("Constructing positional data as dictionary.")
    try:
      positional_data = {}; debug("Created empty construct.")
      debug("Begin iterating positions.")
  
      # Populate the structure.
      for position in positions:
        debug("Appending position: {position.symbol}")
        positional_data[position.symbol] = {
          "symbol": position.symbol,
          "exchange": position.exchange,
          "asset class": position.asset_class,
          "average entry price": position.avg_entry_price,
          "quantity": position.qty,
          "side": position.side,
          "market value": position.market_value,
          "cost basis": position.cost_basis,
          "unrealized profit/loss": position.unrealized_pl,
          "unrealized profit/loss percent": position.unrealized_plpc,
          "unrealized intraday profit/loss": position.unrealized_intraday_pl,
          "unrealized intraday profit/loss percent": position.unrealized_intraday_plpc,
          "current price": position.current_price,
          "last day price": position.lastday_price,
          "change today": position.change_today
        }

    except Exception as error:
      exception(f"There was a problem constructing positional data structure:\n{error}")
      return error
  

    ''' RETURN VALUES '''
    debug("Curating return values.")


    # For interactive usage.
    if cmdline is True:
      debug("Output is set to interactive mode.")
      debug("Writing return string:\n")

      message = "Your positions:"
      for position in positional_data:
        message += f"\n\nSymbol: {positional_data[position]['symbol']}"
        message += f"\nClass: {positional_data[position]['asset class']}"
        message += f"\nCurrent Price: {positional_data[position]['current price']}"
        message += f"\nSide: {positional_data[position]['side']}"
        message += f"\nQuantity: {positional_data[position]['quantity']}"
        message += f"\nValue: {positional_data[position]['market value']}"
        message += f"\nBuy-In: {positional_data[position]['cost basis']}"

      debug(f"{message}\n\n"); return message
  

    # For programmatic usage.
    else:
      debug("Output is set to scripting mode.")
      debug(f"Returning positional data construct:\n{positional_data}\n\n")
      return positional_data
  



  
  def ListAssets(self):
    """
    Curate a list of offerings available on the Alpaca market.
  
    Currently, we only display the cryptocurrency assets, as there are over
    31,000 us_equity assets maintained by Alpaca.
  
    To display equity assets, the 31,000 should be broken up alphabetically
    and given by the broker bot individually, piece by piece.
    """

    debug("Collecting list of tradeable assets.")
    message = ("Cryptocurrency Assets:\n")
  
    # Query the market for asset lists.
    debug("Querying asset list.")
    try:
      search_params = GetAssetsRequest(asset_class=AssetClass.CRYPTO)
      debug("Querying cryptocurrency assets.")

      assets = self.client.get_all_assets(search_params)
      debug(f"Got assets:\n{assets}\n\n")

      for asset in assets: message += f"\n  {asset.symbol}"
      debug(f"Formatted Asset List:\n{message}\n\n"); return message

    except Exception as error:
      exception("There was a problem querying the asset list:\n{error}")
      return error
