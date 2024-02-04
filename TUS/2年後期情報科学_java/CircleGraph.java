import javafx.application.Application;
import javafx.scene.Scene;
import javafx.stage.Stage;
import javafx.scene.Group;
import javafx.scene.canvas.Canvas;
import javafx.scene.paint.Color;
import javafx.scene.canvas.GraphicsContext;
import javafx.scene.shape.ArcType;
import javafx.scene.text.Font;
import java.util.Random;
import javafx.scene.paint.Color;
import java.io.*; 


public class CircleGraph extends Application {
    double wincoordinatex = 400;
    double wincoordinatey = 400;
    
    @Override
    public void start(Stage st) throws Exception {
	Group root = new Group();
	Canvas canvas = new Canvas(wincoordinatex, wincoordinatey); //windowへの描画の設定
	GraphicsContext gc = canvas.getGraphicsContext2D();
	drawShapes(gc);
	
	root.getChildren().add(canvas);

	Scene scene = new Scene(root, wincoordinatex, wincoordinatey, Color.WHITE);
	st.setTitle("Circle Graph");
	st.setScene(scene);
	st.show();
    }
  
    public static void main(String[] a) {
	launch(a);
    }
    
    private void drawShapes(GraphicsContext gc) {
	gc.scale(wincoordinatex / 400, wincoordinatey / 400);
	
	int[] data = new int[1000]; //配列paに読み込んだ値を格納し、データ数をnumOfpa煮格納する
	int numOfdata = 0;
	try {
	    File file = new File("./data.txt");
	    FileReader fr = new FileReader(file);
	    BufferedReader br = new BufferedReader(fr);
	    String str = br.readLine(); 
	    String strdata = str; 

	    while (str != null) {   //読み取った文字を全て結合する
		str = br.readLine(); 
		
		if (str != null){ 
		    strdata = strdata + " " + str;}
	    }
	    
	    br.close(); 
	    String[] arraydata = strdata.split(" ");
	    for(int i = 0; i < arraydata.length; i++){
		data[i] = Integer.parseInt(arraydata[i]);
	    }
	    numOfdata = arraydata.length;

	    
	} catch (FileNotFoundException e) { //例外が生じたときの処理
	    System.err.println("ファイルが開けませんでした．");
	} catch (IOException e) { 
	    System.err.println("ファイルの読み込みに失敗しました．");
	} catch (NumberFormatException e) { 
	    System.err.println("整数化に失敗しました。");
	} 
	//ここまでは３つのグラフ全てに記述するプログラム
	
	gc.strokeOval(110,110,180,180); //円の描画
	gc.setLineWidth(2);
	
	gc.setStroke(Color.BLACK); //右に記載するデータ番号と色についての大枠の描画
	gc.strokeLine(340,50,380,50);
	gc.strokeLine(340,50 + (numOfdata * 20) + 6 ,380, 50 + (numOfdata * 20) + 6);
	gc.strokeLine(340,50,340,50 + (numOfdata * 20) + 6);
	gc.strokeLine(380,50,380,50 + (numOfdata * 20) + 6);
	gc.setFill(Color.LIGHTGRAY);
	gc.fillRect(340,50,40,numOfdata * 20 + 6);
	
	
	double total = 0;//各データの全体に占める割合を算出するために、データの合計値を計算
	for(int i = 0;i < numOfdata;i++){
	    total = total + data[i];
	}
	
	Color[] color = new Color[numOfdata]; //乱数を使用して色をランダムに指定
	Random rnd = new Random();
	for(int i = 0; i < numOfdata; i++){
	    color[i] = Color.rgb(rnd.nextInt(256),rnd.nextInt(256)
				 ,rnd.nextInt(256));
	}

	
	double s = 90;
	double t = -(Math.PI / 2);
	for(int i = 0; i < numOfdata; i++){  //円ぐらふの色の描画
	    gc.setFill(color[i]);
	    gc.fillArc(110,110,180,180,s,-(data[i] * 360 / total ),ArcType.ROUND);
	    s = s - (data[i] * 360 / total); 
	    gc.setFill(Color.BLACK);
	    
	    gc.fillText(String.valueOf(data[i]), //数値の出力
			190 + 110 * Math.cos(t + (Math.PI * data[i] / total / 2)
					     + (Math.PI / 36) ),
			203 + 110 * Math.sin(t + (Math.PI * data[i] / total /2) 
					     + (Math.PI /36)) );
	    t = t + (2 * Math.PI * data[i] / total); 
	    

	    //各データの詳細を記載するときの番号と色の描画
	    gc.fillText(String.valueOf(i+1), 360 , 67 + (i * 20));
	    gc.setStroke(Color.BLACK);
	    gc.setLineWidth(1);
	    gc.strokeLine(347, 60 + (i * 20), 355, 60 + (i * 20));
	    gc.strokeLine(347, 68 + (i * 20), 355, 68 + (i * 20));
	    gc.strokeLine(347, 60 + (i * 20), 347, 68 + (i * 20));
	    gc.strokeLine(355, 60 + (i * 20), 355, 68 + (i * 20));
	    
	    gc.setFill(color[i]);
	    gc.fillRect(347, 60 + (i * 20), 8, 8);
	}
    }
}
