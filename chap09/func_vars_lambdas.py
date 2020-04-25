#!/usr/bin/python3

def f_to_kelvin(deg_f):
    return 273.15 + (deg_f - 32) * 5 / 9

def c_to_kelvin(deg_c):
    return 273.15 + (deg_c)

abs_temp = f_to_kelvin
print(abs_temp(32))

abs_temp = c_to_kelvin
print(abs_temp(0))


t = {'FtoK': f_to_kelvin, 'CtoK': c_to_kelvin}
print(t['FtoK'](32))
print(t['CtoK'](0))



t2 = {
        'FtoK': lambda deg_f: 273.15 + (deg_f -32)  * 5 / 9,
        'CtoK': lambda deg_c: 273.15 + deg_c
    }
print(t2['FtoK'](32))
print(t2['CtoK'](0))
