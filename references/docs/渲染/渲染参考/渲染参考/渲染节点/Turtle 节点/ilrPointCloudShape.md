# ilrPointCloudShape

点云形状用于可视化由 Turtle 生成的点云文件。它由光子贴图、最终聚集点以及从烘焙生成的点云使用。点云形状是通过 Turtle 工具架或使用脚本编辑器中的以下命令创建的：createNode ilrPointCloudShape;

#### 输入文件(Input File)

要可视化的点云文件。

#### 点云类型(Point Cloud Type)

此字段显示加载的点云类型。根据类型的不同，将显示不同的选项。对于“辐照度”(Irradiance)和“辐射”(Radiance)点云，可在“最终聚集选项”(Final Gather Options)下找到其他设置。

#### 重新加载(Reload)

重新加载指定的点云文件。如果已在外部更改文件，可能需要执行此操作。

#### 颜色(Color)

要用于点可视化的颜色。

#### 使用点颜色(Use Point Colors)

如果启用此设置，则将使用点云文件中的颜色信息，而不是上面指定的颜色。该选项对于可视化最终聚集云的强度等等十分有用。

#### 显示 Gamma (Display Gamma)

在 Maya 内查看包含选定 Gamma 的点云。请注意，点云文件始终存储在线性 Gamma (1.0) 中。

#### 点大小(Point Size)

设置要绘制的点的大小。

#### 沿法线置换(Displace Along Normal)

如果点云包含有关法线的信息，则此设置可用于在视口中沿法线置换点。在视口中使用平滑着色处理时，此选项可用于避免曲面上的点相交（深度消隐）。

#### 法线长度(Normal Length)

用于设置可视化点法线的长度。

#### 方向长度(Direction Length)

如果点包含方向（例如，光子的入射方向），则此设置用于设置方向可视化的长度。

#### 最终聚集选项(Final Gather Options)

#### 深度(Depth)

使用点的深度特性确定是否应将其可视化。如果要在一定深度可视化最终聚集的结果，则此选项非常有用。

#### 最大移动和时间(Max Movement and Time)

仅显示假设最大移动在由“时间”(Time)属性指定的时间有效的点。如果“最大移动”(Max Movement)为零，则没有任何影响。

#### 浮点数组选项(Float Array Options)

#### 单元数(Num Elements)

加载的点云中每个点的浮动元素数。

#### 解释(Interpretation)

如果加载的点云是浮点数组点云，则应如何解释这些值？此下拉菜单中显示了所有可用的选项。选择解释之后，可以在“球形谐波选项”(Spherical Harmonics Options)或“光能传递法线选项”(Radiosity Normal Options)下进行其他设置。对于彩色的 SH 点云，可视化器假定先设置所有 R 系数，然后分别是所有 G 系数和 B 系数。最终的 A 通道将被忽略。对于彩色的 RNM 点云，可视化器假定先设置第一个基础向量的所有系数 (RGB)，然后设置第二个向量的所有系数，依此类推。如果还有第四个基础向量可用，则假定在法线方向上对颜色进行编码。

#### 坐标系(Coordinate System)

特定于球形谐波和光能传递法线云。设置用于对 SH/RNM 函数求值的空间（通常是指烘焙所在的空间）。

#### 可视化为球体(Visualize as Spheres)

如果启用此设置，则 SH 点和 RMM 点将使用球体进行可视化。如果禁用，则平行光将用于指定 SH/RNM 函数的求值方向。
