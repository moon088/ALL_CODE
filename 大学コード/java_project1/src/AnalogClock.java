import java.awt.*;
import java.util.Calendar;
import javax.swing.*;

public class AnalogClock extends JPanel implements Runnable {
	Calendar now;
	Thread th;
	Font F = new Font("TimesRoman", Font.PLAIN, 14);
	Color fgcol = Color.blue;
	Color fgcol2 = Color.darkGray;

	public AnalogClock() {
		setOpaque(false);
	}

	public static void main(String args[]) {
		JFrame app = new JFrame();
		AnalogClock clock = new AnalogClock();
		app.add(clock);
		app.setSize(150, 150);
		app.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		app.setVisible(true);
		clock.start();
	}

	public void start() {
		if (th == null) {
			th = new Thread(this);
			th.start();
		}
	}

	public void stop() {
		if (th != null) {
			th = null;
		}
	}

	public void run() {
		while (th != null) {
			repaint();
			try {
				Thread.sleep(1000);
			} catch (InterruptedException e) {
			}
		}
	}

	public void paintComponent(Graphics g) {
		int xh, yh, xm, ym, xs, ys, s, m, h, xcenter, ycenter;

		now = Calendar.getInstance();
		s = now.get(Calendar.SECOND);
		m = now.get(Calendar.MINUTE);
		h = now.get(Calendar.HOUR_OF_DAY);
		xcenter = 80;
		ycenter = 60;

		xs = (int) (Math.sin(s * 3.14f / 30) * 45 + xcenter);
		ys = (int) (-Math.cos(s * 3.14f / 30) * 45 + ycenter);
		xm = (int) (Math.sin(m * 3.14f / 30) * 40 + xcenter);
		ym = (int) (-Math.cos(m * 3.14f / 30) * 40 + ycenter);
		xh = (int) (Math.sin((h * 30 + m / 2) * 3.14f / 180) * 30 + xcenter);
		yh = (int) (-Math.cos((h * 30 + m / 2) * 3.14f / 180) * 30 + ycenter);

		g.setFont(F);
		g.setColor(fgcol);
		g.drawOval(xcenter - 50, ycenter - 50, 100, 100);
		g.drawLine(xcenter, ycenter - 1, xm, ym);
		g.drawLine(xcenter - 1, ycenter, xm, ym);
		g.drawLine(xcenter, ycenter - 1, xh, yh);
		g.drawLine(xcenter - 1, ycenter, xh, yh);

		g.setColor(fgcol2);
		g.drawString("9", xcenter - 45, ycenter + 3);
		g.drawString("3", xcenter + 40, ycenter + 3);
		g.drawString("12", xcenter - 5, ycenter - 37);
		g.drawString("6", xcenter - 3, ycenter + 45);
		g.drawLine(xcenter, ycenter, xs, ys);
	}
}