from api import api_request, apis


KEY6 = ['date',
 ('astronomy',
  [(0,
    ['sunrise',
     'sunset',
     'moonrise',
     'moonset',
     'moon_phase',
     'moon_illumination'])]),
 'maxtempC',
 'maxtempF',
 'mintempC',
 'mintempF',
 'avgtempC',
 'avgtempF',
 'totalSnow_cm',
 'sunHour',
 'uvIndex',
 ('hourly',
  [(0,
    ['time',
     'tempC',
     'tempF',
     'windspeedMiles',
     'windspeedKmph',
     'winddirDegree',
     'winddir16Point',
     'weatherCode',
     ('weatherIconUrl', [(0, ['value'])]),
     ('weatherDesc', [(0, ['value'])]),
     'precipMM',
     'precipInches',
     'humidity',
     'visibility',
     'visibilityMiles',
     'pressure',
     'pressureInches',
     'cloudcover',
     'HeatIndexC',
     'HeatIndexF',
     'DewPointC',
     'DewPointF',
     'WindChillC',
     'WindChillF',
     'WindGustMiles',
     'WindGustKmph',
     'FeelsLikeC',
     'FeelsLikeF',
     'uvIndex']),
   (1,
    ['time',
     'tempC',
     'tempF',
     'windspeedMiles',
     'windspeedKmph',
     'winddirDegree',
     'winddir16Point',
     'weatherCode',
     ('weatherIconUrl', [(0, ['value'])]),
     ('weatherDesc', [(0, ['value'])]),
     'precipMM',
     'precipInches',
     'humidity',
     'visibility',
     'visibilityMiles',
     'pressure',
     'pressureInches',
     'cloudcover',
     'HeatIndexC',
     'HeatIndexF',
     'DewPointC',
     'DewPointF',
     'WindChillC',
     'WindChillF',
     'WindGustMiles',
     'WindGustKmph',
     'FeelsLikeC',
     'FeelsLikeF',
     'uvIndex']),
   (2,
    ['time',
     'tempC',
     'tempF',
     'windspeedMiles',
     'windspeedKmph',
     'winddirDegree',
     'winddir16Point',
     'weatherCode',
     ('weatherIconUrl', [(0, ['value'])]),
     ('weatherDesc', [(0, ['value'])]),
     'precipMM',
     'precipInches',
     'humidity',
     'visibility',
     'visibilityMiles',
     'pressure',
     'pressureInches',
     'cloudcover',
     'HeatIndexC',
     'HeatIndexF',
     'DewPointC',
     'DewPointF',
     'WindChillC',
     'WindChillF',
     'WindGustMiles',
     'WindGustKmph',
     'FeelsLikeC',
     'FeelsLikeF',
     'uvIndex']),
   (3,
    ['time',
     'tempC',
     'tempF',
     'windspeedMiles',
     'windspeedKmph',
     'winddirDegree',
     'winddir16Point',
     'weatherCode',
     ('weatherIconUrl', [(0, ['value'])]),
     ('weatherDesc', [(0, ['value'])]),
     'precipMM',
     'precipInches',
     'humidity',
     'visibility',
     'visibilityMiles',
     'pressure',
     'pressureInches',
     'cloudcover',
     'HeatIndexC',
     'HeatIndexF',
     'DewPointC',
     'DewPointF',
     'WindChillC',
     'WindChillF',
     'WindGustMiles',
     'WindGustKmph',
     'FeelsLikeC',
     'FeelsLikeF',
     'uvIndex'])])]

def remove_url(d):

    if type(d) == dict:
        for k in d.keys():
            if type(d[k]) == str:
                if d[k].startswith('http'):
                    d[k] = ''
            if type(d[k]) == dict:
                remove_url(d[k])

            if type(d[k]) == list:
                remove_url(d[k])
    if type(d) == list:
        for w in d:
            remove_url(w)


def separate(d):
    keys = []
    values = []

    for key in d.keys():
        keys.append(key)
        values.append(d[key])

    for i in range(len(keys)):
        if type(values[i]) == list:
            pseudo_d = dict()
            for j in range(len(values[i])):
                pseudo_d[j] = values[i][j]
            keys1, values1 = separate(pseudo_d)
            keys[i] = (keys[i], keys1)
            values[i] = values1
        if type(values[i]) == dict:
            keys1, values1 = separate(values[i])
            keys[i] = (keys[i], keys1)
            values[i] = values1



    return keys, values


def assemble(k, v):
    res = dict()
    n = len(k)

    if type(k[0]) == int or (type(k[0]) == tuple and type(k[0][0]) == int):
        res = []
        for i in range(n):
            if type(k[i]) == tuple:
                res.append(assemble(k[i][1], v[i]))
            else:
                res.append(v[i])
        return res
    for i in range(n):
        if type(k[i]) == tuple:
            d = assemble(k[i][1], v[i])
            res[k[i][0]] = d
        else:
            res[k[i]] = v[i]
    return res


