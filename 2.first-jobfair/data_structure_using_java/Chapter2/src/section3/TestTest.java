package section3;

public class TestTest {

	public static void main(String[] args) {
		Test test1 = new Test();
		test1.t = 10;
		
//		test1.s = 100;  // 문법적으로 명확한 표현이 아니지만 이클립스에서 경고만 해줌.
		Test.s = 100;  // 이렇게 써야 static 의미에 맞음.
		
//		test1.print1();  // 문법적으로 명확한 표현이 아니지만 이클립스에서 경고만 해줌.
		Test.print1();  // 이렇게 써야 static 의미에 맞음.
		
		test1.print2();
		
		Test test2 = new Test();
		test2.print2();
	}

}
