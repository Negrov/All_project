import ctypes

u = ctypes.windll.LoadLibrary("user32.dll")
pf = getattr(u, "GetKeyboardLayout")
pf = pf(0)
lang = ('Ru_ru' if pf == 68748313 else 'En_en')

import win10toast

toaster = win10toast.ToastNotifier()
toaster.show_toast(lang, ' ', duration=1)