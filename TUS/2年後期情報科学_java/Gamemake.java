import javafx.application.Application;
import javafx.scene.Scene;
import javafx.stage.Stage;
import javafx.scene.Group;
import javafx.scene.canvas.Canvas;
import javafx.scene.paint.Color;
import javafx.scene.canvas.GraphicsContext;
import javafx.animation.AnimationTimer;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.shape.Rectangle;
import javafx.scene.input.KeyEvent;
import javafx.scene.input.KeyCode;

public class Gamemake extends Application{
    private int initialSceneWidth = 400;
    private int initialSceneHeight = 400;
    
    private MapAndChars mapAndChars;
    
  @Override
  public void start(Stage st) throws Exception {
      Group root = new Group();
      
      Scene scene = new Scene(root, initialSceneWidth, initialSceneHeight, Color.rgb(255,255,255));
      st.setTitle("Tile-based Game");
      st.setScene(scene);
      st.show();
      
      scene.setOnKeyPressed(this::keyPressed);
      
      mapAndChars = new MapAndChars(root);
    
      drawScreen();
    
     
      AnimationTimer timer = new AnimationTimer() {
	      @Override
	      public void handle(long t) { 
		  drawScreen();
	      }
	  };
      
      timer.start();
  }
    
    
    public static void main(String[] a) {
	launch(a);
    }
    
     public void drawScreen(){
	 mapAndChars.drawboy();
	 mapAndChars.drawcoin();
    }

    public void keyPressed(KeyEvent e) {
	KeyCode key = e.getCode();
	int dir = -1;
	switch ( key ) {
	case LEFT: dir = 2; break;
	case RIGHT: dir = 0; break;
	case UP: dir = 1; break;
	case DOWN: dir = 3; break;
	case SPACE:System.exit(0);break;
	}
	if ( dir >= 0 ) mapAndChars.boyMove(dir);
    }
}

class MapAndChars{
    char[][] map; 
    int MX = 6, MY = 6;
    String[] initialMap = {
	    "     C",
	    "  C  C",
	    "C     ",
	    "      ",
	    "   M  ",
	    "BBBBBB",
	};
    
    int boyX, boyY;
    ImageView boyView;

    int coinX, coinY;
    ImageView coinView;

    boolean hasCoin = false;

    MapAndChars(Group root){
	map = new char[MY+2][MX+2];
	    for (int x = 0; x <= MX+1; x++){
		map[0][x] = 'B';
		map[MY+1][x] = 'B';
	    }
	    for(int y = 0; y <= MY+1; y++){
	    map[y][0] = 'B';
	    map[y][MY+1] = 'B';
	    }
  
	    for (int y = 1; y <= MY; y++) {
		for (int x = 1; x <= MX; x++) {
		    map[y][x] = initialMap[y-1].charAt(x-1);
		}
	    }
	    drawInitialMapAndChars(root);
	}
	
    public void drawInitialMapAndChars(Group root) {
	Image image;
	for(int y = 1; y <= MX; y++){
	    for (int x = 1; x <= MX; x++){
		int xx = 50*x, yy = 50*y;
		switch ( map[y][x] ) { 
		case 'C':
		    image = new Image("./coin.gif");
		    coinView = new ImageView(image);
		    coinX = x;
		    coinY = y;
		    drawcoin();
		    root.getChildren().add(coinView);
		    break;
		case 'B': 
		    Block b = new Block(xx, yy);
		    root.getChildren().add(b.getParts());
		    break;
		case 'M': 
		    image = new Image("./boy.gif");
		    boyView = new ImageView(image);
		    boyX = x;
		    boyY = y;
		    drawboy();
		    root.getChildren().add(boyView);
		    break;
		}
		
	    }	    
	}
    }	


  


    public void drawboy() {
	boyView.setX(50*boyX);
	boyView.setY(50*boyY);
	boyView.toFront();
	boyView.setFitWidth(50.);
	boyView.setFitHeight(50.);
    }
    
    public void boyMove(int dir) {
	int dx = 0, dy = 0;
	switch ( dir ) {
	case 0: dx =  1; break; 
	case 1: dy = -1; break; 
	case 2: dx = -1; break; 
	case 3: dy =  1; break; 
	}
	if ( dx == 0 && dy == 0 ) return;
	if ( map[boyY+dy][boyX+dx] == 'B' ) return; 
	boyX += dx; boyY += dy;
	if ( map[boyY][boyX] == ' ' && map[boyY+1][boyX] == ' ' ) boyMove(3); 
    }
    
    public void drawcoin(){
	coinView.setX(50*coinX);
	coinView.setY(50*coinY);
	coinView.toFront();
	coinView.setFitWidth(50.);
	coinView.setFitHeight(50.);
    }

}


abstract class Tile {
  protected Group parts;

  Tile(int x, int y) {
    parts = new Group();
    parts.setTranslateX(x);
    parts.setTranslateY(y);
    construct();
  }
  
  //public void setX(double x) {parts.setTranslateX(x)};
  //public void setY(double y) {parts.setTranslateY(y)};
  //public double getX() {return parts.getTranslateX()};
  //public double getY() {return parts.getTranslateY()};
  public Group getParts() {return parts;};

  abstract public void construct(); 
  
}

class Block extends Tile {

  Block(int x, int y) {
    super(x, y);
  }
  
  @Override
  public void construct() { 
    Color c = Color.GREEN;
    
    Rectangle r1 = new Rectangle(0, 0, 26, 10);
    r1.setFill(c);
    Rectangle r2 = new Rectangle(32, 0, 18, 10);
    r2.setFill(c);
    Rectangle r3 = new Rectangle(0, 15, 10, 10);
    r3.setFill(c);
    Rectangle r4 = new Rectangle(16, 15, 34, 10);
    r4.setFill(c);
    Rectangle r5 = new Rectangle(0, 30, 18, 10);
    r5.setFill(c);
    Rectangle r6 = new Rectangle(24, 30, 26, 10);
    r6.setFill(c);
    parts.getChildren().add(r1);
    parts.getChildren().add(r2);
    parts.getChildren().add(r3);
    parts.getChildren().add(r4);
    parts.getChildren().add(r5);
    parts.getChildren().add(r6);
  }
   
}
