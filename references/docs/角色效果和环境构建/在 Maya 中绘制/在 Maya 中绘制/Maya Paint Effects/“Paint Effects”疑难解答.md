# “Paint Effects”疑难解答

以下是使用“Paint Effects”时可能遇到的问题的解决方法。这些问题包括：

## 笔划未绘制，且显示错误消息

如果笔刷非常厚重，且在笔刷笔划中分段或多边形面的数量超过 1000000，则会显示一条消息，并且不会绘制笔刷笔划。这样可避免显示被锁定，并可防止笔划质量受到影响。

若要解决该问题，请简化笔刷。或者，如果内存不是问题，请增大隐藏的 maxDrawSegments 属性的值（其默认值为 1000000）。

若要将 maxDrawSegments 更改为更大的值（例如，5000000），请发出以下 MEL 命令：

```text
setAttr strokeShape1.maxDrawSegments 5000000
```

其中 strokeShape1 是笔划、pfxHair 或 pfxToon 节点的名称。

若要设定它，使其不存在任何限制，请执行下列操作：

```text
setAttr strokeShape1.maxDrawSegments 0
```

**注**

提示：

降低笔划的

“显示质量”(Display Quality)

将简化笔划显示并避免触及该警告，尽管笔划的形状也可能会改变。通过禁用

“绘制为网格”(Draw As Mesh)

也可以使笔划的更多部分显示出来，尽管它将处于某个简单的线框中。

若要减少三角形计数，请降低“管分段”(Tube Sections)值（“生成 > 网格质量属性”(Generate > Mesh Quality Attributes)）。

## 绘制的笔划看起来太暗

执行下列操作之一：

- 向场景中添加灯光。

- 在笔刷“属性编辑器”(Attribute Editor)的“照明”(Illumination)区域中，禁用“真实灯光”(Real Lights)。

- 如果笔刷颜色带有纹理，请检查该笔划“Color1”值是否不是黑色；如果纹理是文件纹理，请检查是否可以找到图像文件。

## 在场景中管状体看起来太小

为笔刷增大“全局比例”(Global Scale)，或者增大“场景比例”(Scene Scale)。

## 渲染的笔划由圆形构成

以很小的增量增大笔刷的“图章密度”(Stamp Density)以避免将该值设置得过大。

## 管状体看起来在曲线型截面上有锯齿或有分段

为笔刷增大管状体分段的数量（“管 > 创建”(Tubes > Creation)）。

## 反馈不反映渲染的图像

提高“显示质量”(Display Quality)或确保处于场景绘制视图中。

## 画布会清除为黑色，即使更改了画布的颜色

可以查看 Alpha 平面。选择“显示 > 所有通道”(Display > All Channels)并再次清除。

## 笔刷笔划看起来通过曲面的接合边漏出

在单个曲面的接合边上绘制（例如，通过复制面的一半并将其附加到第一半上而创建的面上的中心线），且笔刷笔划看起来通过接合处漏出，并跳到头部的背面。

确保曲面在 U 方向和 V 方向上是周期性的。

## “全局比例”(Global Scale)笔刷设置看起来会被忽略

检查“Paint Effects 全局参数”(Paint Effects Globals)。会将所选择的下一个笔刷预设的“全局比例”(Global Scale)与“画布比例”(Canvas Scale)或“场景比例”(Scene Scale)值相乘，具体取决于绘制所在的位置。

## 尝试共享笔刷，但共享了错误的笔刷

选择“生成 > 共享一个笔刷”(Generate > Share One Brush)时，选定的笔划会共享最后选择的笔划（称为主要选择对象，默认情况下该对象会亮显为绿色）的笔刷。

## 笔划纹理颜色与为纹理设定的颜色不匹配

将纹理映射到笔刷颜色，但是当绘制笔划时，这些纹理颜色与为纹理设定的颜色不匹配。

如果将纹理映射到笔刷颜色，则会将纹理颜色值（“Tex Color1”和“Tex Color2”）与笔刷颜色值（“Color1”）相乘。若要确保绘制的纹理颜色与为笔刷设定的纹理颜色匹配，请将笔刷颜色设定为白色（值 1）。

## Wacom 光笔和绘图板没有压力敏感度

在 Linux 上的“Paint Effects”中绘制笔划时，Wacom 光笔和绘图板没有压力敏感度。

选择“Artisan”工具（例如，“绘制选择工具”(Paint Selection Tool)），然后打开“工具设置”(Tool Settings)编辑器。展开“光笔压力”(Stylus Pressure)区域。如果已灰显“光笔压力”(Stylus Pressure)选项，那么 Maya 将找不到 Wacom 绘图板。绘图板可能会安装在通用名称“tablet”下面。

若要在 Linux 上解决该问题，请转到 Wacom 网站 ([https://www.wacom.com/zh-cn](https://www.wacom.com/zh-cn)) 并阅读适用于 Linux 的产品支持信息。

## 安装了新的绘图板但“Paint Effects”无法识别它

安装了新的绘图板，但现在压力敏感度在“Paint Effects”中不起作用。

若要解决该问题，请重置笔刷（“生成 > 重置模板笔刷”(Generate > Reset Template Brush)）。

## 绘制的笔划看起来与选定笔刷预设一点也不像

选择了一个笔刷预设，然后绘制一个笔划，但产生的笔划没有使用为笔刷预设定义的值。

可能会打开“笔刷预设融合”(Brush Preset Blend)窗口。当该窗口打开时，每次选择一个笔刷预设，就会根据融合设置将选定笔刷预设的着色和形状值与模板笔刷中的值相融合。

若要避免再次发生这种情况，请为融合（“BrushPresetBlend”、“BrushPresetBlendShape”、“BrushPresetBlendShading”）设定热键。

若要融合，请在“笔刷预设融合”(Brush Preset Blend)窗口中设置着色和形状比例，然后关闭该窗口。选择第一个笔刷，按住融合热键，然后选择要融合的笔刷预设。按下热键时，每次单击某个预设，就会将这些值与模板笔刷值融合。释放热键可停止融合。

## 管状体生长和纹理流出现不同步

同时设置管状体生长和纹理流的动画（例如，带纹理的树的生长），而纹理的流动速度看起来比树的生长速度要快。

若要解决该问题，请选择笔划，然后在“Paint Effects 笔刷设置”(Paint Effects Brush Settings)窗口的“流动画”(Flow Animation)区域中启用“纹理流”(Texture Flow)。

## 为流动画设定了“开始时间”(Start Time)，但不显示管状体

开始时间和结束时间是以秒为单位进行度量的，因此，举例来说，如果将“开始时间(秒)”(Start time (seconds))框设置为 60，并且“时间”(Time)单位为 24 fps（选择“窗口 > 设置/首选项> 首选项”(Windows > Settings/Preferences > Preferences)，然后单击“设置”(Settings)类别），那么直到第 1440 帧动画才会开始。

如果知道需要管状体显示在哪一帧上，请将该帧的编号除以由“时间”(Time)单位定义的每秒帧数，以确定要在“开始时间(秒)”(Start time (seconds))框中输入哪个值。例如，如果需要管状体显示在第 60 帧上，且“时间”(Time)单位设定为“NTSC(30fps)”(NTSC (30 fps))，请将 60 帧除以每秒 30 帧，得到开始时间为 2 秒。

可以通过在字段中创建表达式来执行该计算。键入等号 (=)，后面跟着计算。在上一个示例中，可键入：

```text
=60.0/30
```

请注意，时间必须有一个浮点小数。

## 在几何体周围它与笔划重叠的位置会显示锯齿

请参见 Paint Effects 笔划相对于场景中的其他对象以错误的顺序渲染部分。

## 可以修改应用到曲面的纹理，但曲面不会更新

在画布上，确保启用了“自动保存”(Auto Save)。如果使用的是 Windows，可能还必须将“硬件纹理分辨率”(Hardware Texture resolution)（在着色器“属性编辑器”(Attribute Editor)中）更改为除“默认”(Default)值”之外的其他值。

## 场景绘制视图的 Alpha 平面显示为白色

场景绘制视图的 Alpha 平面完全是白色的。若要查看场景绘制视图的 Alpha，请渲染场景（“渲染 > 渲染当前帧”(Render > Render Current Frame)），然后在“渲染视图”(Render View)中，选择“显示 > Alpha 通道”(Display > Alpha Channel)。

## 尝试在曲面上绘制，但笔划绘制在视图平面上

禁用“在深度模式下绘制”(Paint At Depth)（[“Paint Effects > Paint Effects 工具”(Paint Effects > Paint Effects Tool)](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharEffEnvBuild/files/GUID-914D2430-7CA2-4CAA-866B-22D293DCC013.htm) > ![图：禁用“在深度模式下绘制”(Paint At Depth)（“Paint Effects Paint Effects 工具…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharEffEnvBuild/images/GUID-96432FB8-EBE9-4D1A-8DED-5173E032EBC0.png) <!-- baize:img-hook downloaded=false reason="正文 5554 字 ≥300，非承重" -->）。

## 笔划会花费很长的时间进行渲染

有一个场景，其中包含使用相同笔刷创建的许多笔划（例如，一片玉米田），并且需要花费很长时间进行渲染。

请尝试通过减少“分段”(Segments)、“叶分段”(Leaf Segments)和“花瓣分段”(Petal Segments)的数量来简化笔刷。

也可以尝试在笔刷上使用纹理，以提供细节，而不是管状体。例如，如果要绘制一片玉米田，请渲染只适配单个管状体的单个玉米秸秆的长细条状图像（包含以黑色为背景的 Alpha），并将该图像用作包含单个管状体的笔刷上的纹理。（有关该技术的示例，请查看 pineTextured 笔刷。）可以将该方法用于不在特写镜头中的秸秆。使管状体的摆动随机化，以使秸秆看起来不相同。为了变化，也可以使用具有不同纹理的不同笔刷。

## Paint Effects 笔划相对于场景中的其他对象以错误的顺序渲染

“Paint Effects”使用由扫描线渲染器生成的深度缓冲区来确定遮挡。对于多个曲面在单个像素内可见的渲染效果（如透明度、抗锯齿边缘、运动模糊、灯光雾和体积密度），这样做会产生问题，因为存在一个深度值和一个每像素颜色用于将绘制效果合成进去。

可以影响渲染器决定以下事项的方式：如何使用摄影机“深度类型”(Depth Type)将一个像素内可见的多个深度值减少到单个输出深度值（在“属性编辑器”(Attribute Editor)的“输出设置”(Output Settings)区域中）。

借助“最远可见深度”(Furthest Visible Depth)，位于这些元素后面的“Paint Effects”笔划将穿通，就好像它们完全在前面一样。

“最近可见深度”(Closest Visible Depth)拾取像素内离摄影机最近的曲面。这样，透明曲面或运动模糊条纹将完全遮挡它们后面的所有“Paint Effects”笔划。“阈值”(Threshold)值确定透明度，在该透明度下，曲面将不会显示在深度缓冲区中。

### 透明度、透明度贴图

在渲染摄影机的“输出设置”(Output Settings)中，请将“深度类型”(Depth Type)属性设定为“最近可见深度”(Closest Visible Depth)，然后调整“阈值”(Threshold)。

#### 抗锯齿边缘

- 在渲染摄影机的“输出设置”(Output Settings)中，启用“深度”(Depth)，然后将“深度类型”(Depth Type)设定为“最远可见深度”(Furthest Visible Depth)。

- 为对象禁用抗锯齿，以较大的大小渲染对象和“Paint Effects”笔划，然后使用第三方软件产品来减小渲染的大小，并对其重新采样。

#### 透明度、透明度贴图和抗锯齿边缘

- 单独地渲染“Paint Effects”笔划并合成。

- 将“Paint Effects”笔划转化为多边形。

## 阶梯状网格笔刷

网格笔刷将具有阶梯状（锯齿）边，除非启用了“Paint Effects”“过采样”(Oversample)（“渲染设置”(Render Settings)窗口的“Maya 软件”(Maya Software)选项卡的“Paint Effects 渲染选项”(Paint Effects Rendering Options)区域）。

## 笔划看上去未完成，例如，树没有完成绘制

Maya 将在场景视图中绘制的分段或多边形面的最大数量默认为 1000000。该值由一个称为 maxDrawSegments 的隐藏属性控制。使用 maxDrawSegments 属性，在达到最大值时，笔划就会停止绘制；笔划不会改变形状，它只是不完整（但是，批渲染将完成）。在笔划上将 maxDrawSegments 设定为零会使笔划变成无限大，也就是说，Maya 将一直绘制，直到完成笔划或内存不足为止。

设定该值可防止非常厚重的笔刷锁定交互式显示。如果超出该限制，将显示一条警告消息：

仅部分绘制了 <strokeName>。有关详细信息，请参见 Maya 帮助中的“maxDrawSegments”。

如果希望显示完整的笔划，且有可用内存，那么请在笔划的 maxDrawSegments 属性上执行 setAttr。例如：

```text
setAttr strokeShape1.maxDrawSegments 10000000
```

若要设定它，使其不存在任何限制，请执行下列操作：

```text
setAttr strokeShape1.maxDrawSegments 0
```

其中 strokeShape1 是笔划、pfxHair 或 pfxToon 节点的名称。

执行该 setAttr 的唯一意义在于，如果需要以交互方式在单个笔划上显示多于默认的 1000000 个多边形。

**注**

提示：

降低笔划的

“显示质量”(Display Quality)

将简化笔划显示并避免触及该警告，尽管笔划的形状也可能会改变。通过禁用

“绘制为网格”(Draw As Mesh)

也可以使笔划的更多部分显示出来，尽管它将处于某个简单的线框中。

若要减少三角形计数，请降低“管分段”(Tube Sections)值。（“生成 > 网格质量属性”(Generate > Mesh Quality Attributes)）
