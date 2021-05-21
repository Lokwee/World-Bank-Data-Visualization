import numpy as np
import wbdata
import datetime
import pandas as pd 

data_date = datetime.datetime(2016, 1, 1), datetime.datetime(2017, 1, 1)

my_Indicators = {'SP.POP.TOTL':'Population', 'NY.GDP.PCAP.CD':'GDP', 'SP.POP.GROW':'Population_Growth', 'SH.MED.PHYS.ZS':'Physicians_per1000', 'SH.HIV.INCD.ZS':'HIV_Incidence', 'AG.LND.TOTL.K2':'Land_area', 'SE.ADT.LITR.ZS':'Literacy_rate', 'SH.MED.BEDS.ZS':'Hospital_beds_per1000', 'SH.XPD.CHEX.GD.ZS':'Government_health_expenditure', 'SH.STA.MALN.ZS':'Prevalence_underweight_under5', 'SP.DYN.IMRT.IN':'Infant_mortality_per1000', 'SH.STA.MMRT':'Maternal_mortality_per100000', 'SP.DYN.LE00.IN':'Life_expectancy', 'SH.STA.OWAD.ZS':'Adult_obesity', 'SH.DYN.AIDS.ZS':'HIV_Prevalence', 'SP.DYN.TFRT.IN':'Fertility_rate', 'SP.POP.TOTL.FE.ZS':'Female_Population', 'SP.POP.TOTL.MA.ZS':'Male_Population', 'SP.POP.65UP.TO':'Population_65+', 'SP.POP.0014.TO':'Population_age_0to14', 'SP.POP.1564.TO':'Population_15to64', 'SP.DYN.CDRT.IN':'Death_per1000'}


df1 = wbdata.get_dataframe(my_Indicators, data_date=data_date)
df1.head()
df1.tail()
df1.shape
df1['Income_level'].tolist()

df1.reset_index(inplace = True)

Income_level = [] 
HIC = [i['name'] for i in wbdata.get_country(incomelevel='HIC')] 
INX = [i['name'] for i in wbdata.get_country(incomelevel='INX')] 
LIC = [i['name'] for i in wbdata.get_country(incomelevel='LIC')]
LMC = [i['name'] for i in wbdata.get_country(incomelevel='LMC')]     
LMY = [i['name'] for i in wbdata.get_country(incomelevel='LMY')] 
MIC = [i['name'] for i in wbdata.get_country(incomelevel='MIC')] 
UMC = [i['name'] for i in wbdata.get_country(incomelevel='UMC')] 

for i in df1['country']:
  if i in HIC:
    Income_level.append('HIC')
  elif i in LIC:
    Income_level.append('LIC')
  elif i in LMC:
    Income_level.append('LMC')
  elif i in LMY:
    Income_level.append('LMY')
  elif i in MIC:
    Income_level.append('MIC')
  elif i in UMC:
    Income_level.apppend('UMC')
  else:
    Income_level.append('INX')

# df1.drop('Income_level', inplace=True, axis = 1)
df1['Income_level'] = Income_level
df1.head()

df1 = df1[df1.date != '2017']
df1.shape

East_Asia_and_Pacific = ['American Samoa', 'Australia', 'Brunei Darussalam', 'Cambodia', 'China', 'Fiji', 'French Polynesia', 'Guam', 'Hong Kong SAR, China', 'Indonesia', 'Japan', 'Kiribati', "Korea, Dem. People's Rep.", "Korea, Rep.", 'Lao PDR', 'Macao SAR, China', 'Malaysia', 'Marshall Islands', 'Micronesia, FED. STS.', 'Mongolia', 'Myanmar', 'Nauru', 'New Caledonia', 'New Zealand', 'Northern Marina Islands', 'Palau', 'Papua New Guinea', 'Philippines', 'Samoa', 'Singapore', 'Solomon Islands', 'Thailand', 'Timor-Leste', 'Tonga', 'Tuvalu', 'Vanuatu', 'Vietnam']

Europe_and_Central_Asia = ['Albania', 'Andorra', 'Armenia', 'Austria', 'Azerbaijan', 'Belarus', 'Belgium','Bosnia and Herzegovina', 'Bulgaria', 'Channel Islands', 'Croatia', 'Cyprus', 'Czech Republic', 'Denmark', 'Estonia', 'Faroe Islands', 'Finland', 'France', 'Georgia', 'Germany', 'Gibraltar', 'Greece', 'Greenland', 'Hungary', 'Iceland', 'Ireland', 'Isle of Man', 'Italy', 'Kazakhstan', 'Kosovo', 'Kyrgyz Republic', 'Latvia', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Moldova', 'Monaco', 'Montenegro', 'Netherlands', 'North Macedonia', 'Norway', 'Poland', 'Portugal', 'Romania', 'Russian Federation', 'San marino', 'Serbia', 'Slovak republic', 'Slovenia', 'Spain', 'Sweden', 'Switzerland', 'Tajikistan', 'Turkey', 'Turkmenistan', 'Ukraine', 'United Kingdom', 'Uzbekistan']

Latin_America_and_Caribbean = ['Antigua and Barbuda', 'Argentina', 'Aruba', 'Bahamas, The', 'Barbados', 'Belize', 'Bolivia', 'Brazil', 'British Virgin Islands', 'Cayman Islands', 'Chile', 'Colombia', 'Costa Rica', 'Cuba', 'Curacao', 'Dominica', 'Dominican Republic', 'Ecuador', 'El Salvador', 'Grenada', 'Guatemala', 'Guyana', 'Haiti', 'Honduras', 'Jamaica', 'Mexico', 'Nicaragua', 'Panama', 'Paraguay', 'Peru', 'Puerto Rico', 'Sint Maarten (Dutch Part)', 'St. Kitts and Nevis', 'St. Lucia', 'St. Martin (French Part)', 'St. Vincent and The Grenadines', 'Suriname', 'Trinidad and Tobago', 'Turks and Caicos Islands', 'Uruguay', 'Venezuela, RB', 'Virgin Islands (U.S.)']

Middle_East_and_North_Africa = ['Algeria', 'Bahrain', 'Djibouti', 'Egypt, Arab Rep.','Iran, Islamic Rep.', 'Iraq', 'Israel', 'Jordan', 'Kuwait', 'Lebanon', 'Libya', 'Malta', 'Morocco', 'Oman', 'Qatar', 'Saudi Arabia', 'Syrian Arab Republic', 'Tunisia', 'United Arab Emirates', 'West Bank and Gaza', 'Yemen, Rep.']

North_America = ['Bermuda', 'Canada','United States']

South_Asia = ['Afghanistan', 'Bangladesh', 'Bhutan', 'India', 'Maldives', 'Nepal', 'Pakistan', 'Sri Lanka']

Sub_Saharan_Africa = ['Angola', 'Benin', 'Botswana', 'Burkina Faso', 'Burundi', 'Cabo Verde', 'Cameroon', 'Central African Republic', 'Chad', 'Comoros', 'Congo, Dem. Rep.', "Cote d'Ivoire", 'Equatorial Guinea', 'Eritrea', 'Eswatini', 'Ethiopia', 'Gabon', 'Gambia, The', 'Ghana', 'Guinea', 'Guinea-Bissau', 'Kenya', 'Lesotho', 'Liberia','Madagascar', 'Malawi', 'Mali', 'Mauritania', 'Mauritius', 'Mozambique', 'Namibia', 'Niger', 'Nigeria', 'Rwanda', 'Sao Tome and Principe', 'Senegal', 'Seychelles', 'Sierra Leone', 'Somalia', 'South Africa', 'South Sudan', 'Sudan', 'Tanzania', 'Togo', 'Uganda', 'Zambia', 'Zimbabwe']

# for i in Sub_Saharan_Africa:
#   i.capitalize()

region = []
for i in df1['country']:
  if i in East_Asia_and_Pacific:
    region.append('East Asia and Pacific')
  elif i in Europe_and_Central_Asia:
    region.append('Europe and Central Asia')
  elif i in Latin_America_and_Caribbean:
    region.append('Latin America and Caribbean')
  elif i in Middle_East_and_North_Africa:
    region.append('Middle East and North Africa')
  elif i in North_America:
    region.append('North America')
  elif i in South_Asia:
    region.append('South Asia')
  elif i in Sub_Saharan_Africa:
    region.append('Sub-saharan Africa')
  else:
    region.append(i)

region
df1.head()
df1['Region'] = region
df1['Region'].tolist()


# country_codes.head()
# country_codes.drop('GDP (BILLIONS)', axis=1, inplace=True)
# country_codes.head()
# country_codes.to_csv('country_codes.csv')
# country_codes = pd.read_csv('country_codes.csv')
# country_codes.CODE.tolist()

# df1.country.tolist()

codes = ['AFG', 'ALB', 'DZA', 'ASM', 'AND', 'AGO', 'ATG', 'Arab World', 'ARG', 'ARM', 'ABW', 'AUS', 'AUT', 'AZE', 'BHM', 'BHR', 'BGD', 'BRB', 'BLR', 'BEL', 'BLZ', 'BEN', 'BMU', 'BTN', 'BOL', 'BIH', 'BWA', 'BRA', 'VGB', 'BRN', 'BGR', 'BFA', 'BDI', 'CPV', 'KHM', 'CMR', 'CAN', 'Caribbean small states', 'CYM', 'CAF', 'Central Europe and the Baltics', 'TCD', 'Channel Islands', 'CHL', 'CHN', 'COL', 'COM', 'COD', 'COG', 'CRI', 'CIV', 'HRV', 'CUB', 'CUW', 'CYP', 'CZE', 'DNK', 'DJI', 'DMA', 'DOM', 'Early-demographic dividend', 'East Asia & Pacific', 'East Asia & Pacific (IDA & IBRD countries)', 'East Asia & Pacific (excluding high income)', 'ECU', 'EGY', 'SLV', 'GNQ', 'ERI', 'EST', 'SWZ', 'ETH', 'Euro area', 'Europe & Central Asia', 'Europe & Central Asia (IDA & IBRD countries)', 'Europe & Central Asia (excluding high income)', 'European Union', 'FRO', 'FJI', 'FIN', 'Fragile and conflict affected situations', 'FRA', 'PYF', 'GAB', 'GMB', 'GEO', 'DEU', 'GHA', 'GIB', 'GRC', 'GRL', 'GRD', 'GUM', 'GTM', 'GIN', 'GNB', 'GUY', 'HTI', 'Heavily indebted poor countries (HIPC)', 'High income', 'HND', 'HKG', 'HUN', 'IBRD only', 'IDA & IBRD total', 'IDA blend', 'IDA only', 'IDA total', 'ISL', 'IND', 'IDN', 'IRN', 'IRQ', 'IRL', 'IMN', 'ISR', 'ITA', 'JAM', 'JPN', 'JOR', 'KAZ', 'KEN', 'KIR', 'KOR', 'PRK', 'KSV', 'KWT', 'KGZ', 'LAO', 'Late-demographic dividend', 'Latin America & Caribbean', 'Latin America & Caribbean (excluding high income)', 'Latin America & the Caribbean (IDA & IBRD countries)', 'LVA', 'Least developed countries: UN classification', 'LBN', 'LSO', 'LBR', 'LBY', 'LIE', 'LTU', 'Low & middle income', 'Low income', 'Lower middle income', 'LUX', 'MAC', 'MDG', 'MWI', 'MYS', 'MDV', 'MLI', 'MLT', 'MHL', 'MRT', 'MUS', 'MEX', 'FSM', 'Middle East & North Africa', 'Middle East & North Africa (IDA & IBRD countries)', 'Middle East & North Africa (excluding high income)', 'Middle income', 'MDA', 'MCO', 'MNG', 'MNE', 'MAR', 'MOZ', 'MMR', 'NAM', 'NRU', 'NPL', 'NLD', 'NCL', 'NZL', 'NIC', 'NER', 'NGA', 'North America', 'MKD', 'MNP', 'NOR', 'Not classified', 'OECD members', 'OMN', 'Other small states', 'Pacific island small states', 'PAK', 'PLW', 'PAN', 'PNG', 'PRY', 'PER', 'PHL', 'POL', 'PRT', 'Post-demographic dividend', 'Pre-demographic dividend', 'PRI', 'QAT', 'ROU', 'RUS', 'RWA', 'WSM', 'SMR', 'STP', 'SAU', 'SEN', 'SRB', 'SYC', 'SLE', 'SGP', 'SXM', 'SVK', 'SVN', 'Small states', 'SLB', 'SOM', 'ZAF', 'South Asia', 'South Asia (IDA & IBRD)', 'SSD', 'ESP', 'LKA', 'KNA', 'LCA', 'St. Martin (French part)', 'VCT', 'Sub-Saharan Africa', 'Sub-Saharan Africa (IDA & IBRD countries)', 'Sub-Saharan Africa (excluding high income)', 'SDN', 'SUR', 'SWE', 'CHE', 'SYR', 'TJK', 'TZA', 'THA', 'TLS', 'TGO', 'TON', 'TTO', 'TUN', 'TUR', 'TKM', 'TCA', 'TUV', 'UGA', 'UKR', 'ARE', 'GBR', 'USA', 'Upper middle income', 'URY', 'UZB', 'VUT', 'VEN', 'VNM', 'VGB', 'WBG', 'World', 'YEM', 'ZMB', 'ZWE']

len(codes)

df1['Codes'] = codes

df1.to_csv('World_bank_data.csv')