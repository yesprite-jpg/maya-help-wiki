# 选择连续边选项(Select Contiguous Edges Options)

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-14F00BDD-AF42-4933-82D1-D7FD3165ABEC.gif) <!-- baize:img-hook downloaded=false reason="正文 520 字 ≥300，非承重" -->

使用这些选项可设置在选择“选择 > 连续边”(Select > Contiguous Edges)时发生的情况。另请参见[选择多边形组件](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-98B65259-DABA-4C5E-9014-4D76B2DE28B3)。

#### 最大 2D 角度(Maximum 2D Angle)、最大 3D 角度(Maximum 3D Angle)

这些设置基于边之间的角度确定当前选择会继续到多远处。如果 Maya 为当前选择考虑某条边，并且它超出了指定的角度，那么自动选择会停止。

2D 角度指的是由曲面拓扑生成的角度，而不考虑曲面的形状。3D 角度指的是由曲面的形状生成的角度，就像在世界空间或局部空间中测量的那样。以下示例说明这些设置的组合如何控制选择。

![图：这些设置基于边之间的角度确定当前选择会继续到多远处。如果 Maya 为当前选择考虑某条边，并且它超出了指定的角度，那么自…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-F6502A66-B5DC-43E0-95E9-CA5A32461B06.png) <!-- baize:img-hook downloaded=false reason="正文 520 字 ≥300，非承重" -->

#### 限制选定边数(Limit number of edges selected)

启用“限制选定边数”(Limit number of edges selected)可设定“每侧边数”(Edges either side)选项。

#### 每侧边数(Edges either side)

每侧边数是 Maya 将在原始选择的任一侧上选择的边数。例如，通过将“每侧边数”设定为较小的值并多次应用“选择连续边”，直到选择了足够的边，可以避免选择太多边。

**注**

提示：

只要选定某个多边形组件，就可以从按住 Ctrl 键并单击鼠标右键时出现的上下文相关多边形标记菜单中访问许多转化选择功能。
