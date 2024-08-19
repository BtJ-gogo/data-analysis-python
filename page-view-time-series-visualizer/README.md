### Instractions  
URL: [https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/page-view-time-series-visualizer](https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/page-view-time-series-visualizer)  
  
このプロジェクトでは、Pandas、Matplotlib、Seabornを使って時系列データを可視化します。データセットは、2016年5月9日から2019年12月3日までのfreeCodeCamp.orgフォーラムの日別ページビュー数を含んでいます。データ可視化により、訪問パターンを理解し、年間および月間の成長を把握することができます。  
  
以下のタスクを実行してください：  
  
* Pandasを使用して"fcc-forum-pageviews.csv" からデータをインポートし、インデックスを日付の列に設定します。  
* データセットの上位2.5%または下位2.5%のページビュー数の日をフィルタリングして除外し、データをクリーンアップする。  
* draw_line_plot 関数を作成します。Matplotlibを使用して、"examples/Figure_1.png" に似た折れ線グラフを描画します。タイトルは「Daily freeCodeCamp Forum Page Views 5/2016-12/2019」とし、x軸のラベルを「Date」、y軸のラベルを「Page Views」に設定します。  
* draw_bar_plot 関数を作成します。各年ごとの月別の平均日別ページビューを表示する棒グラフを描画します。グラフのレジェンドは月のラベルを表示し、タイトルを「Months」にします。グラフのx軸のラベルを「Years」、y軸のラベルを「Average Page Views」に設定します。  
* draw_box_plot 関数を作成します。Seabornを使用して、年別と月別の二つの隣接する箱ひげ図を描画します。"examples/Figure_3.png" に似たものです。1つ目のグラフのタイトルは「Year-wise Box Plot (Trend)」、2つ目のグラフのタイトルは「Month-wise Box Plot (Seasonality)」とし、月のラベルは1月から始まるように設定します。x軸とy軸のラベルも適切に設定します。データを準備するためのコマンドも含まれています。
  
各チャートについて、データフレームのコピーを使用することを確認してください。  

### 開発  

time_series_visualizer.py にコードを書きます。開発中は、main.py を使ってコードをテストできます。  
### テスト  
  
このプロジェクトのユニットテストは test_module.py にあります。テストは main.py にインポートされていますので、便利に使ってください。  
### 提出  
  
プロジェクトのURLをコピーして、freeCodeCampに提出してください。  
