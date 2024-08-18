### Instractions  

URL: [https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/medical-data-visualizer](https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/medical-data-visualizer)  
  
このプロジェクトでは、matplotlib、seaborn、およびpandasを使用して、健康診断データを視覚化し、計算を行います。データセットの値は、健康診断中に収集されました。

データの説明
データセットの行は患者を表し、列は体の測定値、さまざまな血液検査の結果、およびライフスタイルの選択などの情報を表します。このデータセットを使用して、心疾患、体の測定値、血液マーカー、およびライフスタイルの選択との関係を調査します。

ファイル名: medical_examination.csv
| Feature                                | Variable Type        | Variable       | Value Type                            |
|----------------------------------------|----------------------|----------------|---------------------------------------|
| Age                                    | Objective Feature    | age            | int (days)                            |
| Height                                 | Objective Feature    | height         | int (cm)                              |
| Weight                                 | Objective Feature    | weight         | float (kg)                            |
| Gender                                 | Objective Feature    | gender         | categorical code                      |
| Systolic blood pressure                | Examination Feature  | ap_hi          | int                                   |
| Diastolic blood pressure               | Examination Feature  | ap_lo          | int                                   |
| Cholesterol                            | Examination Feature  | cholesterol    | 1: normal, 2: above normal, 3: well above normal |
| Glucose                                | Examination Feature  | gluc           | 1: normal, 2: above normal, 3: well above normal |
| Smoking                                | Subjective Feature   | smoke          | binary                                |
| Alcohol intake                         | Subjective Feature   | alco           | binary                                |
| Physical activity                      | Subjective Feature   | active         | binary                                |
| Presence or absence of cardiovascular disease | Target Variable | cardio         | binary                                |

### タスク
examples/Figure_1.pngに似たチャートを作成します。そこでは、cholesterol、gluc、alco、active、smokeの変数に対する、cardio=1とcardio=0の患者の良好および不良な結果の数を、異なるパネルで表示します。

medical_data_visualizer.pyで次のタスクをデータを使って完了してください：

* データにoverweight列を追加します。人が過体重かどうかを判断するには、最初に体重（kg）を身長（m）の二乗で割ってBMIを計算します。この値が* 25を超える場合、その人は過体重です。過体重でない場合は0、過体重の場合は1の値を使用します。
* データを正規化して、0が常に良好、1が常に不良になるようにします。cholesterolまたはglucの値が1の場合、その値を0にします。値が1を超える場合、その値を1にします。
* データをロング形式に変換し、seabornのcatplot()を使用してカテゴリカルフィーチャーの値の数を表示するチャートを作成します。データセットを* Cardioで分割し、各cardio値に対して1つのチャートを表示します。チャートはexamples/Figure_1.pngのように見えるはずです。
* データをクリーニングします。次の条件に該当する患者セグメントを除外します:
  * 拡張期血圧が収縮期血圧より高い (正しいデータを保持するには (df['ap_lo'] <= df['ap_hi']) を使用)
  * 身長が2.5パーセンタイル未満 (正しいデータを保持するには (df['height'] >= df['height'].quantile(0.025) を使用)
  * 身長が97.5パーセンタイルを超える
  * 体重が2.5パーセンタイル未満
  * 体重が97.5パーセンタイルを超える
* データセットを使用して相関行列を作成します。seabornのheatmap()を使用して相関行列をプロットします。上三角をマスクします。チャートはexamples/Figure_2.pngのように見えるはずです。
* 変数がNoneに設定されている場合は、正しいコードに設定するようにしてください。

ユニットテストはtest_module.pyに記述されています。  

### 手順  
medical_data_visualizer.pyファイルの各番号の横に、以下の指示番号に関連するコードを追加します。  

1. medical_examination.csvからデータをインポートし、それをdf変数に割り当てます。  
1. df変数にoverweight列を作成します。  
1. データを正規化して、0が常に良好、1が常に不良になるようにします。cholesterolまたはglucの値が1の場合、その値を0にします。値が1を超える場合、その値を1にします。  
1. draw_cat_plot関数でカテゴリカルプロットを描画します。  
1. cholesterol、gluc、smoke、alco、active、overweightの値を使って、df_cat変数にpd.meltを使用してデータフレームを作成します。  
1. df_catのデータをグループ化し、cardioごとに分割して再フォーマットします。各フィーチャーのカウントを表示します。catplotが正常に動作するように、1つの列の名前を変更する必要があります。  
1. データをロング形式に変換し、seabornライブラリが提供するメソッドを使用して、カテゴリカルフィーチャーの値の数を表示するチャートを作成します: sns.catplot()をインポートします。  
1. 出力用の図を取得し、それをfig変数に格納します。  
1. 次の2行を変更しないでください。  
1. draw_heat_map関数でヒートマップを描画します。
2. df_heat 変数内のデータをクリーンアップし、不正なデータを含む次の患者セグメントをフィルタリングして除外します。  
    * 身長が2.5パーセンタイル未満の場合 (正しいデータを保持するには (df['height'] >= df['height'].quantile(0.025) を使用)  
    * 身長が97.5パーセンタイルを超える  
    * 体重が2.5パーセンタイル未満  
    * 体重が97.5パーセンタイルを超える  
12. 相関行列を計算し、それをcorr変数に格納します。  
13. 上三角形のマスクを生成し、それをmask変数に格納します。 
1. matplotlibの図を設定します。  
1. seabornライブラリが提供するメソッドを使用して相関行列をプロットします: sns.heatmap()をインポートします。  
1. 次の2行を変更しないでください。  
### 開発  
コードはmedical_data_visualizer.pyに記述してください。開発用に、main.pyを使用してコードをテストできます。  

### テスト  
このプロジェクトのユニットテストはtest_module.pyにあります。便宜上、test_module.pyからmain.pyにテストをインポートしました。  

### 提出  
プロジェクトのURLをコピーし、それをfreeCodeCampに提出してください。  
