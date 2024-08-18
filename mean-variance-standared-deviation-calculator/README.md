### Mean-Variance-Standard Deviation Calculator Project Instructions
URL: [https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/mean-variance-standard-deviation-calculator](https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/mean-variance-standard-deviation-calculator)  
mean_var_std.pyという名前のファイルにcalculate()という関数を作成してください。この関数は、Numpyを使用して、3×3の行列の行、列、および要素に対して、平均、分散、標準偏差、最大値、最小値、および合計を出力します。

この関数の入力は9つの数字を含むリストであるべきです。関数はリストを3×3のNumpy配列に変換し、その後、平均、分散、標準偏差、最大値、最小値、および合計を行と列、そしてフラットな行列に対して含む辞書を返します。

返される辞書は以下の形式に従うべきです：

```
{
  'mean': [axis1, axis2, flattened],
  'variance': [axis1, axis2, flattened],
  'standard deviation': [axis1, axis2, flattened],
  'max': [axis1, axis2, flattened],
  'min': [axis1, axis2, flattened],
  'sum': [axis1, axis2, flattened]
}
```
9つ未満の要素を含むリストが関数に渡された場合、"List must contain nine numbers."というメッセージでValueError例外を発生させるべきです。返される辞書内の値はNumpy配列ではなくリストであるべきです。

例えば、calculate([0,1,2,3,4,5,6,7,8])を実行すると、次のように返されます：

```
{
  'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
  'variance': [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667],
  'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611],
  'max': [[6, 7, 8], [2, 5, 8], 8],
  'min': [[0, 1, 2], [0, 3, 6], 0],
  'sum': [[9, 12, 15], [3, 12, 21], 36]
}
```
開発
mean_var_std.pyにコードを書いてください。開発のために、main.pyを使ってコードをテストすることができます。

テスト
このプロジェクトの単体テストはtest_module.pyにあります。test_module.pyからmain.pyにテストをインポートしてありますので、便利にテストを行うことができます。
