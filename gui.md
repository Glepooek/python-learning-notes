### 图形用户界面（GUI）

wxPython是最成熟的跨平台Python GUI工具包。

###### 1、创建wxPython示例GUI应用程序

1）创建应用程序对象

```python
import wx

# create the object of app
app = wx.App()
# execute the main GUI event loop
app.MainLoop()
```

2）窗口和组件
窗口也称为框架（Frame），是wx.Frame类的实例。
wx框架中的部件都是由父部件作为构造函数的第一个参数创建的。
如果正在创建一个单独的窗口，就不需要考虑父部件，使用None即可。

```python
import wx

# create the object of app
app = wx.App()
# create the window
window = wx.Frame(None)
# add one button on the window
btn = wx.Button(window)
# show the window
window.Show()
# execute the main GUI event loop
app.MainLoop()
```

3）标签、标题和位置
创建窗口时，可用构造函数的title参数设定窗口的标题，pos参数设定窗口的位置，size参数设定窗口的大小。
创建组件时，可用构造函数的label参数设定组件的标签，pos参数设定组件的位置，size参数设定组件的大小。

```python
# add buttons on the window
open_button = wx.Button(window, label='Open', pos=(225, 5), size=(80, 25))
save_button = wx.Button(window, label='Save', pos=(315, 5), size=(80, 25))

# add texts on the window
file_name = wx.TextCtrl(window, pos=(5, 5), size=(210, 25))
contents = wx.TextCtrl(window, pos=(5, 35), size=(390, 260), style=wx.TE_MULTILINE | wx.HSCROLL)
```

4）更加智能的布局
为使组件能够自适应窗口的大小，可使用尺寸器来管理组件的尺寸。
```python
# create boxsizer
hbox = wx.BoxSizer()
hbox.Add(file_name, proportion=1, flag=wx.EXPAND)
hbox.Add(open_button, proportion=0, flag=wx.LEFT, border=5)
hbox.Add(save_button, proportion=0, flag=wx.LEFT, border=5)

vbox = wx.BoxSizer(orient=wx.VERTICAL)
vbox.Add(hbox, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)
vbox.Add(contents, proportion=1, flag=wx.LEFT | wx.BOTTOM | wx.RIGHT | wx.EXPAND, border=5)

panel.SetSizer(vbox)
```

4）事件处理
事件：用户执行的动作。
为让程序响应事件，可利用组件的Bind方法将事件处理函数链接到给定事件上。

```python
# add buttons on the window
open_button = wx.Button(panel, label='Open')
open_button.Bind(wx.EVT_BUTTON, open_file)
save_button = wx.Button(panel, label='Save')
save_button.Bind(wx.EVT_BUTTON, save)
```
