package section3;

public class Test {  // subclass of Object
	public int a;
	public double x;
	
	public boolean equals(Object other) {
		Test other2 = (Test) other;  // type casting
		return a == other2.a && x == other2.x;
	}
	
	public static void main(String[] args) {
		// class Object overriding example
		Test test1 = new Test();
		Test test2 = new Test();
		
//		test2.a = 5;
//		test2.x = 1.293325;
		
		System.out.println(test1.toString());
		if (test2.equals(test1)) {
			System.out.println("yes");
		} else {
			System.out.println("no");
		}
		
		
		// Wrapper class example 
		Object [] array = new Object [100];
		int a = 20;
		Integer age = new Integer(a);  // wrapping
		
		array[0] = age;
		
		int b = age.intValue();  // unwrapping
		System.out.println(b);
		
		
		String str = "1234";
		int c = Integer.parseInt(str);
		System.out.println(c);
	}
}
