#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 07:51:05 2021

@author: bizzy
"""
import csv


countries=[
        'DZ', 'EG', 'EH', 'LY', 'MA', 'SD', 'SS', 'TN', 'BF', 'BJ', 
        'CI', 'CV', 'GH', 'GM', 'GN', 'GW', 'LR', 'ML', 'MR', 'NE', 
        'NG', 'SH', 'SL', 'SN', 'TG', 'AO', 'CD', 'ZR', 'CF', 'CG', 
        'CM', 'GA', 'GQ', 'ST', 'TD', 'BI', 'DJ', 'ER', 'ET', 'KE', 
        'KM', 'MG', 'MU', 'MW', 'MZ', 'RE', 'RW', 'SC', 'SO', 'TZ', 
        'UG', 'YT', 'ZM', 'ZW', 'BW', 'LS', 'NA', 'SZ', 'ZA', 'GG', 
        'JE', 'AX', 'DK', 'EE', 'FI', 'FO', 'GB', 'IE', 'IM', 'IS', 
        'LT', 'LV', 'NO', 'SE', 'SJ', 'AT', 'BE', 'CH', 'DE', 'DD',
        'FR', 'FX', 'LI', 'LU', 'MC', 'NL', 'BG', 'BY', 'CZ', 'HU',
        'MD', 'PL', 'RO', 'RU', 'SU', 'SK', 'UA', 'AD', 'AL', 'BA', 
        'ES', 'GI', 'GR', 'HR', 'IT', 'ME', 'MK', 'MT', 'RS', 'PT',
        'SI', 'SM', 'VA', 'YU', 'AG', 'AI', 'AN', 'AW', 'BB', 'BL',
        'BS', 'CU', 'DM', 'DO', 'GD', 'GP', 'HT', 'JM', 'KN', 'KY',
        'LC', 'MF', 'MQ', 'MS', 'PR', 'TC', 'TT', 'VC', 'VG', 'VI',
        'BZ', 'CR', 'GT', 'HN', 'MX', 'NI', 'PA', 'SV', 'AR', 'BO',
        'BR', 'CL', 'CO', 'EC', 'FK', 'GF', 'GY', 'PE', 'PY', 'SR',
        'UY', 'VE', 'TM', 'TJ', 'KG', 'KZ', 'UZ', 'CN', 'HK', 'JP', 
        'KP', 'KR', 'MN', 'MO', 'TW', 'AF', 'BD', 'BT', 'IN', 'IR',
        'LK', 'MV', 'NP', 'PK', 'BN', 'ID', 'KH', 'LA', 'MM', 'BU',
        'MY', 'PH', 'SG', 'TH', 'TL', 'TP', 'VN', 'AE', 'AM', 'AZ',
        'BH', 'CY', 'GE', 'IL', 'IQ', 'JO', 'KW', 'LB', 'OM', 'PS',
        'QA', 'SA', 'NT', 'SY', 'TR', 'YE', 'YD', 'AU', 'NF', 'NZ', 
        'FJ', 'NC', 'PG', 'SB', 'VU', 'FM', 'GU', 'KI', 'MH', 'MP',
        'NR', 'PW', 'AS', 'CK', 'NU', 'PF', 'PN', 'TK', 'TO', 'TV',
        'WF', 'WS', 'BM', 'CA', 'GL', 'PM', 'US'
]

with open('geochart_iso.csv', 'w') as f: 
    writer = csv.writer(f) 
    writer.writerow(countries)


