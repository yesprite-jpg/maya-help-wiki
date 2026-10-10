# 平视显示仪 (HUD) 选项

对 Maya 平视显示仪 (HUD) 解算管理器状态消息进行了更改，以更好地反映解算管理器 (EM) 的状况。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-18F963A9-A2D7-4CA7-B4B1-EDBC323666BF.png) <!-- baize:img-hook downloaded=false reason="正文 3897 字 ≥300，非承重" -->

从“显示 > 平视显示仪”(Display > Heads Up Display)菜单中选择这些选项。

**注**

按 Ctrl 键以使此菜单在您从中选择多个选项时保持打开状态。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-1E3BB73B-F26D-4582-97DB-359BF4E0A6F5.png) <!-- baize:img-hook downloaded=false reason="正文 3897 字 ≥300，非承重" -->

#### 动画详细信息(Animation Details)

启用或禁用动画详细信息列表的显示，包括“播放速度”(Playback Speed)、“当前角色”(Current Character)以及“IK 融合”(IK Blend)。详细信息显示在面板右下角的“帧速率”上方。默认设置为禁用。

#### 缓存(Cache)

显示播放缓存和内存使用情况的详细信息。

**注**

您可以从

解算工具包(Evaluation Toolkit)

中启用此选项。

请参见[解算工具包(Evaluation Toolkit)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-E22B253D-914B-4056-93F5-755702A6C998)主题中的“缓存”(Caching)以及[使用“缓存播放”(Cached Playback)以提高播放速度](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-D3D1DC33-D0CE-4BE3-B287-CDD4DC0B72C3)。

#### 摄影机名称(Camera Names)

在视图面板的底部正中显示摄影机名称（例如，透视、顶、侧、前）。默认设置为启用。

#### 大写锁定(Caps Lock)

显示启用“大写锁定”(Caps Lock)时的视图中消息。默认设置为启用。

#### 当前资产(Current Asset)

如果已设置，则创建的任何后续节点都将自动添加到该资产。

#### 当前帧(Current Frame)

在右下角显示当前播放帧的编号。默认设置为禁用。

#### 解算(Evaluation)

![图：指示当前的解算模式。请参见“首选项 动画”(Preferences Animation)中的“解算”(Evaluatio…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-18F963A9-A2D7-4CA7-B4B1-EDBC323666BF.png) <!-- baize:img-hook downloaded=false reason="正文 3897 字 ≥300，非承重" -->

![图：指示当前的解算模式。请参见“首选项 动画”(Preferences Animation)中的“解算”(Evaluatio…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-87553309-4A91-4BE1-82E9-5A22BDFC1186.gif) <!-- baize:img-hook downloaded=false reason="正文 3897 字 ≥300，非承重" -->

指示当前的解算模式。请参见“首选项 > 动画”(Preferences > Animation)中的[“解算”(Evaluation)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-0817C74B-C95C-4E5F-BCFA-26DEE1D7747F#GUID-0817C74B-C95C-4E5F-BCFA-26DEE1D7747F__SECTION_8E9506543AFA46AE870961C6143FEA52)以更改解算节点。

- 如果处于 [DG 模式](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-0817C74B-C95C-4E5F-BCFA-26DEE1D7747F#GUID-0817C74B-C95C-4E5F-BCFA-26DEE1D7747F__GUID-86F27F13-FF42-4306-B2CF-CC6E5309ACAE)，则显示**“解算: DG”(Evaluation: DG)**。“EM 状态”(EM State)显示**“禁用”(Off)**，而“GPU 覆盖”(GPU Override)显示**“N/A”**。

- 如果处于[串行](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-0817C74B-C95C-4E5F-BCFA-26DEE1D7747F#GUID-0817C74B-C95C-4E5F-BCFA-26DEE1D7747F__GUID-E8BF82A1-C702-42CA-94A6-D18AEA274F67)或[平行模式](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-0817C74B-C95C-4E5F-BCFA-26DEE1D7747F#GUID-0817C74B-C95C-4E5F-BCFA-26DEE1D7747F__GUID-DC54071D-A332-4121-A956-7A8DE03E5447)，则显示**“解算: 串行”(Evaluation: Serial)**或**“解算: 平行”(Evaluation: Parallel)**以及“EM 状态”(EM State)。

  **“EM 状态”(EM State)**指示解算管理器是否具有最新的解算图，或者下次由播放触发解算时它是否需要重建图表。例如，在 DG 中进行某些更改（如删除节点连接）时，解算管理器将不再与 DG 同步，因此平视显示仪显示**“需要重建”(Rebuild required)**。

  触发解算时，解算管理器重建 EM 图表且 HUD 显示**“构建”(Built)**（后跟**“就绪”(Ready)**）。

- 如果 [GPU 覆盖(GPU Override)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-0817C74B-C95C-4E5F-BCFA-26DEE1D7747F#GUID-0817C74B-C95C-4E5F-BCFA-26DEE1D7747F__GUID-FBAC21CD-7620-48C8-9944-4516CFADC3CB)选项处于活动状态（仅当使用“串行”(Serial)或“平行”(Parallel)模式时才会出现此情况），则**“GPU 覆盖”(GPU Override)**将显示，它对 GPU（而不是 CPU）解算的网格顶点数（数千个）进行计数。例如，如果 HUD 显示“GPU 覆盖: 已启用(94k)”(GPU Override: Enabled (94k))，则这指示 GPU 正在对 94,000 个顶点解算。

#### 焦距(Focal Length)

在右下角显示当前摄影机的焦距。默认设置为禁用。

#### 游戏顶点计数(Game Vertex Count)

![图：显示实时游戏引擎（Unreal 或 Unity）将解算的顶点数。若要看到此选项，必须加载 gameVertexCount…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-889B2E93-B1A5-42D7-9CB5-4408CC0D7121.png) <!-- baize:img-hook downloaded=false reason="正文 3897 字 ≥300，非承重" -->

显示实时游戏引擎（Unreal 或 Unity）将解算的顶点数。若要看到此选项，必须加载 [gameVertexCount](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-DF9366D9-E24B-4A08-88F1-8EE1B78A52F9) 插件。

- 在 Unreal 模式下：

  ##### 切线模式(Tangent Mode)

  配置 Unreal 解算器用于计算顶点切线的方法：

  - 无(None)：不导入切线。这不适用于映射法线的着色器。

  - Maya：使用 Maya 的内置法线生成方法。

  - MikkT：在 Unreal 的 FBX 网格导入中使用 Mikk TSpace 法线生成方法。

- 在 Unity 模式下：

  ##### 焊接顶点

  合并完全共用相同特性的重叠顶点（包括 UV、法线、切线和顶点颜色）。

  ##### 法线

  配置法线的计算方式：

  - 导入(Import)：从 FBX 文件导入法线。如果文件不包含法线，将计算法线。

  - 计算(Calculate)：根据以下因素计算法线。

    **注**

    此设置适用于非常平滑、有机或高多边形模型。由于 Unity 以单个角度为基础处理硬边，因此此选项可能会错误地平滑模型的某些部分。通常，建议手动平滑模型，然后使用上面的

    “导入”(Import)

    设置。

    ###### 法线模式(Normals Mode)

    配置 Unity 计算法线的方式：

    - 未加权(旧版)(Unweighted (Legacy))：使用旧版（2017.1 之前的版本）方法计算法线。

    - 未加权(Unweighted)：法线不加权。

    - 区域加权(Area Weighted)：法线按面区域加权。

    - 角度加权(Angle Weighted)：法线按每个面的顶点角度加权。

    - 区域和角度加权(Area and Angle Weighted)：法线按面区域和每个面的顶点角度加权。

    ###### 源平滑度(Smoothness Source)

    配置 Unity 平滑边的方式：

    - 首选平滑组(Prefer Smoothing Group)：使用导入文件中的平滑组（如果适用）

    - 起始平滑组(From Smoothing Group)：仅使用导入文件中的平滑组。

    - 起始角度(From Angle)：使用平滑角度确定边平滑度。

    - 无(None)：不在硬边上分割顶点。

    ###### 平滑角

    控制如何为硬边分割顶点。值越大，面越少。

  - 无(None)：不导入法线。

  ##### 切线

  配置 Unity 解算器用于计算顶点切线的方法：

  - 导入(Import)：从 FBX 文件导入顶点切线。

  - 旧版(Legacy)：使用 Unity 的旧版法线生成算法。

  - 无(None)：不导入切线。这不适用于映射法线的着色器。

  - MikkT：在 Unity 的 FBX 网格导入中使用 Mikk TSpace 法线生成方法。

#### 帧速率(Frame Rate)

在右下角显示当前视图的帧速率（单位：每秒帧数 (FPS)）。默认设置为禁用。

#### HIK 细节(HIK Details)

在右下角处显示场景的当前 HumanIK 关键帧模式。默认设置为禁用。

#### 材质加载详细信息(Material Loading Details)

显示材质和纹理的加载进度。如果用于“首选项”(Preferences)窗口“显示”(Display)类别下的“延缓”(Deferred)和“平行”(Parallel) “材质加载模式”(Material Loading Mode)，则此信息最有用。详细信息请参见[显示首选项](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-BF017019-B89A-47F0-8AB5-106C058AB854)。

当材质实现完成且纹理加载完毕后，HUD 中的“要加载的材质”(Materials To Load)和“要加载的纹理”(Textures To Load)字段将指示 0。

#### 对象详细信息(Object Details)

显示包含如下对象详细信息的列表：“背面”(Backfaces)、“平滑度”(Smoothness)、“实例”(Instance)、“显示层”(Display Layer)、“与摄影机的距离”(Distance From Camera)以及“选定对象”(Selected Object)数。这些详细信息显示在面板的右上角。默认设置为禁用。

#### 原点轴(Origin Axis)

在透视视图内的原点 (0, 0, 0) 处显示全局轴。默认设置为禁用。

#### 粒子数(Particle Count)

显示场景中的粒子总数和选定 nParticle 的数目。“粒子数”(Particle Count)包含场景中的 nParticle 数目和经典粒子数目。

#### 多边形计数(Poly Count)

显示关于视图面板中显示的可见对象的多边形统计信息，其中包括顶点、边、面、三角形以及 UV。该功能非常适用于游戏开发。左侧第一列中列出了场景中所有多边形的组件总数。第二列中列出了选定多边形的组件总数。第三列中列出了选定组件的总数。默认设置为禁用。

**注**

在 Viewport 2.0 中，“多边形计数”(Poly Count)包括场景中的所有对象，其中包括不在屏幕上的对象。另一方面，在“旧版默认视口”(Legacy Default Viewport)中显示的“多边形计数”(Poly Count)仅包括摄影机看到的对象。

“多边形计数 > ![图：“多边形计数 ”中有两个选项。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 3897 字 ≥300，非承重" -->”中有两个选项。

#### 框架(Cage)

显示面板中可见对象框架（原始网格）的多边形统计信息。

#### 平滑网格预览(Smooth Mesh Preview)

显示面板中可见对象的多边形统计信息。

当显示方式设置为默认模式时，将显示框架统计信息。

当显示方式设置为“平滑网格预览”模式时，将显示关于已平滑对象的统计信息。

![图：显示面板中可见对象的多边形统计信息。 当显示方式设置为默认模式时，将显示框架统计信息。 当显示方式设置为“平滑网格预览”…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-A9756AC4-69A0-470B-BF2B-49982D7DD1ED.png) <!-- baize:img-hook downloaded=false reason="正文 3897 字 ≥300，非承重" -->

#### 场景时间码(Scene Timecode)

在场景视图的右下角显示场景时间码。默认设置为禁用。另请参见[设定和显示场景的时间码](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-8E9553E4-4900-4BFF-98D6-A4964EF8555F)。

#### 选择详细信息(Select Details)

场景视图的右下角将显示“软选择”(Soft Selection)的当前状态。

#### 对称(Symmetry)

如果“对称”(Symmetry)处于活动状态，则场景视图的中上部将显示当前对称轴。默认设置为启用。

#### 视图轴(View Axis)

在所有视图的左下角显示全局轴。默认设置为启用。

#### 视口渲染器(Viewport Renderer)

在视口的顶部正中显示视口类型和渲染引擎。默认设置为禁用。

**注**

从 Maya 2015 开始，视口类型平视显示仪已从

“摄影机名称”(Camera Names)

平视显示仪中分离。现在，您可以单独控制每个平视显示仪。

#### 视图中消息(In-view Messages)

显示或隐藏某些工具、模式和操作的消息显示。默认设置为启用。另请参见[帮助首选项](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-2B90FD26-20F6-4CF6-8A68-2DD4AD6CF334)。

#### 视图中编辑器(In-View Editors)

显示或隐藏在执行许多不同的建模操作后显示的视图中编辑器(In-View Editors)。默认设置为启用。请参见[视图中编辑器](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-C9C88AA3-CE61-4389-9A19-B6456427EBA2)。

## 相关主题

- [在视图面板中显示场景信息 (HUD)](../../../../查看场景/查看场景/在视图面板中显示场景信息%20%28HUD%29.md)

- [在视图面板中显示多边形计数](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-53E46D0C-4B7B-4404-AEB0-3BDD1FF8608A)

- [创建自定义平视显示仪读数](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-5C6AFD87-82DE-4C4B-B3F1-DB4A0C3B59C4)
