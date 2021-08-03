package section1;

import java.io.*;
import java.util.*;

public class Code05 {
	static MyRectangle1 [] rects = new MyRectangle1 [100];
	static int n = 0;
	
	public static void main(String[] args) {
		try {
			Scanner in = new Scanner(new File("data.txt"));
			
			while(in.hasNext()) {
				int x = in.nextInt();
				int y = in.nextInt();
				int w = in.nextInt();
				int h = in.nextInt();
				
				rects[n] = new MyRectangle1();
				rects[n].lu = new MyPoint1();
				rects[n].lu.x = x;
				rects[n].lu.y = y;
				rects[n].width = w;
				rects[n].height = h;
				
				n++;
			}
			
			in.close();
		} catch (FileNotFoundException e) {
			System.out.println("No data file");
			System.exit(1);
		}
		
		bubbleSort();
		
		for (int i=0; i<n; i++) {
			System.out.println(rects[i].lu.x + " " + rects[i].lu.y + " " + rects[i].width + " " + rects[i].height);
		}
	}
	
	private static void bubbleSort() {
		for (int i=n-1; i>0; i--) {
			for (int j=0; j<i; j++) {
				if (calcArea(rects[j]) > calcArea(rects[j+1])) {
					MyRectangle1 tmp = rects[j];
					rects[j] = rects[j+1];
					rects[j+1] = tmp;
				}
			}
		}
	}
	
	public static int calcArea(MyRectangle1 r) {
		return r.width * r.height;
	}

}
