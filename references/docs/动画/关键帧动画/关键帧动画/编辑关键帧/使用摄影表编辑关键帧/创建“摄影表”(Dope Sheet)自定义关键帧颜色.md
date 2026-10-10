# 创建“摄影表”(Dope Sheet)自定义关键帧颜色

可以使用 MEL 创建“摄影表”(Dope Sheet)关键帧的自定义关键帧颜色。可以设定创建的每个颜色的着色和值，并指定它们适用于哪些关键帧状态。

例如，您可以创建颜色为中等蓝色的自定义关键帧颜色，然后指定该蓝色的一个高值应用于选定关键帧，一个低值应用于未选定关键帧。

使用 MEL 更改“摄影表”(Dope Sheet)中关键帧的颜色

1. 在“脚本编辑器”(Script Editor)或命令行中，使用 选择要为其创建自定义关键帧颜色的动画通道。例如：

  ```text
select pSphere1_translateX;
```

2. 使用 将“摄影表”(Dope Sheet)自定义颜色属性添加到选定通道。例如：

  ```text
addAttr -ln dopeSheetColorScheme -at compound -nc 3; addAttr -ln keyframeActive -dt float3 -m -p dopeSheetColorScheme; addAttr -ln keyframeInactive -dt float3 -m -p dopeSheetColorScheme; addAttr -ln colorPriority -at short -p dopeSheetColorScheme;
```

3. 使用 为自定义关键帧颜色设置高值和低值，并指定这些颜色适用于哪些关键帧状态。

  使用 [0] 设定低颜色值，使用 [1] 设定高颜色值。另外，使用 keyframeActive 指定仅适用于选定关键帧的自定义颜色，或使用 keyframeInactive 指定仅适用于未选定关键帧的自定义颜色。例如：

  ```text
setAttr pSphere1_translateX.dopeSheetColorScheme.keyframeActive[0] -type float3 0.5 0 0; setAttr pSphere1_translateX.dopeSheetColorScheme.keyframeActive[1] -type float3 1 0 0; setAttr pSphere1_translateX.dopeSheetColorScheme.keyframeInactive[0] -type float3 0 0 0.5; setAttr pSphere1_translateX.dopeSheetColorScheme.keyframeInactive[1] -type float3 0 0 1;
```

4. （可选）使用 colorPriority 设定选定通道的自定义关键帧颜色的颜色优先级。例如：

  ```text
setAttr pSphere1_translateX.dopeSheetColorScheme.colorPriority 0;
```

  colorPriority 确定哪些子通道的自定义颜色（例如 pSphere1_translateX 或 pSphere1_rotateY）将被父通道（例如 pSphere1）继承。

  **注**

  摘要对象不显示已创建的自定义关键帧颜色，而仅显示优先级通道中的颜色信息。
