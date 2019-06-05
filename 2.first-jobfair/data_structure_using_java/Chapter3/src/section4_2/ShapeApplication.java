package section4_2;

import java.util.*;

public class ShapeApplication {
	private int capacity = 10;
	private Shape [] shapes = new Shape [capacity];
	private int n = 0;
	private Scanner kb = new Scanner(System.in);	

	public void processCommand() {
		while (true) {
			System.out.print("$ ");
			String command = kb.next();
			if (command.equals("add")) {
				handleAdd();
			} else if (command.equals("show") || command.equals("showdetail")) {
				handleShow(command.equals("showdetail"));
			} else if (command.equals("sort")) {
				Arrays.sort(shapes, 0, n);
			} else if (command.equals("exit")) {
				break;
			}
		}
	}

	//	private void bubbleSort() {
	//		for (int i=0; i>0; i--) {
	//			for (int j=0; j<i; j++) {
	//				if ( shapes[j].computeArea() > shapes[j+1].computeArea() ) {
	//					Shape tmp = shapes[j];
	//					shapes[j] = shapes[j+1];
	//					shapes[j+1] = tmp;
	//				}
	//			}
	//		}
	//	}
	
//	// genericÇÑ bubble sort
//	private void bubbleSort(MyComparable [] data, int size) {
//		for (int i=size; i>0; i--) {
//			for (int j=0; j<i; j++) {
//				if ( data[j].compareTo(data[j+1]) > 0) {
//					MyComparable tmp = data[j];
//					data[j] = data[j+1];
//					data[j+1] = tmp;
//				}
//			}
//		}
//	}



	private void handleShow(boolean detailed) {
		for (int i=0; i<n; i++) {
			System.out.println((i+1)+". "+shapes[i].toString());
			if (detailed) {
				System.out.println("     The area is "+shapes[i].computeArea());
				System.out.println("     The perimeter is "+shapes[i].computePerimeter());
			}
		}

	}

	private void handleAdd() {
		String type = kb.next();
		switch (type) {
		case "R":
			int w = kb.nextInt();
			int h = kb.nextInt();

			Rectangle r = new Rectangle(w, h);
			addShape(r);
			break;

		case "C":
			addShape(new Circle(kb.nextInt()));
			break;

		case "T":
			// omitted

		}
	}

	public void addShape(Shape shape) {
		if (n >= capacity)
			reallocate();
		shapes[n++] = shape;
	}

	private void reallocate() {
		capacity *= 2;
		Shape[] tmp = new Shape[capacity];
		System.arraycopy(shapes, 0, tmp, 0, shapes.length);
		shapes = tmp;
	}

	public static void main(String[] args) {
		ShapeApplication app = new ShapeApplication();
		app.processCommand();

	}

}
