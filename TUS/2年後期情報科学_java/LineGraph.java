import javafx.application.Application;
import javafx.scene.Scene;
import javafx.stage.Stage;
import javafx.scene.Group;
import javafx.scene.canvas.Canvas;
import javafx.scene.paint.Color;
import javafx.scene.canvas.GraphicsContext;
import java.io.*; 


public class LineGraph extends Application {
    
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
	st.setTitle("Line Graph");
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
      
	    
	} catch (FileNotFoundException e) {    //例外が生じた時の処理
	    System.err.println("ファイルが開けませんでした．");
	} catch (IOException e) { 
	    System.err.println("ファイルの読み込みに失敗しました．");
	} catch (NumberFormatException e) { 
	    System.err.println("整数化に失敗しました。");
	} 
	//ここまでは３つのグラフ全てに記述するプログラム
	
	
	int maxdata = data[0]; //データの最大値を求める
	for(int i = 1; i < numOfdata; i++){
	    if(maxdata >= data[i]){
	    }else{
		maxdata = data[i];
	    }
	}
	int staOfvertical = 0;         //グラフの縦軸をデータの最大値によって設定
	for(int i = 0; i<1000; i++){
	    if((maxdata >= i*50) && (maxdata < i*50 + 50)){
		staOfvertical = i*50 + 50;
		break;
	    }
	}

	gc.setFill(Color.DARKGRAY);
	gc.fillRect(50, 50, 300, 200); //背景の描画
	gc.setStroke(Color.BLACK);
	gc.setFill(Color.BLACK);
	
	gc.strokeLine(50, 250, 350, 250); // 横軸
	gc.strokeLine(50, 250, 50, 50);   // 縦軸
	
	for (int i = 0; i < (staOfvertical/50 +1); i++) {
	    gc.strokeLine(48, 50 + i * 200 / (staOfvertical/50), 
			  350, 50 + i * 200 / (staOfvertical/50));// 縦軸の目盛
	    gc.fillText(String.valueOf(i * 50), 20, 
			250 - i * 200 / (staOfvertical/50));      // 縦軸の値
	}
	
	for (int i = 0; i < numOfdata + 1; i++) {
	    gc.strokeLine(50+(i*300/numOfdata), 250, 
			  50+(i*300/numOfdata), 252);     // 横軸の目盛
	}
	
	for (int i = 0; i < numOfdata; i++) {
	    gc.setFill(Color.BLACK);
	    gc.fillText(String.valueOf(i + 1), 
			57 + (i * 300 / numOfdata), 263); // 横軸の値
	}
	
	gc.setStroke(Color.BLUE); //棒の塗りつぶし
	for(int i = 0; i < numOfdata - 1; i++){
	    gc.strokeLine(60 + (i * 300 / numOfdata), 250 - data[i]*200/staOfvertical
			  ,60+((i+1)*300/numOfdata), 250-data[i+1]*200/staOfvertical);
	}
    }
}
