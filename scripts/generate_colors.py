# from itertools import chain
#
# import matplotlib
# import matplotlib.pyplot as plt
#
# col = [
#     'Pastel1', 'Pastel2', "Set3"]
#
# colors = [matplotlib.colors.to_hex(v, keep_alpha=False) for v in chain(*[plt.get_cmap(v).colors for v in col])]
# print(colors)

from flet_icon.app import Application
import flet

flet.app(target=Application())
