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
//			return;  // main 함수이기 때문에, 여기에 return을 쓰는 것은 프로그램 종료를 의미함.
			System.exit(9);  // 프로그램 종료시키는 함수.
		}
		
		for (int i=0; i<n; i++) {
			System.out.println(name[i] + ": " + number[i]);
		}
		
	}

}
