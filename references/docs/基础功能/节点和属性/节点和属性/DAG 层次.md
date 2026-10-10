# DAG 层次

DAG 层次（也称为对象层次）是指组成对象的所有节点的父子关系。DAG 代表有向非循环图。从本质上讲，DAG 是关于如何通过一个几何体构建对象的实例的受控关键点。

对象的 DAG 层次始终包括两种类型的节点：变换和形状。

例如，在创建多边形球体时，可以在“属性编辑器”(Attribute Editor)中看到它包括一个形状节点和一个变换节点。形状节点具有用于定义几何体的属性，而变换节点包含控制球体的位置、缩放或旋转的属性。形状节点是变换节点的子对象。

**注**

在 Maya API 中，将 DAG 层次节点与依存关系图 (DG) 节点进行比较。这些是相关但不同的系统，用途不同。依存关系图节点与 DAG 节点不同，可以循环，这意味着它们可以双向传递信息。

还可以通过 Hypergraph 窗口以层次形式查看 DAG 信息。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-33AB063A-7432-4387-A1E2-76F29BF9AA61.png) <!-- baize:img-hook downloaded=false reason="正文 667 字 ≥300，非承重" -->

#### 变换节点

变换节点包含变换信息（平移、旋转、缩放）以及建立父子关系信息。变换节点下面具有多个分组的子节点。节点分组允许在多个 DAG 路径中共享同一形状。（DAG 路径表示节点之间的层次链接，定义从层次的开始向下到最远的节点的方向。）

例如，如果构建手的模型并要应用单个变换以旋转手掌和手指（而非各个单独旋转），可以对手掌和手指使用公用父变换节点。

![图：变换节点包含变换信息（平移、旋转、缩放）以及建立父子关系信息。变换节点下面具有多个分组的子节点。节点分组允许在多个 DA…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-4DF34593-E4E9-416D-BD11-B908333AB3D2.png) <!-- baize:img-hook downloaded=false reason="正文 667 字 ≥300，非承重" -->

#### 形状节点

形状节点描述几何体，不包含建立父子关系或变换信息。几何体不能在变换节点之下。这意味着任意一个几何体都需要有两个 DAG 节点在其上方，一个形状节点在其正上方，以及一个变换节点在形状节点上方。

还可以在打开“大纲视图”(Outliner)窗口并选择[仅 DAG 对象(DAG Objects Only)](大纲视图%28Outliner%29/“大纲视图”%28Outliner%29菜单.md#GUID-2EDE871D-ECA9-4D9F-90DF-FCA1FFF492F8__WS1A9193826455F5FF-4F542F6211C79DEA861-1D29)时，查看运行中的 DAG 层次

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-178B8CE3-D628-4738-A147-CF4F2EFBE085.png) <!-- baize:img-hook downloaded=false reason="正文 667 字 ≥300，非承重" -->
