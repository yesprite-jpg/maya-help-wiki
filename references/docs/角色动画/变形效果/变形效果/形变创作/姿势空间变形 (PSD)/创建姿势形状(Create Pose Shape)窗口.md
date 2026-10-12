# 创建姿势形状(Create Pose Shape)窗口

单击“添加姿势”(Add Pose)按钮或者在[姿势编辑器](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-2AB6C4C3-75AC-4094-A65C-C232739AFB30.htm)中选择“姿势 > 添加姿势”(Poses > Add Pose)以创建姿势，且姿势插值器节点尚未连接到融合形变变形器时，该窗口将会显示。您既可以选择现有的融合形变变形器，也可以在此处创建一个将与该姿势关联的新姿势。

- 选择“创建姿势形状”(Create Pose Shape)选项可激活这些选项，以便创建与此姿势关联的修正融合变形。如果姿势不是用来驱动形状，请取消选择此选项。

- 融合形变变形器(Blend Shape Deformer)：将向其添加姿势形状的融合形变变形器。如果蒙皮网格上已存在一个或多个融合形变变形器，请从该列表中选择一个。

  否则，请选择新建(New)，以在对象上创建融合形变变形器。创建的姿势形状将作为目标形状添加到此融合形变变形器。

- 名称(Name)：显示您在上述列表中选择的融合形变变形器的名称。

  如果要创建新的融合形变变形器，请在此处输入其名称。您可能希望使用 PSD 作为前缀或后缀，以标识该融合形变变形器的用途。

- 基础网格(Base Mesh)：要在其上创建融合形变变形器的网格。

  - 绑定到关节(Bound to joint)：将融合形变变形器添加到当前绑定到具有姿势插值器节点的关节的蒙皮网格。

  - 选定(Selected)：选择另一个网格作为要向其添加融合形变变形器的对象。

- 变形顺序(Deformation Order)：选择融合变形节点在对象的构建历史中相对于蒙皮变形器存在的位置。有关信息，请参见[融合变形选项(Blend Shape Options)](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-C954C197-6D56-4EB8-BEA0-70DD1BBBAD6B.htm)中的“高级”(Advanced)选项卡。

- 单击“创建姿势形状”(Create Pose Shape)，以创建新的融合形变变形器及其姿势相关目标形状。
