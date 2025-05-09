from flask import Flask, render_template
import yfinance as yf
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import io
import base64
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    # Stock lists
    stocks = [
        'ETERNAL.NS','VHL.NS',
        'TITAGARH.NS',
        'TIINDIA.NS','SUZLON.NS','SIEMENS.NS','SCHAEFFLER.NS','SAFARI.NS',
        'RADICO.NS','RAILTEL.NS','RAMCOCEM.NS','PFIZER.NS','PEL.NS',
        'MARUTI.NS','MRPL.NS',
        'MGL.NS','LATENTVIEW.NS','KOTAKBANK.NS',
        'KNRCON.NS','KICL.NS',
        'KPITTECH.NS',
        'KEI.NS','KCP.NS','JINDALSTEL.NS','JSWSTEEL.NS','JWL.NS','JSWHL.NS','JKTYRE.NS','JKPAPER.NS','JKCEMENT.NS',
        'ICICIPRULI.NS','HONDAPOWER.NS','HINDZINC.NS',
        'HAVELLS.NS',
        'HDFCLIFE.NS','GMDCLTD.NS', 'GESHIP.NS', 
        'GAIL.NS','FSL.NS','ELGIEQUIP.NS','DIXON.NS','DATAPATTNS.NS','CUMMINSIND.NS',
        'CHOLAFIN.NS','CHENNPETRO.NS','CRISIL.NS','CCL.NS','CANBK.NS','BHARATFORG.NS','BEL.NS','BDL.NS','BERGEPAINT.NS',
        'DMART.NS','DALBHARAT.NS','APARINDS.NS','ANDHRAPAP.NS','ACL.NS',
        
        
        'ZYDUSLIFE.NS','WIPRO.NS', 'VEDL.NS','UNIONBANK.NS',  'SULA.NS', 'SAIL.NS', 
        'SOUTHBANK.NS', 'MOTHERSON.NS','SHRIRAMFIN.NS','SHREECEM.NS', 'SRF.NS',   'RECLTD.NS',
         'PFC.NS',  'PERSISTENT.NS', 'POWERGRID.NS', 
        'OIL.NS','ONGC.NS','NMDC.NS',
        'NTPC.NS','NAM-INDIA.NS','NATCOPHARM.NS','NATIONALUM.NS',  'M&M.NS', 'MAHSEAMLES.NS','JIOFIN.NS', 'KTKBANK.NS','KAYNES.NS', 
         'IREDA.NS', 'IRCTC.NS','INDHOTEL.NS','IDFCFIRSTB.NS',  'HDFCAMC.NS', 'HEROMOTOCO.NS', 
        'ESCORTS.NS', 'EICHERMOT.NS','COCHINSHIP.NS', 'COALINDIA.NS', 
        'CUB.NS', 'CHOLAFIN.NS', 'CDSL.NS',  'CEATLTD.NS', 
        'BSE.NS','BHARTIHEXA.NS', 'BHARTIARTL.NS', 'BPCL.NS', 'BALKRISIND.NS', 
         'APLAPOLLO.NS','ADANIENT.NS','ADANIPORTS.NS',
        
        
		'VBL.NS', 'UBL.NS', 'UNITDSPR.NS', 
        'ULTRACEMCO.NS', 'TRENT.NS', 'TITAN.NS', 'THANGAMAYL.NS','TMB.NS', 'TECHM.NS', 
        'TATAELXSI.NS','TATACOMM.NS','TATACONSUM.NS','TATASTEEL.NS', 'TATAPOWER.NS', 'TATAINVEST.NS', 
         'TATACHEM.NS', 'TATAMOTORS.NS', 'TCS.NS',
        'SUNPHARMA.NS', 'RELIANCE.NS', 'PGHH.NS', 'PIDILITIND.NS','POLYCAB.NS', 
        'NESTLEIND.NS', 'MARICO.NS','MUTHOOTFIN.NS', 'MANAPPURAM.NS','LT.NS','RVNL.NS','IRCON.NS', 'IRFC.NS', 
        'INFY.NS', 'ITC.NS', 'ICICIBANK.NS', 'KALYANKJIL.NS',
        'HINDALCO.NS', 'HINDUNILVR.NS', 'HAL.NS', 'HDFCBANK.NS', 'HCLTECH.NS', 'EXIDEIND.NS', 
        'DRREDDY.NS', 'DIVISLAB.NS','DEEPAKFERT.NS', 'DEEPAKNTR.NS', 'COLPAL.NS', 'BRITANNIA.NS',
		'BAJAJHLDNG.NS', 'BAJAJHFL.NS', 'BAJAJFINSV.NS', 'BAJFINANCE.NS', 'BAJAJ-AUTO.NS',
		'ASIANPAINT.NS','APOLLOHOSP.NS', 'APOLLOTYRE.NS','ARE&M.NS', 'ACC.NS','AMBUJACEM.NS','ITC.NS'
    ]

    railway_stocks = ['RAILTEL.NS','RITES.NS','JWL.NS','TITAGARH.NS','IRCTC.NS', 'RVNL.NS', 'IRCON.NS','IRFC.NS']
    
    bank_stocks = ['YESBANK.NS','CSBBANK.NS','UTKARSHBNK.NS','JSFB.NS','DCBBANK.NS','ESAFSFB.NS','FINOPB.NS','SURYODAY.NS','CAPITALSFB.NS','DHANBANK.NS','UCOBANK.NS',
    'BANDHANBNK.NS', 'PSB.NS','RBLBANK.NS','J&KBANK.NS', 'MAHABANK.NS', 'UJJIVANSFB.NS','EQUITASBNK.NS',
    'BANKINDIA.NS', 'CENTRALBK.NS', 'AUBANK.NS',  'FEDERALBNK.NS', 'INDIANB.NS', 'IDBI.NS', 'IOB.NS', 'INDUSINDBK.NS',
    'KARURVYSYA.NS', 'PNB.NS','SOUTHBANK.NS', 'BANKBARODA.NS', 'UNIONBANK.NS','CUB.NS', 'CANBK.NS', 'IDFCFIRSTB.NS', 
    'KOTAKBANK.NS', 'AXISBANK.NS', 'SBIN.NS', 'TMB.NS', 'ICICIBANK.NS', 'HDFCBANK.NS']

    defence_stocks = ['BEML.NS','CYIENTDLM.NS','SOLARINDS.NS','BDL.NS','MAZDOCK.NS','DATAPATTNS.NS','COCHINSHIP.NS','BEL.NS','HAL.NS']
     
    gold_finance_stocks = ['PNGJL.NS', 'THANGAMAYL.NS','KALYANKJIL.NS','TITAN.NS','SHRIRAMFIN.NS','JIOFIN.NS','MUTHOOTFIN.NS','MANAPPURAM.NS','BAJAJHFL.NS', 'BAJAJFINSV.NS', 'BAJFINANCE.NS']

    power_cement_stocks =[ 'INDIACEM.NS', 'ACL.NS','RAMCOCEM.NS','DALBHARAT.NS','JKLAKSHMI.NS', 'JKCEMENT.NS', 'SHREECEM.NS','ACC.NS', 'AMBUJACEM.NS', 'ULTRACEMCO.NS',
    'SJVN.NS','EXIDEIND.NS','ARE&M.NS','TORNTPOWER.NS','NHPC.NS', 'CESC.NS','ADANIENSOL.NS','ADANIGREEN.NS', 
    'HINDZINC.NS', 'ADANIPOWER.NS', 'TATAPOWER.NS', 'JSWENERGY.NS', 'RECLTD.NS', 'PFC.NS','NTPC.NS', 'POWERGRID.NS']



    fmcg_amc_stocks =[ 'RADICO.NS', 'MARICO.NS', 'COLPAL.NS', 'TATACONSUM.NS', 'BRITANNIA.NS', 'HINDUNILVR.NS', 'VBL.NS', 'NESTLEIND.NS', 'ITC.NS','VHL.NS','JSWHL.NS','BAJAJHLDNG.NS','UTIAMC.NS', 'ABSLAMC.NS', 'NAM-INDIA.NS', 'HDFCAMC.NS']
    
    
    pharma_stock = [  'APLLTD.NS',   'ABBOTINDIA.NS', 'GLENMARK.NS','PFIZER.NS', 'ALKEM.NS', 'BIOCON.NS','LUPIN.NS','AUROPHARMA.NS', 
                   'ZYDUSLIFE.NS', 'MAXHEALTH.NS', 'APOLLOHOSP.NS', 'TORNTPHARM.NS', 'NATCOPHARM.NS',  'CIPLA.NS', 'DRREDDY.NS','DIVISLAB.NS', 'SUNPHARMA.NS']

    it_stock = ['TATATECH.NS','FSL.NS','KPITTECH.NS','TATAELXSI.NS', 'MPHASIS.NS', 'LTIM.NS', 'TECHM.NS', 'WIPRO.NS', 'HCLTECH.NS', 'INFY.NS', 'TCS.NS']
    
    
    nifty_stocks =[ 'INDUSINDBK.NS', 'HEROMOTOCO.NS', 'DRREDDY.NS','APOLLOHOSP.NS', 'TATACONSUM.NS', 'SHRIRAMFIN.NS', 'EICHERMOT.NS', 'CIPLA.NS', 'BPCL.NS', 'BRITANNIA.NS', 'HDFCLIFE.NS', 'TECHM.NS', 'HINDALCO.NS', 'SBILIFE.NS', 'GRASIM.NS', 'BEL.NS', 'TATASTEEL.NS', 'NESTLEIND.NS', 'JSWSTEEL.NS', 'TRENT.NS', 'WIPRO.NS', 'ASIANPAINT.NS', 'BAJAJFINSV.NS', 'ADANIPORTS.NS', 'COALINDIA.NS', 'POWERGRID.NS', 'TITAN.NS', 'BAJAJ-AUTO.NS', 'ULTRACEMCO.NS', 'TATAMOTORS.NS', 'ADANIENT.NS', 'KOTAKBANK.NS', 'AXISBANK.NS', 'ONGC.NS', 'M&M.NS', 'MARUTI.NS', 'NTPC.NS', 'BAJFINANCE.NS', 'SUNPHARMA.NS', 'LT.NS', 'HCLTECH.NS', 'ITC.NS', 'HINDUNILVR.NS', 'SBIN.NS', 'INFY.NS', 'ICICIBANK.NS', 'BHARTIARTL.NS', 'HDFCBANK.NS', 'TCS.NS', 'RELIANCE.NS']

    
    american_stocks =['AXP','WMT','AVGO','GIB','IBM','ACN','BAC', 'NVDA', 'HPQ', 'META', 'AMZN', 'GOOG', 'MSFT', 'DELL','JPM', 'BRK-B', 'COKE', 'TM', 'AAPL']

    # Helper function to fetch stock data fast
    def fetch_stock_data_fast(tickers):
        df = yf.download(tickers, period="2d", interval="1d", group_by="ticker", auto_adjust=False, threads=True, progress=False)
        stock_data = {}

        for ticker in tickers:
            try:
                today = df[ticker].iloc[-1]
                yesterday = df[ticker].iloc[-2]
                current_price = today['Close']
                previous_close = yesterday['Close']
                change_pct = ((current_price - previous_close) / previous_close) * 100

                info = yf.Ticker(ticker).info
                company_name = info.get('shortName') or ticker.replace('.NS', '')

                # Clean company name
                suffixes = ['Limited', 'Ltd.', 'Ltd', 'LTD', 'LTD.', 'LIMITED', '.', ' L', ' (I)', ' (L)']
                for suffix in suffixes:
                    if company_name.endswith(suffix):
                        company_name = company_name.replace(suffix, '').strip()
                        break

                stock_data[ticker] = {
                    'Name': company_name,
                    'Current Price': current_price,
                    'Previous Close': previous_close,
                    '1D Change %': change_pct,
                    '52 Week Low': info.get('fiftyTwoWeekLow', 0),
                    '52 Week High': info.get('fiftyTwoWeekHigh', 0)
                }
            except Exception as e:
                print(f"Failed to fetch {ticker}: {e}")
                continue

        return stock_data

    # Plot creation function
    def create_plot(stock_data):
        if not stock_data:
            return None

        names = [data['Name'] for data in stock_data.values()]
        current_price = [data['Current Price'] for data in stock_data.values()]
        low_52w = [data['52 Week Low'] for data in stock_data.values()]
        high_52w = [data['52 Week High'] for data in stock_data.values()]
        changes = [data['1D Change %'] for data in stock_data.values()]

        bar_width = 90
        bar_start = 2500
        plot_height = len(names) * 0.8

        fig, ax = plt.subplots(figsize=(8, plot_height))
        y = np.arange(len(names))

        for i in range(len(names)):
            bar_end = bar_start + bar_width
            ax.plot([bar_start, bar_end], [i, i], color='lightblue', lw=5, zorder=1)

            if high_52w[i] > low_52w[i]:
                price_position = bar_start + (current_price[i] - low_52w[i]) / (high_52w[i] - low_52w[i]) * bar_width
            else:
                price_position = bar_start

            price_symbol = '₹' if '.NS' in list(stock_data.keys())[i] else '$'

            # Draw the current price symbol ▲
            # Draw the ▲ symbol
            ax.annotate('▲', xy=(price_position, i), fontsize=12, color='green', ha='center', va='center')

            # Decide color based on change value
            change_color = 'green' if changes[i] >= 0 else 'red'

            # Combine current price and change % in the same line, but separately positioned
            # First draw current price (left side)
            ax.text(
                price_position - 0.25, i + 0.25,   # Shift a bit left
                f'{price_symbol}{current_price[i]:.2f}',
                va='center', ha='right', color='black', fontsize=10, fontweight='bold'
            )

            # Then draw change % (right side)
            ax.text(
                price_position + 0.25, i + 0.25,    # Shift a bit right
                f'({changes[i]:+.2f}%)',
                va='center', ha='left', color=change_color, fontsize=9
            )

            # Draw 52-week low and high values
            ax.text(bar_start, i - 0.45, f'L {price_symbol}{low_52w[i]:.2f}', ha='right', fontsize=9)
            ax.text(bar_end, i - 0.45, f'H {price_symbol}{high_52w[i]:.2f}', ha='left', fontsize=9)


        ax.set_yticks(y)
        ax.set_yticklabels(names, fontweight='bold')
        ax.xaxis.set_visible(False)
        ax.yaxis.set_ticks_position('none')
        for spine in ax.spines.values():
            spine.set_visible(False)

        buf = io.BytesIO()
        plt.savefig(buf, format='png', bbox_inches='tight', transparent=True)
        buf.seek(0)
        plot_url = base64.b64encode(buf.read()).decode('utf-8')
        plt.close()

        return plot_url

    # Fetch and plot for main, railway, bank
    all_stock_data = fetch_stock_data_fast(stocks)
    railway_stock_data = fetch_stock_data_fast(railway_stocks)
    bank_stock_data = fetch_stock_data_fast(bank_stocks)
    defence_stock_data = fetch_stock_data_fast(defence_stocks)
    gold_finance_stock_data = fetch_stock_data_fast(gold_finance_stocks)
    power_cement_stock_data = fetch_stock_data_fast(power_cement_stocks)
    fmcg_amc_stock_data = fetch_stock_data_fast(fmcg_amc_stocks)
    pharma_stock_data = fetch_stock_data_fast(pharma_stock)
    it_stock_data = fetch_stock_data_fast(it_stock)
    nifty_stock_data = fetch_stock_data_fast(nifty_stocks)
    american_stock_data = fetch_stock_data_fast(american_stocks)

    main_plot = create_plot(all_stock_data)
    railway_plot = create_plot(railway_stock_data)
    bank_plot = create_plot(bank_stock_data)
    defence_plot = create_plot(defence_stock_data)
    gold_finance_plot = create_plot(gold_finance_stock_data)
    power_cement_plot = create_plot(power_cement_stock_data)
    fmcg_amc_plot = create_plot(fmcg_amc_stock_data)
    pharma_plot = create_plot(pharma_stock_data)
    it_plot = create_plot(it_stock_data)
    nifty_plot = create_plot(nifty_stock_data)
    american_plot = create_plot(american_stock_data)

    return render_template('index.html', main_plot=main_plot, railway_plot=railway_plot, bank_plot=bank_plot, defence_plot=defence_plot, gold_finance_plot=gold_finance_plot, power_cement_plot=power_cement_plot, fmcg_amc_plot=fmcg_amc_plot, pharma_plot=pharma_plot, it_plot=it_plot, nifty_plot=nifty_plot, american_plot=american_plot
)

if __name__ == '__main__':
    app.run(debug=True)
