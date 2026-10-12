# 创建 PSD 网络选项

若要打开“创建 PSD 网络选项”(Create PSD Network Options)，请选择[“Hypershade”窗口](../../../Hypershade%20窗口.md)中的“编辑 > 创建 PSD 网络”(Edit > Create PSD Network)，或选择“渲染”(Rendering)菜单集中的“纹理 > 创建 PSD 网络”(Texturing > Create PSD Network)。

#### 图像名称(Image Name)

输入将要绘制的 Adobe Photoshop 文件的名称。默认情况下，Maya 使用场景名称和模型名称。

#### 大小 X (Size X)

设定水平分辨率（以像素为单位）。

#### 大小 Y (Size Y)

设定垂直分辨率（以像素为单位）。

#### 保持纵横比(Keep Aspect Ratio)

约束 X 和 Y 分辨率的比例。即，如果移动 X 滑块，Y 滑块也会移动相应的距离。

#### 包括 UV 快照(Include UV Snapshot)

创建 UV 快照作为参考，以帮助在 Adobe Photoshop 中使用更高精确度进行绘制。

#### 顶部/底部位置(Position Top/Bottom)

确定在 Adobe Photoshop 中层堆栈的顶部还是底部创建 UV 层。

#### UV 集(UV Set)

指定要用于“UV 快照”(UV Snapshot)的“UV 集”(UV Set)。

#### 颜色值(Color Value)

指定要用于快照图像中 UV 网格的颜色。

#### 抗锯齿线(Anti-alias Lines)

指定形成快照图像中 UV 网格的线是否抗锯齿。抗锯齿线看上去更平滑，但可在具有不同不透明度的多个像素上延伸。

#### 属性(Attributes)、选定属性(Selected Attributes)

从材质的默认“属性”(Attributes)列表中进行选择。（如果需要更多高级选项，请打开“详细属性列表”。）

“选定属性”(Selected Attributes)列表中的选定属性表示要绘制的通道。在 Adobe Photoshop 中打开 PSD 文件后，此处列出的每个属性都显示为层集。

下表显示了与创建 PSD 文件时所创建的层集对应的默认可用通道。

|  | Lambert | Blinn | Phong | Phong E |
|---|---|---|---|---|
| 颜色(Color) | 是 | 是 | 是 | 是 |
| 透明度(Transparency) | 是 | 是 | 是 | 是 |
| 环境色(Ambient Color) | 是 | 是 | 是 | 是 |
| 白炽度(Incandescence) | 是 | 是 | 是 | 是 |
| 凹凸贴图(法线摄影机) (Bump Map (Normal Camera)) | 是 | 是 | 是 | 是 |
| 位移(Displacement) | 是 | 是 | 是 | 是 |
| 偏心率(Eccentricity) |  | 是 |  |  |
| 镜面反射衰减(Specular Roll Off) |  | 是 |  |  |
| 粗糙度(Roughness) |  |  |  | 是 |
| 高光大小(Highlight size) |  |  |  | 是 |
| 白度(Whiteness) |  |  |  | 是 |
| 余弦幂(Cosine Power) |  |  | 是 |  |

#### 详细属性列表(Detailed Attribute List)

显示更加详细的可绘制高级选项列表。
