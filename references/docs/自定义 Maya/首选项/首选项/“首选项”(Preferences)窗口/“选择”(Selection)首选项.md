# “选择”(Selection)首选项

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Customizing/images/GUID-4AB6AA8F-094A-422B-981B-D2867DCC6E66.png) <!-- baize:img-hook downloaded=false reason="正文 3297 字 ≥300，非承重" -->

可以在[首选项(Preferences)窗口](../“首选项”%28Preferences%29窗口.md)的“选择”(Selection)类别中设置以下首选项。

若要返回到出厂默认设置，请在此窗口中选择“编辑 > 还原默认设置”(Edit > Restore Default Settings)。请注意，这将重置“首选项”(Preferences)窗口中每个类别的首选项。

**注**

要激活背面消隐，以便您可以从您的选择中排除其他面后面的多边形面，请参见

多边形选项

中的

“背面消隐”(Backface Culling)

，或从主菜单中选择

“显示 > 多边形 > 背面消隐”(Display > Polygons > Backface Culling)

。

## 修改器(Modifiers)

修改器可控制 Maya 选择操作。修改器使用遮罩来控制选择项目时显示的内容。可以启用以下一个或多个选项：

#### 单一框选(Single marquee select)

选择层次中的第一个对象。

#### 单击拖动选择(Click drag select)

可用于通过变换工具执行一步式单击拖动。可以使用“移动工具”(Move Tool)移动一个对象，然后单击第二个对象，此时将显示“移动工具”(Move Tool)。这意味着无需再次选择对象和“移动工具”(Move Tool) - 可以对任何后续选定对象继续使用“移动工具”(Move Tool)。默认设置为“禁用”。

#### 影响活动对象(Affects active)

如果将对象选择模式更改为组件选择模式，则选定对象将不会受到影响。通过该选项，可同时选择对象和组件。默认设置为“启用”。

#### 拾取选择器(Pick chooser)

对象在视图中重叠时，通过该选项可显示对象的弹出列表，以便对其进行选择。单击重叠区域以显示菜单。默认设置为“禁用”。当在该列表中选择某个项目时，场景视图中会高光所做选择。列表出现时会使用框标记当前选定的项目。（以前称为弹出菜单选择。）

![图：对象在视图中重叠时，通过该选项可显示对象的弹出列表，以便对其进行选择。单击重叠区域以显示菜单。默认设置为“禁用”。当在该…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Customizing/images/GUID-C0D2CB15-BF57-4C3B-8A27-418333425327.png) <!-- baize:img-hook downloaded=false reason="正文 3297 字 ≥300，非承重" -->

**注**

(Linux) 必须按住鼠标左键才能选择该列表中的项目。

#### 忽略选择优先级(Ignore selection priority)

处理优先级相同的所有对象。无需考虑选择顺序。默认设置为“禁用”。

#### 展开弹出菜单列表(Expand popup list)

如果启用了“展开弹出菜单列表”(Expand Popup List)，则会显示对象的所有弹出列表及层次中其下方的所有内容。默认设置为“禁用”。

![图：如果启用了“展开弹出菜单列表”(Expand Popup List)，则会显示对象的所有弹出列表及层次中其下方的所有内容…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Customizing/images/GUID-845CAD27-4508-4EBE-8FED-7D2EFFAB12F4.png) <!-- baize:img-hook downloaded=false reason="正文 3297 字 ≥300，非承重" -->

#### 选择前亮显(Preselection Highlight)

鼠标光标经过组件时会以不同的颜色亮显这些组件，这有助于定位选择项。例如，如果处于“顶点”(Vertex)模式，当光标移至顶点上时顶点将改变颜色。

![图：鼠标光标经过组件时会以不同的颜色亮显这些组件，这有助于定位选择项。例如，如果处于“顶点”(Vertex)模式，当光标移至…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Customizing/images/GUID-59429F68-29B0-4956-9F00-5F8A770E9868.gif) <!-- baize:img-hook downloaded=false reason="正文 3297 字 ≥300，非承重" -->

**注**

如果要在选择元素时使其亮显，请参见

“显示”(Show)面板菜单

中的

“选择亮显”(Selection Highlighting)

。（

面板菜单

将在场景视图之上显示。）

#### 对组件禁用拾取选择器(Disable pick chooser for components)

选择对对象启用弹出选择，并对组件禁用弹出选择。这有助于防止出现以下情况：已启用“拾取选择器”(Pick Chooser)菜单并处于组件模式下时，可能会在对象反面意外选择不希望选择的面或顶点（这种情况在“使用整面选择面”处于启用状态时最为明显）。

![图：选择对对象启用弹出选择，并对组件禁用弹出选择。这有助于防止出现以下情况：已启用“拾取选择器”(Pick Chooser)…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Customizing/images/GUID-7EB7C3AD-8CCB-4459-8AB1-A36802E3B72E.png) <!-- baize:img-hook downloaded=false reason="正文 3297 字 ≥300，非承重" -->

此行为是“拾取选择器”(Pick Chooser)菜单所引起的结果。若要确保只选中单击组件，请启用“对组件禁用拾取选择器”(Disable Pick Chooser for Components)。

#### 以资产为中心选择(Asset centric selection)

使用该选项，可通过选择资产封装的任何对象来选择该资产。

#### 自动基于摄影机的选择(Automatic camera based selection)

在着色模式中自动激活“基于摄影机的选择”(Camera based selection)，但在线框和 X 射线模式中将其禁用。覆盖其他所有基于摄影机的选择设置。

#### 基于摄影机的选择(Camera based selection)

启用后，无法在着色模式下选择摄影机的视点所遮挡的组件（例如，背面组件或隐藏在前景组件后面的组件）。

#### 自动选择资产(Auto-select asset)

只要将某个节点指定为选择变换，该选项就适用。高级资产为黑色盒装且将节点作为选择变换发布时，如果随后选择该节点，则也会选择该高级资产。

#### 跟踪选择顺序(Track selection order)

该选项允许 Maya 开始跟踪组件的选择顺序。

#### 在大纲视图中自动选择集成员(Auto-select set members in the Outliner)

![图：启用此选项后，选择集时，也会选择其成员。 如果在启用了此选项的情况下右键单击集，“选择集”(Select Set)子菜单…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Customizing/images/GUID-889B2E93-B1A5-42D7-9CB5-4408CC0D7121.png) <!-- baize:img-hook downloaded=false reason="正文 3297 字 ≥300，非承重" -->

启用此选项后，选择集时，也会选择其成员。

如果在启用了此选项的情况下右键单击集，“选择集”(Select Set)子菜单项将显示在“大纲视图”(Outliner)上下文菜单中，而不是“选择集成员”(Select Set Members)。

#### 保留组件选择(Preserve Component Selections)

该选项仅适用于多边形组件。启用后，该选项会在切换选择类型时备份用户的组件选择，并还原要切换到的类型。默认情况下，此选项处于启用状态。

#### 重置选定通道(Reset selected channels)

可用于在选择新对象时清除通道选择。如果此首选项已禁用（默认），则在通道盒中选择属性再选择新对象时，将不重置通道盒属性，而是保留之前选择中的信息，这可能会引起误解。

#### 单击框大小(Click box size)

该选项可控制鼠标指针周围选择区域的大小或单击框的大小。如果选择对象或组件时遇到问题，请尝试调整该选项。例如，单击框大小的值越高，选择曲线可能就越容易。增加单击框大小在具有高分辨率屏幕显示的情况下也非常有用。

#### 预先选择大小(Preselect size)

此选项可确定通过选择前亮显操作亮显组件的最小光标距离。较高的值会在光标距离较远时亮显组件，而较低的值则要求光标距离较近。值为 0 时要求光标正好位于组件的顶部，然后才会亮显组件。

#### 选择未使用空间(Select Dead Space)

在未使用空间中，当光标在对象外时，您可以通过设置选择前容差来选择边和顶点。默认情况下，“选择未使用空间”(Select Dead Space)设置为 4 像素。请参见[在未使用空间中选择](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-B9108D69-E805-4674-8C1C-E4BE1810DFFF)。

#### 调整未使用空间(Tweak Dead Space)

在未使用空间中，当光标在对象外时，您可以通过设置选择前容差来调整边和顶点。默认情况下，“调整未使用空间”(Tweak Dead Space)设置为 120 像素。

#### 选择子对象亮显(Selection Child Highlight)

使用此功能，您可以确定选定父节点时是否也要选择子节点：

- 始终亮显(Always highlight)：选定父节点时始终选择子节点（默认设置）。

- 从不亮显(Never highlight)：选定父节点时从不选择子节点，只选择父节点。

- 使用对象亮显设置(Use object highlight setting)：按照对象的特定设置来确定选定父节点时是否应选择每个子节点。在每个子节点的变换节点“属性编辑器”(Attribute Editor)中，展开“显示”(Display)区域和“选择”(Selection)子区域。选定父节点时会选择启用（默认设置）了其“选择子对象亮显”(Selection Child Highlighting)属性的任何节点。如果禁用该属性，则在选定父节点时不亮显该节点。

## 多边形选择(Polygon Selection)

#### 选择面的方式(Select faces with)

指定希望选择多边形面的方式：

#### 中心(Center)

在中心选择多边形面。也就是说，必须在面的中心单击此框才能选择整面。

#### 整面(Whole Face)

选择整面。单击面上的任意位置（甚至是任何面的边）即可选择该面。

## 优先级(Priority)

可以为对象和组件指定选择优先级。默认情况下，NURBS 曲线的选择优先级高于曲面。这意味着，在选择同时包含 NURBS 曲线和曲面的几何体时，Maya 会先选择 NURBS 曲线，再选择其曲面。

**注**

只能为“自定义”(Custom)预设设置优先级选择。“动画”(Animation)和“渲染”(Rendering)等其他上下文是预设的，但可以在此处进行查看。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Customizing/images/GUID-F2392F2A-112C-4B8F-AEFD-069A41FD8BE8.png) <!-- baize:img-hook downloaded=false reason="正文 3297 字 ≥300，非承重" -->
