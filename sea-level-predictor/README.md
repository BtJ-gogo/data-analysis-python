### Instractions
URL[https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/sea-level-predictor](https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/sea-level-predictor)  
  
以下のタスクを完了するために、1880年からの世界の平均海面変動に関するデータセットを分析します。このデータを使用して、2050年までの海面変動を予測します。  

* Pandasを使用して、データをepa-sea-level.csvからインポートします。  
* matplotlibを使用して、Year列をx軸、CSIRO Adjusted Sea Level列をy軸にした散布図を作成します。  
*  scipy.statsからlinregress関数を使用して、最小二乗法による線形回帰の傾きとy切片を取得します。この回帰直線を散布図にプロットし、2050年まで延長して海面上昇を予測します。  
* 2000年以降のデータを使用して新しい回帰直線をプロットします。この回帰直線も2050年まで延長して、2000年以降の上昇率が続いた場合の海面上昇を予測します。  
* x軸のラベルは「Year」、y軸のラベルは「Sea Level (inches)」、タイトルは「Rise in Sea Level」にします。  
* boilerplateには画像を保存し、返すためのコマンドも含まれています。
  
### 開発  
コードをsea_level_predictor.pyに書きます。開発の際には、main.pyを使用してコードをテストできます。  
  
### テスト
このプロジェクトの単体テストはtest_module.pyにあります。main.pyにtest_module.pyからテストをインポートしているので、便利に使用できます。
  
### 提出  
プロジェクトのURLをコピーし、freeCodeCampに提出します。  
  
### データソース  
CSIRO、2015年; NOAA、2015年のデータを使用した、米国環境保護庁による1880年から2014年の世界平均絶対海面変動。
