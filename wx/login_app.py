import wx

class Text_Example(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent)

        self.Centre()

        self.panel = wx.Panel(self)
        self.sizer = wx.GridBagSizer(3, 2)

        self.text_user = wx.StaticText(self.panel, label="User")
        self.sizer.Add(self.text_user, pos=(0, 0), flag=wx.TOP | wx.LEFT | wx.BOTTOM, border=5)
        self.text_password = wx.StaticText(self.panel, label="Password")
        self.sizer.Add(self.text_password, pos=(1, 0), flag=wx.TOP | wx.LEFT | wx.BOTTOM, border=5)
        self.text_response = wx.StaticText(self.panel, label="Response")
        self.sizer.Add(self.text_response, pos=(2, 0), flag=wx.TOP | wx.LEFT | wx.BOTTOM, border=5)

        self.text_edit_user = wx.TextCtrl(self.panel)
        self.sizer.Add(self.text_edit_user, pos=(0, 1), span=(1, 3), flag=wx.EXPAND | wx.LEFT | wx.RIGHT)
        self.text_edit_password = wx.TextCtrl(self.panel)
        self.sizer.Add(self.text_edit_password, pos=(1, 1), span=(1, 3), flag=wx.EXPAND | wx.LEFT | wx.RIGHT)

        self.button = wx.Button(self.panel, label="Log in", size=(50, 25))
        self.sizer.Add(self.button, pos=(3, 3), flag=wx.RIGHT | wx.BOTTOM)

        self.panel.Bind(wx.EVT_BUTTON, self.ValidateFunct, self.button)
        self.panel.SetSizerAndFit(self.sizer)

    def ValidateFunct(self, event):
        user = self.text_edit_user.GetValue()
        password = self.text_edit_password.GetValue()

        if user == "Emmanuel" and password == "123":
            self.text_response.SetLabel("Correct password")

            new_window = NewWindow(None)

            new_window.Show()

        else:
            self.text_response.SetLabel("Incorrect password")

class NewWindow(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent)

        panel = wx.Panel(self, -1)
        txt = wx.StaticText(panel, label="Logged in")

app = wx.App(False)
frame = Text_Example(None)

frame.Show()
app.MainLoop()