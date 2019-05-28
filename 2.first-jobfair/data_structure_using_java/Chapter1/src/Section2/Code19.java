package Section2;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Code19 {

	public static void main(String[] args) {
		String [] name = new String [1000];
		String [] number = new String [1000];
		int n = 0;
		
		try {
			Scanner inFile = new Scanner(new File("input.txt"));
			
			while(inFile.hasNext()) {  // detect End of file
				name[n] = inFile.next();
				number[n] = inFile.next();
				n++;
			}
			
			inFile.close();
		} catch (FileNotFoundException e) {
			System.out.println("No file");
//			return;  // main �Լ��̱� ������, ���⿡ return�� ���� ���� ���α׷� ���Ḧ �ǹ���.
			System.exit(9);  // ���α׷� �����Ű�� �Լ�.
		}
		
		for (int i=0; i<n; i++) {
			System.out.println(name[i] + ": " + number[i]);
		}
		
	}

}
