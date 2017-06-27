import falcon
import json
#import urllib.request
import feedparser
import requests
import json
# Falcon follows the REST architectural style, meaning (among
# other things) that you think in terms of resources and state
# transitions, which map to HTTP verbs.

flight_status = {'A': 'Active', 'C': 'Canceled', 'D': 'Diverted','DN': 'Data source needed', 'L': 'Landed', 'NO': 'Not Operational', 'R': 'Redirected', 'S': 'Scheduled', 'U': 'Unknown'}

currency_symbol = {'NZ': '$', 'CK': '$', 'NU': '$', 'PN': '$', 'TK': '$', 'AU': '$', 'CX': '$', 'CC': '$', 'HM': '$', 'KI': '$', 'NR': '$', 'NF': '$', 'TV': '$', 'AS': '€', 'AD': '€', 'AT': '€', 'BE': '€', 'FI': '€', 'FR': '€', 'GF': '€', 'TF': '€', 'DE': '€', 'GR': '€', 'GP': '€', 'IE': '€', 'IT': '€', 'LU': '€', 'MQ': '€', 'YT': '€', 'MC': '€', 'NL': '€', 'PT': '€', 'RE': '€', 'WS': '€', 'SM': '€', 'SI': '€', 'ES': '€', 'VA': '€', 'GS': '£', 'GB': '£', 'JE': '£', 'IO': '$', 'GU': '$', 'MH': '$', 'FM': '$', 'MP': '$', 'PW': '$', 'PR': '$', 'TC': '$', 'US': '$', 'UM': '$', 'VG': '$', 'VI': '$', 'HK': '$', 'CA': '$', 'JP': '¥', 'AF': 'AFN', 'AL': 'ALL', 'DZ': 'DZD', 'AI': '$', 'AG': '$', 'DM': '$', 'GD': '$', 'MS': '$', 'KN': '$', 'LC': '$', 'VC': '$', 'AR': '$', 'AM': 'AMD', 'AW': 'ƒ', 'AN': 'ƒ', 'AZ': 'AZN', 'BS': '$', 'BH': 'BHD', 'BD': 'BDT', 'BB': '$', 'BY': 'p.', 'BZ': 'BZ$', 'BJ': 'XOF', 'BF': 'XOF', 'GW': 'XOF', 'CI': 'XOF', 'ML': 'XOF', 'NE': 'XOF', 'SN': 'XOF', 'TG': 'XOF', 'BM': '$', 'BT': 'Rp', 'IN': 'Rp', 'BO': '$b', 'BW': 'P', 'BV': 'kr', 'NO': 'kr', 'SJ': 'kr', 'BR': 'R$', 'BN': '$', 'BG': 'BGN', 'BI': 'BIF', 'KH': '៛', 'CM': 'XAF', 'CF': 'XAF', 'TD': 'XAF', 'CG': 'XAF', 'GQ': 'XAF', 'GA': 'XAF', 'CV': 'CVE', 'KY': '$', 'CL': '$', 'CN': '¥', 'CO': '$', 'KM': 'KMF', 'CD': 'CDF', 'CR': '₡', 'HR': 'kn', 'CU': '₱', 'CY': 'CYP', 'CZ': 'Kč', 'DK': 'kr', 'FO': 'kr', 'GL': 'kr', 'DJ': 'DJF', 'DO': 'RD$', 'TP': 'Rp', 'ID': 'Rp', 'EC': 'ECS', 'EG': '£', 'SV': '$', 'ER': 'ETB', 'ET': 'ETB', 'EE': 'EEK', 'FK': '£', 'FJ': '$', 'PF': 'XPF', 'NC': 'XPF', 'WF': 'XPF', 'GM': 'GMD', 'GE': 'GEL', 'GI': '£', 'GT': 'Q', 'GN': 'GNF', 'GY': '$', 'HT': 'HTG', 'HN': 'L', 'HU': 'Ft', 'IS': 'kr', 'IR': '﷼', 'IQ': 'IQD', 'IL': '₪', 'JM': 'J$', 'JO': 'JOD', 'KZ': 'лв', 'KE': 'KES', 'KP': '₩', 'KR': '₩', 'KW': 'KWD', 'KG': 'лв', 'LA': '₭', 'LV': 'Ls', 'LB': '£', 'LS': 'LSL', 'LR': '$', 'LY': 'LYD', 'LI': 'CHF', 'CH': 'CHF', 'LT': 'Lt', 'MO': 'MOP', 'MK': 'ден', 'MG': 'MGA', 'MW': 'MWK', 'MY': 'RM', 'MV': 'MVR', 'MT': 'MTL', 'MR': 'MRO', 'MU': '₨', 'MX': 'MXN', 'MD': 'MDL', 'MN': '₮', 'MA': 'MAD', 'EH': 'MAD', 'MZ': 'MZN', 'MM': 'MMK', 'NA': '$', 'NP': '₨', 'NI': 'C$', 'NG': 'NGN', 'OM': '﷼', 'PK': '₨', 'PA': 'B/.', 'PG': 'PGK', 'PY': 'Gs', 'PE': 'PEN', 'PH': 'Php', 'PL': 'PLN', 'QA': '﷼', 'RO': 'RON', 'RU': 'руб', 'RW': 'RWF', 'ST': 'STD', 'SA': '﷼', 'SC': '₨', 'SL': 'SLL', 'SG': '$', 'SK': 'SKK', 'SB': '$', 'SO': 'S', 'ZA': 'R', 'LK': '₨', 'SD': 'SDG', 'SR': '$', 'SZ': 'SZL', 'SE': 'kr', 'SY': '£', 'TW': 'NT$', 'TJ': 'TJS', 'TZ': 'TZS', 'TH': '฿', 'TO': 'TOP', 'TT': 'TT$', 'TN': 'TND', 'TR': 'TL', 'TM': 'TMT', 'UG': 'UGX', 'UA': '₴', 'AE': 'AED', 'UY': '$U', 'UZ': 'лв', 'VU': 'VUV', 'VE': 'Bs', 'VN': '₫', 'YE': '﷼', 'ZM': 'ZMK', 'ZW': 'Z$', 'AX': '€', 'AO': 'AOA', 'AQ': 'AQD', 'BA': 'KM', 'GH': 'GHS', 'GG': '£', 'IM': '£', 'ME': '€', 'PS': 'JOD', 'BL': '€', 'SH': '£', 'MF': 'ƒ', 'PM': '€', 'RS': 'Дин.', 'USAF': '$'}

currency_code = {'NZ': 'NZD', 'CK': 'NZD', 'NU': 'NZD', 'PN': 'NZD', 'TK': 'NZD', 'AU': 'AUD', 'CX': 'AUD', 'CC': 'AUD', 'HM': 'AUD', 'KI': 'AUD', 'NR': 'AUD', 'NF': 'AUD', 'TV': 'AUD', 'AS': 'EUR', 'AD': 'EUR', 'AT': 'EUR', 'BE': 'EUR', 'FI': 'EUR', 'FR': 'EUR', 'GF': 'EUR', 'TF': 'EUR', 'DE': 'EUR', 'GR': 'EUR', 'GP': 'EUR', 'IE': 'EUR', 'IT': 'EUR', 'LU': 'EUR', 'MQ': 'EUR', 'YT': 'EUR', 'MC': 'EUR', 'NL': 'EUR', 'PT': 'EUR', 'RE': 'EUR', 'WS': 'EUR', 'SM': 'EUR', 'SI': 'EUR', 'ES': 'EUR', 'VA': 'EUR', 'GS': 'GBP', 'GB': 'GBP', 'JE': 'GBP', 'IO': 'USD', 'GU': 'USD', 'MH': 'USD', 'FM': 'USD', 'MP': 'USD', 'PW': 'USD', 'PR': 'USD', 'TC': 'USD', 'US': 'USD', 'UM': 'USD', 'VG': 'USD', 'VI': 'USD', 'HK': 'HKD', 'CA': 'CAD', 'JP': 'JPY', 'AF': 'AFN', 'AL': 'ALL', 'DZ': 'DZD', 'AI': 'XCD', 'AG': 'XCD', 'DM': 'XCD', 'GD': 'XCD', 'MS': 'XCD', 'KN': 'XCD', 'LC': 'XCD', 'VC': 'XCD', 'AR': 'ARS', 'AM': 'AMD', 'AW': 'ANG', 'AN': 'ANG', 'AZ': 'AZN', 'BS': 'BSD', 'BH': 'BHD', 'BD': 'BDT', 'BB': 'BBD', 'BY': 'BYR', 'BZ': 'BZD', 'BJ': 'XOF', 'BF': 'XOF', 'GW': 'XOF', 'CI': 'XOF', 'ML': 'XOF', 'NE': 'XOF', 'SN': 'XOF', 'TG': 'XOF', 'BM': 'BMD', 'BT': 'INR', 'IN': 'INR', 'BO': 'BOB', 'BW': 'BWP', 'BV': 'NOK', 'NO': 'NOK', 'SJ': 'NOK', 'BR': 'BRL', 'BN': 'BND', 'BG': 'BGN', 'BI': 'BIF', 'KH': 'KHR', 'CM': 'XAF', 'CF': 'XAF', 'TD': 'XAF', 'CG': 'XAF', 'GQ': 'XAF', 'GA': 'XAF', 'CV': 'CVE', 'KY': 'KYD', 'CL': 'CLP', 'CN': 'CNY', 'CO': 'COP', 'KM': 'KMF', 'CD': 'CDF', 'CR': 'CRC', 'HR': 'HRK', 'CU': 'CUP', 'CY': 'CYP', 'CZ': 'CZK', 'DK': 'DKK', 'FO': 'DKK', 'GL': 'DKK', 'DJ': 'DJF', 'DO': 'DOP', 'TP': 'IDR', 'ID': 'IDR', 'EC': 'ECS', 'EG': 'EGP', 'SV': 'SVC', 'ER': 'ETB', 'ET': 'ETB', 'EE': 'EEK', 'FK': 'FKP', 'FJ': 'FJD', 'PF': 'XPF', 'NC': 'XPF', 'WF': 'XPF', 'GM': 'GMD', 'GE': 'GEL', 'GI': 'GIP', 'GT': 'GTQ', 'GN': 'GNF', 'GY': 'GYD', 'HT': 'HTG', 'HN': 'HNL', 'HU': 'HUF', 'IS': 'ISK', 'IR': 'IRR', 'IQ': 'IQD', 'IL': 'ILS', 'JM': 'JMD', 'JO': 'JOD', 'KZ': 'KZT', 'KE': 'KES', 'KP': 'KPW', 'KR': 'KRW', 'KW': 'KWD', 'KG': 'KGS', 'LA': 'LAK', 'LV': 'LVL', 'LB': 'LBP', 'LS': 'LSL', 'LR': 'LRD', 'LY': 'LYD', 'LI': 'CHF', 'CH': 'CHF', 'LT': 'LTL', 'MO': 'MOP', 'MK': 'MKD', 'MG': 'MGA', 'MW': 'MWK', 'MY': 'MYR', 'MV': 'MVR', 'MT': 'MTL', 'MR': 'MRO', 'MU': 'MUR', 'MX': 'MXN', 'MD': 'MDL', 'MN': 'MNT', 'MA': 'MAD', 'EH': 'MAD', 'MZ': 'MZN', 'MM': 'MMK', 'NA': 'NAD', 'NP': 'NPR', 'NI': 'NIO', 'NG': 'NGN', 'OM': 'OMR', 'PK': 'PKR', 'PA': 'PAB', 'PG': 'PGK', 'PY': 'PYG', 'PE': 'PEN', 'PH': 'PHP', 'PL': 'PLN', 'QA': 'QAR', 'RO': 'RON', 'RU': 'RUB', 'RW': 'RWF', 'ST': 'STD', 'SA': 'SAR', 'SC': 'SCR', 'SL': 'SLL', 'SG': 'SGD', 'SK': 'SKK', 'SB': 'SBD', 'SO': 'SOS', 'ZA': 'ZAR', 'LK': 'LKR', 'SD': 'SDG', 'SR': 'SRD', 'SZ': 'SZL', 'SE': 'SEK', 'SY': 'SYP', 'TW': 'TWD', 'TJ': 'TJS', 'TZ': 'TZS', 'TH': 'THB', 'TO': 'TOP', 'TT': 'TTD', 'TN': 'TND', 'TR': 'TRY', 'TM': 'TMT', 'UG': 'UGX', 'UA': 'UAH', 'AE': 'AED', 'UY': 'UYU', 'UZ': 'UZS', 'VU': 'VUV', 'VE': 'VEF', 'VN': 'VND', 'YE': 'YER', 'ZM': 'ZMK', 'ZW': 'ZWD', 'AX': 'EUR', 'AO': 'AOA', 'AQ': 'AQD', 'BA': 'BAM', 'GH': 'GHS', 'GG': 'GGP', 'IM': 'GBP', 'ME': 'EUR', 'PS': 'JOD', 'BL': 'EUR', 'SH': 'GBP', 'MF': 'ANG', 'PM': 'EUR', 'RS': 'RSD', 'USAF': 'USD'}



class Flightdetail(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200  # This is the default status
        num = str(req.params['flight_number'])
        carrier = num[:2]
        print(carrier)
        flight_number = num[2:]
        print(flight_number)
        year = req.params['year']
        month = req.params['month']
        day = req.params['day']
        # Base api query url
        try:
            flight_stats_url = "https://api.flightstats.com/flex/flightstatus/rest/v2/json/flight/status/{0}/{1}/arr/{2}/{3}/{4}?appId=2cc2cd2e&appKey=cb69bfcbbbe66bff1d97253d04d435e2&utc=false"
            flight_stats = requests.get(flight_stats_url.format(carrier,flight_number,year,month,day))
            flight_json = json.loads(flight_stats.text)
            flight_status_extracted_json = {}
            flight_status_extracted_json["airlines"] = flight_json['appendix']['airlines'][0]['name']
        except:
            flight_status_extracted_json["Input"] = "Given data is wrong"
        try:
            flight_status_extracted_json["airport_from_code"] = flight_json['appendix']['airports'][0]['fs']
            flight_status_extracted_json["airport_from"] = flight_json['appendix']['airports'][0]['name']
            flight_status_extracted_json["from_city"] = flight_json['appendix']['airports'][0]['city']
            flight_status_extracted_json["currency_from_symbol"] = currency_symbol[flight_json['appendix']['airports'][0]['countryCode']]
            flight_status_extracted_json["currency_from"] = currency_code[flight_json['appendix']['airports'][0]['countryCode']]
            flight_status_extracted_json["airport_to_code"] = flight_json['appendix']['airports'][1]['fs']
            flight_status_extracted_json["airport_to"] = flight_json['appendix']['airports'][1]['name']
            flight_status_extracted_json["to_city"] = flight_json['appendix']['airports'][1]['city']
            flight_status_extracted_json["currency_to_symbol"] = currency_symbol[flight_json['appendix']['airports'][0]['countryCode']]
            flight_status_extracted_json["currency_to"] = currency_code[flight_json['appendix']['airports'][1]['countryCode']]
            flight_status_extracted_json["departure_time"] = flight_json["flightStatuses"][0]["operationalTimes"]["scheduledGateDeparture"]["dateLocal"]
            flight_status_extracted_json["departure_terminal"] = flight_json["flightStatuses"][0]['airportResources']['departureTerminal']
            flight_status_extracted_json["arrival_terminal"] = flight_json["flightStatuses"][0]['airportResources']['arrivalTerminal']
            flight_status_extracted_json["flight_status"] = flight_status[flight_json["flightStatuses"][0]['status']]
        except:
            pass
        try:
            flight_status_extracted_json["delay"] = flight_json["flightStatuses"][0]["delays"]["departureGateDelayMinutes"]
        except:
            pass

        resp.body = json.dumps(flight_status_extracted_json)

# falcon.API instances are callable WSGI apps
app = falcon.API()
# things will handle all requests to the '/things' URL path
app.add_route('/flight', Flightdetail())
