##
wavelength = float(input('insert wavelength: '))
print(wavelength)

if wavelength > 10**(-1):
    print('the type of the wavelength is RADIO WAVES')
elif 10**(-3) < wavelength < 10**(-1):
    print('the type of the wavelength is MICROWAVES')
elif 7*10**(-7) < wavelength < 10**(-3):
    print('the type of the wavelength is INFRARED')
elif 4*10**(-7) < wavelength < 7*10**(-7):
    print('the type of the wavelength is VISIBLE LIGHT')
elif 10**(-8) < wavelength < 4*10**(-7):
    print('the type of the wavelength is ULTRAVIOLET')
elif 10**(-11) < wavelength < 10**(-8):
    print('the type of the wavelength is X-RAYS')
else:
    print('the type of the wavelength is GAMMA RAYS')





