package section3;

public class TestTest {

	public static void main(String[] args) {
		Test test1 = new Test();
		test1.t = 10;
		
//		test1.s = 100;  // ���������� ��Ȯ�� ǥ���� �ƴ����� ��Ŭ�������� ��� ����.
		Test.s = 100;  // �̷��� ��� static �ǹ̿� ����.
		
//		test1.print1();  // ���������� ��Ȯ�� ǥ���� �ƴ����� ��Ŭ�������� ��� ����.
		Test.print1();  // �̷��� ��� static �ǹ̿� ����.
		
		test1.print2();
		
		Test test2 = new Test();
		test2.print2();
	}

}
