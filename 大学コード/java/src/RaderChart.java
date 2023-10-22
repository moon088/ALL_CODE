package 大学コード.java.src;

import javafx.application.Application;
import javafx.scene.Scene;
import javafx.stage.Stage;
import javafx.scene.Group;
import javafx.scene.canvas.Canvas;
import javafx.scene.paint.Color;
import javafx.scene.canvas.GraphicsContext;
import java.io.*;

public class RadarChart extends Application {
    double wincoordinatex = 400;
    double wincoordinatey = 400;

    @Override
    public void start(Stage st) throws Exception {
        Group root = new Group();
        Canvas canvas = new Canvas(wincoordinatex, wincoordinatey); // windowへの描画の設
        GraphicsContext gc = canvas.getGraphicsContext2D();
        drawShapes(gc);

        root.getChildren().add(canvas);

        Scene scene = new Scene(root, wincoordinatex, wincoordinatey, Color.WHITE);
        st.setTitle("Radar Chart");
        st.setScene(scene);
        st.show();
    }

    public static void main(String[] a) {
        launch(a);
    }

    private void drawShapes(GraphicsContext gc) {
        gc.scale(wincoordinatex / 400, wincoordinatey / 400);
        int[] data = new int[1000]; // 配列paに読み込んだ値を格納し、データ数をnumOfpa煮格納する
        int numOfdata = 0;
        try {
            File file = new File("./data.txt");
            FileReader fr = new FileReader(file);
            BufferedReader br = new BufferedReader(fr);
            String str = br.readLine();
            String strdata = str;

            while (str != null) { // 読み取った文字を全て結合する
                str = br.readLine();

                if (str != null) {
                    strdata = strdata + " " + str;
                }
            }

            br.close();
            String[] arraydata = strdata.split(" ");
            for (int i = 0; i < arraydata.length; i++) {
                data[i] = Integer.parseInt(arraydata[i]);
            }
            numOfdata = arraydata.length;

        } catch (FileNotFoundException e) { // 例外が生じた時の処
            System.err.println("ファイルが開けませんでした．");
        } catch (IOException e) {
            System.err.println("ファイルの読み込みに失敗しました．");
        } catch (NumberFormatException e) {
            System.err.println("整数化に失敗しました。");
        }
        // ここまでは３つのグラフ全てに記述するプログラム

        int maxdata = data[0]; // データの最大値を求める
        for (int i = 1; i < numOfdata; i++) {
            if (maxdata >= data[i]) {
            } else {
                maxdata = data[i];
            }
        }

        int staOfvertical = 0; // グラフの縦軸をデータの最大値によって設
        for (int i = 0; i < 1000; i++) {
            if ((maxdata >= i * 50) && (maxdata < i * 50 + 50)) {
                staOfvertical = i * 50 + 50;
                break;
            }
        }

        gc.setStroke(Color.BLACK);
        gc.setFill(Color.BLACK);
        double[] coordinateOfx = new double[numOfdata];
        double[] coordinateOfy = new double[numOfdata];

        for (int i = 0; i < numOfdata; i++) {
            for (int j = 1; j < (staOfvertical / 50) + 1; j++) { // 背景の網目の描画-1
                gc.strokeLine(200 + 130 / (staOfvertical / 50) * j *
                        Math.cos(-(Math.PI / 2) + i * 2 * Math.PI / numOfdata),
                        200 + 130 / (staOfvertical / 50) * j *
                                Math.sin(-(Math.PI / 2) + i * 2 * Math.PI / numOfdata),
                        200 + 130 / (staOfvertical / 50) * j *
                                Math.cos(-(Math.PI / 2) + (i + 1) * 2 * Math.PI / numOfdata),
                        200 + 130 / (staOfvertical / 50) * j *
                                Math.sin(-(Math.PI / 2) + (i + 1) * 2 * Math.PI / numOfdata));
            }

            // 多角形の内部を塗りつぶすために、データのx,y座標をそれぞれ配列に格納
            coordinateOfx[i] = 200 + (130 * data[i] / staOfvertical) *
                    Math.cos(-(Math.PI / 2) + (i * 2 * Math.PI / numOfdata));
            coordinateOfy[i] = 200 + (130 * data[i] / staOfvertical) *
                    Math.sin(-(Math.PI / 2) + (i * 2 * Math.PI / numOfdata));
        }

        // レーダーチャートの内部の塗りつぶし
        gc.setFill(Color.CORNFLOWERBLUE);
        gc.fillPolygon(coordinateOfx, coordinateOfy, numOfdata);
        gc.setFill(Color.BLACK);

        for (int i = 0; i < numOfdata; i++) {
            gc.strokeLine(200, 200, // 背景の網目の描画-
                    200 + 130 *
                            Math.cos(-(Math.PI / 2) + (i * 2 * Math.PI / numOfdata)),
                    200 + 130 *
                            Math.sin(-(Math.PI / 2) + (i * 2 * Math.PI / numOfdata)));

            gc.fillText(String.valueOf(i + 1), // データ番号の記述
                    196 + 140 *
                            Math.cos(-(Math.PI / 2) + (i * 2 * Math.PI / numOfdata)),
                    204 + 140 *
                            Math.sin(-(Math.PI / 2) + (i * 2 * Math.PI / numOfdata)));

            // 各データを直線で結ぶ-1
            gc.strokeLine(200 + (130 * data[i] / staOfvertical) *
                    Math.cos(-(Math.PI / 2) + (i * 2 * Math.PI / numOfdata)),
                    200 + (130 * data[i] / staOfvertical) *
                            Math.sin(-(Math.PI / 2) + (i * 2 * Math.PI / numOfdata)),
                    200 + (130 * data[i + 1] / staOfvertical) *
                            Math.cos(-(Math.PI / 2) + ((i + 1) * 2 * Math.PI / numOfdata)),
                    200 + (130 * data[i + 1] / staOfvertical) *
                            Math.sin(-(Math.PI / 2) + ((i + 1) * 2 * Math.PI / numOfdata)));
        }
        // 各データを直線で結ぶ-2(最後の直線)
        gc.strokeLine(200 + (130 * data[numOfdata - 1] / staOfvertical) *
                Math.cos(-(Math.PI / 2) + ((numOfdata - 1) * 2 * Math.PI / numOfdata)),
                200 + (130 * data[numOfdata - 1] / staOfvertical) *
                        Math.sin(-(Math.PI / 2) + ((numOfdata - 1) * 2 * Math.PI / numOfdata)),
                200, 200 - (130 * data[0] / staOfvertical));

        // 縦軸の値の記述
        for (int i = 0; i < (staOfvertical / 50) + 1; i++) {
            gc.fillText(String.valueOf(i * 50),
                    203, 200 - (i * 6500 / staOfvertical));
        }
    }
}
