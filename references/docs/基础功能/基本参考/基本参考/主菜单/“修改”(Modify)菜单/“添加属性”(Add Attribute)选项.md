# “添加属性”(Add Attribute)选项

在“添加属性”(Add Attribute)窗口中设置以下选项，用于控制所添加属性的名称和性质。另请参见[创建、编辑或删除自定义属性](../../../../节点和属性/节点和属性/查看和编辑属性/创建、编辑或删除自定义属性.md)。

#### 长名称(Long name)

这是要添加的属性的名称。

#### 覆盖易读名称(Override nice name)

启用该选项可提供一个不同的/更加用户友好的名称，在“属性编辑器”(Attribute Editor)或“通道盒”(Channel Box)中查看该属性时将使用该名称

（如果属性名称是用大写字母分隔的，那么将创建默认易读名称，即“setAttributeBlackOrWhite”变为“Set Attribute Black Or White”）。

仅当选中“覆盖易读名称”(Override nice name)框时才会将易读名称存储在文件中；否则会从长名称中计算该名称。如果易读名称使用多字节语言（如日语），那么这样可能会将多字节字符插入到 .ma (Maya ASCII) 文件中。

#### “易读”(Nice)名称

这是属性的更短的或更加用户友好的名称。仅当启用“覆盖易读名称”(Override nice name)时才能在其中键入内容。

#### “生成”(Make)属性

定义下列属性：

有关这些属性类型的详细信息，请参见[通道控制编辑器](../../../../节点和属性/节点和属性/查看和编辑属性/通道盒%28Channel%20Box%29/“通道控制”%28Channel%20Control%29编辑器.md)。

#### 可设定关键帧(Keyable)

使属性可设置关键帧。

#### 可显示(Displayable)

使属性不可设置关键帧但可在“通道盒”(Channel Box)中显示。

#### 隐藏(Hidden)

使属性隐藏（且不可设置关键帧）。

## 数据类型(Data Type)

为属性选择数据类型：

#### 向量(Vector)

创建由三个浮点值组成的向量属性。

#### 浮点型(Float)

创建浮点属性。

#### 整型(Integer)

创建整型属性。

#### 布尔(Boolean)

创建由开/关切换组成的属性

#### 字符串(String)

创建接受字母数字条目作为数据输入的字符串属性。

#### 枚举(Enum)

创建属性，该属性接受“枚举”或下拉列表中的选择。

**注**

如果选择

“浮点型”(Float)

或

“整型”(Integer)

，还可以设定

“数值属性的特性”(Numeric Attribute Properties)

。

## 属性类型(Attribute Type)

选择一种类型：

#### 标量(Scalar)

创建每对象属性，可以将该属性设定为应用到对象中的每个粒子的单个值。可以将向量标量视为包含三个数字的单个值。如果选择“标量”(Scalar)，可以为浮点型或整型属性指定“最小值”(Minimum)、“最大值”(Maximum)和“默认”(Default)值。

#### 每粒子(数组) (Per Particle (Array))

创建每粒子属性。对于每个粒子，可以将该类型属性设定为不同的值。如果选择“每粒子(数组)”(Per Particle (Array))，还可以通过启用“添加初始状态属性”(Add Initial State Attribute)来创建对应的初始状态属性。

#### 添加初始状态属性(Add Initial State Attribute)

启用该选项可为添加的属性创建相应的初始状态属性。没有该相应的属性，则无法保存粒子对象的当前属性值以供初始状态使用。如果决定在回放动画时初始化自定义属性的值，则必须编写一个创建表达式。如果知道要为自定义属性编写一个创建表达式，则在添加属性时可将“添加初始状态属性”(Add Initial State Attribute)设定为禁用。否则，无论何时添加自定义每粒子属性，请将“添加初始状态属性”(Add Initial State Attribute)设定为启用。

## 数值属性的特性(Numeric Attribute Properties)

对于标量属性，“最小值”(Minimum)和“最大值”(Maximum)设定在“属性编辑器”(Attribute Editor)或“通道盒”(Channel Box)中可以为属性输入的最小值和最大值。“默认”会为属性设定默认值。

## 枚举名称(Enum Names)

如果要添加新的枚举属性，需要定义可接受的字符串列表。在可以更改的“枚举名称”(Enum Names)列表中，存在两个默认的字符串：“Green”和“Blue”。若要更改，请选择“Green”或“Blue”，然后在“新名称”文本框中输入新字符串。若要添加新字符串，请单击最后一个列表项下方的空白条目，然后在“新名称”(New Name)文本框中键入字符串。

**注**

注意：

下面列出的名称是为（动态）着色属性内部保留的。可以将这些名称用于自定义属性，但请注意它们可能会在着色网络中产生异常结果。例如，在着色过程中已提供 uvCoord 值，因此将忽略自定义 uvCoord 属性值。

- blobbySurfaceFactor

- displacement

- easMask

- farPointCamera

- farPointObj

- farPointWorld

- filterSize

- flippedNormal

- illuminationIndex

- infoBits

- lightData

- lightTable

- matrixObjectToWorld

- matrixWorldToObject

- mediumRefractiveIndex

- normalCamera

- numShadingSamples

- objectId

- objectType

- opticalDepth

- outColor

- outGlowColor

- outMatteOpacity

- outParticleEmission

- outTransparency

- particleAge

- particleAttrArray

- particleColor

- particleEmission

- particleEntryParam

- particleExitParam

- particleIncandescence

- particleLifespan

- particleOrder

- particleTransparency

- particleWeight

- pixelCenter

- pixelCoverage

- pointCamera

- pointObj

- pointWorld

- primitiveId

- rayDepth

- rayDirection

- rayOrigin

- receiveShadows

- refPointCamera

- refPointObj

- refPointWorld

- renderState

- shadowAttenuation

- tangentUCamera

- tangentVCamera

- translucenceDepth

- triangleNormalCamera

- uvCoord

- uvFilterSize

- vertexCameraOne

- vertexCameraThree

- vertexCameraTwo

- vertexUvOne

- vertexUvThree

- vertexUvTwo
