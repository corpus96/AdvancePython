import wx

class Ejemplo_Menu(wx.Frame):
    def __init__(self, parent, title):
        super(Ejemplo_Menu, self).__init__(parent, title=title)
        self.InitUi()

    def InitUi(self):
        menu_bar = wx.MenuBar()
        file_Menu = wx.Menu()
        file_item = file_Menu.Append(wx.ID_EXIT, 'Exit', 'Exit application')

        menu_bar.Append(file_Menu, '&File')
        self.SetMenuBar(menu_bar)
        self.Bind(wx.EVT_MENU, self.OnQuit, file_item)
        self.Show(True)

    def OnQuit(self, e):
        self.Close()

frame = wx.App()

Ejemplo_Menu(None, 'Word')
frame.MainLoop()