import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import java.util.*;

public class OseroAI extends JPanel {
	static final int EMPTY = 0, Kuro = 1, Shiro = 2;
    //拡張(1)8*8マスにする
	static final int YMAX = 8, XMAX = 8;
	ArrayList<Figure> figs = new ArrayList<Figure>();//図形オブジェクトの保持
	boolean turn = true;//黒がtrue
	int winner = EMPTY;
	int[][] board = new int[YMAX][XMAX];
	Text t1 = new Text(20, 20, "オセロ、次の手番：黒", new Font("Serif", Font.BOLD, 22));

	public OseroAI() {
		figs.add(t1);
		for (int i = 0; i < YMAX * XMAX; ++i) {
			int r = i / YMAX, c = i % XMAX;
            //拡張(1)盤面を緑にする
			figs.add(new Rect(Color.GREEN, 80 + r * 30, 40 + c * 30, 28, 28));
		}
        //拡張(3)初期石の配置
        for (int i = 0; i < 4; i++) {
            //初期石の置きたいマスに対して配列インデックスを指定
			int index = i == 0 ? 28 : i == 1 ? 29 : i == 2 ? 36 : 37;
            Figure targetFigure = figs.get(index);
            Rect targetRect = (Rect) targetFigure;
            int targetX = targetRect.getX();
            int targetY = targetRect.getY();
            
            // i の値に応じて addKuroishi または addShiroisi を実行
            if (i == 0 || i == 3) {
                figs.add(new Kuroishi(targetX, targetY,10));
				if(i == 0){
					board[3][3] = Kuro;
				}else{
					board[4][4] = Kuro;
				}
            } else {
                figs.add(new Shiroisi(targetX, targetY,10));
				if(i == 1){
					board[3][4] = Shiro;
				}else{
					board[4][3] = Shiro;
				}
            }
        }
		setOpaque(false);
		
        //大きく変更。拡張(4~8)
        addMouseListener(new MouseAdapter() {
			public void mouseClicked(MouseEvent evt) {
				Rect r = pick(evt.getX(), evt.getY());
				int x = (r.getX() - 80) / 30, y = (r.getY() - 40) / 30;

                //AI作成のためチャレンジ課題拡張
                //黒を手動、白はAI(自動化)とする
                
                if (isValidMove(x, y)) {
                    // オセロを置く処理
                    board[y][x] = (turn ? Kuro : Shiro);
                    if(turn){
                        figs.add(new Kuroishi(80 + 30 * x, 40 + 30 * y,10));

                    }else{
                        figs.add(new Shiroisi(80 + 30 * x, 40 + 30 * y,10));
                    }
                    flipOpponentStones(x, y);
                    turn = !turn;
                    t1.setText((turn ? "黒" : "白") + "のターン");
                } else if(board[y][x] != EMPTY){
                    t1.setText((turn ? "黒" : "白") + "のターン:そこは空いていません");
                    repaint();
                    return;
                }else{
                    t1.setText((turn ? "黒" : "白") + "のターン:そこには石を置けません");
                    repaint();
                    return;
                }

                finOrSkip();
                repaint();

                //白のターンはAIで自動化             
                putAI();
                finOrSkip();
                return;
            
            }
        });
    } 

	//拡張(4)
	//石が置けるか判定
	private boolean isValidMove(int x, int y) {
		if (board[y][x] != EMPTY) {
			return false;
		}
		int opponentStone = turn ? Shiro : Kuro;
	
		// 8方向それぞれに対してチェック
		for (int dx = -1; dx <= 1; dx++) {
			for (int dy = -1; dy <= 1; dy++) {
				if (dx == 0 && dy == 0) continue;//スキップ
				if (canFlip(x, y, dx, dy, opponentStone)) {
					return true;
				}
			}
		}
		return false;
	}

	//拡張(4)
	//ある方向に対して反転できるか判定
	private boolean canFlip(int x, int y, int dx, int dy, int opponentStone) {
		int nx = x + dx;
		int ny = y + dy;
		boolean hasOpponentStone = false;
	
		while (nx >= 0 && nx < XMAX && ny >= 0 && ny < YMAX) {
			if(board[ny][nx] == (turn ? Kuro : Shiro)) {
				if(hasOpponentStone){
					return true;
				}
				break;
			}else if (board[ny][nx] == EMPTY) {
				break;
			}else{
				hasOpponentStone = true;
				nx += dx;
				ny += dy;
			}
		}
		return false;
	}

	//拡張(5)
	//石の反転
	private void flipOpponentStones(int x, int y) {
		int myStone = (turn ? Kuro : Shiro);
		int opponentStone = (turn ? Shiro : Kuro);

		// 上下左右および斜めの方向に相手の石が続いているかどうかを判定し、反転させる
		flipDirection(x, y, 1, 1, myStone, opponentStone);
		flipDirection(x, y, 1, -1, myStone, opponentStone);
		flipDirection(x, y, 1, 0, myStone, opponentStone);
		flipDirection(x, y, 0, 1, myStone, opponentStone);
		flipDirection(x, y, -1, 1, myStone, opponentStone);
		flipDirection(x, y, -1, -1, myStone, opponentStone);
		flipDirection(x, y, -1, 0, myStone, opponentStone);
		flipDirection(x, y, 0, -1, myStone, opponentStone);
	}

	//拡張(5)
	//ある方向に対しての石の反転
	private void flipDirection(int x, int y, int dx, int dy, int myStone, int opponentStone) {
		int nx = x + dx;
		int ny = y + dy;
		ArrayList<Point> stonesToFlip = new ArrayList<>();
	
		while (nx >= 0 && nx < XMAX && ny >= 0 && ny < YMAX && board[ny][nx] == opponentStone) {
			stonesToFlip.add(new Point(nx, ny));
			nx += dx;
			ny += dy;
		}
	
		if (nx >= 0 && nx < XMAX && ny >= 0 && ny < YMAX && board[ny][nx] == myStone) {
			for (Point p : stonesToFlip) {
				board[p.y][p.x] = myStone;
				if(myStone == Kuro){
					figs.add(new Kuroishi(80 + 30 * p.x, 40 + 30 * p.y,10));
				}else{
					figs.add(new Shiroisi(80 + 30 * p.x, 40 + 30 * p.y,10));
				}
			}
		}
	}

    //拡張(7,8)
    public void finOrSkip(){   
        //石の数が0個になる、または全部石で埋まったら対局終了
        if(!exIshi(turn ? Kuro : Shiro) || !exEmpty()){
            t1.setText("試合終了!勝ったのは..." + decideWin());
            return;
        }

        //拡張(6),(チャレンジ1)
        //IsPutで置けるマスがあるか判定し、ないなら自動的に手番スキップ
        if(!isPut()){	
            turn = !turn;
            t1.setText("置けるマスがないのでスキップ。次の手番：" + (turn ? "黒" : "白"));
        }
    }

	//拡張(6),(チャレンジ1)
	//置けるマスが一つでも存在するか判定
	public boolean isPut(){
		for(int i = 0; i < YMAX * XMAX; ++i){
			int r = i / YMAX, c = i % XMAX;
			if(board[r][c] == EMPTY && isValidMove(c,r)){
				return true;
			}
		}
		return false;
	}

	//拡張(7)
	//盤面に自分の石が存在するか
	public boolean exIshi(int mycolor){
		for(int i = 0; i < YMAX * XMAX; ++i){
			int r = i / YMAX, c = i % XMAX;
			if(board[r][c] == mycolor){
				return true;
			}
		}
		return false;
	}

	//拡張(7)
	//盤面に空きマスが存在するか
	public boolean exEmpty(){
		for(int i = 0; i < YMAX * XMAX; ++i){
			int r = i / YMAX, c = i % XMAX;
			if(board[r][c] == EMPTY){
				return true;
			}
		}
		return false;
	}

	//拡張(8)
	//勝者の判別
	public String decideWin(){
		int countShiro = 0, countKuro = 0;
		for(int i = 0; i < YMAX * XMAX; ++i){
			int r = i / YMAX, c = i % XMAX;
			if(board[r][c] == Shiro){
				countShiro += 1;
			}else if (board[r][c] == Kuro){
				countKuro += 1;
			}
		}
		if(countShiro > countKuro){
			return "白!";
		}else if(countShiro < countKuro){
			return "黒!";
		}else{
			return "引き分け!";
		}
	}


    //AIによる実装
    public void putAI(){
        try {
            Thread.sleep(3000); // 人が過程を追いやすいように３秒スリープ
        } catch (InterruptedException e) {
            // InterruptedExceptionが発生した場合の処理
            e.printStackTrace();
        }
        if(turn){
            t1.setText("エラーが発生しました");        
        }else{
            //配置可能なマスを全て抽出
            int currentArray = 0; //indexArrayのlength
            int[][] indexArray = new int[64][2]; //配置可能なマスのインデックスを格納する配列
            for(int i = 0; i < YMAX * XMAX; ++i){
                int r = i / YMAX, c = i % XMAX;
                if(board[r][c] == EMPTY && isValidMove(c,r)){
                    indexArray[currentArray][0] = r;
                    indexArray[currentArray][1] = c;
                    currentArray += 1;
                }
            }

            //ランダムで置く場所を選択
            int randomNumber = (int) (Math.random() * (currentArray + 1));
            int y = indexArray[randomNumber][0];
            int x = indexArray[randomNumber][1];
            board[y][x] = Shiro;
            figs.add(new Shiroisi(80 + 30 * x, 40 + 30 * y,10));
            flipOpponentStones(x, y);
            turn = !turn;
            t1.setText((turn ? "黒" : "白") + "のターン");
            repaint();
        }
    }

	public Rect pick(int x, int y) {
		Rect r = null;
		for (Figure f : figs) {
            //Rectクラスのインスタンスであるか判定
			//与えられた座標が四角形の中にあるかどうかの判定
            if (f instanceof Rect && ((Rect) f).hit(x, y)) { 
                r = (Rect) f;//rにRectオブジェクトを代入
			}
		}
		return r;
	}

	public void paintComponent(Graphics g) {
		for (Figure f : figs) { //figsリスト内のオブジェクトの描画
			f.draw(g);
		}
	}

	private int ck(int x, int y, int dx, int dy) {
		int s = board[y][x], count = 1;//取得した状態(EMP,BATU,MARU)の連続数をカウント
		for (int i = 1; ck1(x + dx * i, y + dy * i, s); ++i) {
			++count;
		}
		for (int i = 1; ck1(x - dx * i, y - dy * i, s); ++i) {
			++count;//逆方向
		}
		return count;
	}

	private boolean ck1(int x, int y, int s) {
		return 0 <= x && x < XMAX && 0 <= y && y < YMAX && board[y][x] == s;
	}

	public static void main(String[] args) {
		JFrame app = new JFrame();
		app.add(new OseroAI());
		app.setSize(500, 320);
		app.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		app.setVisible(true);
	}

	interface Figure {
		public void draw(Graphics g);
	}

	static class Text implements Figure {
		int xpos, ypos;
		String txt;
		Font fn;

		public Text(int x, int y, String t, Font f) {
			xpos = x;
			ypos = y;
			txt = t;
			fn = f;
		}

		public void setText(String t) {
			txt = t;
		}

		public void draw(Graphics g) {
			g.setColor(Color.BLACK);
			g.setFont(fn);
			g.drawString(txt, xpos, ypos);
		}
	}
    //拡張(2)○×を白黒にする
	static class Kuroishi implements Figure {
		int xpos, ypos, size;

		public Kuroishi(int x, int y, int s) {
			xpos = x;
			ypos = y;
			size = s;
		}

		public void draw(Graphics g) {
			g.setColor(Color.BLACK);
			//((Graphics2D) g).setStroke(new BasicStroke(4));
			g.fillOval(xpos - size, ypos - size, 2 * size, 2 * size);
		}
	}
    //拡張(2)○×を白黒にする
	static class Shiroisi implements Figure {
		int xpos, ypos, size;

		public Shiroisi(int x, int y, int s) {
			xpos = x;
			ypos = y;
			size = s;
		}

		public void draw(Graphics g) {
			g.setColor(Color.WHITE);
			//((Graphics2D) g).setStroke(new BasicStroke(4));
			g.fillOval(xpos - size, ypos -size, 2* size, 2 * size);
		}
	}

	static class Rect implements Figure {
		Color col;
		int xpos, ypos, width, height;

		public Rect(Color c, int x, int y, int w, int h) {
			col = c;
			xpos = x;
			ypos = y;
			width = w;
			height = h;
		}

		public boolean hit(int x, int y) {
			return xpos - width / 2 <= x && x <= xpos + width / 2 && ypos - height / 2 <= y && y <= ypos + height / 2;
		}

		public int getX() {
			return xpos;
		}

		public int getY() {
			return ypos;
		}

		public void draw(Graphics g) {
			g.setColor(col);
			g.fillRect(xpos - width / 2, ypos - height / 2, width, height);
		}
	}
}
