# 关系编辑器(Relationship Editor)

- 在主菜单栏中：“窗口 > 关系编辑器”(Windows > Relationship Editors)

- 在场景视图中：“面板 > 面板 > 关系编辑器”(Panels > Panel > Relationship Editor)

使用“关系编辑器”(Relationship Editor)编辑关系，其中关系是对象或组件的集合或分组。这些关系包括：

- 集

- 变形器集

- 角色集

- 划分

- 显示层

- 渲染层

- 渲染过程集

- 动画层

- 动力学关系

- 灯光链接（以灯光为中心和以对象为中心）

- UV 链接（以纹理为中心、以 UV 为中心、Paint Effects/UV、头发/UV 和毛发/UV）

- 头发/毛发链接

  **注**

  “关系编辑器”(Relationship Editor)独立于“动力学关系编辑器”(Dynamic Relationships Editor)，用于控制粒子对象的关系。

## 相关主题

- [组织显示层上的对象](组织显示层中的对象/创建和管理显示层.md)

- [创建和编辑集](集和划分/创建和编辑集.md)

- [防止集的组合中有重叠的成员身份](集和划分/创建划分以避免集成员身份重叠.md)

- [在动画层中添加和移除属性](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-E7E41BFB-30F9-45BF-AAB9-D4FD59338F78)

## “关系编辑器”(Relationship Editor)菜单

### 列表(List)

#### 自动加载所有集(Auto Load All Sets)

启用该选项可自动显示场景中选定类型的所有关系。这是默认设置。

#### 手动加载集(Manual Load Sets)

启用该选项可通过选择下列选项之一来显示关系：

#### 从当前选择加载集(Load Set from Selection)

仅显示与该场景中选定的对象关联的关系。

#### 从当前选择添加集(Add Set from Selection)

添加以显示与该场景中选定的对象关联的关系。

#### 从当前选择中移除集(Remove Set from Selection)

移除以不显示与该场景中选定的对象关联的关系。

显示对象

1. 在右侧面板中，从“列表”(List)菜单中选择下列选项之一。

  #### 自动加载全部(Auto Load All)

  启用该选项可自动显示场景中的所有对象。

  #### 自动加载当前选择(Auto Load Selection)

  启用该选项可自动显示与场景中选定对象关联的关系中的对象。

  #### 手动加载(Manual Load)

  启用该选项可通过选择下列选项之一来显示对象：

  #### 从当前选择加载列表(Load List from Selection)

  仅显示选定对象。

  #### 将当前选择添加到列表(Add Selection to List)

  添加以显示场景中选定的对象。

  #### 从列表中移除当前选择(Remove Selection from List)

  移除以不显示场景中选定的对象。

## “关系编辑器”(Relationship Editor)工具栏

#### 下拉菜单

控制要编辑的关系类型。这与“窗口 > 关系编辑器”子菜单中的项目相同。

#### 加号和减号图标

在编辑类似资产的某个关系（例如集、划分或角色）时，通过加号和减号图标，可从编辑器中亮显的资产中添加或移除当前选择。

例如，如果要编辑集，可以在编辑器的左侧亮显一个集，并单击加号图标以将当前选定的对象添加到该集中。

## 面板

- 在每个面板顶部的文本框中键入文本以仅显示其名称中包含该文本的项目。单击文本框左侧的图标以打开或关闭过滤器。

- 单击左侧的某个集，然后单击右侧的项目以亮显或取消亮显它们。右侧亮显的项目将连接到左侧的项目。
