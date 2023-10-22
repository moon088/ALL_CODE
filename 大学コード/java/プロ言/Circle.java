package 大学コード.java.プロ言;

import javax.swing.text.AttributeSet.ColorAttribute;

public class Circle {
    public static void main(String[] args) {
    }
}

// 円を表すクラス
public class Circle {
    // インスタンス変数
    int xpos, ypos, rad;// 中心座標と半径
    Color col;// 色

    // クラス変数
    static int count; // 円の個数
    static ArrayList<Circle> circles;// 円をリストで管理

    // コンストラクタ
    // クラス名と一致させる、返戻地の型を指定しない
    // 多重定義可能
    public Circle() {
        int xpos, ypos, rad;
        Color col;
    }

    public Circle(Color c, int x, int y, int r) {
    }

    public Circle(Color c, int x1, int y1, int x2, int y2) {
    }

}
