"""
MIT License

Copyright (c) 2022 ferrofan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import scipy as scp
from scipy.integrate import quad
import numpy as np
import matplotlib.pyplot as plt

"""
If you want to know more about the lore concerning this intelligence scale and how the author of this code, 
ferrofan, made up the idea of creating this meme in the form of a python code, kindly see this link:
https://bigthink.com/hard-science/landau-genius-scale-ranking-of-the-smartest-physicists-ever/#:~:text=Nobel%2DPrize%2Dwinning%20Soviet%20physicist,being%2010%20times%20more%20valuable
"""

# set function for formatting numbers (use ',' as thousands separator)


def num_format(power):
    power_int = int(power)
    power_fmt = format(power_int, ',')
    return power_fmt


sigma = 15  # standard deviation
mu = 100  # mean
s = 0.71  # shounen constant
iq = np.linspace(0, 200.0, num=500)

# set gaussian (normal) function


def g_func(w):
    return (1 / (sigma * (2 * np.pi)) ** (1 / 2)) * np.exp((-1 / 2) * ((w - mu) / sigma) ** 2)


# plot gaussian (IQ) function
g_func_vector = np.vectorize(g_func)
x = iq
y = g_func_vector(x)
plt.plot(x, y, color='red')
plt.title('Frequency (arbitrary units) vs IQ')
plt.xlabel('IQ')
plt.tick_params(left=False, right=False, labelleft=False, labelbottom=True, bottom=True)
# plt.show

iq_user = float(input('Kindly insert your IQ so the scouter will estimate your power level: '))
i_user = scp.integrate.quad(g_func, 0.0, iq_user)[0]
i_total = scp.integrate.quad(g_func, 0.0, 200.0)[0]
iq_percentile = (i_user / i_total) * 100
power_level = np.exp(iq_percentile ** s)
power_level_fmt = num_format(np.exp(iq_percentile ** s))
power_level_log = round(np.log10(power_level), 2)
print(f'Your IQ is higher than {iq_percentile:.2f} % of humanity!')
print(f'Your power level is {power_level_fmt} in linear scale and {power_level_log} in log scale')

if power_level_log < 3:
    print("Congratulations! You are at the Red Ribbon Saga! Look for the Dragon Balls, but don't "
          "let Tao Pai Pai steal them from you!")
elif 3 <= power_level_log < 5:
    print('Congratulations! You are at the Sayan Saga! Grab your scouter and save Earth from those alien invaders!')
elif 5 <= power_level_log < 7:
    print('Congratulations! You are at the Frieza Saga! You may not be the legendary super sayan, '
          'but the Ginyu Force and Freeza should fear you now!')
elif 7 <= power_level_log < 9:
    print('Congratulations! You are at the Androids Saga! You are now ready to participate in the Cell Games '
          'and show who is the best in the universe!')
elif 9 <= power_level_log < 11:
    print("Congratulations! You are at the Buu Saga! Don't forget your chocolate bar and try to impede Babidi's"
          "evil plan of resurrecting his ancient demon!")
elif 11 <= power_level_log < 13:
    print("Congratulations! You are at the Super Saga! Now that you've reached the level of a deity,"
          " even Lord Beerus and Whis respect you!")
