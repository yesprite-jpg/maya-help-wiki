# “摄影机设置”(Camera Settings)选项

通过“视图 > 摄影机设置”(View > Camera Settings)面板菜单选择这些选项。

#### 透视/正交(Perspective/Orthographic)

默认情况下，从“创建”(Create)菜单创建摄影机时，视图为透视视图。如果想要正交摄影机视图，请禁用该复选框。或者，可以使用热键 Alt+P 在二者之间切换。有关透视摄影机和正交摄影机的详细信息，请参见[控制在视图面板中显示的摄影机](../../../../查看场景/查看场景/导航摄影机/控制在视图面板中显示的摄影机.md)。

#### 可撤消的移动(Undoable Movements)

如果启用，则所有的摄影机移动（如翻滚、平移和缩放）将写入“命令历史记录”(Command History)或“脚本编辑器”(Script Editor)（MEL 日志），使您能够撤消或重做摄影机移动，或复制摄影机移动来将其用于其他摄影机或场景。

默认情况下，“可撤消的移动”(Undoable Movements)处于禁用状态，但是您仍然可以使用 [ 和 ] 来撤消和重做摄影机移动。

#### 忽略二维平移/缩放(Ignore 2D Pan/Zoom)

选择此选项可忽略“二维平移/缩放”(2D Pan/Zoom)设置，从而使您的场景视图显示在完整摄影机视图中。

如果您有两个面板，希望在一个面板中使用平移/缩放细节区域，而在另一个面板中使用完整摄影机视图，则该功能最为有用。

#### 无门(No Gate)

禁用“胶片门”(Film Gate)和“分辨率门”(Resolution Gate)显示。

如果没有通过摄影机查看，则不显示视野（可见体积）。这是默认设置。

视野是摄影机可看到的区域或空间。摄影机视野中的任何对象都显示在从该摄影机视图进行渲染的图像中。 有关视野的图表，请参见[剪裁平面](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-D69C23DA-ECFB-4D95-82F5-81118ED41C95)。

#### 胶片门(Film Gate)

显示一个边界，用于指示摄影机视图的区域（真实世界的摄影机在胶片上进行记录）。胶片门的维度表示摄影机光圈的尺度。

胶片门并不表示渲染区域。使用摄影机“属性编辑器”(Attribute Editor)中的“摄影机光圈”(Camera Aperture)和“胶片适配”(Film Fit)属性，可以自定义该区域。也可以使用“渲染设置”(Render Settings)窗口中的“图像大小”(Image Size)选项来设定渲染分辨率，然后选择锁定“设备纵横比”(Device aspect ratio)，或设定“设备纵横比”(Device aspect ratio)属性。

胶片门视图导向指示仅在摄影机光圈的纵横比和渲染分辨率相同时才进行渲染的摄影机视图区域。

![图：显示一个边界，用于指示摄影机视图的区域（真实世界的摄影机在胶片上进行记录）。胶片门的维度表示摄影机光圈的尺度。 胶片门并…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-4BECE641-E4CB-42FC-99F8-B2AC185EDD27.png) <!-- baize:img-hook downloaded=false reason="正文 2368 字 ≥300，非承重" -->

根据胶片背面大小显示可见视野。窗口的纵横比（或渲染分辨率）确定您实际看到的内容。另外，将摄影机“过扫描”(Overscan)属性设定为 1.5。下图显示胶片门，表示最大可见（或可渲染）区域。

![图：显示一个边界，用于指示摄影机视图的区域（真实世界的摄影机在胶片上进行记录）。胶片门的维度表示摄影机光圈的尺度。 胶片门并…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-54C3D5D0-51A9-4B25-9565-55B17AE1A4A7.png) <!-- baize:img-hook downloaded=false reason="正文 2368 字 ≥300，非承重" -->

#### 分辨率门(Resolution Gate)

“分辨率门”(Resolution Gate)的尺度表示渲染分辨率（要渲染的区域）。渲染分辨率值在视图中显示在“分辨率门”(Resolution Gate)上方。可以在“渲染设置”(Render Settings)窗口的“图像大小”(Image Size)区域中更改这些尺度。

![图：“分辨率门”(Resolution Gate)的尺度表示渲染分辨率（要渲染的区域）。渲染分辨率值在视图中显示在“分辨率门…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-46BE6907-0049-4DE2-8AD0-AF96D82974D3.png) <!-- baize:img-hook downloaded=false reason="正文 2368 字 ≥300，非承重" -->

启用该选项时，将为“渲染设置”(Render Settings)窗口中指定的当前分辨率显示可渲染区域。通常指定比“胶片门”(Film Gate)选项更为精确的渲染图像。另外，将摄影机“过扫描”(Overscan)属性设定为 2.0，以便可以查看指定分辨率以外的更多区域。

**注**

如果胶片背面和分辨率之间的纵横比相同，则生成的两个渲染图像相匹配。

#### 门遮罩(Gate Mask)

启用“门遮罩”(Gate Mask)可更改“胶片门”(Film Gate)或“分辨率门”(Resolution Gate)之外的区域的不透明度和颜色。当“胶片门”(Film Gate)或“分辨率门”(Resolution Gate)处于启用状态时，您只能查看“门遮罩”(Gate Mask)的效果。可以在“显示选项”(Display Options)下的摄影机属性中调整门遮罩的不透明度和颜色。

![图：启用“门遮罩”(Gate Mask)可更改“胶片门”(Film Gate)或“分辨率门”(Resolution Gate…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-000E91B7-0002-41C7-B391-AF4913357BED.png) <!-- baize:img-hook downloaded=false reason="正文 2368 字 ≥300，非承重" -->

#### 区域图(Field Chart)

启用“区域图”(Field Chart)可显示栅格，该栅格表示十二个标准单元动画区域的大小。最大区域大小（第 12 号）与渲染分辨率（分辨率门）相同。必须将“渲染分辨率”(Render Resolution)设定为 NTSC 尺度，该选项才有意义。

#### 安全动作(Safe Action)

如果计划在电视屏幕上显示渲染的图像，请启用该选项来显示一个框，以定义您应在其中保留所有场景动作的区域。

有关“安全动作”(Safe Action)的详细信息，请参见[显示电视制作的安全显示区域](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-13D613FF-994F-480A-AF0E-DFE06418A351)。

#### 安全标题(Safe Title)

如果计划在电视屏幕上显示渲染的图像，请启用该选项来显示一个框，以定义您应在其中保留所有场景文本（标题）的区域。

必须将“渲染分辨率”(Render Resolution)设定为 NTSC 或 PAL 尺度，该选项才有意义。

有关“安全标题”(Safe Title)的详细信息，请参见[显示电视制作的安全显示区域](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-13D613FF-994F-480A-AF0E-DFE06418A351)。

### “填充”(Fill)、“水平”(Horizontal)、“垂直”(Vertical)、“过扫描”(Overscan)（适用于高级用户）

以下选项控制“分辨率门”(Resolution Gate)相对于“胶片门”(Film Gate)的大小。如果分辨率门和胶片门具有相同的纵横比，则这些设置无效。默认设置为“填充”(Fill)。

#### 填充(Fill)

使分辨率门适配胶片门。

自动选择一个水平或垂直适配，以便选定图像填充渲染帧。

#### 水平(Horizontal)

使分辨率门水平适配胶片门。

在渲染帧中为选定图像选择水平适配。

#### 垂直(Vertical)

在胶片门中垂直适配分辨率门。

在渲染帧中为选定图像选择垂直适配。

#### 过扫描(Overscan)

使胶片门适配分辨率门。

在渲染帧中为选定图像选择稍大的适配。
