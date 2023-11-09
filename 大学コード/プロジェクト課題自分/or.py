#TensorFlowを用いたORの学習モデルのサンプル
import tensorflow as tf
from tensorflow import keras
import numpy as np
import os
#KerasはTensorFlowの中に組み込まれている
#Keras公式もTensorFlowで使用することを推奨しているらしい

def main():
    #入力データ
    input_data = np.array([[0,0], [0,1], [1,0], [1,1]], dtype=np.float32)
    #教師データ
    label_data = np.array([0, 1, 1, 1], dtype=np.int32)

    train_data, train_label = input_data, label_data

    #検証データ(入力データと教師データを流用)
    validation_data, validation_label = input_data, label_data

    #モデルの定義
    model = keras.Sequential(
        #層をリストで与える
        #入力層は入力ベクトルから推測してくれるらしい
        #層数は3
        [
            #Denseは全結合層、つまり普通のニューラルネット
            keras.layers.Dense(3, activation='relu'),#中間層
            keras.layers.Dense(2, activation='softmax')#出力層
        ]
    )
    #これだけでモデルが作れる

    #学習に必要なアルゴリズムの設定
    #optimizer: 最適化アルゴリズム, loss: 損失関数, metrics: 学習結果の評価方法
    model.compile(
        optimizer = 'adam',
        loss = 'sparse_categorical_crossentropy',
        metrics = ['accuracy']
    )

    #学習の実行
    #x: 入力, y: 正解, epochs: エポック数(バッチの入力回数)
    #batch_size: バッチサイズ(一回の重み更新のための入力の個数)
    #validation_data: 検証データとその正解ラベル
    model.fit(
        x = train_data,
        y = train_label,
        epochs = 1000,
        batch_size = 8,
        validation_data = (validation_data, validation_label)
    )

    #model.save(os.path.join('result', 'outmodel'))
    #↑はモデルの保存に関しての記述


if __name__ == '__main__':
    main()


#Google Colabにでも貼り付けて実行してください
#実行すると
#------------------------------------------------------------
#Epoch 1/1000
#1/1 [==============================] - 1s 806ms/step - loss: 0.9129 - accuracy: 0.2500 - val_loss: 0.9097 - val_accuracy: 0.0000e+00
#Epoch 2/1000
#1/1 [==============================] - 0s 47ms/step - loss: 0.9097 - accuracy: 0.0000e+00 - val_loss: 0.9064 - val_accuracy: 0.0000e+00
#Epoch 3/1000
#1/1 [==============================] - 0s 51ms/step - loss: 0.9064 - accuracy: 0.0000e+00 - val_loss: 0.9032 - val_accuracy: 0.0000e+00
#Epoch 4/1000
#1/1 [==============================] - 0s 113ms/step - loss: 0.9032 - accuracy: 0.0000e+00 - val_loss: 0.9000 - val_accuracy: 0.0000e+00
#    ・
#    ・
#    ・
#Epoch 999/1000
#1/1 [==============================] - 0s 62ms/step - loss: 0.2205 - accuracy: 1.0000 - val_loss: 0.2202 - val_accuracy: 1.0000
#Epoch 1000/1000
#1/1 [==============================] - 0s 77ms/step - loss: 0.2202 - accuracy: 1.0000 - val_loss: 0.2200 - val_accuracy: 1.0000
#------------------------------------------------------------
#のような表示が出ると思います
#損失関数の値や精度をリアルタイムで見せてくれます
#accuracyは学習データに対する精度
#val_accuracyは検証データに対する精度
#val_accuracyの値で過学習の有無が判断できると思います
#実行終了まで一分くらいはかかります
#精度が100％にならないこともあります