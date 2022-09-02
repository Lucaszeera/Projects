package PacMan;

public class Booster extends Item {

	private int turnCount;

	public Booster() {};

	public Booster(int x, int y, int turnCount) {
		super.setX(x);
		super.setY(y);
		this.turnCount = turnCount;
	}

	public int getTurnos() {
		return turnCount;
	}

	public void setTurnos(int turnCount) {
		this.turnCount = turnCount;
	}

}
