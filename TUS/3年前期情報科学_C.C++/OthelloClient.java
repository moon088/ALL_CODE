import java.net.*;
import java.io.*;
import java.util.*;

class OthelloClient {
    static int c;
    static Socket s;
    static InputStream sIn;
    static OutputStream sOut;
    static BufferedReader br;
    static PrintWriter pw;
    static int MyColor = 0;
    static int[] boardint = new int[64];
    static int[][] board = new int[8][8];
    static String[] strSer;
    static String str;
    static boolean[][] checkput = new boolean[8][8];
    static int OthelloValue[][] = {{2500,767,607,642,642,607,767,2500},{767,344,284,103,103,284,344,767},{607,284,114,182,182,114,284,607},{642,103,182,202,202,182,103,642},{642,103,182,202,202,182,103,642},{607,284,114,182,182,114,284,607},{767,344,284,103,103,284,344,767},{2500,767,607,642,642,607,767,2500}};
    
    static boolean Check_Put(int g, int r, int mycolor){
	if(board[g][r] != 0){ //石がすでに置いてある
	    return false;
	}
	
	if(g < 0 || g >= 8 || r < 0 || r >= 8){ // 盤面外
	    return false;        	    
	}
	
	for(int dg = -1; dg <= 1; dg++){
	    for(int dr = -1; dr <= 1; dr++){  //８
		if(dg == 0 && dr == 0){ // その場所はスルー
		    continue;//スキップ
		}
		
		int ng = g + dg;
		int nr = r + dr;
		boolean op = false;		
		while(ng >= 0 && ng < 8 && nr >= 0 && nr < 8){
		    if(board[ng][nr] == mycolor){
			if(op){//石の反転条件
			    return true; //trueの時点で終了
			}	    
			break;
	    
		    }else if(board[ng][nr] == 0){ //空きマス
			break;
		    }else{
			op = true; 
			ng = ng + dg; 
			nr = nr + dr; //同じ方向の一つ先のマスに進む
		    }
		}
	    }
	}
	return false;//なかった場合
    }
    
    public static void main(String args[]) {
	
	if (args.length != 1) {
	    System.out.println("No hostname given");
	    System.exit(1);
	}
	
	try {
	    s = new Socket(args[0], 46000);
	    
	    sIn = s.getInputStream();
	    sOut = s.getOutputStream();	
	    br = new BufferedReader(new InputStreamReader(sIn));
	    pw = new PrintWriter(new OutputStreamWriter(sOut),true);
	    
	    pw.println("NICK 6321120");
	    str = br.readLine(); //読み込み
	    strSer = str.split(" "); //読み込んだ文字列を空白で区切り配列に格納
	    
	    //ここまではチャットプログラム引用
	    while(strSer[0] != "END"){		
		switch (strSer[0]){
	  
		case "START":
		    if(Integer.parseInt(strSer[1]) == 1){
			MyColor = 1; //黒
			System.out.println("あなたは黒です");
			
		    }else{
			MyColor = -1;
			System.out.println("あなたは白です");
			
		    }
		    break;
		    
		case "BOARD":
		    int i = 0, j = 0, k = 0, l = 0;
		    while(l < 64){
			boardint[l] = Integer.parseInt(strSer[l+1]);
			l++;
		    }
		    System.out.println("現在の盤面状況");
		    while(j < 8){
			i = 0;
			while(i < 8){
			    board[i][j] = boardint[k]; 
			    if(boardint[8*i+j] == 1){
				System.out.print("●");
			    }else if(boardint[8*i+j] == -1){
				System.out.print("〇");
			    }else{
				System.out.print("　");
			    }
			    i++;
			    k++;
			}
			System.out.print("\n");
			j++;			
		    }
		    for(int x = 0; x < 8; x++){
			for(int y = 0; y < 8; y++){
			    checkput[y][x] = Check_Put(y, x, MyColor);
			}
		    }
		    
		    break;
		    
		    
		case "ERROR":
		    switch(strSer[1]){
		    case "1":
			System.out.println("書式が間違っています\n");
			break;
		    case "2":
			System.out.println("そこには置けません\n");
			break;
		    case "3":
			System.out.println("相手のターン中です\n");
			break;
		    case "4":
			System.out.println("処理できない命令です");
			break;
		    }
		    
		case "TURN":  
		    if(Integer.parseInt(strSer[1]) == MyColor){
			int x = 0;
			int y = 0;
			int value = 155;
			for(i = 0; i < 8; i++){
			    for(j = 0; j < 8; j++){
				if(Check_Put(j, i, MyColor)){
				    if(value < OthelloValue[j][i]){
					y = j;
					x = i;
					value = OthelloValue[j][i];
				    }
				}				
			    }
			}
			pw.println("PUT"+" "+x+" "+y);
			System.out.println("PUT"+" "+x+" "+y);  
		    }else{
		    }
		    break;
		    
		    
		case "CLOSE":
		    System.out.println("相手が切断しました");
		    break;
		}
		str = br.readLine();
		System.out.println(str);
		strSer = str.split(" ");
	    }	
	    sIn.close();
	    sOut.close();
	    s.close();
	    
	}
	
	
	catch (IOException e){
	    System.err.println("Caught IOException");
	    System.exit(1);
	}
    }
}

