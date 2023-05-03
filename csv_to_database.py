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

        #self.table_data = []

    #---列名(ヘッダ)を表示するメソッド
    def print_columns(self):
        print(self.columns)

    #---テーブル(CSVファイル)を作成するメソッド
    def create_table(self):
        with open(self.csv_name,"w") as f:
            writer = csv.writer(f)
            writer.writerow(self.columns)
        f.close

    def read_table(self):
        with open(self.csv_name,"r") as f:
            data = csv.reader(f)
            copy = data
            for row in data:
                for col in row:
                    print(col,end=",")
                print()
        f.close
        return copy

#    def get_table_data(self):
#        return self.table_data













