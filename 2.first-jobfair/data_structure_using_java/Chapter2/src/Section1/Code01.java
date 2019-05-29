package Section1;

public class Code01 {

	public static void main(String[] args) {
		int x;
		x = 100;
		
		double y = 1.0023;
		
		Person1 first;
		first = new Person1();  // object
		
		first.name = "John";
		first.number = "01024835555";
		
		System.out.println("Name: " + first.name + ", Number: " + first.number);
		
		Person1 [] members = new Person1 [10];
		members[0] = first;
		members[1] = new Person1();
		members[1].name = "David";
		members[1].number = "516165165165";
		
		System.out.println("Name: " + members[1].name + ", Number: " + members[1].number);
	}

}
