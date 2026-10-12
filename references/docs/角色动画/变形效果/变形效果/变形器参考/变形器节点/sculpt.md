# sculpt

## 雕刻历史(Sculpt History)

#### 模式(Mode)

指定雕刻变形器的模式。

#### 翻转(Flip)

在“翻转”(Flip)模式中，变形将在雕刻工具接近目标对象的几何体时发生。此外，“翻转”(Flip)模式会在雕刻工具的中心放置隐式定位器。该模式之所以称为“翻转”(Flip)，是因为雕刻工具的中心通过曲面时，变形的曲面将翻转到雕刻工具的另一侧。

#### 投影(Project)

在“投影”(Project)模式中，雕刻变形器将目标对象几何体投影到雕刻工具的曲面上。投影的范围取决于雕刻变形器的“衰减距离”(Dropoff Distance)属性。此外，“最大置换”(Max Displacement)属性指定投影直接发生在雕刻工具上，发生在雕刻工具内部，还是发生在雕刻工具外部。

#### 拉伸(Stretch)

在“拉伸”(Stretch)模式中，将雕刻工具移离几何体时，受影响的几何体曲面会拉伸或凸起，以追随雕刻工具。拉伸方向是从拉伸原点定位器标记的点到雕刻工具图形的曲面。

#### 内部模式(Inside Mode)

指定变形器如何影响可变形对象中位于雕刻球体内部的点。

#### 环形(Ring)

该模式会将内部点推动到雕刻球体外部，从而在雕刻球体周围创建一种具有轮廓的类环效果。

#### 平坦(Even)

该模式会将内部点在雕刻球体周围均匀地扩散，从而创建一种平滑的球形效果。默认值为“平坦”(Even)。

#### 最大置换(Max Displacement)

指定雕刻球体可以将可变形对象的点从球体曲面推动的距离。使用滑块选择 -10.000 到 10.000 之间的值。默认值为 0.100。“最大置换”(Max Displacement)将使用在 Maya“设置/首选项”(Settings/Preferences)中设置的“工作单位”(Working Units)。

#### 衰减类型(Dropoff Type)

指定雕刻球体的影响范围如何下倾或衰减。影响范围通过“衰减距离”(Dropoff Distance)指定。

#### 无(None)

指定没有下降，即提供突然的衰减效果。

#### 线性(Linear)

指定逐渐下降，即提供线性降低的衰减效果。

#### 衰减距离(Dropoff Distance)

指定雕刻球体的影响范围。请注意，“衰减类型”(Dropoff Type)指定影响范围如何下倾。该效果取决于变形器的“模式”(Mode)属性设置。例如，如果“模式”(Mode)设置为“投影”(Project)，请参见[投影](../“变形”%28Deform%29菜单/雕刻变形器选项%28Sculpt%20Deformer%20Options%29.md#WS1A9193826455F5FF6026605B1181C8F4F2E-3FDD)。

### 添加高级雕刻属性(Add Advanced Sculpt Attribute)

使用“高级雕刻属性”(Advanced Sculpt Attributes)，可以通过 2D 纹理来控制围绕“雕刻”(Sculpt)对象的变形场的强度。这样可以以非均匀的方式变形几何体。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-F531D4FE-F833-438A-B06C-0D4D6F1E48DC.png) <!-- baize:img-hook downloaded=false reason="正文 1923 字 ≥300，非承重" -->

#### 启用高级(Enable Advanced)

启用该属性时，“高级雕刻变形器属性”(Advanced Sculpt Deformer Attributes)将处于活动状态。禁用该属性时，“高级雕刻变形器属性”(Advanced Sculpt Deformer Attributes)将处于非活动状态。

#### 纹理(Texture)

可以设置 2D 纹理来加大雕刻变形器的强度。按照与方向类似的 NURBS 对象相同的方式为雕刻对象指定纹理坐标。

#### 纹理倍增(Texture Multiplier)

设置 2D 纹理对变形的影响强度。

#### 非均匀(Non Uniform)

启用该属性时，Maya 将归一化雕刻变形。如果要补偿可能已应用于目标对象或雕刻变形器的任意非均匀缩放，则启用该属性。

#### 可视化纹理(Visualize Texture)

启用该属性时，将在线框中显示受变形器影响的对象，并且以纹理模式显示变形器本身。这样可以看到所使用的纹理，在绘制变形纹理时非常有用。

![图：启用该属性时，将在线框中显示受变形器影响的对象，并且以纹理模式显示变形器本身。这样可以看到所使用的纹理，在绘制变形纹理时…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-454D3383-9E84-4569-B7EB-E7C91C634543.png) <!-- baize:img-hook downloaded=false reason="正文 1923 字 ≥300，非承重" -->

#### 绘制雕刻贴图(Paint Sculpt Map)

打开“3D 绘制工具”(3D Paint Tool)在变形器的曲面上绘制变形强度。此外，“绘制雕刻贴图”(Paint Sculpt Map)还可创建新的文件纹理并将其连接到雕刻变形器的“纹理”(Texture)属性。如果非文件纹理连接到变形器，则单击该按钮可使其断开连接。

**注**

- 绘制雕刻贴图时，请确保正在绘制的“3D 绘制工具”(3D Paint Tool)属性是“颜色”。否则，绘制的值不会对雕刻变形产生任何影响。可以从“3D 绘制工具”(3D Paint Tool)设置的“文件纹理”(File Textures)区域中的“要绘制的属性”(Attribute to Paint)下拉菜单中设定要绘制的属性。

- 可以通过“3D 绘制工具”(3D Paint Tool)分辨率控制调整雕刻贴图的分辨率。

详细信息请参见[3D 绘制工具设置](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-11EAC728-8E0A-46F6-A0D8-A68E3D60DD13)和[3D 绘制工具](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-11EAC728-8E0A-46F6-A0D8-A68E3D60DD13)（位于手册的“Paint Effects 和 3D 绘制”部分中）。
