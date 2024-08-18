### Instructions  
URL: [https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/demographic-data-analyzer](https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/demographic-data-analyzer)  
  
この課題では、Pandasを使用して人口統計データを分析する必要があります。1994年の国勢調査データベースから抽出された人口統計データセットが与えられています。データは次のような形式です。  
```
|    |   age | workclass        |   fnlwgt | education   |   education-num | marital-status     | occupation        | relationship   | race   | sex    |   capital-gain |   capital-loss |   hours-per-week | native-country   | salary   |
|---:|------:|:-----------------|---------:|:------------|----------------:|:-------------------|:------------------|:---------------|:-------|:-------|---------------:|---------------:|-----------------:|:-----------------|:---------|
|  0 |    39 | State-gov        |    77516 | Bachelors   |              13 | Never-married      | Adm-clerical      | Not-in-family  | White  | Male   |           2174 |              0 |               40 | United-States    | <=50K    |
|  1 |    50 | Self-emp-not-inc |    83311 | Bachelors   |              13 | Married-civ-spouse | Exec-managerial   | Husband        | White  | Male   |              0 |              0 |               13 | United-States    | <=50K    |
|  2 |    38 | Private          |   215646 | HS-grad     |               9 | Divorced           | Handlers-cleaners | Not-in-family  | White  | Male   |              0 |              0 |               40 | United-States    | <=50K    |
|  3 |    53 | Private          |   234721 | 11th        |               7 | Married-civ-spouse | Handlers-cleaners | Husband        | Black  | Male   |              0 |              0 |               40 | United-States    | <=50K    |
|  4 |    28 | Private          |   338409 | Bachelors   |              13 | Married-civ-spouse | Prof-specialty    | Wife           | Black  | Female |              0 |              0 |               40 | Cuba             | <=50K    |
```
次の質問に答えるためにPandasを使用してください：  

* 各人種にどれくらいの人が含まれているかを求めてください。これは人種名をインデックスラベルとしたPandasシリーズでなければなりません（race列）。  
* 男性の平均年齢は？  
* 学士号を持っている人の割合は？  
* 高度な教育（学士、修士、博士）を受けた人のうち、50Kを超える収入を得ている人の割合は？  
* 高度な教育を受けていない人のうち、50Kを超える収入を得ている人の割合は？  
* 週あたりの最低労働時間は？  
* 最低労働時間の人のうち、50Kを超える収入を得ている人の割合は？  
* 50Kを超える収入を得ている人の割合が最も高い国はどこで、その割合は？  
* インドで50Kを超える収入を得ている人の最も人気のある職業は何ですか？  
* demographic_data_analyzer.pyのスターターコードを使用してください。Noneに設定されているすべての変数を、適切な計算またはコードに設定するようにコードを更新してください。すべての小数点以下の数値は一番近い1桁に丸めてください。  

開発  
demographic_data_analyzer.pyでコードを記述してください。開発中はmain.pyを使用してコードをテストできます。  

テスト  
このプロジェクトのユニットテストはtest_module.pyにあります。便宜上、test_module.pyからのテストはmain.pyにインポートされています。  

提出  
プロジェクトのURLをコピーして、freeCodeCampに提出してください。  

データセットの出典  
Dua, D. and Graff, C. (2019). UCI Machine Learning Repository. Irvine, CA: University of California, School of Information and Computer Science.  
