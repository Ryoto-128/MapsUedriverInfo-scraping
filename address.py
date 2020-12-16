import time
import multiprocessing
from multiprocessing import Pool

from modules.fileIO import Csv
from modules.serchGoogle import Address

# 定数
input_path = './address_inputFile/助成金九州〜 - 九州①.csv'
read_row = [0, 1 ,2, 3,4]
target_row = 1
other_write_row = [0, 1, 2, 3,4]
output_path = './output/助成金九州〜 - 九州①.csv'


if __name__ == '__main__':
    # csvの読み込み
    csv = Csv()
    contents = csv.readCsv(input_path, read_row)
    
    # 検索
    address = Address()
    resolt_contents = address.serchAddress(contents, target_row, other_write_row)
    
    # 出力
    csv.addContents(output_path, resolt_contents)