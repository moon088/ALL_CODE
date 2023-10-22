package 大学コード.java.src;

import java.awt.*;
import javax.swing.*;

public class Sample21 extends JFrame {
    public void pantComponent(Graphics g) {
        g.setColor(new Color(255, 180, 99));
        g.fillOval(100, 50, 100, 100);
    }

    public static void main(String[] args) {
        JFrame app = new JFrame();
        app.add(new Sample21());
        app.setSize(400, 300);
        app.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        app.setVisible(true);
    }
}