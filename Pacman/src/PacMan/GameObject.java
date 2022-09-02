package PacMan;

public class GameObject {
	private int x;
	private int y;
	private int screenSize = 500;

	public GameObject() {
	};

	public GameObject(int x, int y) {
		setX(x);
		setY(y);
	}
	
	public int getX() {
		return x;
	}

	public void setX(int x) {
		if(x >= 0) this.x = x;
	}

	public int getY() {
		return y;
	}

	public void setY(int y) {
		if(y >= 0)this.y = y;
	}

	public int getScreenSize() {
		return screenSize;
	}

	public void setScreenSize(int screen) {
	
		if(screen > 0) this.screenSize = screen;
	};

}

