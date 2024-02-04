tensorflow import keras
model = keras.models.load_model("C:\Users\81809\Documents\ALL_CODE\大学コード\プロジェクト課題自分\models\model1.py")
import dataset\_processor as dp
pr = dp.DatasetProcessor(
dirpath=’/content/drive/MyDrive/実験 2/prj-14/mj_files/2012’,
save_path=’/content/drive/MyDrive/実験 2/prj-14/mj_files’,
max_file=200
)
pr.process_dataset()