#-----------------------------------------------------------------------------------
#                   CSVをデータベースとして使用するパッケージ
#-----------------------------------------------------------------------------------
import csv

class CsvToDatabase:

    #---コンストラクタ
    def __init__(self,table_name,columns):
        
        # テーブル名をセット
        self.table_name = table_name

        #ファイル名をセット
        self.csv_name = table_name + ".csv"
        
        # 列名(ヘッダ)を分割してリストに
        self.columns = columns.split(',')

    #---列名(ヘッダ)を表示
    def print_columns(self):
        print(self.columns)

    #---テーブル(CSVファイル)を作成
    def create_table(self):
        with open(self.csv_name,"w") as f:
            writer = csv.writer(f)
            writer.writerow(self.columns)
        f.close




a = CsvToDatabase("test","a,d")
a.create_table()








