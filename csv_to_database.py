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
    
    #---column名からindex番号を取得
    def get_column_no(self,clumn_name):
        column_no = 0

        table_data = self.select_all()

        data = table_data[0]
        column_no = data.index(clumn_name)

        return column_no

    #---SELECT ALL
    def select_all(self):
        table_data = []
        
        with open(self.csv_name,"r") as f:
            data = csv.reader(f)
            for row in data:
                table_data.append(row)
        f.close

        return table_data














