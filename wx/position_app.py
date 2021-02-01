import wx

class Ventana_Ejemplo(wx.Frame):
    def __init__(self, parent, title):
        super(Ventana_Ejemplo, self).__init__(parent, title="Segunda ventana", size=(200, 200))
        self.SetPosition((10, 10))
        self.Show(True)

if __name__ == '__main__':
    app = wx.App()

    Ventana_Ejemplo(None, title='New window')

    app.MainLoop()