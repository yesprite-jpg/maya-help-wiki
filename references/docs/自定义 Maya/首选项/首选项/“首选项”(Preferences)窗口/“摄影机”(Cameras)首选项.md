# “摄影机”(Cameras)首选项

可以在[首选项(Preferences)窗口](../“首选项”%28Preferences%29窗口.md)的“摄影机”(Cameras)类别中设置以下首选项。

若要返回到出厂默认设置，请在此窗口中选择“编辑 > 还原默认设置”(Edit > Restore Default Settings)。请注意，这将重置“首选项”(Preferences)窗口中每个类别的首选项。

## 默认摄影机(Default Cameras)

为摄影机设定近剪裁平面和远剪裁平面值。有关详细信息，请参见[剪裁平面](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-D69C23DA-ECFB-4D95-82F5-81118ED41C95)。

## 动画显示摄影机过渡(Animate Camera Transitions)

默认情况下，视图摄影机现在会对摄影机位置之间的过渡设定动画。

启用或禁用任何动画过渡：

- 适配视图(Fit view)

- 适配所有视图(Fit all view)

- 转至书签(Go to bookmark)

- 下一/上一摄影机视图(Next/Last camera view)

若要选择过渡使用的时间量，请使用滑块设定值或在提供的框中键入值。可选择值的范围在十分之一秒到五秒之间。

**注**

为了提高性能，在大型场景中对摄影机过渡设定动画时，Maya 将对较少的帧设定动画。

## 查看拟合(View Fit)

调整默认的“拟合系数”(Fit Factor)值，以指定当执行“框显当前选择”(Frame Selection)（热键 F）或“框显全部”(Frame All)（热键 A）时应使用框显项填充的视图的百分比。该值将确定框显选定或所有对象时，摄影机应放大显示对象的接近程度。

对于“框显当前选择”(Frame Selection)，可以通过执行带有 -fitFactor 标志的 viewFit 命令为一个特定实例覆盖此设置。请参见[框显选定对象](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-DB6732A4-2ACD-4A71-8D95-C090F9907B50)。
