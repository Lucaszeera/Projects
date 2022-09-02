package PacMan;

public class Ghost extends GameObject{
	
	private int direction;
	private static final int STEP = 10;
	
	public Ghost() {};
	
	public Ghost(int x, int y, int direction) {
		super.setX(x);
		super.setY(y);
		this.direction = direction;
	}
	
	public boolean canMove() { // valida se o proximo passo estará dentro do screenSize
		int newY = calculateNewY();
		int newX = calculateNewX();
		if(newY > getScreenSize()) { //180 é eixo y
			double sorteio = Math.random();
			if(sorteio < 0.3) this.direction = 0;
			else if(sorteio < 0.6) this.direction = 90;
			else if(sorteio < 0.9) this.direction = 270;
		};
		if(newX > getScreenSize()) {
			double sorteio = Math.random();
			if(sorteio < 0.3) this.direction = 0;
			else if(sorteio < 0.6) this.direction = 180;
			else if(sorteio < 0.9) this.direction = 270;
		}
		
		if(newY < 0 || newY > getScreenSize() || newX < 0 || newX > getScreenSize()) {
			this.setDirection(turn());
		}
		return true;
	}

	public void move() {
		if(canMove()) {
			double sorteio = Math.random();
			if(sorteio < 0.2) direction = turn();
			if(getX() == getScreenSize() && direction == 90)
				while(direction < 90 || direction > 90) {
					this.setDirection(turn());
				}
			setX(calculateNewX());
			setY(calculateNewY());
		}	
	}
	private int turn() { // retorna direction
		int newDirection = 0;
		double sorteio = Math.random();
		if(sorteio < 0.25) newDirection = 90;
		if(sorteio >= 0.25 && sorteio < 0.5) newDirection = 180;
		if(sorteio >= 0.5 && sorteio < 0.75) newDirection = 270;
		this.direction = direction;
		return newDirection;
	}
	private int calculateNewX() {
		int newX = getX();
		
		if(direction == 90) newX = getX() + STEP;
		if(direction == 270) newX = getX() - STEP;
		return newX;
	}
	private int calculateNewY() {
		int newY = getY();
		
		if(direction == 0) newY = getY() - STEP;
		if(direction == 180) newY = getY() + STEP;
		return newY;
	}
	
	
	public int getDirection() {
		return direction;
	}

	public void setDirection(int direction) {
		this.direction = direction;
	}
	
	

}
