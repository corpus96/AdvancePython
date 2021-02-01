import wx

app = wx.App()
frame = wx.Frame(None, -1, 'First Window', style=wx.MINIMIZE_BOX |  wx.MAXIMIZE_BOX | wx.RESIZE_BORDER | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)

frame.Show()
app.MainLoop() #ciclo infinito durante el tiempo de vida de la aplicación