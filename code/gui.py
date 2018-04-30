import wx

def open_file(event):
    with open(file_name.GetValue()) as file:
        contents.SetValue(file.read())


def save(event):
    with open(file_name.GetValue(), mode='w') as file:
        file.write(contents.GetValue())


# create the object of app
app = wx.App()
# create the window
window = wx.Frame(None, title="Simple Editor", size=(410, 340))
panel = wx.Panel(window)
# label = wx.StaticText(panel, label="Hello World", pos=(100, 100))

# add buttons on the window
open_button = wx.Button(panel, label='Open')
# bind event for button
open_button.Bind(wx.EVT_BUTTON, open_file)
save_button = wx.Button(panel, label='Save')
save_button.Bind(wx.EVT_BUTTON, save)

# add texts on the window
file_name = wx.TextCtrl(panel)
contents = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.HSCROLL)

# create boxsizer
hbox = wx.BoxSizer()
hbox.Add(file_name, proportion=1, flag=wx.EXPAND)
hbox.Add(open_button, proportion=0, flag=wx.LEFT, border=5)
hbox.Add(save_button, proportion=0, flag=wx.LEFT, border=5)

vbox = wx.BoxSizer(orient=wx.VERTICAL)
vbox.Add(hbox, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)
vbox.Add(contents, proportion=1, flag=wx.LEFT | wx.BOTTOM | wx.RIGHT | wx.EXPAND, border=5)

panel.SetSizer(vbox)

# show the window
window.Show()
# execute the main GUI event loop
app.MainLoop()
