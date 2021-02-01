import wx

app = wx.App()

#Create fathter container
frame = wx.Frame(None, -1, 'first window') 

frame.Show()
app.MainLoop() #ciclo infinito durante el tiempo de vida de la aplicación