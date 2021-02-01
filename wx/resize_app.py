import wx

class Ventana_Ejemplo(wx.Frame):
    def __init__(self, parent, title):
        super(Ventana_Ejemplo, self).__init__(parent, title="Segunda ventana", size=(20, 20))
        self.Show(True)

app = wx.App()

#None means there are no parents
ventana = Ventana_Ejemplo(None, 'Hola')

ventana.Show()
app.MainLoop() #ciclo infinito durante el tiempo de vida de la aplicación