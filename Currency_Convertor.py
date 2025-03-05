import streamlit as st
import requests

st.set_page_config(page_icon = "💱")

API_KEY = "aa13b3f5df0d081c7c94b8da"
BASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/"

st.write("### Real-Time Currency Converter 💱")

currencies = [
    "AED", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS", "AUD", "AWG", "AZN",
    "BAM", "BBD", "BDT", "BGN", "BHD", "BIF", "BMD", "BND", "BOB", "BRL",
    "BSD", "BTN", "BWP", "BYN", "BZD", "CAD", "CDF", "CHF", "CLP", "CNY",
    "COP", "CRC", "CUP", "CVE", "CZK", "DJF", "DKK", "DOP", "DZD", "EGP",
    "ERN", "ETB", "EUR", "FJD", "FKP", "FOK", "GBP", "GEL", "GGP", "GHS",
    "GIP", "GMD", "GNF", "GTQ", "GYD", "HKD", "HNL", "HRK", "HTG", "HUF",
    "IDR", "ILS", "IMP", "INR", "IQD", "IRR", "ISK", "JEP", "JMD", "JOD",
    "JPY", "KES", "KGS", "KHR", "KID", "KMF", "KRW", "KWD", "KYD", "KZT",
    "LAK", "LBP", "LKR", "LRD", "LSL", "LYD", "MAD", "MDL", "MGA", "MKD",
    "MMK", "MNT", "MOP", "MRU", "MUR", "MVR", "MWK", "MXN", "MYR", "MZN",
    "NAD", "NGN", "NIO", "NOK", "NPR", "NZD", "OMR", "PAB", "PEN", "PGK",
    "PHP", "PKR", "PLN", "PYG", "QAR", "RON", "RSD", "RUB", "RWF", "SAR",
    "SBD", "SCR", "SDG", "SEK", "SGD", "SHP", "SLE", "SOS", "SRD", "SSP",
    "STN", "SYP", "SZL", "THB", "TJS", "TMT", "TND", "TOP", "TRY", "TTD",
    "TVD", "TWD", "TZS", "UAH", "UGX", "USD", "UYU", "UZS", "VES", "VND",
    "VUV", "WST", "XAF", "XCD", "XDR", "XOF", "XPF", "YER", "ZAR", "ZMW",
    "ZWL"
    ]

amount = st.number_input("Enter Amount: ", min_value = 0.01, format = "%.2f")
from_currency = st.selectbox("From Currency", options = currencies)
to_currency = st.selectbox("To Currency", options = currencies)
if st.button("Convert", type = "primary"):
    if from_currency == to_currency:
        st.warning("Select different currencies for conversion.")
    else:
        try:
            response = requests.get(BASE_URL + from_currency, verify = False)
            data = response.json()
            if response.status_code == 200:
                rate = data["conversion_rates"].get(to_currency)
                converted_amount = amount * rate
                st.success(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
            else:
                st.error("Error fetching exchange rates. Try again later.")
        except Exception as e:
            st.error("An error occured. Check your internet connection.")
