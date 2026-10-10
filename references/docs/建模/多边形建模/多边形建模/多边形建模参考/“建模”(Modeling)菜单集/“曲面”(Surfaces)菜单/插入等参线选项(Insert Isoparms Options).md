# 插入等参线选项(Insert Isoparms Options)

使用以下选项可设置在选择“曲面 > 插入等参线”(Surfaces > Insert Isoparms)时发生的情况。

#### 插入位置(Insert Location)

“在当前选择处”(At Selection)允许在当前位置创建等参线，可有效创建曲面细分。该选项会启用“多重性”(Multiplicity)选项。

“在当前选择之间”(Between Selections)可在选定等参线或所有 U/V 向等参线之间创建等参线。例如，如果选择一对等参线并启用“在当前选择之间”(Between Selections)，Maya 将在这对等参线中间创建等参线。

请注意，如果启用“在当前选择之间”(Between Selections)并为“多重性”(Multiplicity)设置大于 1 的值（请参见以下选项），Maya 将在选定等参线之间创建均匀隔开的多条等参线。

#### 使用所有曲面等参线(Use all Surface Isoparms)

如果选择整个曲面并选择“在当前选择之间”(Between Selections)，则必须为“使用所有曲面等参线”(Use all Surface Isoparms)选项启用 U 或 V。U 将在所有 U 向等参线之间创建等参线，V 则在所有 V 向等参线之间创建等参线。如果选择一对指定等参线而不是整个对象，Maya 将忽略您的选择（U 或 V）。只在选定等参线之间插入等参线。

#### 多重性(Multiplicity)

允许在选定位置插入多个等参线，如下文所述。新的等参线不会改变曲面的形状。

“设置为”(Set to)选项允许依照“多重性”(Multiplicity)值插入等参线的绝对数。例如，如果“多重性”(Multiplicity)为 3，同时启用了“在当前选择处”(At Selection)，则将在该位置插入三个等参线，无论它是否已拥有等参线。

“增量”(Increase by)选项允许依照“多重性”(Multiplicity)值将额外数量的等参线添加到相应位置。

#### 保持原始(Keep Original)

如果希望保持除带有新等参线的曲面之外的原始曲面，则启用“保持原始”(Keep Original)。

**注**

提示：

若要在插入后使用操纵器重新定位新的等参线，则启用“保持原始”(Keep Original)。单击“插入等参线选项”(Insert Isoparms options)窗口中的“插入按钮”(Insert button)，然后选择“显示操纵器工具”(Show Manipulator Tool)并重新定位大块黄色方形。放置完等参线后，取消选择曲线。

![图：如果希望保持除带有新等参线的曲面之外的原始曲面，则启用“保持原始”(Keep Original)。 提示： 若要在插入后…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-4550BA3C-3F09-45D5-AFE5-6A0A34B887B4.png) <!-- baize:img-hook downloaded=false reason="正文 1289 字 ≥300，非承重" -->

#### 输入曲面(Input Surface)

该信息是只读的。它将显示插入等参线的曲面。“在中间插入”(Insert Between)和“添加结”(Add Knots)属性将影响插入节的位置。

#### 方向(Direction)

该选项会在 U 或 V 向定位等参线。

#### 参数(Parameter)

该选项可设定一个值来重新定位曲面上的等参线。

#### 结数(Number of Knots)

该选项可指定要插入等参线的数量。这与选项窗口中的“多重性”(Multiplicity)选项没有区别。

## 相关主题

- [在曲线或曲面中插入其他编辑点/等参线以添加更多 CV](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/files/GUID-3907B6D2-3FEA-48B7-AED5-26519D6F33AD.htm)
