import wx

class Ejemplo_Menu(wx.Frame):
    def __init__(self, parent, title):
        super(Ejemplo_Menu, self).__init__(parent, title=title)
        self.InitUi()

    def InitUi(self):
        menu_bar = wx.MenuBar()
        file_Menu = wx.Menu()

        file_Menu.Append(wx.ID_FILE, '&File')
        file_Menu.Append(wx.ID_EDIT, '&Edit')
        file_Menu.Append(wx.ID_SAVE, '&Save')
        file_Menu.Append(wx.ID_HELP, '&Help')
        file_Menu.AppendSeparator()

        edit = wx.Menu()
        edit.Append(wx.ID_ANY, '&ZItem')
        edit.Append(wx.ID_ANY, '&YItem')
        edit.Append(wx.ID_ANY, '&WItem')
        
        file_Menu.AppendMenu(wx.ID_ANY, '&Edit', edit)

        option = wx.MenuItem(file_Menu, wx.ID_ANY, '&Exit')

        file_Menu.AppendItem(option)

        self.Bind(wx.EVT_MENU, self.OnQuit, option)
        menu_bar.Append(file_Menu, '&File')

        self.SetMenuBar(menu_bar)
        self.Show(True)

    def OnQuit(self, e):
        self.Close()

frame = wx.App()

Ejemplo_Menu(None, 'Word')
frame.MainLoop()