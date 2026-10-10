# 开放/闭合曲面选项(Open/Close Surface Options)

使用以下选项可设置在选择“曲面 > 开放/闭合”(Surfaces > Open/Close)时发生的情况。

#### 曲面方向(Surface Direction)

通过“曲面方向”(Surface Direction)选项、“U”、“V”和“二者”(Both)，可以选择曲面在哪个方向是开放或周期性的。下图显示了这些选项如何用于闭合有倒角的曲线。

![图：通过“曲面方向”(Surface Direction)选项、“U”、“V”和“二者”(Both)，可以选择曲面在哪个方向…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-4F056557-3DF3-462E-AF74-28744D67479E.png) <!-- baize:img-hook downloaded=false reason="正文 714 字 ≥300，非承重" -->

#### 形状(Shape)

“忽略”(Ignore)不会保留原始选择的形状。

“保留”(Preserve)会根据需要添加或删除控制点以保留原始曲面的形状。该选项是默认设置。

“融合”(Blend)会尝试强制对输入曲面施加连续性，并使用融合偏移设置确定将出现的平滑度。

**注**

如果端点相接，可以在启用“保留”(Preserve)设置时闭合它们，您可能会接收到相互交叉的 CV，并在移动 CV 时在曲面中导致循环。在这些情况下，请改为启用“融合”(Blend)设置。

#### 融合偏移(Blend Bias)

改变新曲面的连续性程度；值越大，原始曲面的切线的扭曲程度会随之增加。

#### 插入结(Insert Knot)

仅当选择“形状”(Shape)对应的“融合”(Blend)选项时，该选项才可用。将会沿接合缝插入结，并允许您为“插入参数”(Insert Parameter)设定值。

#### 插入参数(Insert Parameter)

控制插入的结对融合变形的影响程度。

#### 保持原始(Keep Original)

设定在开放/闭合后是否保留原始曲线或曲面。

## 选择等参线来更改周期方向

可以从选项窗口选择希望曲面在哪个方向是周期性的，也可以单击来选择曲面上的等参线。执行该操作时，会覆盖选项窗口的中“曲面方向”(Surface Direction)设置。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-BCE3108E-2A95-439C-8FDD-CECC9308BE74.png) <!-- baize:img-hook downloaded=false reason="正文 714 字 ≥300，非承重" -->

## 相关主题

- [使曲线或曲面开放或闭合](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/files/GUID-17B86448-0237-4369-AB7A-8F381FEAACA7.htm)
