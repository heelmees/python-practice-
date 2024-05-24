from scipy.special import legendre
import matplotlib.pyplot as plt
import matplotlib.pyplot as Slider
import matplotlib.animation as animation
import numpy as np

# Задание 1
x = np.linspace(-1, 1, 400)
degrees = range(1, 8)

plt.figure(figsize=(10, 6))

for n in degrees:
  Pn = legendre(n)
  plt.plot(x, Pn(x), label=f'n = {n}')

plt.title('Полиномы Лежандра')
plt.legend(title='Степень полинома', loc='upper right', bbox_to_anchor=(1.1, 1))
plt.grid(True)
plt.show()

#Задание 2
def lissajous(a, b, delta, t):
  x = np.sin(a * t + delta)
  y = np.sin(b * t)
  return x, y

t = np.linspace(0, 2 * np.pi, 1000)
ratios = [(3, 2), (3, 4), (5, 4), (5, 6)]

plt.figure(figsize=(10, 10))

for i, (a, b) in enumerate(ratios, 1):
  x, y = lissajous(a, b, 0, t)
  plt.subplot(2, 2, i)
  plt.plot(x, y)

plt.tight_layout()
plt.show()

#Задание 3
fig, ax = plt.subplots()
t = np.linspace(0, 2 * np.pi, 1000)
line, = ax.plot([], [], lw=2)

ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)

def init():
  line.set_data([], [])
  return line,

def animate(freq):
  x = np.sin(5 * t)
  y = np.sin((5 + freq) * t)
  line.set_data(x, y)
  return line,

ani = animation.FuncAnimation(fig, animate, init_func=init, frames=np.linspace(0, 1, 100), blit=True)

plt.show()

#Задание 4
amplitude1 = 1.0
frequency1 = 1.0
amplitude2 = 1.0
frequency2 = 1.0

def calculate_wave(amplitude, frequency, x):
    return amplitude * np.sin(2 * np.pi * frequency * x)

def update(val):
    wave1.set_ydata(calculate_wave(slider_amp1.val, slider_freq1.val, x))
    wave2.set_ydata(calculate_wave(slider_amp2.val, slider_freq2.val, x))
    result_wave.set_ydata(wave1.get_ydata() + wave2.get_ydata())
    fig.canvas.draw_idle()

fig, ax = plt.subplots(3, 1, figsize=(10, 7))

x = np.linspace(0, 2 * np.pi, 1000)

wave1, = ax[0].plot(x, calculate_wave(amplitude1, frequency1, x), lw=2)
wave2, = ax[1].plot(x, calculate_wave(amplitude2, frequency2, x), lw=2)
result_wave, = ax[2].plot(x, calculate_wave(amplitude1, frequency1, x) + calculate_wave(amplitude2, frequency2, x), lw=2)

ax_amp1 = plt.axes([0.25, 0.02, 0.65, 0.03], facecolor='lightgoldenrodyellow')
slider_amp1 = Slider(ax_amp1, 'Амплитуда 1', 0.1, 2.0, valinit=amplitude1)

ax_freq1 = plt.axes([0.25, 0.06, 0.65, 0.03], facecolor='lightgoldenrodyellow')
slider_freq1 = Slider(ax_freq1, 'Частота 1', 0.1, 5.0, valinit=frequency1)

ax_amp2 = plt.axes([0.25, 0.10, 0.65, 0.03], facecolor='lightgoldenrodyellow')
slider_amp2 = Slider(ax_amp2, 'Амплитуда 2', 0.1, 2.0, valinit=amplitude2)

ax_freq2 = plt.axes([0.25, 0.14, 0.65, 0.03], facecolor='lightgoldenrodyellow')
slider_freq2 = Slider(ax_freq2, 'Частота 2', 0.1, 5.0, valinit=frequency2)

slider_amp1.on_changed(update)
slider_freq1.on_changed(update)
slider_amp2.on_changed(update)
slider_freq2.on_changed(update)

ax[0].set_title('Волна 1')
ax[1].set_title('Волна 2')
ax[2].set_title('Результат сложения')

plt.tight_layout()
plt.show()

#Задание 5
x = np.linspace(0, 10, 100)
y = np.linspace(0, 10, 100)
X, Y = np.meshgrid(x, y)
Z1 = np.sin(X) * np.cos(Y)
Z2 = np.cos(X) * np.sin(Y)

MSE = np.sqrt((Z1 - Z2)**2)

fig = plt.figure(figsize=(12, 6))

ax1 = fig.add_subplot(121)
ax1.imshow(MSE, extent=[0, 10, 0, 10], cmap='viridis', origin='lower')
ax1.set_title('MSE')

ax2 = fig.add_subplot(122)
c = ax2.imshow(np.log(MSE), extent=[0, 10, 0, 10], cmap='viridis', origin='lower', aspect='auto')
ax2.set_title('MSE(логар.)')
fig.colorbar(c, ax=ax2)

plt.show()
