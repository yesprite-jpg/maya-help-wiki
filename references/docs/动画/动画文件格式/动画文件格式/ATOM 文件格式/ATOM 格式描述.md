# ATOM 格式描述

.atom 文件格式类似于 .anim 格式，并使用相同的模式保存动画曲线。但该格式还包含其他数据，例如未设置动画的静态值、烘焙值、动画层以及嵌入式导出编辑文件，这些文件中包含有关重新构造约束的信息并设置受驱动关键帧。（请参见 [ATOM 文件格式](../../../动画基础知识/动画基础知识/以%20ATOM%20格式导入和导出动画/ATOM%20文件格式.md)。）

导出 .atom 文件（[导出 .atom 动画](../../../动画基础知识/动画基础知识/以%20ATOM%20格式导入和导出动画/导出%20.atom%20动画.md)）之后，即可使用您选择的任意文本编辑器查看和编辑该文件。为了描述该格式，本主题将文件分为以下部分：

- [标头部分](ATOM%20格式描述.md#GUID-9FA7198C-6BC9-4CB7-AA86-74C3C0A47576__SECTION_AB0A6D0D59D94241B94C2FAB2D8C0011)

- [动画层部分](ATOM%20格式描述.md#GUID-9FA7198C-6BC9-4CB7-AA86-74C3C0A47576__SECTION_1115D14D00AB4210A954F6F9F450A9FD)

- [主体（对象）部分](ATOM%20格式描述.md#GUID-9FA7198C-6BC9-4CB7-AA86-74C3C0A47576__SECTION_B4254F15AC99417889B337FB844BE7AF)

- [嵌入的脱机编辑文件 (.editMA)](ATOM%20格式描述.md#GUID-9FA7198C-6BC9-4CB7-AA86-74C3C0A47576__SECTION_48E231CD50E541FEA9C32514D19FA390)

若要查看不含描述的完整 .atom 文件，请参见[示例 .atom 文件](示例%20.atom%20文件.md)。

有关 .atom 语法的其他介绍性说明：

- # 是有效的注释字符。请注意，// 不是有效的注释字符，这一点与 .anim 文件不同。

  ```text
#Atom File Format Description
```

- 文件中不包含大括号 { 或 } 的任何行都必须以分号 (;) 结尾。从分号 (;) 后另起一行。

- 关键字和数据以空格分隔。

## 标头部分

.atom 文件的标头部分可以包括以下内容。

```text
atomVersion 1.0;
mayaVersion ;
mayaSceneFile string
timeUnit [game|film|pal|ntsc|show|palf|ntscf|hour|min|sec|millisec]
linearUnit [mm|cm|m|km|in|ft|yd|mi]
angularUnit [rad|deg|min|sec]
startTime [float]
endTime [float]
startUnitless [float]
endUnitless [float]
offlineFile [string:optional]
```

例如：

```text
atomVersion 1.0;
mayaVersion ;
mayaSceneFile C:/Users/user/Documents/maya/projects/default/scenes/test.ma;
timeUnit film;
linearUnit cm;
angularUnit deg;
startTime 1;
endTime 8;
offlineFile ;
```

| atomVersion | 该文件格式的版本号。此行是必需的。 |
|---|---|
| mayaVersion | Maya 的版本。此字符串是 MGlobal::mayaVersion() mayaVersion 字符串的值。 |
| mayaSceneFile | （可选）从中保存 .atom 文件的场景文件的名称。 |
| timeUnit | 这些关键字用于设置文件的单位。每条动画曲线以及每个静态值和烘焙值都可以有自己的单位，但这些单位在未指定动画曲线单位时为默认单位（请参见 [animData](ATOM%20格式描述.md#GUID-9FA7198C-6BC9-4CB7-AA86-74C3C0A47576__GUID-C77FCA51-5B77-4F26-85C9-9A2348AD83B1)）。如果未指定这些单位，则使用 UI 单位。 **只能**包含在文件的标头部分。 |
| linearUnit |  |
| angularUnit |  |
| startTime | 剪贴板的开始帧和剪贴板的结束帧。这些行由具有时间输入的动画曲线以及烘焙值使用。 如果文件中不包含烘焙值，则这些行是可选的。如果文件中不包含烘焙值，则剪贴板将设置为剪贴板中所含动画曲线定义的范围。 注： 如果文件中包含烘焙值，则这些值是必需的，因为它们可以确定烘焙值的开始时间和结束时间。 |
| endTime |  |
| startUnitless | 剪贴板的开始值和剪贴板的结束值。这些值由没有时间输入的动画曲线使用。 |
| endUnitless |  |
| offlineFile | 此关键字是可选的，在文件包含导出编辑时指定。默认行为是在 .atom 文件结束之时嵌入导出编辑。如果在 offlineFile 关键字后指定文件名，则该文件用作脱机编辑文件。 .atom 格式使用脱机编辑来存储约束和设置受驱动关键帧动画。 **只能**包含在文件的标头部分。 另请参见[嵌入的脱机编辑文件 (.editMA)](ATOM%20格式描述.md#GUID-9FA7198C-6BC9-4CB7-AA86-74C3C0A47576__SECTION_48E231CD50E541FEA9C32514D19FA390)。 |

## 动画层部分（可选）

动画层部分的起始行包含此文件中对象上显示的所有动画层的名称。

```text
animLayers {string string ...}
```

此行后跟每个动画层的一系列属性。

该信息用于执行导入操作以检查目标场景中是否缺少任何指定的动画层，如果确实缺少，则创建缺少的动画层。

例如：

```text
animLayers {   BaseAnimation  AnimLayer1 }
animLayer {
  BaseAnimation 0 0;
  static mute mute 0;
  { 0 }
  static lock lock 1;
  { 0 }
  static solo solo 2;
  { 0 }
  static override override 3;
  { 1 }
  static passthrough passthrough 4;
  { 1 }
  static preferred preferred 5;
  { 0 }
  static weight weight 6;
  { 1 }
  static rotationAccumulationMode rotationAccumulationMode 7;
  { 0 }
  static scaleAccumulationMode scaleAccumulationMode 8;
  { 1 }
}
animLayer {
  AnimLayer1 0 0;
  static mute mute 0;
```

## 主体（对象）部分

文件主体列出了已在 .atom 文件中保存的每个节点。受支持的节点类型包括 DAG 节点（dagNode 关键字）和形状节点（shape 关键字）。对于其他类型的节点是否受支持，取决于节点（node 关键字）是否列出。

**注**

重要：

与 .anim 文件不同，.atom 文件中的 DAG 和形状节点按照特定的顺序进行排序，以与它们在 Maya 场景中的显示方式匹配。例如，在 .atom 文件中，DAG 节点的子形状节点紧随父 DAG 节点列出。请注意，编辑 .atom 文件来更改此顺序可能会导致某些操作无法正常执行。

该文件中包含的每个对象的第一行指定了节点名称、深度和子节点数。

```text
dagNode {
pSphere1 1 1;
```

**注**

对于 DAG 节点之外的其他所有节点，这些值均为零。对于 DAG 节点，深度是指该对象所含父节点的数量，包括根节点（因此默认值为 1），子节点计数可标识其同级项顺序编号（默认值为 1）。这些值用于在导入时执行层次匹配。

每个节点标识符后面都有一个开括号和闭括号对 { }，其中包含每个属性的信息。ATOM 文件支持静态值（单个非动画值）、烘焙值（一个逐帧值列表）或动画曲线值。

这是 .anim 和 .atom 文件之间的主要区别之一。.anim 文件只包含一个简单的属性列表（属性列表中列出了关联的对象），而 .atom 文件则在每个属性所属的对象下面列出了该属性，从而使得 .atom 文件更易于查看，并提高了导入时完成的匹配操作。

```text
dagNode {
pSphere1 1 1;
}
static string string int string|optional
cached int|float|double int|float|double int|float|double ...
anim string string int string|optional
```

例如：

```text
dagNode {
  pSphere1 1 1;
  anim translate.translateY translateY 0;
  animData {
    input time;
    output linear;
    weighted 0;
    preInfinity constant;
    postInfinity constant;
    keys {
      1 0 auto auto 1 1 0;
      10 -0.48952813 auto auto 1 1 0;
    }
```

每个属性的导出方式都是相同的，即 static、cached（对于烘焙值）或 anim（对于动画曲线）标识符后跟属性的长名称、短名称、属性编号和可选的动画层名称。

```text
dagNode {
  pSphere1 1 1;
  anim translate.translateY translateY 0;
  animData {
    input time;
    output linear;
    weighted 0;
    preInfinity constant;
    postInfinity constant;
    keys {
      1 0 auto auto 1 1 0;
      10 -0.48952813 auto auto 1 1 0;
    }
  }
  cached translate.translateX translateX 0;
  { -5.2988979 -4.7870473 -3.4152877 -1.4293071 0.92520503 3.4025622 5.4610407 0.70032059  }
}
dagNode {
  pPlane1 1 2;
  static rotate.rotateX rotateX 0;
  { 0 }
  static rotate.rotateY rotateY 1;
  { 0 }
  static rotate.rotateZ rotateZ 2;
  { 0 }
  static scale.scaleX scaleX 3;
  { 1 }
  static scale.scaleY scaleY 4;
  { 1 }
  static scale.scaleZ scaleZ 5;
  { 1 }
  static visibility visibility 9;
  { 1 }
}
```

**注**

如果动画层名称存在，则指定的数据位于该节点上以及指定的该动画层的属性上，因此属性名称将显示多次，针对属性所属的每个动画层显示一次。

| static | static 标识符是一个指定未设置动画的属性值的值，在括号对内列出。 此值可以为整数、浮点数、双精度、字符串或枚举。 |
|---|---|
| cached | 烘焙值类似于静态值，不过烘焙值表示开始时间和结束时间指定的时间范围内每帧的值。如果在导出时启用了[已烘焙动画(Baked Animation)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-DFC34004-6E79-42A5-A3CD-7B9A4072D7CF#GUID-DFC34004-6E79-42A5-A3CD-7B9A4072D7CF__GUID-3A18A2A8-5CAA-4B3C-A970-3816F3BEA524)选项，则对值进行烘焙。 如果导出的属性不受简单的动画曲线驱动，也没有导出为动画层、约束或设置受驱动关键帧。 因此对于烘焙值，我们采用一个开括号和闭括号对，后跟一组值，表示指定的开始时间和结束时间之间的帧数。 |
| anim | 保存的属性可以受动画曲线驱动，就像在 .anim 文件中一样。 就像在前面讲过的，anim 关键字后跟属性的长名称、短名称和属性编号。 注意： 这一点不同于 .anim 文件，在 .anim 文件中，保存属性编号之前还要保存行（深度）和子编号，因此在将 .anim 数据导入 .atom 文件时务必要小心，因为这些多余的编号需要删除。 （请参见以下内容。） |

如果属性受动画曲线驱动，则 anim 行后跟用于指定关键帧数据的 animData 块。

```text
animData  {
  input [time|unitless]
  output [time|linear|angular|unitless]
  weighted [1|0]
  inputUnit [game|film|pal|ntsc|show|palf|ntscf|hour|min|sec|millisec]
	 outputUnit [game|film|pal|ntsc|show|palf|ntscf|hour|min|sec|millisec]
  outputUnit [mm|cm|m|km|in|ft|yd|mi]
  outputUnit [rad|deg|min|sec]
  tangentAngleUnit [rad|deg|min|sec]
  preInfinity [constant|linear|cycle|cycleRelative|oscillate]
  postInfinity [constant|linear|cycle|cycleRelative|oscillate]
```

例如：

```text
anim rotate.rotateY rotateY 5 AnimLayer1;
  animData {
    input time;
    output angular;
    weighted 0;
    preInfinity constant;
    postInfinity constant;
    keys {
      1 0 auto auto 1 1 0;
      8 0 flat auto 1 1 0;
```

| animData | 指示动画曲线的关键帧数据的开始，包括以下定义： |
|---|---|
| input | 动画曲线的输入类型。默认设置为 time。 |
| output | 动画曲线的输出类型。默认设置为 linear。 |
| weighted | 指定曲线是否具有加权切线。默认设置为 false。 |
| inputUnit | 动画曲线输入的单位（如果是时间输入）。默认设置为在文件标头部分指定的时间单位。 |
| outputUnit | 动画曲线输出的单位。输出单位应与曲线的输出类型相匹配。默认设置为在标头中指定的单位。 |
| tangentAngleUnit | 切线角度的单位（如果有任何固定切线）。默认设置为在文件标头中指定的角度单位。 |
| preInfinity | 前方无限类型。默认设置为 constant。 |
| postInfinity | 后方无限类型。默认设置为constant |
| keys | （请参见以下内容。） |

每个块中的最终行包含实际的关键帧数据。每个关键帧在大括号括起的部分中都自成一行。

```text
 keys {
 [float] [float] [in tan] [out tan] [tan locked] [weight locked][breakdown]
```

| float | 前两个值是采用由 inputUnit 和 outputUnit 关键字定义的单位表示的输入和输出值。 |
|---|---|
| in tan out tan | 入切线和出切线类型。应为有效的切线类型。 |
| tan locked weight locked breakdown | 用于切线锁定、权重锁定和受控关键点标志的整数值。如果这些值为 0、未锁定或不是受控关键点，否则这些值将被锁定。 如果切线是入切线和/或出切线，或者切线是固定的，则需要更多信息：切线的角度和权重。 每条固定曲线的这两个值会添加在该行的末尾。 例如，62.345 是第一条切线的切线角度，切线权重为 0.04： 1.0 2.0 fixed linear 1 1 0 62.345 0.04; 两条固定切线的示例： 1.0 2.0 fixed fixed 1 1 0 62.345 0.04 45.3 0.023; |

## 嵌入的脱机编辑文件 (.editMA)

如果 offlineFile 标识符出现在标头中，则 .atom 文件可以包含嵌入的脱机编辑文件（.editma 文件）。

例如：

```text
offlineFileData //Maya ASCII 2013ff03 scene
//Name: test.editMA
```

offlineFileData 标识符后，将出现一串数据，其中包含嵌入的 .editMA 文件。此数据必须位于文件结尾处。

**注**

重要：

请勿修改此数据。

## 相关主题

[ATOM 动画文件格式](../../../动画基础知识/动画基础知识/以%20ATOM%20格式导入和导出动画/ATOM%20文件格式.md)

[导出 .atom 动画](../../../动画基础知识/动画基础知识/以%20ATOM%20格式导入和导出动画/导出%20.atom%20动画.md)
