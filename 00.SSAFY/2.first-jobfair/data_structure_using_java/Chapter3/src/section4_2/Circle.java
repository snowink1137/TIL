package section4_2;

public class Circle extends Shape {
	private int radius;
	
	public Circle( int rad ) {
		super("Circle");
		radius = rad;
	}
	
	public void setRadius( int rad ) {
		radius = rad;
	}
	
	public int getRadius() {
		return radius;
	}
	
	public double computeArea() {
		return radius * radius * Math.PI;
	}
	
	public double computePerimeter() {
		return 2 * radius * Math.PI;
	}
	
	public String toString() {
		return "Circle radius is " + radius;
	}
	
}
