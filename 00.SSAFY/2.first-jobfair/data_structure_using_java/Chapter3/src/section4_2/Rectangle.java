package section4_2;

public class Rectangle extends Shape {
	private int width = 0;
	private int height = 0;
	
	public Rectangle(int w, int h) {
		super("Rectangle");
		width = w;
		height = h;
	}
	
	public int getWidth() {
		return width;
	}
	
	public int getHeight() {
		return height;
	}
	
	public double computeArea() {
		return (double)height * width;
	}
	
	public double computePerimeter() {
		return 2.0 * (height + width);
	}
	
	public String toString() {
		return "Rectangle: width is " + width + ", height is " + height;
	}
	
}
