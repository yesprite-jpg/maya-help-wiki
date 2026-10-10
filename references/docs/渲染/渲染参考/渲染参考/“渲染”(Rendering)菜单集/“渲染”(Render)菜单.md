# “渲染”(Render)菜单

某些菜单项是渲染器专用的，仅当适用的渲染器处于活动状态时才可访问。

## 渲染设置

#### 渲染设置(Render Settings)

打开“渲染设置”(Render Settings)窗口。有关此窗口中选项的详细信息，请参见[“渲染设置”(Render Settings)窗口](../渲染窗口和编辑器/“渲染设置”%28Render%20Settings%29窗口.md)。

#### 使用以下渲染器渲染(Render Using)

从可用选项中选择要使用的渲染器。

有关渲染器的详细信息，请参见[硬件、软件和向量渲染](../../../硬件、软件和向量渲染/硬件、软件和向量渲染.md)。

#### 测试分辨率(Test Resolution)

“渲染视图”(Render View)窗口中图像渲染所使用的分辨率。使用降低的分辨率测试渲染场景以缩短渲染时间。

| 摄影机面板 | 使用当前视图的分辨率渲染。 |
|---|---|
| 渲染设置 | 使用[渲染设置窗口](../渲染窗口和编辑器/“渲染设置”%28Render%20Settings%29窗口.md)中设定的分辨率渲染。默认设置为 960x540。 |
| 10% 设置 | 使用[渲染设置窗口](../渲染窗口和编辑器/“渲染设置”%28Render%20Settings%29窗口.md)中设定的分辨率的 10% 渲染。默认设置为 96x54。 |
| 25% 设置 | 使用[渲染设置窗口](../渲染窗口和编辑器/“渲染设置”%28Render%20Settings%29窗口.md)中设定的分辨率的 25% 渲染。默认设置为 240x135。 |
| 50% 设置 | 使用[渲染设置窗口](../渲染窗口和编辑器/“渲染设置”%28Render%20Settings%29窗口.md)中设定的分辨率的 50% 渲染。默认设置为 480x270。 |
| 75% 设置 | 使用[渲染设置窗口](../渲染窗口和编辑器/“渲染设置”%28Render%20Settings%29窗口.md)中设定的分辨率的 75% 渲染。默认设置为 720x405。 |
| 110% 设置 | 使用[渲染设置窗口](../渲染窗口和编辑器/“渲染设置”%28Render%20Settings%29窗口.md)中设定的分辨率的 110% 渲染。默认设置为 1056x594。 |
| 125% 设置 | 使用[渲染设置窗口](../渲染窗口和编辑器/“渲染设置”%28Render%20Settings%29窗口.md)中设定的分辨率的 125% 渲染。默认设置为 1200x675。 |
| 150% 设置 | 使用[渲染设置窗口](../渲染窗口和编辑器/“渲染设置”%28Render%20Settings%29窗口.md)中设定的分辨率的 150% 渲染。默认设置为 1440x810。 |

#### 设置 NURBS 细分(Set NURBS Tessellation)

为选定的 NURBS 曲面设置细分。

选择“渲染 > 设置 NURBS 细分”(Render > Set NURBS Tessellation) > ![图：选择“渲染 设置 NURBS 细分”(Render Set NURBS Tessellation) ，可打开“设置 NU…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-96432FB8-EBE9-4D1A-8DED-5173E032EBC0.png) <!-- baize:img-hook downloaded=false reason="正文 2223 字 ≥300，非承重" -->，可打开“设置 NURBS 细分”(Set NURBS Tessellation)窗口。有关该窗口中选项的详细信息，请参见[设置 NURBS 细分选项](“渲染”%28Render%29菜单/设置%20NURBS%20细分选项%28Set%20NURBS%20Tessellation%20Options%29.md)。

#### 运行渲染诊断(Run Render Diagnostics)

运行“运行渲染诊断”(Run Render Diagnostics)工具。有关详细信息，请参见[运行诊断](../../../质量、渲染速度、诊断/质量、渲染速度、诊断/运行诊断.md)。

#### 导出预合成(Export Pre-Compositing)

进行选择，以将渲染层、过程和摄影机导出到合成、或其他合成和预处理软件（如火焰）。此选项可使用与上一次导出相同的文件名和设置来导出元素。如果之前未执行过导出，则默认的文件名为 scenename.precomp，然后，导出场景中的所有渲染层、过程和摄影机。

**注**

使用此菜单项将渲染层、过程和摄影机导出到合成。

选择“渲染 > 导出预合成”(Render > Export Pre-Compositing) > ![图：选择“渲染 导出预合成”(Render Export Pre-Compositing) ，可打开“导出预合成”(Expo…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-96432FB8-EBE9-4D1A-8DED-5173E032EBC0.png) <!-- baize:img-hook downloaded=false reason="正文 2223 字 ≥300，非承重" -->，可打开“导出预合成”(Export Pre-Compositing)窗口。有关该窗口中选项的详细信息，请参见[导出预合成选项](“渲染”%28Render%29菜单/导出预合成选项%28Export%20Pre-Compositing%20Options%29.md)。

## 渲染

#### 渲染当前帧(Render Current Frame)

打开“渲染视图”(Render View)窗口，并渲染当前场景。

#### 重做上一次渲染(Redo Previous Render)

打开“渲染视图”(Render View)窗口，并从上一个视图重新渲染场景。

#### IPR 渲染当前帧(IPR Render Current Frame)

打开“渲染视图”(Render View)窗口，“IPR”将渲染当前场景。有关详细信息，请参见[关于交互式真实照片级渲染 (IPR)](../../../可视化和渲染图像/可视化和渲染图像/渲染方法/关于交互式真实照片级渲染%20%28IPR%29.md)。

#### 重做上一次 IPR 渲染(Redo Previous IPR Render)

打开“渲染视图”(Render View)窗口，然后对上一个视图的场景重新进行 IPR 渲染。有关详细信息，请参见[关于交互式真实照片级渲染 (IPR)](../../../可视化和渲染图像/可视化和渲染图像/渲染方法/关于交互式真实照片级渲染%20%28IPR%29.md)。

## 批渲染

#### 批渲染(Batch Render)

运行批渲染。有关详细信息，请参见[关于从 Maya (UI) 中进行批渲染](../../../可视化和渲染图像/可视化和渲染图像/渲染方法/关于从%20Maya%20%28UI%29%20中进行批渲染.md)。

选择“渲染 > 批渲染”(Render > Batch Render) > ![图：选择“渲染 批渲染”(Render Batch Render) ，可打开“批渲染帧”(Batch Render Fram…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-96432FB8-EBE9-4D1A-8DED-5173E032EBC0.png) <!-- baize:img-hook downloaded=false reason="正文 2223 字 ≥300，非承重" -->，可打开“批渲染帧”(Batch Render Frame)窗口。此窗口提供用于在本地或远程计算机上或者在具有多个处理器的计算机上渲染动画的选项。有关这些选项的详细信息，请参见[批渲染选项](“渲染”%28Render%29菜单/批渲染选项%28Batch%20Render%20Options%29.md)。

#### 取消批渲染(Cancel Batch Render)

取消在 Maya 当前会话中启用的批渲染。

有关批渲染的详细信息，请参见[关于从 Maya (UI) 中进行批渲染](../../../可视化和渲染图像/可视化和渲染图像/渲染方法/关于从%20Maya%20%28UI%29%20中进行批渲染.md)。

#### 显示批渲染(Show Batch Render)

打开 fcheck 显示窗口，然后显示上次渲染的图像。

有关批渲染的详细信息，请参见[关于从 Maya (UI) 中进行批渲染](../../../可视化和渲染图像/可视化和渲染图像/渲染方法/关于从%20Maya%20%28UI%29%20中进行批渲染.md)。

**注**

如果在 Linux 平台上使用的是 Fedora 操作系统，必须禁用 SELinux 功能，才能使用

“渲染 > 显示批渲染”(Render > Show Batch Render)

功能。

#### 创建 Backburner 作业(Create Backburner Job)

**注**

Maya 中不包含 Backburner。可以从

Autodesk App Store

下载它。

打开“Maya 版 BackBurner”(BackBurner for Maya)窗口。此窗口提供了使用 Autodesk Backburner 管理渲染作业和渲染节点的选项。有关选项的详细信息，请参见[创建 Backburner 作业选项](“渲染”%28Render%29菜单/创建%20Backburner%20作业选项%28Create%20Backburner%20Job%20Options%29.md)。

Backburner 仅可以将作业细分为至少有一个帧那么长的任务，而无法将单帧细分为多个任务。因此，仅可以将该功能用于动画场景，而不能用于静物。每个任务必须至少有一个帧那么长。

**注**

为了将作业提交给 backburner，必须将项目设定到可在网络上访问的某个位置。场景文件也必须可在网络上访问（例如，不能放在

C:\MyDocuments

下）。
