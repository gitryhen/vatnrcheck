from vat import *
import datetime
import numpy as np

vatnumbers = []
with open('/home/henry/Documents/DeltaMask/2021/202104/idb_agg.tsv', mode='r') as f:
    for line in f:
        vatnumbers.append(line.split(None, 1)[0])

""" check numbers: from library example:
    check_vies_approx(vatnumbers[1], 'NL815941225B01', timeout=30)
    {
    'countryCode': 'DE',
    'vatNumber': '121684321',
    'requestDate': datetime.date(2018, 12, 26),
    'valid': True,
    'traderName': None,
    'traderCompanyType': None,
    'traderAddress': None,
    'traderStreet': None,
    'traderPostcode': None,
    'traderCity': None,
    'traderNameMatch': None,
    'traderCompanyTypeMatch': None,
    'traderStreetMatch': None,
    'traderPostcodeMatch': None,
    'traderCityMatch': None,
    'requestIdentifier': 'WAPIAAAAWfrVAPuC'
}
"""

responses = {}
for vatnumber in vatnumbers:
    if is_valid(vatnumber):
        # responses[vatnumber] =
        try:
        # check_vies_approx(validate(vatnumber), 'NL815941225B01', timeout=30)
            if vatnumber in responses:
                print(vatnumber, "Verified allready", sep=' ')
            else:
                responses[vatnumber]=check_vies(validate(vatnumber), timeout=30)
                print(vatnumber, 'Returned result', sep=' ')
        except ModuleNotFoundError:
            print('Check installation, module not found')
        except IndexError:
            print(vatnumber, 'Failed', sep=' ')
        # input("wait for keypress...")

""" load and save dicts with numpy:
# Save
dictionary = {'hello':'world'}
np.save('my_file.npy', dictionary) 

# Load
read_dictionary = np.load('my_file.npy').item()
print(read_dictionary['hello']) # displays "world"
"""

np.save('responses_dicts.npy', responses)


"""
responses = {'DE121684321' :
             {'countryCode': 'DE',
              'vatNumber': '121684321',
              'requestDate': datetime.date(2018, 12, 26),
              'valid': True
              }
             } # test case
"""

# responsetest = {'foo' : { 'a' : 1, 'b' : 2}, 'bar' : {'a' :34}}

for vatnr, response in responses.items():
    print(vatnr, response['valid'])
