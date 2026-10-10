# 附录 A：切线和 binormal 向量

下面简要介绍了如何在 Maya 中计算多边形网格几何体的切线和 binormal 向量。

## 逐三角形切线计算

输入：对于三角形的每个顶点，输入：v（顶点位置，3 浮点）、n（法线位置，3 浮点）、t（纹理坐标值，2 浮点）：V[3][3], N[3][3] t[3][2]；

输出：对于每个顶点，计算并返回一个切线向量（3 浮点）：tangentArray[3][3]；

```text
 float $edge1[3];
 float $edge2[3];
 float $crossP[3];
 float $tangentArray[3][3];
 //==============================================
 // x, s, t
 // S & T vectors get used several times in this vector,
 // but are only computed once.
 //==============================================
 $edge1[0] = $v[1][0] - $v[0][0];
 $edge1[1] = $t[1][0] - $t[0][0]; // s-vector - don't need to compute this multiple times
 $edge1[2] = $t[1][1] - $t[0][1]; // t-vector
 $edge2[0] = $v[2][0] - $v[0][0];
 $edge2[1] = $t[2][0] - $t[0][0]; // another s-vector
 $edge2[2] = $t[2][1] - $t[0][1]; // another t-vector
 $crossP = crossProduct( $edge1, $edge2 ) ;
 normalize( $crossP );
 bool $degnerateUVTangentPlane = equivalent( $crossP[0], 0.0f );
 if (degnerateUVTangentPlane)
 $crossP[0] = 1.0f;
 float $tanX = -$crossP[1]/$crossP[0];
 $tangentArray[0][0] = $tanX;
 $tangentArray[1][0] = $tanX;
 $tangentArray[2][0] = $tanX;
 //--------------------------------------------------------
 // y, s, t
 //--------------------------------------------------------
 $edge1[0] = $v[1][1] - $v[0][1];
 $edge2[0] = $v[2][1] - $v[0][1];
 $edge2[1] = $t[2][0] - $t[0][0];
 $edge2[2] = $t[2][1] - $t[0][1];
 $crossP = crossProduct( $edge1, $edge2 );
 normalize( $crossP );
 degnerateUVTangentPlane = equivalent( $crossP[0], 0.0f );
 if (degnerateUVTangentPlane)
 $crossP[0] = 1.0f;
 float $tanY = -$crossP[1]/$crossP[0];
 $tangentArray[0][1] = $tanY;
 $tangentArray[1][1] = $tanY;
 $tangentArray[2][1] = $tanY;
 //------------------------------------------------------
 // z, s, t
 //------------------------------------------------------
 $edge1[0] = $v[1][2] - $v[0][2];
 $edge2[0] = $v[2][2] - $v[0][2];
 $edge2[1] = $t[2][0] - $t[0][0];
 $edge2[2] = $t[2][1] - $t[0][1];
 $crossP = crossProduct( $edge1 , $edge2 );
 normalize( $crossP );
 degnerateUVTangentPlane = equivalent( $crossP[0], 0.0f );
 if (degnerateUVTangentPlane)
 $crossP[0] = 1.0f;
 float $tanZ = -$crossP[1]/$crossP[0];
 $tangentArray[0][2] = $tanZ;
 $tangentArray[1][2] = $tanZ;
 $tangentArray[2][2] = $tanZ;
 // Orthnonormalize to normal
 for( int $i = 0; $i < 3; $i++)
 {
 $tangentArray[i] -= $n[i] * $tangentArray[i].dot( n[i]);
 }
 // Normalize tangents
 normalize( $tangentArray[0] );
 normalize( $tangentArray[1] );
 normalize( $tangentArray[2] );

 return $tangentArray;
```

## 曲面切线和 Binormal 计算

切线计算基于给定纹理坐标集 (uvset) 的纹理坐标 (uv)。所用法线为参照了平滑和用户法线的几何体法线。

对于一个面上的每个三角形，需计算三角形每个顶点的切线。如果三角形已被映射（即具有 uv）且这些 uv 是非退化类型，就会执行[逐三角形切线计算](附录%20A：切线和%20binormal%20向量.md#WS17956D7ADBC6E7367F9C4AAC117AE333A12-8000)中的计算。

退化 uv 表示三角形任意边的 uv 空间中具有 0 长度向量。如果三角形未被映射或退化，就会用几何体边来计算切线。对于三角形的每个顶点 (i)，将进行以下计算：

```text
tangent[i] = vertex[i+1 % 3] - vertex[i];
tangent[i] = tangent[i] - normal[i] * dotProduct( tangent[i], normal[i]);
normalize( tangent[i] );
```

对于已映射的面，只有在顶点的关联 normalId 完全相同的情况下，才会为顶点上的每个 uvId 保留共享切线的列表。

uvId 是 UV 集数据数组的偏移，normalId 是法线数据数组的偏移。切线数据数组将与 uvId 数据数组的大小匹配。每个列表都经过归一化处理，以计算最终共享的切线向量。

Binormal 被计算为面的给定顶点上切线和法线向量的归一化叉积。按需要计算并缓存 Binormal。
