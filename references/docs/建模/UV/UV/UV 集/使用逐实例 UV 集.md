# 使用逐实例 UV 集

尽管始终可以将某个特定形状的不同实例与不同的材质相关联，现在可以将不同的 UV 集与不同的实例相关联。在对象的实例上烘焙阴影（例如，照明游戏级别）时，或使用不同的纹理创建单个形状的实例（例如，一堆箱子，其中一些在不同的位置处有孔，等等）时，这非常有用。

如果 UV 集是逐实例的，那么术语 UV 集系列指的就是应用于不同实例的关联 UV 集。在某个给定系列内，可能会将单个 UV 集应用到一个或多个实例。

创建逐实例 UV 贴图

1. 选择形状。

2. 选择“UV > 创建空 UV 集”(UV > Create Empty UV Set) > ![图：选择“UV 创建空 UV 集”(UV Create Empty UV Set) 。 可以选择共享该 UV 集（每个实例都…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-96432FB8-EBE9-4D1A-8DED-5173E032EBC0.png) <!-- baize:img-hook downloaded=false reason="正文 1055 字 ≥300，非承重" -->。

  可以选择共享该 UV 集（每个实例都有该 UV 集）、“逐共享实例”(Per Instance Shared)（所有选定实例都共享新的 UV 集）或“逐非共享实例”(Per Instance Unshared)（所有选定实例都获得一个唯一的 UV 集）。

3. 根据需要命名 UV 集。

4. 选择形状的另一个实例。

5. 在实例上单击鼠标右键，选择 UV 集，并使所创建的逐实例 UV 集成为选定集。

6. 在“创建 UV”(Create UVs)菜单下选择一种 UV 映射类型（如“平面”(Planar)、“圆柱形”(Cylindrical)或“球形”(Spherical)）。确保在映射的选项窗口中已禁用“创建新 UV 集”(Create New UV Set)。

  会为共享当前集的名称的选定实例创建一个新 UV 贴图。

7. 将着色器指定给网格的所有实例。

8. 在实例上单击鼠标右键，然后选择“UV 集 > UV 链接”(UV Sets > UV Linking)。使用“关系编辑器”(Relationship Editor)将任一逐实例集连接到着色器的颜色。

使用硬件纹理在“场景视图”(Scene view)中渲染或显示不同的（逐实例）UV 映射时，现在应该会在实例化对象上显示这些映射。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-7C6E862D-C773-484C-A293-71F5FD874AD9.png) <!-- baize:img-hook downloaded=false reason="正文 1055 字 ≥300，非承重" -->

## 删除逐实例 UV 集

由于可能会有在实例之间共享的 UV 集系列，因此删除 UV 集的方式会略有不同。

例如，名为 myMap 的逐实例集系列有两个子集。一个应用于多个实例（实例 a、b 和 c），另一个仅应用于实例 d。它是当前 UV 集。如果选择实例 d，然后选择“删除当前 UV 集”(Delete Current UV Set)，那么仅会删除实例 d 上的贴图（另一个 UV 贴图由未选定实例使用，不会被删除）。

如果选择实例 a，然后选择“删除当前 UV 集”(Delete Current UV Set)，那么不会从实例 a 共享该 UV 集，但该 UV 集仍存在于实例 b 和 c 上。若要完全删除它，可以选择实例 b 和 c，然后选择“删除当前 UV 集”(Delete Current UV Set)。

## 限制

逐实例 UV 集不支持颜色集或绘制效果。
