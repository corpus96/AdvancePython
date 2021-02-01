import wx

class Text_Example(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent)
        self.InitUi()
        self.Centre()

    def InitUi(self):
        self.panel = wx.Panel(self)
        self.sizer = wx.GridBagSizer(3, 2)

        self.text = wx.StaticText(self.panel, label="Name:")
        self.sizer.Add(self.text, pos=(0, 0), flag=wx.TOP | wx.LEFT | wx.BOTTOM, border=5)

        self.newtext = wx.StaticText(self.panel, label="My name is")
        self.sizer.Add(self.newtext, pos=(1, 0), flag=wx.TOP | wx.LEFT | wx.BOTTOM, border=5)

        self.textedit = wx.TextCtrl(self.panel)
        self.sizer.Add(self.textedit, pos=(0, 1), span=(1, 3), flag=wx.EXPAND)

        self.botton = wx.Button(self.panel, label='Send', size=(90, 50))
        self.sizer.Add(self.botton, pos=(3, 3), flag=wx.RIGHT | wx.BOTTOM)

        self.panel.Bind(wx.EVT_BUTTON, self.TakeText, self.botton)

        self.panel.SetSizerAndFit(self.sizer)

    def TakeText(self, event):
        texttaken = "Hello World"
        texttaken = self.textedit.GetValue()
        
        self.newtext.SetLabel(texttaken)

app = wx.App(False)
frame = Text_Example(None)

frame.Show()
app.MainLoop()
